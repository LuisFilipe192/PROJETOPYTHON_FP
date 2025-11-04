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

def carregar_animais():
    try:
        arquivo = open("animais.csv", "r", encoding="utf8")
    except FileNotFoundError:
        return

    linhas = arquivo.readlines()
    arquivo.close()

    animais.clear()

    animal = {}

    for linha in linhas:
        linha = linha.strip()
        if linha != "":
            partes = linha.split(":", 1)
            chave = partes[0].strip().lower()
            valor = partes[1].strip()

            animal[chave] = valor

            
            if chave == "comportamento":
                animais.append(animal)
                animal = {}
    

def adicionar_animal():
    limpar_tela()
    print("Digite as informações do animal:")
    animal = {
        "id": gerar_id(),
        "nome": input("Nome: ").lower().strip(),
        "espécie": input("Espécie: ").lower().strip(),
        "raça": input("Raça: ").lower().strip(),
        "idade": input("Idade: ").lower().strip(),
        "estado de saude": input("Estado de saude: ").lower().strip(),
        "data de chegada": datetime.today().strftime("%d/%m/%Y"),
        "comportamento": input("Comportamento: ").lower().strip()
    }

    animais.append(animal)

    arquivo=open("animais.csv","a",encoding="utf8")
    arquivo.write(
        f"Id: {animal['id']}\n"
        f"Nome: {animal['nome']}\n"
        f"Espécie: {animal['espécie']}\n"
        f"Raça: {animal['raça']}\n"
        f"Idade: {animal['idade']}\n"
        f"Estado de saude: {animal['estado de saude']}\n"
        f"Data de chegada: {animal['data de chegada']}\n"
        f"Comportamento: {animal['comportamento']}\n")
    arquivo.close()

    print(f"Animal {animal['nome']} adicionado com sucesso!")

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

    print("Animais cadastrados:")
    for animal in animais:
        print(f"ID: {animal['id']} \nNome: {animal['nome']} \nEspécie: {animal['espécie']}")

    id_busca = input("Digite o id do animal que deseja editar: ")

    for animal in animais:
        if animal["id"] == id_busca:
            print(f"Editando informações de {animal['nome']}: ")

            novo_nome = input("Novo nome (ou Enter para manter): ")
            if novo_nome != "":
                animal["nome"] = novo_nome

            nova_especie = input("Nova espécie (ou Enter para manter): ")
            if nova_especie != "":
                animal["espécie"] = nova_especie

            nova_raca = input("Nova raça (ou Enter para manter): ")
            if nova_raca != "":
                animal["raça"] = nova_raca

            while True:
                nova_idade = input("Nova idade (ou Enter para manter): ").strip()
                if nova_idade == "":
                    break
                try:
                    idade = int(nova_idade)
                    if idade < 0:
                        print("Idade não pode ser negativa. Tente novamente.")
                    else:
                        animal["idade"] = idade
                        break
                except ValueError:
                    print("Entrada inválida! Digite um número inteiro para a idade ou Enter para manter.")

            nova_saude = input("Novo estado de saúde (ou Enter para manter): ")
            if nova_saude != "":
                animal["estado de saude"] = nova_saude

            novo_comportamento = input("Novo comportamento (ou Enter para manter): ")
            if novo_comportamento != "":
                animal["comportamento"] = novo_comportamento

            print(f"Animal {animal['nome']} atualizado com sucesso!\n")

            salvar_animais()
            break
    else:
        print("Animal não encontrado.")

def excluir_animal():
    limpar_tela()
    if len(animais) == 0:
        print("Nenhum animal cadastrado.")
        return

    print("Animais cadastrados:")
    for animal in animais:
        print(f"ID: {animal['id']} \nNome: {animal['nome']} \nEspécie: {animal['espécie']}")

    id_busca = input("Digite o id do animal que deseja excluir: ").strip()
    for i, animal in enumerate(animais):
        if animal["id"] == id_busca:
            confirmar = input(f"Tem certeza que quer excluir {animal['nome']}? ").strip().lower()
            if confirmar in ["sim", "s"]:
                animais.pop(i)
                salvar_animais()
                print(f"{animal['nome']} excluído com sucesso.")
                break
            elif confirmar in ["nao", "não", "n"]:
                print("Exclusão cancelada.")
                break
            else:
                print("Resposta inválida. Exclusão cancelada.")
                break
    else:
        print("Animal não encontrado.")

    


carregar_animais()
limpar_tela()
print(("-"*10)+"MENU"+("-"*10))
while True:
    while True:
        escolha = input("1-adicionar\n2-listar\n3-editar\n4-excluir\n5-parar\nQual opção você quer: ").strip()
        if escolha in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Opção inválida, digite um número de 1 a 5.")

    if escolha =="1":
        print("Você escolheu adicionar seu animal.")
        adicionar_animal()        
    elif escolha =="2":
        print("Você escolheu listar os animais.")
        listar()
    elif escolha =="3":
        print("Você escolheu editar as informações de um animal.")
        editar_animal()
    elif escolha =="4":
        print("Você escolheu excluir um animal.")
        excluir_animal()
    elif escolha =="5":
        print("ENCERRANDO...")
        break
    else:
        print("escolha invalida, escolha um no intervalo 1-5.")