def validateType(object: object, objectType: type) -> bool:
    return isinstance(object, objectType)


def validateRange(number: int, numberRange: tuple[int]) -> bool:
    if number >= numberRange[0] and number <= numberRange[1]:
        return True
    else:
        return False


def validateNumber(inputPrompt: str, numberType: type, numberRange=(float('-inf'), float('inf'))):
    userInput = input(inputPrompt)
    while True:
        if validateType(userInput, numberType):
            if validateRange(numberType(userInput), numberRange):
                return numberType(userInput)
        userInput = input(inputPrompt)