def is_fibonacci(num):

    if num < 0:
        return False


    a, b = 0, 1


    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False


numero = int(input("Informe um número: "))


if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")