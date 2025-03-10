#Funçao para adicionar uma pessoa a lista

def adicionar_pessoas(lista,nome,idade,profissao):
    pessoa ={"nome":nome, "idade":idade,"profissao":profissao}
    lista.append(pessoa)

#função para mostrar as pessoas

def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome:{pessoa['nome']},Idade: {pessoa['idade']}, Profissao:{pessoa['profissao']}")

#lista para armazenar pessoas 
pessoas = []

#adicionando pessoas em uma lista
adicionar_pessoas(pessoas,"Ana",25,"Engenheira")
adicionar_pessoas(pessoas,"Leo",30,"Médico")
adicionar_pessoas(pessoas,"Lucas",33,"Professor")

#exibir a lista de pessoas
exibir_pessoas(pessoas)