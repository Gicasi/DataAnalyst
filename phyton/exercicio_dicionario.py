funcionarios = [
    {"nome": "João", 
     "idade": 30, 
     "profissao": "Engenheiro"},

]

novo_funcionario = { #criando um dicionário vazio para armazenar os dados do novo funcionário
    "nome": input("Digite o nome: "),
    "idade": int(input("Digite a idade: ")),
    "profissao": input("Digite a profissão: ")
}

funcionarios.append(novo_funcionario)

print(funcionarios)

# CHAMADA DO EXERCICIO:
# criar um input que permita o usuário adicionar um novo funcionário em uma lista
# o novo funcionário terá nome, idade e profissão
# mostre a lista atualizada em tela
