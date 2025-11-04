from datetime import datetime
import random
import os

animais=[]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def gerar_id():
    return str(random.randint(1000, 9999))

def salvar_animais():
    arquivo = open("animais.csv", "w", encoding="utf8")
    for animal in animais:
        arquivo.write(
            f"Id: {animal['id']}\n"
            f"Nome: {animal['nome']}\n"
            f"Espécie: {animal['espécie']}\n"
            f"Raça: {animal['raça']}\n"
            f"Idade: {animal['idade']}\n"
            f"Estado de saude: {animal['estado de saude']}\n"
            f"Data de chegada: {animal['data de chegada']}\n"
            f"Comportamento: {animal['comportamento']}\n"
        )
    arquivo.close()

def adicionar_animal():
    limpar_tela()
    animal = {
        "id": gerar_id().lower().strip(),
        "nome": input("Nome: ").lower().strip(),
        "espécie": input("Espécie: ").lower().strip(),
        "raça": input("Raça: ").lower().strip(),
        "idade": input("Idade: ").lower().strip(),
        "estado de saude": input("Estado de saúde: ").lower().strip(),
        "data de chegada": datetime.today().strftime("%d/%m/%Y"),
        "comportamento": input("Comportamento: ").lower().strip()
    }

    animais.append(animal)

    arquivo=open("animais.csv","a",encoding="utf8")
    arquivo.write(
        f"Id: {gerar_id()}\n"
        f"Nome: {animal['nome']}\n"
        f"Espécie: {animal['espécie']}\n"
        f"Raça: {animal['raça']}\n"
        f"Idade: {animal['idade']}\n"
        f"Estado de saúde: {animal['estado de saude']}\n"
        f"Data de chegada: {animal['data de chegada']}\n"
        f"Comportamento: {animal['comportamento']}\n")
    arquivo.close()

    print(f"\nCachorro {animal['nome']} adicionado com sucesso!\n")

def listar():
    limpar_tela()
    print()
    arquivo=open("animais.csv","r",encoding="utf8")
    linhas=arquivo.readlines()
    arquivo.close()

    if len(linhas)==0:
        print("nenhum animal foi cadastrado")
    else:
        print("Lista de nomes:")
        for linha in linhas:
            print(linha.strip())

def editar_animal():
    limpar_tela()
    id_busca = input("Digite o id do animal que deseja editar: ")

    for animal in animais:
        if animal["id"] == int(id_busca):
            print(f"Editando informações de {animal['nome']}: ")

            novo_nome = input("Novo nome (ou Enter para manter): ")
            if novo_nome != "":
                animal["nome"] = novo_nome

            nova_idade = input("Nova idade (ou Enter para manter): ")
            if nova_idade != "":
                animal["idade"] = int(nova_idade)

            nova_saude = input("Novo estado de saúde (ou Enter para manter): ")
            if nova_saude != "":
                animal["estado de saude"] = nova_saude

            print(f"Animal {animal['nome']} atualizado com sucesso!\n")

            salvar_animais()
            break
    else:
        print("Animal não encontrado.")

while True:
    escolha=input("1-adicionar\n2-listar\n3-editar\n4-parar\nqual opçao vc quer: ")
    if escolha =="1":
        adicionar_animal()
    elif escolha =="2":
        listar()
    elif escolha =="3":
        editar_animal()
    elif escolha =="4":
        break


