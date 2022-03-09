import os
from dotenv import load_dotenv


from filemanager import LocalFileManager
from messagebroker import MessageBroker
from lifecyclemanager import LifecycleManager
from image_loader import ImageLoader


def main():
    load_dotenv()
        
    lifecycle_manager = LifecycleManager()

    file_manager = LocalFileManager()
    message_broker = MessageBroker(os.getenv('NATS_URL'))
    image_loader = ImageLoader(file_manager, message_broker, os.getenv('STORAGE_PATH'))

    lifecycle_manager.run_forever(image_loader)
