"""
Módulo de Gerenciamento de Sistema de Automação de Serviços.

Este script contém as funções e classes necessárias para gerenciar o fluxo de 
cadastros de clientes, técnicos e ordens de serviço. As principais funcionalidades
incluem validação de duplicidade por CPF, manipulação de catálogos e navegação 
através de menus interativos em modo texto.
"""

import enum

def validar_duplicidade(lista : list, cpf : str) -> tuple:
        for indice, objeto in enumerate(lista):
            if objeto.cpf == cpf:
                return indice, objeto
        return -1

class StatusOrdem(enum.Enum):
    ABERTA = 1
    ANDAMENTO = 2
    FINALIZADA = 3
    CANCELADA = 4


class Cliente():
    # Representa a entidade de um cliente individual com suas informações de contato.
    def __init__(self, cpf, nome, telefone, email, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco


class CatalogoClientes():
    # Gerencia o armazenamento em lote, alteração e exclusão dos objetos Cliente.
    def __init__(self):
        self.lista = []

    def cadastrar(self, cliente : object):
        self.lista.append(cliente)

    def modificar(self, indice : int):
        while True:
            print("\n" + "="*35)
            print("         MODIFICAR CLIENTE")
            print("="*35)
            print("[1] Telefone")
            print("[2] E-mail")
            print("[3] Endereço")
            print("[0] Voltar")
            print("="*35)
            
            escolha = input("O que deseja modificar: ")
            
            match escolha.lower():
                case "1":
                    self.lista[indice].telefone = input("\nInsira o novo número de telefone: ")
                case "2":
                    self.lista[indice].email = input("\nInsira o novo E-mail: ")
                case "3":
                    self.lista[indice].endereco = input("\nInsira o novo endereço: ")
                case "0":
                    break
                case _:
                    print("\nOpção inválida! tente novamente.")

    def remover(self, objeto : object):
        self.lista.remove(objeto)


class CadastroCliente():
    # Controla a interface de menu e captura de dados para as operações do catálogo de clientes.
    def __init__(self, catalogo : CatalogoClientes):
        self.catalogo = catalogo

    def dados_cliente(self, cpf: str) -> object:
        nome = input("Insira o nome do cliente: ")
        telefone = input("Insira o telefone do cliente: ")
        email = input("Insira o e-mail do cliente: ")
        endereco = input("Insira o endereço do cliente: ")
        return Cliente(cpf, nome, telefone, email, endereco)

    def menu(self):
        while True:
            print("\n" + "="*35)
            print("       CADASTRO DE CLIENTES")
            print("="*35)
            print("[1] Cadastrar novo cliente")
            print("[2] Modificar um cadastro")
            print("[3] Remover um cadastro")
            print("[4] Procurar um cadastro")
            print("[0] Retornar")
            print("="*35)
            
            escolha = input("Escolha uma opção: ")
            
            match escolha:
                case "1":
                    cpf = input("\nInsira o CPF do cliente: ")
                    resultado = validar_duplicidade(self.catalogo.lista, cpf)

                    if resultado != -1:
                        print("Cliente já está cadastrado.")
                    else:
                        cliente = self.dados_cliente(cpf)
                        self.catalogo.cadastrar(cliente)
                        print("Cadastro feito com sucesso.")
                        
                case "2":
                    cpf = input("\nInsira o CPF do cliente: ")
                    resultado = validar_duplicidade(self.catalogo.lista, cpf)
                    if resultado == -1:
                        print("Cliente não localizado.")
                    else:
                        indice, _ = resultado
                        self.catalogo.modificar(indice)
                        print("\nCadastro modificado com sucesso")

                case "3":
                    cpf = input("\nInsira o CPF do cliente: ")
                    resultado = validar_duplicidade(self.catalogo.lista, cpf)

                    if resultado == -1:
                        print("Cliente não localizado.")
                    else:
                        _, cliente = resultado
                        self.catalogo.remover(cliente)
                        print("Cadastro removido com sucesso.")

                case "4":
                    cpf = input("\nInsira o CPF do cliente: ")
                    resultado = validar_duplicidade(self.catalogo.lista, cpf)

                    if resultado == -1:
                        print("Cliente não localizado.")
                    else:
                        _, cliente = resultado
                        print(f"\nNome: {cliente.nome} | Telefone: {cliente.telefone} | E-mail: {cliente.email} | Endereço: {cliente.endereco}")

                case "0":
                    break

                case _:
                    print("\nOpção inválida")


class Tecnico():
    # Representa a entidade de um técnico operacional e suas interações com as ordens de serviço.
    def __init__(self, cpf, nome, especialidade):
        self.cpf = cpf
        self.nome = nome
        self.especialidade = especialidade


class CatalogoTecnico():
    # Gerencia a coleção de objetos do tipo Tecnico, permitindo alterações em suas qualificações.
    def __init__(self):
        self.lista = []
    
    def cadastrar(self, tecnico : object):
        self.lista.append(tecnico)

    def modificar(self, indice : int):
        while True:
            print("\n" + "="*35)
            print("         MODIFICAR TÉCNICO")
            print("="*35)
            print("[1] Especialidade")
            print("[0] Voltar")
            print("="*35)
            
            escolha = input("O que deseja modificar: ")
            
            match escolha.lower():
                case "1":
                    self.lista[indice].especialidade = input("\nInsira a nova especialidade: ")
                case "0":
                    break
                case _:
                    print("\nOpção inválida! tente novamente.")

    def remover(self, objeto : object):
        self.lista.remove(objeto)


class CadastroTecnico():
    # Controla a interface de menu e a manipulação do fluxo de dados para o catálogo de técnicos.
    def __init__(self, catalogo : CatalogoTecnico):
        self.catalogo = catalogo

    def dados_tecnico(self, cpf : str) -> object:
        nome = input("Insira o nome do técnico: ")
        especialidade = input("Insira a especialidade do técnico: ")
        return Tecnico(cpf, nome, especialidade)

    def menu(self):
        while True:
            print("\n" + "="*35)
            print("       CADASTRO DE TÉCNICOS")
            print("="*35)
            print("[1] Cadastrar novo técnico")
            print("[2] Modificar um cadastro")
            print("[3] Remover um cadastro")
            print("[4] Procurar um cadastro")
            print("[0] Retornar")
            print("="*35)
            
            escolha = input("Escolha uma opção: ")
            
            match escolha:
                case "1":
                    cpf = input("\nInsira o CPF do técnico: ")
                    resultado = validar_duplicidade(self.catalogo.lista, cpf)

                    if resultado != -1:
                        print("Técnico já está cadastrado.")
                    else:
                        tecnico = self.dados_tecnico(cpf)
                        self.catalogo.cadastrar(tecnico)
                        print("Cadastro feito com sucesso.")

                case "2":
                    cpf = input("\nInsira o CPF do técnico: ")
                    resultado = validar_duplicidade(self.catalogo.lista, cpf)

                    if resultado == -1:
                        print("Técnico não localizado.")
                    else:
                        indice, _ = resultado
                        self.catalogo.modificar(indice)
                        print("\nCadastro modificado com sucesso")

                case "3":
                    cpf = input("\nInsira o CPF do técnico: ")
                    resultado = validar_duplicidade(self.catalogo.lista, cpf)

                    if resultado == -1:
                        print("Técnico não localizado.")
                    else:
                        _, tecnico = resultado
                        self.catalogo.remover(tecnico)
                        print("Cadastro removido com sucesso.")

                case "4":
                    cpf = input("\nInsira o CPF do técnico: ")
                    resultado = validar_duplicidade(self.catalogo.lista, cpf)

                    if resultado == -1:
                        print("Técnico não localizado.")
                    else:
                        _, tecnico = resultado
                        print(f"\nNome: {tecnico.nome} | Especialidade: {tecnico.especialidade}")

                case "0":
                    break
                case _:
                    print("\nEntre com uma opção válida")


class OrdemServico():
    # Uma classe de dados pura. Não cria catálogos dentro dela!
    def __init__(self, numero: int, cliente: object, tecnico: object, descricao: str, valor: float):
        self.numero = numero
        self.cliente = cliente  # Guarda o objeto Cliente achado
        self.tecnico = tecnico  # Começa como None e depois guarda o objeto Tecnico
        self.descricao = descricao
        self.valor = valor
        self.status = StatusOrdem.ABERTA


class CatalogoOrdemServico():
    # O catálogo recebe os outros dois catálogos para conseguir fazer validações
    def __init__(self, catalogo_cliente: CatalogoClientes, catalogo_tecnico: CatalogoTecnico):
        self.lista = []
        self.catalogo_cliente = catalogo_cliente
        self.catalogo_tecnico = catalogo_tecnico

    def cadastrar(self, ordem: object):
        self.lista.append(ordem)

    def dados_ordem(self):
        numero = len(self.lista) + 1
        
        cpf_cliente = input("Insira o CPF do cliente: ")
        # Busca o cliente na lista global de clientes recebida
        resultado = validar_duplicidade(self.catalogo_cliente.lista, cpf_cliente)
        
        if resultado == -1:
            print("\nErro: Cliente não localizado! Cadastre-o primeiro.")
            return -1
        
        _, cliente = resultado
        tecnico = None
        descricao = input("Insira a descrição da ordem de serviço: ")
        
        try:
            valor = float(input("Insira o valor esperado da operação: "))
        except ValueError:
            print("\nValor inválido! Definido como 0.00")
            valor = 0.0
            
        return OrdemServico(numero, cliente, tecnico, descricao, valor)

    def procurar(self, numero: int):
        for indice, objeto in enumerate(self.lista):
            if objeto.numero == numero:
                return indice, objeto
        return -1


class CadastroOrdemServico():
    def __init__(self, catalogo_ordem: CatalogoOrdemServico, catalogo_tecnico: CatalogoTecnico):
        self.catalogo_ordem = catalogo_ordem
        self.catalogo_tecnico = catalogo_tecnico

    def menu(self):
            while True:
                print("\n" + "="*35)
                print("Ordem de serviços")
                print("="*35)
                print("[1] Cadastrar nova ordem.")
                print("[2] Designar um técnico a uma ordem.")
                print("[3] Cancelar uma ordem.")
                print("[4] Procurar ordens de um cliente")
                print("[0] Voltar para o menu anterior.")
    
                escolha = input("Escolha uma opção: ")
    
                match escolha:
                    case "1":
                        ordem = self.catalogo_ordem.dados_ordem()
                        if ordem == -1:
                            continue
                        self.catalogo_ordem.cadastrar(ordem)
                        print(f"Ordem Nº {ordem.numero} criada com sucesso!")
    
                    case "2":
                        num_ordem = input("Insira o número da ordem: ")
                        if not num_ordem.isdigit():
                            print("Por favor, insira apenas números inteiros.")
                            continue

                        resultado_ordem = self.catalogo_ordem.procurar(int(num_ordem))
                        if resultado_ordem == -1:
                            print("Número de ordem não encontrado.")
                            continue
                        
                        _, ordem = resultado_ordem

                        cpf_tecnico = input("Insira o CPF do técnico a ser designado.")
                        resultado_tecnico = validar_duplicidade(self.catalogo_tecnico.lista, cpf_tecnico)
                        if resultado_tecnico == -1:
                            print("Técnico não encontrado.")
                            continue
                        
                        _, tecnico = resultado_tecnico

                        ordem.tecnico = tecnico
                        ordem.status = StatusOrdem.ANDAMENTO
                        print(f"Técnico {tecnico.nome} designado para a Ordem Nº {ordem.numero}.")

                    case "3":
                        num_ordem = input("Insira o número da ordem: ")
                        if not num_ordem.isdigit():
                            print("Por favor, insira apenas números inteiros.")
                            continue

                        resultado_ordem = self.catalogo_ordem.procurar(int(num_ordem))
                        if resultado_ordem == -1:
                            print("Número de pedido não encontrado.")
                            continue

                        _, ordem = resultado_ordem
                        ordem.status = StatusOrdem.CANCELADA
                        print(f"Ordem Nº {ordem.numero} cancelada com sucesso.")

                    case "4":
                        cpf_cliente = input("\nInsira o CPF do cliente: ")
                        resultado = validar_duplicidade(self.catalogo_ordem.catalogo_cliente.lista, cpf_cliente)

                        if resultado == -1:
                            print("Cliente não localizado")
                            continue

                        _, cliente = resultado
                        for x in self.catalogo_ordem.lista:
                            if x.cliente == cliente:
                                tecnico = x.tecnico.nome if x.tecnico else "Técnico não designado."
                                print(f"Ordem Nº: {x.numero} | Técnico responsável: {tecnico} | Descrição do serviço: {x.descricao} | Valor estimado do serviço: {x.valor:.2f}")

                    case "0":
                        break

                    case _:
                        print("Por favor, entre com uma opção válida.")


class MenuPrincipal():
    def __init__(self):
        self.catalogo_clientes = CatalogoClientes()
        self.catalogo_tecnicos = CatalogoTecnico()
        self.catalogo_ordens = CatalogoOrdemServico(self.catalogo_clientes, self.catalogo_tecnicos) 

    def menu(self):
        while True:
            print("\n" + "="*30)
            print("       SISTEMA DE GESTÃO")
            print("="*30)
            print("[1] Cadastro de Clientes")
            print("[2] Cadastro de Técnicos")
            print("[3] Ordem de Serviços (OS)")
            print("[0] Sair")
            print("="*30)
            
            opcao = input("Escolha uma opção: ")
            
            match opcao:
                case "1":
                    CadastroCliente(self.catalogo_clientes).menu()
                case "2":
                    CadastroTecnico(self.catalogo_tecnicos).menu()
                case "3":
                    CadastroOrdemServico(self.catalogo_ordens, self.catalogo_tecnicos).menu()
                case "0":
                    print("Encerrando o sistema...")
                    break
                case _:
                    print("\nOpção inválida! Por favor, tente novamente.")
