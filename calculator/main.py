from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("Digite o primeiro número: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Digite uma operação: ")
        num2 = float(input("Digite o próximo número: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Digite 's' para continuar calculando com {answer}, ou digite 'n' para iniciar um novo calculo: ") == 's':
            n1 = answer
        else:
            should_continue = False
            calculator()

calculator()      
        

