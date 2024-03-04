

class Validator:
    def __init__(self, next_validator=None):
        self.next_validator = next_validator

    def validate(self, data):
        if self.next_validator:
            return self.next_validator.validate(data)
        return True
    

class NumberValidator(Validator):
    def validate(self, data:str):
        for symbol in data:
            if symbol.isdigit():
                return super().validate(data)
        return False
    

class LowerLetterValidator(Validator):
    def validate(self, data:str):
        for symbol in data:
            if symbol.islower():
                return super().validate(data)
        return False
    

class UpperLetterValidator(Validator):
    def validate(self, data:str):
        for symbol in data:
            if symbol.isupper():
                return super().validate(data)
        return False
    

if __name__ == '__main__':
    data = "abcABC123"

    # validator_list = [NumberValidator, LowerLetterValidator, UpperLetterValidator]
    # validator = Validator()
    # for str_validator in validator_list:
    #     validator.next_validator = str_validator.__init__()
    
    validator = NumberValidator(LowerLetterValidator(UpperLetterValidator()))

    print(validator.validate(data))