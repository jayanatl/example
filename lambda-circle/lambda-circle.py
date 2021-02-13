import sys
sys.path.append("../")
from shapes import Circle

def lambda_handler(event, context):
    shape = Circle(3)
    return f"Shape: {shape} | Area: {shape.area()} | Perimeter: {shape.perimeter()}"


if __name__ == "__main__":
    print(lambda_handler(None, None))
