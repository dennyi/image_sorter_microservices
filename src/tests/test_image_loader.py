from image_loader.src.image_loader import ImageLoader
from filemanager import IFileManager
from messagebroker import MessageBroker

import unittest
import unittest.mock as mock

class ImageLoaderTestCase(unittest.TestCase):
    
    def setUp(self):
        mock_broker = mock.create_autospec(MessageBroker)
        self.mock_filemanager = mock.create_autospec(IFileManager)
        self.image_loader = ImageLoader(self.mock_filemanager, mock_broker, "test_path")


    def test_file_is_image_accepts_images(self):
        self.assertTrue(self.image_loader.file_is_image("image.png"))
        self.assertTrue(self.image_loader.file_is_image("/image.png"))
        self.assertTrue(self.image_loader.file_is_image("/app/storage/image.PNG"))
        self.assertTrue(self.image_loader.file_is_image("/app/storage/image.pNg"))
        self.assertTrue(self.image_loader.file_is_image("/app/storage/image.jpg"))
        self.assertTrue(self.image_loader.file_is_image("/app/storage/image.jpeg"))
        self.assertTrue(self.image_loader.file_is_image("/app/storage/image.webp"))

    def test_file_is_image_rejects_nonimages(self):
        self.assertFalse(self.image_loader.file_is_image("/app/storage/image.svg"))
        self.assertFalse(self.image_loader.file_is_image("/app/storage/file.pdf"))
        self.assertFalse(self.image_loader.file_is_image("/app/storage/file.PDF"))
        self.assertFalse(self.image_loader.file_is_image("/app/storage/file.doc"))
        self.assertFalse(self.image_loader.file_is_image("/app/storage/file.txt"))
        self.assertFalse(self.image_loader.file_is_image("/app/storage/file"))
        self.assertFalse(self.image_loader.file_is_image("/app/storage/file."))
        self.assertFalse(self.image_loader.file_is_image("/app/storage/file/"))
        self.assertFalse(self.image_loader.file_is_image("file"))
        self.assertFalse(self.image_loader.file_is_image("file/"))
        self.assertFalse(self.image_loader.file_is_image("file."))

    def test_image_size(self):
        self.mock_filemanager.get_file_size.return_value = 3000000
        self.assertTrue(self.image_loader.is_valid_image("image.png", 5000000))
        self.assertFalse(self.image_loader.is_valid_image("image.png", 2000000))


if __name__ == '__main__':
    unittest.main()