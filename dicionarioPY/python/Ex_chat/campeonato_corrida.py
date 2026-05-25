from random import randint
from time import sleep
from operator import itemgetter

corredores ={'piloto1': randint(100, 300),
             'piloto2': randint(100, 300),
             'piloto3': randint(100, 300),
             'piloto4': randint(100, 300)}

ranking = dict()

print('velocidade')
for k, v in corredores.items():
    print(f'{k} estava a {v}km.')
    sleep(1)
ranking = sorted(corredores.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('=== ranking dos corredores ===')
print(ranking)
for i , v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)