from abc import ABC, abstractmethod

class IRunnable(ABC):
    @abstractmethod
    async def run(self):
        raise NotImplementedError
    @abstractmethod
    async def destruct(self):
        raise NotImplementedError
