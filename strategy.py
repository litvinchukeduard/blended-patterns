from abc import ABC, abstractmethod
from zipfile import ZipFile
from tarfile import TarFile
import os


class ArchiveStrategy(ABC):
    @abstractmethod
    def create_archive(self, folder_path):
        pass


class ZipArchiveStrategy(ArchiveStrategy):
    def create_archive(self, folder_path):
        list_of_files = os.listdir(folder_path)
        with ZipFile('spam.zip', 'w') as myzip:
            for file in list_of_files:
                myzip.write(f'{folder_path}/{file}')


class TarArchiveStrategy(ArchiveStrategy):
    def create_archive(self, folder_path):
        list_of_files = os.listdir(folder_path)
        with TarFile('spam.tar', 'w') as mytar:
            for file in list_of_files:
                mytar.add(f'{folder_path}/{file}')


class ArchiveExecutor:
    def __init__(self, strategy: ArchiveStrategy):
        self.strategy = strategy

    def create_archive(self, folder_path):
        self.strategy.create_archive(folder_path)


def create_executor(algorithm: str):
    if algorithm == 'zip':
        return ArchiveExecutor(ZipArchiveStrategy())
    elif algorithm == 'tar':
        return ArchiveExecutor(TarArchiveStrategy())
    else:
        None


if __name__ == '__main__':
    create_executor('tar').create_archive('folder')