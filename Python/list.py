import os 
os.system("cls")

def obter_quantidade_alunos():
    quantidade = int(input("Quantos alunos deseja registrar na lista? "))
    return quantidade

def obter_dados_aluno(numero):
    os.system("cls")
    nome = input(f"Digite o nome do {numero}\u00BA aluno: ")
    respostas = []
    for i in range(1, 6):
        pergunta = f"QUEST {i}:"
        resposta = input(pergunta).upper()
        respostas.append(resposta)
    return nome, respostas

def calcular_media(respostas_aluno):
    ordem_respostas = ['A', 'B', 'C', 'C', 'D']
    pontuacao = 0
    for resposta in respostas_aluno:
        if resposta != ordem_respostas[0]:
            pontuacao += 20
        ordem_respostas.pop(0)
    media = 10 - (pontuacao / 5)
    return media

def calcular_media_turma(alunos):
    total_alunos = len(alunos)
    soma_medias = sum(media for _, media in alunos)
    media_turma = soma_medias / total_alunos
    return media_turma

def listar_melhores_alunos(alunos):
    melhores_alunos = sorted(alunos, key=lambda x: x[1], reverse=True)
    print("Melhores alunos:")
    for aluno in melhores_alunos:
        nome, media = aluno
        print("{:<10}: {:.1f}".format(nome, media))
   
quantidade_alunos = obter_quantidade_alunos()
alunos = []

for i in range(1, quantidade_alunos + 1):
    dados_aluno = obter_dados_aluno(i)
    alunos.append(dados_aluno)
    
melhores_alunos = []

for aluno in alunos:
    nome, respostas = aluno
    media = calcular_media(respostas)
    melhores_alunos.append((nome, media))  
    
media_turma = calcular_media_turma(melhores_alunos)
 
print("\nMédia da turma: {:.1f}".format(media_turma))

listar_melhores_alunos(melhores_alunos)
print(" ")