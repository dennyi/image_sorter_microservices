
import asyncio
from filemanager import IFileManager
from lifecyclemanager import IRunnable
from messagebroker import MessageBroker
import numpy as np
import json

class ImageProcessor(IRunnable):
    """
    Waits for messages about new queued up images, 
    calculates average color for each image, then sends 
    a message to image_sorter signaling images are ready to be sorted
    """

    def __init__(self, file_manager:IFileManager, message_broker:MessageBroker, storage_path):
        self.file_manager = file_manager
        self.message_broker = message_broker
        self.storage_path = storage_path
    
    def get_image_average_color(self, img):
        return tuple(np.mean(img,(0,1)).tolist())

    async def run(self):
        await self.message_broker.connect()
        await self.message_broker.listen_for_messages("loader.file.new", self.message_received, "workers")

    async def destruct(self):
        await self.message_broker.disconnect()
        
    def message_received(self, subject, data): 
        print("Subject: {0}, data: {1}".format(subject, data))

        filename = data
        img = self.file_manager.read_image(filename)

        message_data = json.dumps({"filename": filename, "color": self.get_image_average_color(img)})

        print("Sending message on subject processor.file.processed with data {0}".format(message_data))
        asyncio.create_task(self.message_broker.send_message("processor.file.processed", message_data))
