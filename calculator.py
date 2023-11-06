from calc_art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    num1 = int(input("Enter the first number:\n"))

    for key in operations:
        print(key)

    while True:
        symbol = input("Pick a symbol:\n")
        num2 = int(input("Enter another number:\n"))
        answer = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        wish_to_continue = input("Wish to continue? Type 'yes' or 'no'\n")
        if wish_to_continue == "yes":
            num1 = answer
        else:
            # break
            calculator()


calculator()
