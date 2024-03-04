from abc import ABC, abstractmethod
from singleton import LoggingSingleton

logger = LoggingSingleton()

def log(func):
    def wrapper(*args, **kwargs):
        logger.log_info_message(f'Calling function {func}')
        result = func(*args, **kwargs)
        logger.log_debug_message(f'With result: {result}')
        return result
    return wrapper

# @log
def sum_numbers(lst):
    return sum(lst)


class AbstractFunction(ABC):
    @abstractmethod
    def execute(self, func, lst):
        pass


class FunctionExecutor(AbstractFunction):
    def execute(self, func, lst):
        return func(lst)
    

class FunctionExecutorLoggerDecorator(AbstractFunction):
    def __init__(self, functionExecutor: FunctionExecutor):
        self.wrappee = functionExecutor

    def execute(self, func, lst):
        logger.log_info_message(f'Calling function {func}')
        result = self.wrappee.execute(func, lst)
        logger.log_debug_message(f'With result: {result}')
        return result

if __name__ == '__main__':
    # print(sum_numbers([1, 2, 3, 4]))

    executor = FunctionExecutor()
    # print(executor.execute(sum_numbers, [1, 2, 3]))

    executorDecorator = FunctionExecutorLoggerDecorator(executor)
    print(executorDecorator.execute(sum_numbers, [1, 2, 3]))