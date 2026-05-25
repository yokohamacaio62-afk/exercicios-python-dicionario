filme = {}

filme ["nome"] = input("Filme:")
filme ["ano"] = int(input("Ano:"))
filme ["nota"] = int(input("Nota:"))

if filme["nota"] >= 8:
    print("Filme excelente")
else:
    print("Filme mediano")