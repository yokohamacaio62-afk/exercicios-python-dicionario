from random import randint
from time import sleep
from operator import itemgetter

alunos = {'aluno1':  randint(0, 10),
          'aluno2':  randint(0, 10),
          'aluno3':  randint(0, 10),
          'aluno4':  randint(0, 10)}
ranking = dict ()

for k, v in alunos.items():
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted (alunos.items(), key=itemgetter(1), reverse=True)

print('o melhor aluno', {ranking[0][0]})
print('o pior aluno', {ranking(-1)[0]})

print('-=' * 30)
print('=== ranking dos alunos ===')
print(ranking)
for i , v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)