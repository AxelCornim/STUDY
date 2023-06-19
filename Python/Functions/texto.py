import os
os.system("cls")

def contar_caracteres(texto):
    return len(texto)

def inverter_texto(texto):
    return texto[::-1]

def maiusculas_minusculas(texto):
    texto_maiusculo = texto.upper()
    texto_minusculo = texto.lower()
    return texto_maiusculo, texto_minusculo

texto = '''
Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos,
de tipagem dinâmica e forte. Possui uma sintaxe clara e expressiva que favorece a legibilidade e produtividade.
É amplamente utilizada em diversos campos, como desenvolvimento web, ciência de dados, automação de tarefas,
inteligência artificial, entre outros. Sua vasta biblioteca padrão e a grande comunidade de desenvolvedores
contribuem para a disponibilidade de recursos e suporte. Python é uma excelente escolha para quem está
iniciando na programação ou deseja desenvolver soluções eficientes e elegantes.
'''

quantidade_caracteres = contar_caracteres(texto)
print("Quantidade de caracteres:", quantidade_caracteres)
print()  
texto_invertido = inverter_texto(texto)
print("Texto invertido:", texto_invertido)

texto_maiusculo, texto_minusculo = maiusculas_minusculas(texto)
print("Texto em maiúsculas:", texto_maiusculo)
print("Texto em minúsculas:", texto_minusculo)

print("Texto original:", texto)