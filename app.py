# Criando um dicionário vazio
pessoas = {}

# Adicionando pessoas ao dicionário
pessoas["Alice"] = 25
pessoas["Bruno"] = 30
pessoas["Carla"] = 22
pessoas["Diego"] = 28

# Percorrendo o dicionário e mostrando as informações
for nome, idade in pessoas.items():
    print(f"Nome: {nome}, Idade: {idade}")
