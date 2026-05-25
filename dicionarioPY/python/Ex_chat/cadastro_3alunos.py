aluno = {}
alunos = []

for i in range(3):
    aluno ["nome"] = input("Nome:")
    aluno ["nota1"] = int(input("Nota1:"))
    aluno ["nota2"] = int(input("Nota2:"))

    media = (aluno["nota1"] + aluno["nota2"])/2


    aluno ["media"] = media

    alunos.append(aluno)

    if aluno["media"] >= 7:
        print(aluno["nome"],"aluno passou de ano")
    else:
        print(aluno["nome"],"aluno reprovou")