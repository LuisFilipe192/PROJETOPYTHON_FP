from datetime import datetime
import random
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def gerar_id():
    return str(random.randint(1000, 9999))

def adicionar_animal():
    limpar_tela()
    animal = {
        "id": gerar_id(),
        "nome": input("Nome: "),
        "raça": input("Raça: "),
        "idade": input("Idade: "),
        "estado de saúde": input("Estado de saúde: "),
        "data de chegada": datetime.today().strftime("%d/%m/%Y"),
        "comportamento": input("Comportamento: ")
    }

    arquivo=open("animais.csv","a",encoding="utf8")
    arquivo.write(f"Id: {gerar_id()}\n")
    arquivo.write(f"Nome: {animal['nome']}\n")
    arquivo.write(f"Raça: {animal['raça']}\n")        
    arquivo.write(f"Idade: {animal['idade']}\n")                
    arquivo.write(f"Estado de saúde: {animal['estado de saúde']}\n")
    arquivo.write(f"Data de chegada: {animal['data de chegada']}\n")
    arquivo.write(f"Comportamento: {animal['comportamento']}\n")
    arquivo.close()

    print(f"\nCachorro {animal['nome']} adicionado com sucesso!\n")

def listar():
    limpar_tela()
    print()
    arquivo=open("animais.csv","r",encoding="utf8")
    animais=arquivo.readlines()
    arquivo.close()

    if len(animais)==0:
        print("nenhum animal foi cadastrado")
    else:
        print("Lista de nomes:")
        for i in range(len(animais)):
            print(animais[i].strip())

adicionar_animal()
listar()