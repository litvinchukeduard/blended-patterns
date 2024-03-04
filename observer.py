from abc import ABC, abstractmethod
import psutil
import time


class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass


class CPUObserver(Observer):
    def update(self, data):
        print(f'CPU: {data.get('cpu_percent')}')


class DiskObserver(Observer):
    def update(self, data):
        print(f'Disk: {data.get('disk')}')


class MemoryObserver(Observer):
    def update(self, data):
        print(f'Memory: {data.get('memory')}')


class ComputerPublisher:
    def __init__(self):
        self.subscribers = []
        self.data = dict()

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.data)

    def get_system_information(self):
        while True:
            self.data['cpu_percent'] = psutil.cpu_percent(interval=1)
            self.data['memory'] = psutil.virtual_memory().percent
            self.data['disk'] = psutil.disk_usage('.').percent

            self.notify_subscribers()
            time.sleep(1)


if __name__ == '__main__':
    cpu_observer = CPUObserver()
    memory_observer = MemoryObserver()
    disk_observer = DiskObserver()

    publisher = ComputerPublisher()
    publisher.add_subscriber(cpu_observer)
    publisher.add_subscriber(memory_observer)
    publisher.add_subscriber(disk_observer)
    publisher.get_system_information()