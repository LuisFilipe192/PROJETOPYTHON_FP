from datetime import datetime
import random
import os

animais = []
tarefas = []

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def gerar_id():
    return str(random.randint(1000, 9999))

def salvar_animais():
    arquivo = open("animais.txt", "w", encoding="utf8")
    for animal in animais:
        arquivo.write(
            f"Id: {animal['id']}\n"
            f"Nome: {animal['nome']}\n"
            f"Espécie: {animal['espécie']}\n"
            f"Raça: {animal['raça']}\n"
            f"Idade: {animal['idade']}\n"
            f"Estado de saude: {animal['estado de saude']}\n"
            f"Data de chegada: {animal['data de chegada']}\n"
            f"Comportamento: {animal['comportamento']}\n\n"
        )
    arquivo.close()

def carregar_animais():

    animais.clear()

    try:
        arquivo = open("animais.txt", "r", encoding="utf8")
        linhas = arquivo.readlines()
    except FileNotFoundError:
        return print("arquivo não encontrado")

    #arquivo.close()

 
    animal = {}

    for linha in linhas:
        linha = linha.strip()
        if linha != "":

            '''
            partes = linha.split(":", 1)
            chave = partes[0].strip().lower()
            valor = partes[1].strip()
            animal[chave] = valor
            '''

            chave, valor = linha.split(":", 1)
            animal[chave.strip().lower()] = valor.strip()

            if animal:
                animais.append(animal)
              
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

    arquivo=open("animais.txt","a",encoding="utf8")
    arquivo.write(
        f"Id: {animal['id']}\n"
        f"Nome: {animal['nome']}\n"
        f"Espécie: {animal['espécie']}\n"
        f"Raça: {animal['raça']}\n"
        f"Idade: {animal['idade']}\n"
        f"Estado de saude: {animal['estado de saude']}\n"
        f"Data de chegada: {animal['data de chegada']}\n"
        f"Comportamento: {animal['comportamento']}\n\n")
    arquivo.close()

    print(f"Animal {animal['nome']} adicionado com sucesso!")

def listar_animais():

    limpar_tela()
    if len(animais) == 0:
        print("Nenhum animal cadastrado.")
        return

    print("Lista de Animais:\n")
    for a in animais:
        print(f"ID: {a['id']}\nNome: {a['nome']}\nEspécie: {a['espécie']}\nRaça: {a['raça']}\n"
              f"Idade: {a['idade']}\nSaúde: {a['estado de saude']}\nChegada: {a['data de chegada']}\n"
              f"Comportamento: {a['comportamento']}\n{'-'*40}")

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

def salvar_trefas():
    with open("tarefas.txt", "w", encoding="utf8") as arquivo:
        for t in tarefas:
             arquivo.write(
                f"Id Animal: {t['id_animal']}\n"
                f"Tipo: {t['tipo_tarefa']}\n"
                f"Data prevista: {t['data_prevista']}\n"
                f"Responsável: {t['responsavel']}\n\n"
            )

def carregar_tarefas():
    try:
        with open("tarefas.txt", "r", encoding="utf8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        return

    tarefas.clear()
    tarefa = {}

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            if tarefa:
                tarefas.append(tarefa)
                tarefa = {}
            continue

        chave, valor = linha.split(":", 1)
        tarefa[chave.strip().lower()] = valor.strip()

    if tarefa:
        tarefas.append(tarefa)

def registrar_tarefa():
    limpar_tela()

    if len(animais)== 0 :
        print("Nenhum animal cadastrado")
        return
    
    print("Animais disponiveis")
    for a in animais:
        print(f"{a['id']} - {a['nome']} ({a['espécie']})") 

    id_animal = input("\nDigite o ID do animal que deseja registrar uma tarefa: ").strip()
    
    for a in animais:
        if a['id'] == id_animal:
            animal = a
            break
        else:
            print("Animal não encontrado")
            break

    print("\nTipos de tarefa:")
    print("1 - Vacina\n")
    print("2 - Banho\n")
    print("3 - Consulta veterinária\n")
    print("4 - Treino\n")
    print("5 - Outra\n")

    opc = input("Escolha o tipo de tarefa").strip()
    tipos = {"1": "Vacina", "2": "Banho", "3": "Consulta veterinária", "4": "Treino", "5": "Outra"}
    tipo_tarefa = tipos.get(opc)

    data_prevista = input("Data prevista (DD/MM/AAAA): ").strip()
    responsavel = input("Responsavel: ").strip()

    tarefa = {
        "id_animal": id_animal,
        "tipo_tarefa": tipo_tarefa,
        "data_prevista": data_prevista,
        "responsavel": responsavel
    }

    tarefas.append(tarefa)
    salvar_trefas()

def listar_tarefas():
    limpar_tela()
    if len(tarefas) == 0:
        print("Nenhuma tarefa registrada.")
        return

    print("Lista de Tarefas:\n")

    for t in tarefas:
        nome_animal = "Desconhecido"

        for a in animais:
            if a["id"] == t["id_animal"]:
                nome_animal = a["nome"]
                break

        print(f"Animal: {nome_animal}")
        print(f"Tarefa: {t['tipo_tarefa']}")
        print(f"Data prevista: {t['data_prevista']}")
        print(f"Responsável: {t['responsavel']}")
        print("-" * 40)

def editar_tarefa():
    limpar_tela()
    if not tarefas:
        print("Nenhuma tarefa registrada.")
        return

    print("Tarefas atuais:\n")
    for idx, t in enumerate(tarefas, start=1):
        # mostra índice para facilitar edição
        nome_animal = "Desconhecido"
        for a in animais:
            if a.get('id') == t.get('id_animal'):
                nome_animal = a.get('nome')
                break
        print(f"{idx} - Animal: {nome_animal} | Tarefa: {t.get('tipo_tarefa')} | Data: {t.get('data_prevista')} | Responsável: {t.get('responsavel')}")

    escolha = input("\nDigite o número da tarefa que deseja editar (ou Enter para cancelar): ").strip()
    if escolha == "":
        print("Edição cancelada.")
        return

    try:
        i = int(escolha) - 1
        if i < 0 or i >= len(tarefas):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    t = tarefas[i]
    print("\nDeixe em branco para manter o valor atual.")
    nova_data = input(f"Data prevista [{t.get('data_prevista')}]: ").strip()
    if nova_data != "":
        t['data_prevista'] = nova_data

    novo_responsavel = input(f"Responsável [{t.get('responsavel')}]: ").strip()
    if novo_responsavel != "":
        t['responsavel'] = novo_responsavel

    print("\nTipos de tarefa:")
    print("1 - Vacina")
    print("2 - Banho")
    print("3 - Consulta veterinária")
    print("4 - Treino")
    print("5 - Outra")
    op = input(f"Tipo atual [{t.get('tipo_tarefa')}], escolha novo tipo (1-5) ou Enter para manter: ").strip()
    tipos = {"1": "Vacina", "2": "Banho", "3": "Consulta veterinária", "4": "Treino", "5": "Outra"}
    if op in tipos:
        t['tipo_tarefa'] = tipos[op]

    salvar_trefas()
    print("\nTarefa atualizada com sucesso!")

def excluir_tarefa():
    limpar_tela()
    if not tarefas:
        print("Nenhuma tarefa registrada.")
        return

    print("Tarefas atuais:\n")
    for idx, t in enumerate(tarefas, start=1):
        nome_animal = "Desconhecido"
        for a in animais:
            if a.get('id') == t.get('id_animal'):
                nome_animal = a.get('nome')
                break
        print(f"{idx} - Animal: {nome_animal} | Tarefa: {t.get('tipo_tarefa')} | Data: {t.get('data_prevista')} | Responsável: {t.get('responsavel')}")

    escolha = input("\nDigite o número da tarefa que deseja excluir (ou Enter para cancelar): ").strip()
    if escolha == "":
        print("Exclusão cancelada.")
        return

    try:
        i = int(escolha) - 1
        if i < 0 or i >= len(tarefas):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    confirmar = input(f"Tem certeza que deseja excluir a tarefa '{tarefas[i].get('tipo_tarefa')}'? (s/n): ").strip().lower()
    if confirmar in ['s', 'sim']:
        tarefas.pop(i)
        salvar_trefas()
        print("Tarefa excluída.")
    else:
        print("Exclusão cancelada.")

def menu_tarefas():
    print(("-"*10)+"MENU DE TAREFAS"+("-"*10))



carregar_tarefas()
carregar_animais()

while True:
    limpar_tela()
    print("====== MENU PRINCIPAL ======")
    print("1 - Adicionar Animal")
    print("2 - Listar Animais")
    print("3 - Editar Animal")
    print("4 - Excluir Animal")
    print("5 - Registrar Tarefa")
    print("6 - Listar Tarefas")
    print("7 - Editar Tarefa")
    print("8 - Excluir Tarefa")
    print("9 - Sair")

    op = input("Escolha uma opção: ").strip()

    if op == "1":
        adicionar_animal()
        input("\nPressione ENTER para voltar ao menu...")
    elif op == "2":
        listar_animais()
        input("\nPressione ENTER para voltar ao menu...")
    elif op == "3":
        editar_animal()
        input("\nPressione ENTER para voltar ao menu...")
    elif op == "4":
        excluir_animal()
        input("\nPressione ENTER para voltar ao menu...")
    elif op == "5":
        registrar_tarefa()
        input("\nPressione ENTER para voltar ao menu...")
    elif op == "6":
        listar_tarefas()
        input("\nPressione ENTER para voltar ao menu...")
    elif op == "7":
        editar_tarefa()
        input("\nPressione ENTER para voltar ao menu...")
    elif op == "8":
        excluir_tarefa()
        input("\nPressione ENTER para voltar ao menu...")
    elif op == "9":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        input("\nPressione ENTER para voltar ao menu...")