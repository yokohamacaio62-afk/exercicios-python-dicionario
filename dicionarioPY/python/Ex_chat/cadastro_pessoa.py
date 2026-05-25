pessoas = []
pessoa = {}

pessoa ["nome"] = input("Nome:")
pessoa ["idade"] = int(input("Idade:"))

pessoas.append(pessoa.copy())

for i in pessoas:
    print(pessoa["nome"], "tem", pessoa ["idade"], "anos")
