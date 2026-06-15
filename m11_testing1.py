import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Calculator:
    def add(self, a, b):
        result = a + b
        logging.info(f"Addition performed: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        logging.info(f"Subtraction performed: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        logging.info(f"Multiplication performed: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            logging.error("Attempted division by zero")
            raise ValueError("Division by zero is not allowed")
        result = a / b
        logging.info(f"Division performed: {a} / {b} = {result}")
        return result


if __name__ == "__main__":
    calc = Calculator()

    print("Add:", calc.add(10, 5))
    print("Subtract:", calc.subtract(10, 5))
    print("Multiply:", calc.multiply(10, 5))
    print("Divide:", calc.divide(10, 0))

