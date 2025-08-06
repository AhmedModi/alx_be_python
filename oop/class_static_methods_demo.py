# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition without needing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: can access class attributes and methods."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
