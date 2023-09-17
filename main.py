from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


print(logo)


def Calculator():

    op = {"+": add, "-": sub, "*": mul, "/": div}
    calc_exit = False
    n1 = float(input("What is the first number?: "))

    for x in op.keys():
        print(x)

    while not calc_exit:
        operation = str(input("Pick an operation: "))
        n2 = float(input("What is the next number: "))

        calc = op[operation]
        answer = calc(n1, n2)
        print(f" {n1} {operation} {n2} = {answer}")
        cont = str(
            input(
                f"Type 'y' to continue calculating with {answer}, or 'n' to start a new Calculation.: "
            ))

        if cont == "y":
            n1 = answer
        elif cont == "n":
            Calculator()


Calculator()