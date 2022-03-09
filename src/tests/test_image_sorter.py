from image_sorter.src.image_sorter import ImageSorter
from filemanager import IFileManager
from messagebroker import MessageBroker

import unittest
import unittest.mock as mock

class ImageSorterTestCase(unittest.TestCase):
    
    def setUp(self):
        mock_broker = mock.create_autospec(MessageBroker)
        self.mock_filemanager = mock.create_autospec(IFileManager)
        colors = {"red":"FF0000", "green": "00FF00", "blue": "0000FF"}
        self.image_sorter = ImageSorter(self.mock_filemanager, mock_broker, "test_path", colors)

    def test_color_from_hex_string(self):
        self.assertTrue(self.image_sorter.get_color_from_hex_string("FFFFFF") == (255, 255, 255))
        self.assertTrue(self.image_sorter.get_color_from_hex_string("FF00FF") == (255, 0, 255))
        self.assertTrue(self.image_sorter.get_color_from_hex_string("d4edda") == (212, 237, 218))

    def test_closest_color(self):
        almost_red = (228,41,54)
        almost_blue = (23,11,241)
        almost_green = (25,230,32)
        self.assertTrue(self.image_sorter.get_closest_color(almost_red) == "red")
        self.assertTrue(self.image_sorter.get_closest_color(almost_green) == "green")
        self.assertTrue(self.image_sorter.get_closest_color(almost_blue) == "blue")

if __name__ == '__main__':
    unittest.main()