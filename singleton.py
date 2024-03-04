import logging
from singleton_configuration import ConfigurationSingleton

class LoggingSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls.setup_logging(cls)
            cls._instance = super().__new__(cls)
        return cls._instance

    def setup_logging(cls):
        log_level = logging.DEBUG
        if ConfigurationSingleton().get_property('log_level') == 'INFO':
            log_level = logging.INFO

        logging.basicConfig(
                filename="my_log.log",
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=log_level
        )

    def log_info_message(self, message):
        logging.info(message)

    def log_debug_message(self, message):
        logging.debug(message)


if __name__ =='__main__':
    logger = LoggingSingleton()
    logger.log_info_message('Hello, world!')

    logger_two = LoggingSingleton()
    logger_two.log_info_message('Hello, from log two')
    print(logger == logger_two)

    logger.log_debug_message('THIS IS DEBUG!')

