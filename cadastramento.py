
# Função responsável pelo cadastro de colaboradores
def cadastrar_colaborador(id):
    print("-----MENU DE CADASTRO-----")
    while True:
        nome = input("Insira o nome do colaborador(0 para sair):")
        if nome == "0":
            break
        setor = input("Insira o setor do colaborador:")
        try: # Código para verificar se o pagamento é um inteiro
            pagamento = int(input("Insira o pagamento do colaborador:"))
        except ValueError:
            print("Valor inválido. Tente novamente")
            continue
        # Define as características do colaborador
        dic_colaborador = {"id" : id_global,
                           "nome": nome,
                           "setor" : setor,
                           "pagamento": pagamento}
        lista_colaboradores.append(dic_colaborador.copy()) # Coloca o colaborador dentro da lista
        break

# Função para consultar os colaboradores
def consultar_colaborador():
    print(("-----MENU DE CONSULTA-----"))
    while True:
        metodo = input("Qual método de consulta você deseja utilizar?\n"
                       "Consultar TODOS os colaboradores(1)\n"
                       "Consultar colaborador por ID(2)\n"
                       "Consultar colaborador por SETOR(3)\n"
                       "Voltar ao menu principal(4)\n"
                       "=>")

        if metodo not in "1234": # Verifica se o método é válido
            print("Método inválido, tente novamente\n")
            continue
        if metodo == "1":
            for colaborador in lista_colaboradores: # Passa por todos os dicionários da lista e....
                print("-"*30)
                for i,j in colaborador.items(): # .... mostra os pares key:value
                    print(f"{i}: {j}")
                print("-"*30)

        elif metodo == "2":
            ident = input("Insira a ID que você deseja consultar:")
            for colaborador in lista_colaboradores: # Semelhantemente, passa por todos os dicionários da lista
                if colaborador["id"] == int(ident): # No entanto, mostra apenas o dicionário com o id correspondente
                    print("-" * 30)
                    for i, j in colaborador.items():
                        print(f"{i}: {j}")
                    print("-" * 30)

        elif metodo == "3":
            setor_escolhido = input("Insira o setor que você deseja consultar:")
            for colaborador in lista_colaboradores:
                if colaborador["setor"] == setor_escolhido: # Nesse caso, mostra apenas os dicionários com a chave "setor" correspondentes
                    print("-" * 30)
                    for i, j in colaborador.items():
                        print(f"{i}: {j}")
                    print("-" * 30)

        else: # O método é igual a 4(sair)
            return

# Função para remover um colaborador
def remover_colaborador():
    print("-----MENU DE EXCLUSÃO-----")
    while True:
        try: # try e except para validar o dado inserido
            excluir = int(input("Insira a ID que você deseja excluir(0 para voltar): "))
        except ValueError:
            print("ID inválida")
            continue
        if excluir == 0:
            break
        for colaborador in lista_colaboradores: # Passa por todos os dicionários e exclui o que possui o id correspondente
            if colaborador["id"] == excluir:
                lista_colaboradores.remove(colaborador)
                break
        break

# Programa principal
lista_colaboradores = []
id_global = 0

print("Bem-vindo ao gerenciador de colaboradores do Marco Antonio Ferreira Pinto(RU:4411500)\n")
while True:
    print("-----MENU PRINCIPAL-----")
    funcao = input("\nQual função você deseja utilizar?\n"
          "Cadastrar colaborador(1)\n"
          "Consultar colaborador(2)\n"
          "Remover colaborador(3)\n"
          "Sair(4)\n"
          "=>")

    if funcao not in "1234": # Filtro para validar o dado inserido
        print("Função inválida, tente novamente\n")
        continue
    if funcao == "1":
        id_global += 1
        cadastrar_colaborador(id_global)
    elif funcao == "2":
        consultar_colaborador()
    elif funcao == "3":
        remover_colaborador()
    else: # funcao == 4, para encerrar o programa
        break

print("Encerrando....")