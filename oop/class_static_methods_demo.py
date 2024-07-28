class Calculator:
    #attribute
    calculation_type = "Arithmetic Operation"

    @staticmethod
    def add(a, b):
        return a + b 

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b        