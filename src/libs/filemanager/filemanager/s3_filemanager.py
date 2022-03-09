
from filemanager.i_filemanager import IFileManager

class S3FileManager(IFileManager):

    def list_files(self, folder):
        raise NotImplementedError

    def read_file(self, filename):
        raise NotImplementedError

    def read_image(self, filename):
        raise NotImplementedError

    def get_file_size(self, filename):
        raise NotImplementedError
        
    def move_file(self, source, target):
        raise NotImplementedError

    def delete_file(self, filename):
        raise NotImplementedError

    def save_file(self, filename, data):
        raise NotImplementedError

    
