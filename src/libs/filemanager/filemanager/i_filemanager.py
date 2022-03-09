from abc import ABC, abstractmethod

class IFileManager(ABC):

    @abstractmethod
    def list_files(self, folder):
        raise NotImplementedError

    @abstractmethod
    def read_file(self, filename):
        raise NotImplementedError

    @abstractmethod
    def read_image(self, filename):
        raise NotImplementedError

    @abstractmethod
    def get_file_size(self, filename):
        raise NotImplementedError
        
    @abstractmethod
    def move_file(self, source, target):
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, filename):
        raise NotImplementedError

    @abstractmethod
    def save_file(self, filename, data):
        raise NotImplementedError

    @abstractmethod
    def folder_exists(self, name):
        raise NotImplementedError
    @abstractmethod 
    def create_folder(self, name):
        raise NotImplementedError