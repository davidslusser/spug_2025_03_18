# cli.py
import argparse
from calculator import add, subtract, multiply, divide


def main():
    parser = argparse.ArgumentParser(description="CLI Calculator")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument(
        "operator",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform",
    )
    args = parser.parse_args()

    if args.operator == "add":
        result = add(args.num1, args.num2)
    elif args.operator == "subtract":
        result = subtract(args.num1, args.num2)
    elif args.operator == "multiply":
        result = multiply(args.num1, args.num2)
    elif args.operator == "divide":
        try:
            result = divide(args.num1, args.num2)
        except ValueError as e:
            print(e)
            return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
