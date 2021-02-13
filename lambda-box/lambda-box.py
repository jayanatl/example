from shapes import Rectangle

def lambda_handler(event, context):
    shape = Rectangle(1, 2)
    return f"Shape: {shape} | Area: {shape.area()} | Perimeter: {shape.perimeter()}"


if __name__ == "__main__":
    print(lambda_handler(None, None))
