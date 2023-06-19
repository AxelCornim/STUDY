import os 
os.system("cls")

def qtd_alunos():
    quantidade = int(input("Quantos alunos deseja registrar nota?"))
    os.system("cls")
    return quantidade

def obter_dados_alunos(numero):
    nome = input(f"Digite o nome do {numero}\u00BA aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    media = (nota1 + nota2) / 2
    return nome, nota1, nota2, media

def listar_alunos_por_media(alunos):
    alunos_ordenados = sorted(alunos, key=lambda x: x[3], reverse=True) 
    print("Lista de alunos por média:")
    print("                 ")
    for aluno in alunos_ordenados:
        nome, nota1, nota2, media = aluno
        print(f"Nome: {nome}")
        print(f"Média: {media}")
        print("-----------------------")
        
def calcular_media_turma(turma):
    soma_medias = sum([aluno[3] for aluno in alunos])
    media_turma = soma_medias / len(alunos)
    return media_turma

def contar_alunos_acima_media(alunos, media_turma):
    alunos_acima_media = [aluno for aluno in alunos if aluno[3] > media_turma]
    return len(alunos_acima_media)
    
obter_qtd_alunos = qtd_alunos()
alunos = []

for i in range(1, obter_qtd_alunos + 1):
    dados_alunos = obter_dados_alunos(i)
    alunos.append(dados_alunos)
    os.system("cls")

listar_alunos_por_media(alunos)

media_turma = calcular_media_turma(alunos)
quantidade_alunos_acima_media = contar_alunos_acima_media(alunos, media_turma)

print(f"Ao todo, temos {quantidade_alunos_acima_media} alunos acima da media turma {media_turma:.1f}.")