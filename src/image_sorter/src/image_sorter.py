
import json
import math
import os

from filemanager import IFileManager
from lifecyclemanager import IRunnable
from messagebroker import MessageBroker

class ImageSorter(IRunnable):
    """
    Receives a message containing image filename
    and its average color, moves the image to a 
    corresponding folder based on the average color of
    the image
    """
    
    def __init__(self, file_manager:IFileManager, message_broker:MessageBroker, storage_path, colors):
        self.file_manager = file_manager
        self.message_broker = message_broker
        self.storage_path = storage_path
        self.colors = colors

    def get_color_from_hex_string(self, color_string):
        """Returns a color tuple(R,G,B) from a hex color code"""
        return (
            int("0x"+color_string[:2], 16), 
            int("0x"+color_string[2:4], 16), 
            int("0x"+color_string[4:], 16)
        )

    def get_distance_between_colors(self, color1, color2):
        return math.sqrt(
                int(color1[0]-color2[0])**2 + 
                int(color1[1]-color2[1])**2 + 
                int(color1[2]-color2[2])**2
            )

    def get_closest_color(self, color):
        closest_color = ("black", math.inf)
        for color_name, color_code in self.colors.items():
            web_color = self.get_color_from_hex_string(color_code)
            distance = self.get_distance_between_colors(web_color, color)
            if(distance < closest_color[1]):
                closest_color = (color_name, distance)
        return closest_color[0]

    async def run(self):
        await self.message_broker.connect()
        await self.message_broker.listen_for_messages("processor.file.processed", self.message_received, "workers")

    async def destruct(self):
        await self.message_broker.disconnect()
        
    def message_received(self, subject, data): 
        print("Subject: {0}, data: {1}".format(subject, data))
        
        data = json.loads(data)
        file_path = data["filename"]
        color = data["color"]

        closest_color = self.get_closest_color(color)

        folder_path = os.path.join(self.storage_path, "sorted", closest_color)
        if(not self.file_manager.folder_exists(folder_path)):
            self.file_manager.create_folder(folder_path)

        new_file_path =  os.path.join(folder_path, os.path.basename(file_path))

        self.file_manager.move_file(file_path, new_file_path)
