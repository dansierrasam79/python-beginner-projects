"""
Simple Calculator Program using Object-Oriented Programming (OOP) in Python.

The Calculator class encapsulates all basic arithmetic functions as methods.
"""

class SimpleCalculator:
    """
    A class to perform basic arithmetic operations (addition, subtraction, 
    multiplication, and division).
    """

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """
        Returns the quotient of two numbers.
        Handles division by zero error.
        """
        if b == 0:
            # Raise an error instead of returning a generic message,
            # allowing the calling code to handle the exception gracefully.
            raise ValueError("Error: Cannot divide by zero.")
        return a / b

    def run_cli(self):
        """
        Runs a simple command-line interface (CLI) loop for the calculator.
        """
        print("------------------------------------------------")
        print("Simple OOP Calculator (Type 'quit' or 'exit' to stop)")
        print("Supported operations: +, -, *, /")
        print("------------------------------------------------")

        while True:
            try:
                # Get the operation and numbers from the user
                user_input = input("Enter expression (e.g., 5 + 3) or 'quit': ").strip()

                if user_input.lower() in ['quit', 'exit']:
                    print("Exiting calculator. Goodbye!")
                    break

                # Split the input into parts: number1, operator, number2
                parts = user_input.split()

                if len(parts) != 3:
                    print("Invalid format. Please use 'number operator number' (e.g., 10 * 5).")
                    continue

                num1_str, operator, num2_str = parts

                # Convert input strings to float for calculation
                try:
                    num1 = float(num1_str)
                    num2 = float(num2_str)
                except ValueError:
                    print("Invalid number entered. Please ensure both inputs are numeric.")
                    continue

                result = None
                
                # Perform the operation based on the operator symbol
                if operator == '+':
                    result = self.add(num1, num2)
                elif operator == '-':
                    result = self.subtract(num1, num2)
                elif operator == '*':
                    result = self.multiply(num1, num2)
                elif operator == '/':
                    result = self.divide(num1, num2)
                else:
                    print(f"Unsupported operator: '{operator}'.")
                    continue

                # Print the result
                print(f"Result: {result}")
            
            except ValueError as e:
                # Catch specific errors raised by methods (like division by zero)
                print(e)
            except Exception as e:
                # Catch unexpected general errors
                print(f"An unexpected error occurred: {e}")
            
# --- Main Execution Block ---
# This block runs when the script is executed directly.

if __name__ == "__main__":
    # Create an instance (object) of the SimpleCalculator class
    calculator = SimpleCalculator()
    
    # Run the interactive CLI
    calculator.run_cli()

    # Example of calling the methods directly:
    # print("\n--- Method Tests ---")
    # print(f"25 + 5 = {calculator.add(25, 5)}")       # 30
    # print(f"10 - 4 = {calculator.subtract(10, 4)}")  # 6
    # print(f"7 * 6 = {calculator.multiply(7, 6)}")    # 42
    # print(f"50 / 10 = {calculator.divide(50, 10)}")  # 5.0
    # try:
    #     calculator.divide(10, 0)
    # except ValueError as e:
    #     print(e)
    
