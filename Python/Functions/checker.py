def verificador_numero(n1):
    if n1 % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

n1 = int(input("Digite um número: "))
soma = verificador_numero(n1)
print(soma)