nomes = ["Rafaela", "André", "Marcela", "João", "Pedro", "Lorenzo", "Paula", "Marilia", "Ana"]
consulta = input("Qual nome deseja saber se esta na lista? ")

try:
    index_nome = nomes.index(consulta)
    print(" O nome está na lista!")
except Exception:
    print(" O nome não esta na lista!")