produto = {}

produto ["nome"] = input ("Nome:")
produto ["preco"] = float(input ("preco:"))

print("nome:", produto["nome"])
print("preco:", produto["preco"])

if produto ["preco"] >= 100:
    print("Classificação: Caro")
else:
    print ("Classificação: barato")