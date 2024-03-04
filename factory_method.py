from abc import ABC, abstractmethod
import json
import pickle

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight


class Serializer(ABC):
    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def deserialize(self):
        pass


class JsonSerializer(Serializer):
    def serialize(self, data):
        with open('data.json', 'w') as file:
            json.dump(data, file)

    def deserialize(self):
        with open('data.json', 'r') as file:
            return json.load(file)


class PickleSerializer(Serializer):
    def serialize(self, data):
        with open('data.bin', 'wb') as file:
            pickle.dump(data, file)

    def deserialize(self):
        with open('data.bin', 'rb') as file:
            return pickle.load(file)


class SerializerCreator(ABC):
    @abstractmethod
    def create_serializer(self):
        pass


class JsonSerializerCreator(SerializerCreator):
    def create_serializer(self):
        return JsonSerializer()
    

class PickleSerializerCreator(SerializerCreator):
    def create_serializer(self):
        return PickleSerializer()
    

def choose_serializer(serializer):
    if serializer == 'pickle':
        return PickleSerializerCreator().create_serializer()
    elif serializer == 'json':
        return JsonSerializerCreator().create_serializer()
    return None

if __name__ == '__main__':
    # animal = Animal('Barsik', 5)
    animal_dict = {'name': 'Barsik', 'weight': 5}

    choose_serializer('json').serialize(animal_dict)
    choose_serializer('pickle').serialize(animal_dict)

    print(choose_serializer('pickle').deserialize()['name'])