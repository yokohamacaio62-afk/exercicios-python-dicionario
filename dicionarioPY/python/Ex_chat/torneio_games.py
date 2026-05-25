from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(0,100),
             'jogador2': randint(0,100),
             'jogador3': randint(0,100),
             'jogador4': randint(0,100)}

ranking = dict ()

for k, v in jogadores.items():
    print(f'{k} com {v} pontos.')
    sleep(1)

ranking = sorted (jogadores.items(), key=itemgetter(1), reverse=True)

media = sum(jogadores.values()) / 4

print(f'o melhor jogador foi:', {ranking [0][0]})
print(f'o pior jogador foi:', {ranking [-1][0]})

print('-=' * 30)
print('=== ranking dos alunos ===')
print(ranking)
for i , v in enumerate(ranking):
    print(f'{i+1} lugar {v[0]} com {v[1]}.')
    
    sleep(1)

print(f'Tiveram uma média de {media} pontos')

