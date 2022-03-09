import os
from dotenv import load_dotenv


from filemanager import LocalFileManager
from messagebroker import MessageBroker
from lifecyclemanager import LifecycleManager
from image_sorter import ImageSorter



def main():
    load_dotenv()
        
    lifecycle_manager = LifecycleManager()

    file_manager = LocalFileManager()
    message_broker = MessageBroker(os.getenv('NATS_URL'))
    web_colors = { 
        "white": "FFFFFF",
        "silver": "C0C0C0",
        "gray": "808080",
        "black": "000000",
        "red": "FF0000",
        "maroon": "800000",
        "yellow": "FFFF00",
        "olive": "808000",
        "lime": "00FF00",
        "green": "008000",
        "aqua": "00FFFF",
        "teal": "008080",
        "blue": "0000FF",
        "navy": "000080",
        "fuchsia": "FF00FF",
        "purple": "800080"
    } 
    image_sorter = ImageSorter(file_manager, message_broker, os.getenv('STORAGE_PATH'), web_colors)

    lifecycle_manager.run_forever(image_sorter)
