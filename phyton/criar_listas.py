# lista_cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
# lista_nomes = ["Alice", "Bob", "Charlie", "David", "Ane"]
# lista_estados = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia", "Paraná"]
# lista_mista = [1, "dois", 3.0, True, "cinco"]

# print("Lista de cores:", lista_cores)
# print("Lista de nomes:", lista_nomes)
# print("Lista de estados:", lista_estados)
# print("Lista mista:", lista_mista)


# outra forma de criar uma lista:

vendedores = []

novo_vendedor = "Wagner"

vendedores.append(novo_vendedor) #adicionando por meio de variavel
vendedores.append("Augusto") #adicionando diretamente
vendedores.append("Romeu")

print(vendedores)

novo_vendedor = input("Informe o nome do novo vendedor: ") #pedindo ao usuario para adicionar
vendedores.append(novo_vendedor)
print(vendedores)


#append() = adiciona um item a lista