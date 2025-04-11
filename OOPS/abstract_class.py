from abc import ABC, abstractmethod

class InvalidOperations(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
        
    def open(self):
        if self.opened:
            raise InvalidOperations("The stream is already open.")
        self.opened = True
        
    def close(self):
        if not self.opened:
            raise InvalidOperations("The stream is already closed")
        self.opened = False
        
    @abstractmethod
    def read(self):
        pass
    
class FileStream(Stream):
    def read(self):
        print("The date is read from a file stream.")
        
class NetworkStream(Stream):
    def read(self):
        print("reading from network stream.")
        
class MemoryStream(Stream):
    def read(self):
        print("Reading from memor stream.")

stream = MemoryStream()
print(stream)
