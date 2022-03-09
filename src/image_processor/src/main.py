import os
from dotenv import load_dotenv


from filemanager import LocalFileManager
from messagebroker import MessageBroker
from lifecyclemanager import LifecycleManager
from image_processor import ImageProcessor



def main():
    load_dotenv()
        
    lifecycle_manager = LifecycleManager()

    file_manager = LocalFileManager()
    message_broker = MessageBroker(os.getenv('NATS_URL'))
    image_processor = ImageProcessor(file_manager, message_broker, os.getenv('STORAGE_PATH'))

    lifecycle_manager.run_forever(image_processor)
