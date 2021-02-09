class Calculator:
    def __init__(self, initial_calculation=0) -> None:
        if type(initial_calculation) != int:
            raise ValueError("INVALID OUTPUT")
        self.__last_calculation = initial_calculation

    def get_last_calculation(self) -> int:
        return self.__last_calculation

    def add_to_last_calculation(self, operand=0) -> int:
        if type(operand) != int:
            raise ValueError("INVALID OUTPUT")
        calculation = self.__last_calculation + operand
        self.__last_calculation = calculation
        return calculation

    def subtract_from_last_calculation(self, operand=0) -> int:
        if type(operand) != int:
            raise ValueError("INVALID OUTPUT")
        calculation = self.__last_calculation - operand
        self.__last_calculation = calculation
        return calculation

    def add(self, operand_one, operand_two=0) -> int:
        if type(operand_one) != int or type(operand_two) != int:
            raise ValueError("INVALID OUTPUT")
        if operand_two == 0:
            operand_two = self.__last_calculation
        calculation = operand_one + operand_two
        self.__last_calculation = calculation
        return calculation

    def subtract(self, operand_one, operand_two=0) -> int:
        if type(operand_one) != int or type(operand_two) != int:
            raise ValueError("INVALID OUTPUT")
        calculation = operand_one - operand_two
        self.__last_calculation = calculation
        return calculation
