
def MathOperations(No1, No2):
    Add = No1 + No2
    Subtract = No1 - No2
    Multiply = No1 * No2
    Divide = No1 / No2
    return Add, Subtract, Multiply, Divide

def main(No1, No2):
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    Add, Subtract, Multiply, Divide = MathOperations(No1, No2)
    print(f"Addition: {Add}")
    print(f"Subtraction: {Subtract}")
    print(f"Multiplication: {Multiply}")
    print(f"Division: {Divide}")

if __name__ == "__main__":
    main(No1=0, No2=0)