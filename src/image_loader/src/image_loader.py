
import asyncio
import os
import re

from filemanager import IFileManager
from lifecyclemanager import IRunnable
from messagebroker import MessageBroker


class ImageLoader(IRunnable):
    """
    Periodically checks for images in a folder,
    if valid, moves them to a queue for further processing
    """

    def __init__(self, file_manager:IFileManager, message_broker:MessageBroker, storage_path):
        self.file_manager = file_manager
        self.message_broker = message_broker
        self.storage_path = storage_path
    
    def file_is_image(self, filename):
        extension = os.path.splitext(filename)[-1].lower()
        return extension in {".png", ".jpg", ".webp", ".jpeg"}
        
    def is_valid_image(self, filename, max_size):
        """Checks whether the file is an image and is smaller then specified size"""
        return self.file_is_image(filename) and self.file_manager.get_file_size(filename) < max_size 

    def sanitize_filename(self, filename):
        s = str(filename).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s)

    async def run(self):
        await self.message_broker.connect()

        while True:
            await asyncio.sleep(1)
            new_files = self.file_manager.list_files(os.path.join(self.storage_path, "new"))
            for filename in new_files:
                file_path = os.path.join(self.storage_path, "new", filename)

                if(not self.is_valid_image(file_path, max_size=3000000)):
                    self.file_manager.delete_file(file_path)
                    continue

                new_path = os.path.join(self.storage_path, "queue", self.sanitize_filename(filename))
                self.file_manager.move_file(file_path, new_path)
                await self.message_broker.send_message("loader.file.new", new_path)

    async def destruct(self):
        await self.message_broker.disconnect()