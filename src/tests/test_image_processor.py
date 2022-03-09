from image_processor.src.image_processor import ImageProcessor
from filemanager import IFileManager
from messagebroker import MessageBroker
import numpy as np

import unittest
import unittest.mock as mock

class ImageProcessorTestCase(unittest.TestCase):
    
    def setUp(self):
        mock_broker = mock.create_autospec(MessageBroker)
        self.mock_filemanager = mock.create_autospec(IFileManager)
        self.image_processor = ImageProcessor(self.mock_filemanager, mock_broker, "test_path")

    def test_average_color(self):
        b = np.linspace(0,30, num=4)
        g = np.linspace(0,20, num=4)
        r = np.linspace(0,10, num=4)
        img = np.dstack((r,g,b))
        self.assertTrue(self.image_processor.get_image_average_color(img) == (5.0,10.0,15.0))

if __name__ == '__main__':
    unittest.main()