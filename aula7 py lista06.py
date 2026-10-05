alunos = {}
for i in range(10):
    nome = input(f'Qual o nome {i+1}: ')
    soma = 0
    
    for f in range(4):
        nota = float(input(f'Digite a nota {f+1}: '))
        soma += nota  
    
    media = soma / 4
    alunos[nome] = media
if media >= 7:
    print(f'{nome} foi aprovado com a media {media}')
