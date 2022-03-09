import os
import os.path
import shutil
from PIL import Image
import numpy as np


from filemanager.i_filemanager import IFileManager

class LocalFileManager(IFileManager):
    
    def check_filename(self, filename):
        if(not self.is_valid_file(filename)):
            raise Exception("{0} is not a valid file".format(filename))

    def list_files(self, folder):
        return os.listdir(folder)

    def is_valid_file(self, filename):
        return os.path.isfile(filename) and os.path.exists(filename)

    def read_file(self, filename):
        self.check_filename(filename)

        with open(filename, 'rb') as f:
            data = f.read()
        return data

    def read_image(self, filename):
        self.check_filename(filename)
        img = Image.open( filename )
        try:
            return np.asarray( img, dtype='uint8' )
        except SystemError:
            return np.asarray( img.getdata(), dtype='uint8' )

    def get_file_size(self, filename):
        self.check_filename(filename)
        return os.path.getsize(filename)

    def move_file(self, source, target):
        self.check_filename(source)

        shutil.copy(source, target)
        os.remove(source)

    def delete_file(self, filename):
        self.check_filename(filename)
        
        os.remove(filename)

    def save_file(self, filename, data):
        with open(filename, 'wb') as f:
            data = f.write(data)    

    def folder_exists(self, name):
        return os.path.exists(name)
        
    def create_folder(self, name):
        os.mkdir(name)