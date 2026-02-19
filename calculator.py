
def main():
    
    while True:

        user = input("calculate or 'exit': ").strip().lower()
        if user == "exit":
            print("program finished")
            break

        else:
            result = calculate(user)
        print(f"Result: {result}")


def calculate(code):
    
    cleaned = code.strip()
    
    x, y, z = code.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    else:
        return "something wrong with your line, try use space"
    
main()
