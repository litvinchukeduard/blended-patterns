
class ConfigurationSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.property_dict = dict()
            cls.setup_configuration(cls)
        return cls._instance

    def setup_configuration(cls):
        with open('my_app.properties', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                cls._instance.property_dict.update({key: value})

    def get_property(self, key):
        return self.property_dict.get(key)


if __name__ =='__main__':
    configuration = ConfigurationSingleton()

    print(configuration.get_property('color'))
    print(configuration.get_property('log_level'))