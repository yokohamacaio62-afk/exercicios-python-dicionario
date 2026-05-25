aluno = {}

aluno ["nome"] = input("Nome:")
aluno ["nota 1"] = int(input("Nota1 :"))
aluno ["nota 2"] = int(input("Nota2 :"))

media = (aluno["nota 1"] + aluno["nota 2"])/2

aluno["media"] = media

if aluno[media] >= 7:
    print("Aluno aprovado")
else:
    print("reprovado")

