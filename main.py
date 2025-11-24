from datetime import datetime
import random
import os

animais = []
tarefas = []
historico = []

def id_existe(novo_id):
    for animal in animais:
        if animal["id"] == novo_id:
            return True 
    return False 

def menu_CRUD():
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
        print("9 - Exibir Alertas")
        print("10- Sair")
        print("11- Mostrar Atrasos")
        print("12- Registrar Histórico Médico")
        print("13- Listar Histórico Médico")
        
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            adicionar_animal()
        elif op == "2":
            listar_animais()
        elif op == "3":
            editar_animal()
        elif op == "4":
            excluir_animal()
        elif op == "5":
            registrar_tarefa()
        elif op == "6":
            listar_tarefas()
        elif op == "7":
            editar_tarefa()
        elif op == "8":
            excluir_tarefa()
        elif op == "9":
            exibir_alerta()
        elif op == "10":
            print("Saindo...")
            break
        elif op == "11":
            atraso()
        elif op == "12":
            registrar_historico()
        elif op == "13":
            listar_historico()
        else:
            print("Opção inválida.")

        escolha = input("Deseja voltar O MENU? (s/n) ").lower()
        if escolha == "n":
            break
        elif escolha =="s":
            continue
        else:
            print("Escolha invalida!")
            while True:
                esc = input("Deseja voltar O MENU? (s/n) ").lower()
                if esc == "n":
                    return
                elif esc =="s":
                    return menu_CRUD()
                else:
                    print("Opção inválida!")

            
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def gerar_id():
    while True:
        novo_id = str(random.randint(1000, 9999))
        if not id_existe(novo_id):
            return novo_id


def salvar_animais():
    with open("animais.txt", "w", encoding = "utf8") as arquivo:
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


def carregar_animais():
    
    animais.clear()
    try:
        arquivo = open("animais.txt", "r", encoding = "utf8")
        linhas = arquivo.readlines()
    except FileNotFoundError:
        return print("Arquivo não encontrado")
    arquivo.close()
 
    animal = {}
    for linha in linhas:
        linha = linha.strip()
        if linha == "":
            if animal:
                animais.append(animal)
                animal = {}
        else:
            chave, valor = linha.split(":", 1)
            animal[chave.strip().lower()] = valor.strip()
    if animal:
        animais.append(animal)
              

def adicionar_animal():
    limpar_tela()
    print("Digite as informações do animal: ")
    while True:
        nome = input("Nome: ")
        if nome == "" or any(letra.isdigit()for letra in nome):
            print("Nome não pode ter números e nem ficar vazio.")
        else:
            break
    while True:
        especie = input("Espécie: ")
        if especie == "" or any(letra.isdigit()for letra in especie):
            print("Espécie não pode ter números e nem ficar vazio.")
        else:
            break
    while True:
        raça = input("Raça: ")
        if raça == "" or any(letra.isdigit()for letra in raça):
            print("Raça não pode ter números e nem ficar vazio.") 
        else:
            break
    while True:
        idade_input = input("Idade: ")
        try:
            idade = int(idade_input)
            if idade < 0:
                print("Não existe idade negativa, digite novamente")
            else:
                break
        except ValueError:
            print("Digite a idade como um número inteiro")
    while True:
        estado = input("Estado de saúde: ")
        if estado == "" or any(letra.isdigit()for letra in estado):
            print("Estado de saúde não pode ter números e nem ficar vazio.")
        else:
            break
    while True:
        comportamento = input("Comportamento: ")
        if comportamento == "" or any(letra.isdigit()for letra in comportamento):
            print("Comportamento não pode ter números e nem ficar vazio.")
        else:
            break
    
    animal = {
        "id": gerar_id(),
        "nome": nome.lower().strip(),
        "espécie": especie.lower().strip(),
        "raça": raça.lower().strip(),
        "idade": str(idade).strip(),
        "estado de saude": estado.lower().strip(),
        "data de chegada": datetime.today().strftime("%d/%m/%Y"),
        "comportamento": comportamento.lower().strip()
    }

    animais.append(animal)
    arquivo = open("animais.txt","a",encoding = "utf8")
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
        print(f"ID: {a['id']}\n"
              f"Nome: {a['nome']}\n"
              f"Espécie: {a['espécie']}\n"
              f"Raça: {a['raça']}\n"
              f"Idade: {a['idade']}\n"
              f"Saúde: {a['estado de saude']}\n"
              f"Chegada: {a['data de chegada']}\n"
              f"Comportamento: {a['comportamento']}\n"
              f"{'-'*40}")
        

def editar_animal():
    limpar_tela()
    print("Animais cadastrados:")
    for animal in animais:
        print(f"ID: {animal['id']}\n"
              f"Nome: {animal['nome']}\n"
              f"Espécie: {animal['espécie']}\n"
              f"{'-'*50}")
    id_busca = input("Digite o id do animal que deseja editar: ")

    for a in animais:
        if a["id"] == id_busca:
            animal = a
            break
    else:
        print("Animal não encontrado.")
        return
    
    print("\nDeixe em branco caso não deseje alterar e pressione Enter para continuar.\n")
    while True:
        nome = input(f"Nome atual - {animal['nome']}: ").strip()
        if nome == "":
            break
        if any(c.isdigit() for c in nome):
            print("\nNão pode ter números.\n")
        else:
            animal["nome"] = nome.lower()
            break
    while True:
        especie = input(f"Espécie atual - {animal['espécie']}: ").strip()
        if especie == "":
            break
        if any(c.isdigit() for c in especie):
            print("\nNão pode ter números.\n")
        else:
            animal["espécie"] = especie.lower()
            break
    while True:
        raca = input(f"Raça atual - {animal['raça']}: ").strip()
        if raca == "":
            break
        if any(c.isdigit() for c in raca):
            print("\nNão pode ter números.\n")
        else:
            animal["raça"] = raca.lower()
            break
    while True:
        idade_input = input(f"Idade atual - {animal['idade']}: ").strip()
        if idade_input == "":
            break
        try:
            idade = int(idade_input)
            if idade < 0:
                print("\nNão pode ser um valor negativo.\n")
            else:
                animal["idade"] = str(idade)
                break
        except ValueError:
            print("\nTem que ser um número inteiro\n")
    while True:
        estado = input(f"Estado de saúde atual - {animal['estado de saude']}: ").strip()
        if estado == "":
            break
        if any(c.isdigit() for c in estado):
            print("\nNão pode ter números.\n")
        else:
            animal["estado de saude"] = estado.lower()
            break
    while True:
        comportamento = input(f"Comportamento atual - {animal['comportamento']}: ").strip()
        if comportamento == "":
            break
        if any(c.isdigit() for c in comportamento):
            print("\nNão pode ter números.\n")
        else:
            animal["comportamento"] = comportamento.lower()
            break

    salvar_animais()
    print("Animal atualizado")


def excluir_animal():
    limpar_tela()
    if len(animais) == 0:
        print("Nenhum animal cadastrado.")
        return
    print("Animais cadastrados:")
    for animal in animais:
        print(f"ID: {animal['id']}\n"
              f"Nome: {animal['nome']}\n"
              f"Espécie: {animal['espécie']}\n")
    while True:
        id_busca = input("Digite o id do animal que deseja excluir: ").strip()
        for animal in animais:
            if animal["id"] == id_busca:
                confirmar = input(
                    f"Tem certeza que quer excluir {animal['nome']}?\n(s/n): "
                ).strip().lower()
                if confirmar in ["sim", "s"]:
                    animais.remove(animal)
                    salvar_animais()
                    print(f"\n{animal['nome']} excluído com sucesso.\n")
                    return
                elif confirmar in ["nao", "não", "n"]:
                    print("\nExclusão cancelada.\n")
                    return
                else:
                    print("\nResposta inválida. Exclusão cancelada.\n")
                    return
        print("\nID não encontrado. Tente novamente.\n")


def salvar_tarefas():
    try:
        with open("tarefas.txt", "w", encoding = "utf8") as arquivo:
            for t in tarefas:
                 arquivo.write(
                    f"Id Animal: {t.get('id_animal')}\n"
                    f"Tipo: {t.get('tipo_tarefa')}\n"
                    f"Data prevista: {t.get('data_prevista')}\n"
                    f"Responsável: {t.get('responsavel')}\n\n"
                )
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")
             

def carregar_tarefas():
    try:
        with open("tarefas.txt", "r", encoding="utf8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        return
    
    tarefas.clear()
    tarefa = {}

    conversao = {
        "id animal": "id_animal",
        "tipo": "tipo_tarefa",
        "tipo tarefa": "tipo_tarefa",
        "data prevista": "data_prevista",
        "responsável": "responsavel",
        "responsavel": "responsavel"
    }

    for linha in linhas:
        linha = linha.strip()

        if not linha:
            if tarefa:
                tarefas.append(tarefa)
                tarefa = {}
            continue

        if ":" not in linha:
            continue

        chave, valor = linha.split(":", 1)
        chave = chave.strip().lower()
        valor = valor.strip()

        nova_chave = conversao.get(chave, chave)

        tarefa[nova_chave] = valor

    if tarefa:
        tarefas.append(tarefa)

    for t in tarefas:
        t.setdefault("id_animal", "")
        t.setdefault("tipo_tarefa", "")
        t.setdefault("data_prevista", "")
        t.setdefault("responsavel", "")


def salvar_historico():
    with open("historico_medico.txt", "w", encoding = "utf8") as arquivo:
        for item in historico:
            arquivo.write(
                f"Id Animal: {item['id_animal']}\n"
                f"Data: {item['data']}\n"
                f"Tipo Evento: {item['tipo_evento']}\n"
                f"Detalhes: {item['detalhes']}\n\n"
            )


def carregar_historico():
    try:
        with open("historico_medico.txt", "r", encoding="utf8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        return

    historico.clear()
    item = {}

    for linha in linhas:
        linha = linha.strip()

        if not linha:
            if item and "id_animal" in item and item["id_animal"]:
                historico.append(item)
            item = {}
            continue
        try:
            chave, valor = linha.split(":", 1)
            chave = chave.strip().lower()
            valor = valor.strip()

            item[chave] = valor
        except ValueError:
            continue
    if item and "id_animal" in item and item["id_animal"]:
        historico.append(item)


def registrar_historico():
    limpar_tela()
    if not animais:
        print("Nenhum animal cadastrado.")
        return
    
    print("Animais disponíveis:")
    for a in animais:
        print(f"{a['id']} - {a['nome']} ({a['espécie']})") 
        
    id_animal = input("\nDigite o ID do animal para registrar o histórico: ").strip()
    
    nome_animal = ""
    for a in animais:
        if a["id"] == id_animal:
            nome_animal = a["nome"]
            break
    else:
        print("Animal não encontrado")
        return

    print(f"\n--- Registrando Histórico para {nome_animal} ---")
    
    while True:
        data_evento = input("Data do Evento (DD/MM/AAAA): ").strip()
        try:
            data_convertida = datetime.strptime(data_evento, "%d/%m/%Y").date()

            if data_convertida < datetime.today().date():
                print("A data não pode estar no passado.")
                continue

            break
        except ValueError:
            print("Data inválida! Digite no formato DD/MM/AAAA e usando uma data real.")

    tipo_evento = input("Tipo de Evento (Ex: Vacina, Castração, Cirurgia, Medicamento): ").strip()
    detalhes = input("Detalhes/Descrição do Evento: ").strip()

    item_historico = {
        "id_animal": id_animal,
        "data": data_evento,
        "tipo_evento": tipo_evento,
        "detalhes": detalhes
    }
    
    historico.append(item_historico)
    salvar_historico()
    print(f"\nHistórico médico para {nome_animal} registrado com sucesso!")


def listar_historico():
    limpar_tela()
    if not historico:
        print("Nenhum registro de histórico médico encontrado.")
        return
    
    print("Animais com Histórico Registrado:")
    ids_com_historico = {item['id_animal'] for item in historico}
    
    if not ids_com_historico:
        print("Nenhum registro de histórico médico encontrado.")
        return

    for a in animais:
        if a['id'] in ids_com_historico:
            print(f"{a['id']} - {a['nome']} ({a['espécie']})") 
            
    id_busca = input("\nDigite o ID do animal para listar o Histórico Médico: ").strip()

    nome_animal = next((a['nome'] for a in animais if a['id'] == id_busca), "Desconhecido")
    
    registros_animal = [item for item in historico if item['id_animal'] == id_busca]
    
    if not registros_animal:
        print(f"\nNenhum registro de histórico médico encontrado para o animal ID {id_busca} ({nome_animal}).")
        return

    print(f"\n===== HISTÓRICO MÉDICO DE {nome_animal.upper()} =====\n")
    
    registros_ordenados = sorted(registros_animal, key=lambda x: datetime.strptime(x['data'], "%d/%m/%Y"), reverse=True)
    
    for idx, item in enumerate(registros_ordenados, 1):
        print(f"--- Evento {idx} ---")
        print(f"Data: {item['data']}")
        print(f"Tipo: {item['tipo_evento']}")
        print(f"Detalhes: {item['detalhes']}")
        print("-" * 20)


def registrar_tarefa():
    limpar_tela()
    if len(animais) == 0:
        print("Nenhum animal cadastrado")
        return
    
    print("Animais disponíveis:")
    for a in animais:
        print(f"{a['id']} - {a['nome']} ({a['espécie']})")

    while True:
        id_animal = input("\nDigite o ID do animal que deseja registrar uma tarefa: ").strip()

        animal = None
        for a in animais:
            if a["id"] == id_animal:
                animal = a
                break

        if animal is not None:
            break
        else:
            print("Animal não encontrado. Tente novamente.")

    print(f"\nAnimal selecionado: {animal['nome']} ({animal['espécie']})")

    print("\nTipos de tarefa:")
    print("1 - Vacina")
    print("2 - Banho")
    print("3 - Consulta veterinária")
    print("4 - Treino")
    print("5 - Outra")

    tipos = {"1": "Vacina", "2": "Banho", "3": "Consulta veterinária", "4": "Treino", "5": "Outra"}

    while True:
        opc = input("Escolha o tipo de tarefa: ").strip()
        tipo_tarefa = tipos.get(opc)
        if opc == "5":
            while True:
                outra = input("Digite o tipo da tarefa: ").strip()

                if outra == "":
                    print("O campo não pode estar vazio.")
                elif any(c.isdigit() for c in outra):
                    print("Digite apenas texto, sem números.")
                else:
                    tipo_tarefa = outra
                    break
            break

        if tipo_tarefa:
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 5.")

    while True:
        data_prevista = input("Data prevista (DD/MM/AAAA): ").strip()
        try:
            data_tarefa = datetime.strptime(data_prevista, "%d/%m/%Y").date()
            if data_tarefa < datetime.today().date():
                print("A data não pode estar no passado.")
                continue
            break
        except ValueError:
            print("Digite no formato DD/MM/AAAA usando uma data real.")

    while True:
        responsavel = input("Responsável: ").strip()
        if responsavel == "" or any(c.isdigit() for c in responsavel):
            print("Responsável não pode conter números e nem estar vazio.")
        else:
            break

    tarefa = {
        "id_animal": id_animal,
        "tipo_tarefa": tipo_tarefa,
        "data_prevista": data_prevista,
        "responsavel": responsavel
    }

    tarefas.append(tarefa)
    salvar_tarefas()
    print("\nTarefa registrada com sucesso!")


def listar_tarefas():
    limpar_tela()
    if len(tarefas) == 0:
        print("Nenhuma tarefa registrada.")
        return

    print("Lista de Tarefas:\n")

    for t in tarefas:
        id_animal = t.get("id_animal") or t.get("id animal") or t.get("id") or "?"

        tipo = t.get("tipo_tarefa") or t.get("tipo") or "Desconhecido"
        data_prevista = t.get("data_prevista") or t.get("data prevista") or "Desconhecida"
        responsavel = t.get("responsavel") or "Desconhecido"

        nome_animal = "Desconhecido"
        for a in animais:
            if a.get("id") == id_animal:
                nome_animal = a.get("nome")
                break

        print(f"Animal: {nome_animal}")
        print(f"Tarefa: {tipo}")
        print(f"Data prevista: {data_prevista}")
        print(f"Responsável: {responsavel}")
        print("-" * 40)


def editar_tarefa():
    limpar_tela()
    if not tarefas:
        print("Nenhuma tarefa registrada.")
        return

    print("Tarefas atuais:\n")
    for idx, t in enumerate(tarefas, start=1):
        nome_animal = "Desconhecido"
        for a in animais:
            if a.get("id") == t.get("id_animal"):
                nome_animal = a.get("nome")
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

    while True:
        nova_data = input(f"Data prevista [{t.get('data_prevista')}]: ").strip()

        if nova_data == "":
            break
        try:
            data_teste = datetime.strptime(nova_data, "%d/%m/%Y").date()
            if data_teste < datetime.today().date():
                print("A data não pode estar no passado.")
                continue
            t["data_prevista"] = nova_data
            break
        except ValueError:
            print("Digite a data no formato DD/MM/AAAA e usando uma data válida.")

    while True:
        novo_responsavel = input(f"Responsável [{t.get('responsavel')}]: ").strip()
        if novo_responsavel == "":
            break
        if any(c.isdigit() for c in novo_responsavel):
            print("O responsável não pode conter números. Tente novamente.")
        else:
            t["responsavel"] = novo_responsavel
            break

    print("\nTipos de tarefa:")
    print("1 - Vacina")
    print("2 - Banho")
    print("3 - Consulta veterinária")
    print("4 - Treino")
    print("5 - Outra")

    tipos = {"1": "Vacina", "2": "Banho", "3": "Consulta veterinária", "4": "Treino", "5": "Outra\n"}
    op = input(f"Tipo atual [{t.get('tipo_tarefa')}], escolha novo tipo (1-5) ou Enter para manter: ").strip()

    if op == "5":
        while True:
            outro = input("Digite o novo tipo de tarefa: ").strip()
            if outro == "" or any(c.isdigit() for c in outro):
                print("Digite apenas letras para o nome da tarefa.")
            else:
                t["tipo_tarefa"] = outro
                break

    elif op in tipos:
        t["tipo_tarefa"] = tipos[op]

    salvar_tarefas()
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
            if a.get('id') == t.get("id_animal"):
                nome_animal = a.get('nome')
                break
        print(f"{idx} - Animal: {nome_animal} | Tarefa: {t.get("tipo_tarefa")} | Data: {t.get("data_prevista")} | Responsável: {t.get("responsavel")}")
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
    confirmar = input(f"Tem certeza que deseja excluir a tarefa '{tarefas[i].get("tipo_tarefa")}'? (s/n): ").strip().lower()
    if confirmar in ["s", "sim"]:
        tarefas.pop(i)
        salvar_tarefas()
        print("Tarefa excluída.")
    else:
        print("Exclusão cancelada.")


def dias_para_tarefa(data_prevista_str):
    try:
        data_prevista = datetime.strptime(data_prevista_str,"%d/%m/%Y" )
        hoje = datetime.today()
        return (data_prevista - hoje).days
    except ValueError:
        return None
    

def exibir_alerta():
    limpar_tela()
    if not tarefas:
        print("Nenhuma tarefa registrada.")
        return 
    print("===== ALERTAS E DIAS RESTANTES PARA AS PRÓXIMAS TAREFAS =====\n")
    for t in tarefas:
        dias = dias_para_tarefa(t["data_prevista"])
        nome_animal = "Desconhecido"
        for a in animais:
            if a ["id"] == t["id_animal"]:
                nome_animal = a["nome"]
                break
        
        if dias is None:
            status = f" Data inválida! ({t["data_prevista"]})"
        elif dias < 0:
             status = f" Atrasada há {-dias} dia(s)! ({t["data_prevista"]})"
        elif dias <= 3:  
            status = f" Faltam {dias} dia(s) — Tarefa está próxima! ({t["data_prevista"]})"
        else:
             status = f"Faltam {dias} dia(s) ({t["data_prevista"]})"
        print(f"Animal: {nome_animal}")
        print(f"Tarefa: {t["tipo_tarefa"]}")
        print(f"Responsável: {t["responsavel"]}")
        print(f"Status: {status}")
        print("-" * 40)


def atraso():
    limpar_tela()
    atrasadas = []
    for t in tarefas:
        if dias_para_tarefa(t["data_prevista"]) < 0:
            atrasadas.append(t)

    if not atrasadas:
        print("Nenhuma tarefa atrasada")
        
    for t in atrasadas:
        nome = "Desconhecido"
        for a in animais:
            if a["id"] == t["id_animal"]:
                nome = a["nome"]
                break
        
        dias_atraso = abs(dias_para_tarefa(t["data_prevista"]))
            
        print(f"\nAnimal: {nome}")
        print(f"Tarefa: {t["tipo_tarefa"]}")
        print(f"Responsável: {t["responsavel"]}")
        print(f"Atrasada á {dias_atraso} dia(s)\n")



carregar_tarefas()
carregar_animais()
carregar_historico()

menu_CRUD()
