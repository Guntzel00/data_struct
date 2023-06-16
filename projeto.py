class UF:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome


class Fabricante:
    def __init__(self, codigo, marca, site, telefone, uf):
        self.codigo = codigo
        self.marca = marca
        self.site = site
        self.telefone = telefone
        self.uf = uf


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Produto:
    def __init__(self, descricao, peso, valor_compra, valor_venda, fabricante):
        self.descricao = descricao
        self.peso = peso
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.fabricante = fabricante
        self.lucro = valor_venda - valor_compra
        self.percentual_lucro = (self.lucro / valor_compra) * 100


ufs = [
    UF("AC", "Acre"),
    UF("AL", "Alagoas"),
    UF("AP", "Amapá"),
    UF("AM", "Amazonas"),
    UF("BA", "Bahia"),
    UF("CE", "Ceará"),
    UF("DF", "Distrito Federal"),
    UF("ES", "Espírito Santo"),
    UF("GO", "Goiás"),
    UF("MA", "Maranhão"),
    UF("MT", "Mato Grosso"),
    UF("MS", "Mato Grosso do Sul"),
    UF("MG", "Minas Gerais"),
    UF("PA", "Pará"),
    UF("PB", "Paraíba"),
    UF("PR", "Paraná"),
    UF("PE", "Pernambuco"),
    UF("PI", "Piauí"),
    UF("RJ", "Rio de Janeiro"),
    UF("RN", "Rio Grande do Norte"),
    UF("RS", "Rio Grande do Sul"),
    UF("RO", "Rondônia"),
    UF("RR", "Roraima"),
    UF("SC", "Santa Catarina"),
    UF("SP", "São Paulo"),
    UF("SE", "Sergipe"),
    UF("TO", "Tocantins"),
]

fabricantes = []
clientes = []
produtos = []
lista_60 = []


def cadastrar_fabricante():
    codigo = int(input("Digite o código do fabricante: "))
    marca = input("Digite a marca do fabricante: ")
    site = input("Digite o site do fabricante: ")
    telefone = input("Digite o telefone do fabricante: ")
    uf = selecionar_uf()

    fabricante = Fabricante(codigo, marca, site, telefone, uf)
    fabricantes.append(fabricante)


def selecionar_uf():
    print("Unidades da Federação disponíveis:")
    for uf in ufs:
        print(uf.sigla, "-", uf.nome)
    sigla = input("Digite a sigla da UF: ")
    for uf in ufs:
        if uf.sigla.lower() == sigla.lower():
            return uf
    print("UF não encontrada. Tente novamente.")
    return selecionar_uf()


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))

    cliente = Cliente(nome, idade)
    clientes.append(cliente)


def cadastrar_produto():
    descricao = input("Digite a descrição do produto: ")
    peso = float(input("Digite o peso do produto: "))
    valor_compra = float(input("Digite o valor de compra do produto: "))
    valor_venda = float(input("Digite o valor de venda do produto: "))
    fabricante = selecionar_fabricante()

    produto = Produto(descricao, peso, valor_compra, valor_venda, fabricante)
    produtos.append(produto)


def selecionar_fabricante():
    print("Fabricantes disponíveis:")
    for fabricante in fabricantes:
        print(fabricante.codigo, "-", fabricante.marca)
    codigo_fabricante = int(
        input("Digite o código do fabricante do produto: "))
    for fabricante in fabricantes:
        if fabricante.codigo == codigo_fabricante:
            return fabricante
    print("Fabricante não encontrado. Tente novamente.")
    return selecionar_fabricante()


def cadastrar_fabricantes():
    print("Cadastrar fabricantes:")
    while len(fabricantes) < 2 or (len(fabricantes) < 5 and continuar_cadastro("fabricantes")):
        cadastrar_fabricante()
    if len(fabricantes) >= 5:
        print("Número máximo de fabricantes alcançado.")


def cadastrar_clientes():
    print("Cadastrar clientes:")
    while len(clientes) < 3 or (len(clientes) < 30 and continuar_cadastro("clientes")):
        cadastrar_cliente()
    if len(clientes) >= 30:
        print("Número máximo de clientes alcançado.")


def cadastrar_produtos():
    print("Cadastrar produtos:")
    while len(produtos) < 5 or (len(produtos) < 50 and continuar_cadastro("produtos")):
        cadastrar_produto()
    if len(produtos) >= 50:
        print("Número máximo de produtos alcançado.")


def continuar_cadastro(tipo):
    resposta = input(f"Deseja continuar cadastrando {tipo}? (s/n): ")
    return resposta.lower() == "s"


# Cadastrar fabricantes
cadastrar_fabricantes()

# Cadastrar clientes
cadastrar_clientes()

# Cadastrar produtos
cadastrar_produtos()

# Exibir informações cadastradas
print("Produtos cadastrados:")
for produto in produtos:
    print("Descrição:", produto.descricao)
    print("Peso:", produto.peso)
    print("Valor de Compra:", produto.valor_compra)
    print("Valor de Venda:", produto.valor_venda)
    print("Fabricante:", produto.fabricante.marca)
    print("Lucro:", produto.lucro)
    print("Percentual de Lucro:", produto.percentual_lucro)
    print()


# Função para listar produtos de um determinado fabricante em ordem alfabética
def listar_produtos_fabricante():
    codigo_fabricante = input("Digite o código do fabricante: ")
    produtos_fabricante = [
        produto for produto in produtos if produto.fabricante.codigo == codigo_fabricante]
    if len(produtos_fabricante) > 0:
        produtos_fabricante.sort(key=lambda produto: produto.descricao)
        print("Produtos do fabricante:")
        for produto in produtos_fabricante:
            print("Descrição:", produto.descricao)
    else:
        print("Nenhum produto encontrado para o fabricante informado.")


# Função para apresentar o(s) estado(s) onde tenha(m) algum produto com o valor igual ao maior valor registrado no sistema
def apresentar_estados_maior_valor():
    maior_valor = max(
        produtos, key=lambda produto: produto.valor_venda).valor_venda
    estados = set(
        [produto.fabricante.uf for produto in produtos if produto.valor_venda == maior_valor])
    if len(estados) > 0:
        print("Estado(s) com produto(s) de maior valor:", ", ".join(estados))
    else:
        print("Nenhum estado encontrado com produto de maior valor.")


# Função para apresentar o(s) fabricante(s) onde tenha(m) algum produto com o valor igual ao menor valor registrado no sistema
def apresentar_fabricantes_menor_valor():
    menor_valor = min(
        produtos, key=lambda produto: produto.valor_venda).valor_venda
    fabricantes = set(
        [produto.fabricante.marca for produto in produtos if produto.valor_venda == menor_valor])
    if len(fabricantes) > 0:
        print("Fabricante(s) com produto(s) de menor valor:",
              ", ".join(fabricantes))
    else:
        print("Nenhum fabricante encontrado com produto de menor valor.")


# Função para listar todos os produtos em ordem crescente de valor
def listar_produtos_ordem_valor():
    produtos_ordenados = sorted(
        produtos, key=lambda produto: produto.valor_venda)
    print("Produtos em ordem crescente de valor:")
    for produto in produtos_ordenados:
        print("Descrição:", produto.descricao)
        print("Valor de Venda:", produto.valor_venda)
        print()


# Função para listar todos os produtos em ordem crescente de maior "valor do lucro"
def listar_produtos_ordem_lucro():
    produtos_ordenados = sorted(
        produtos, key=lambda produto: produto.lucro, reverse=True)
    print("Produtos em ordem crescente de maior valor do lucro:")
    for produto in produtos_ordenados:
        print("Descrição:", produto.descricao)
        print("Valor do Lucro:", produto.lucro)
        print()


# Função para cadastrar novo cliente para atendimento na lista
def cadastrar_cliente_lista():
    cadastrar_cliente()
    print("Novo cliente cadastrado para atendimento na lista.")


# Função para verificar se existe algum cliente para atendimento na lista com idade superior a 60 anos (busca sequencial)
def verificar_cliente_idade():
    for cliente in clientes:
        if cliente.idade > 60:
            print("Existe cliente com idade superior a 60 anos.")
            return
    print("Nenhum cliente encontrado com idade superior a 60 anos.")

    # Valor especificado pelo usuário (busca binária)


def verificar_produto_valor():
    valor = float(input("Digite o valor do produto a ser verificado: "))
    produtos_ordenados = sorted(
        produtos, key=lambda produto: produto.valor_venda)
    inicio = 0
    fim = len(produtos_ordenados) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if produtos_ordenados[meio].valor_venda == valor:
            print("Produto encontrado com o valor especificado.")
            return
        elif produtos_ordenados[meio].valor_venda < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    print("Nenhum produto encontrado com o valor especificado.")


# Função para realizar o atendimento dos clientes na lista original com "ordem de acesso" baseado em fila


def atender_clientes_fila():
    if len(clientes) == 0:
        print("Não há clientes para atender na lista.")
    else:
        cliente_atendido = clientes.pop(0)
        print("Cliente atendido:", cliente_atendido.nome)

# Função para realizar o atendimento dos clientes na lista_60 com "ordem de acesso" baseado em pilha


def atender_clientes_pilha():
    if len(lista_60) == 0:
        print("Não há clientes com idade superior a 60 anos para atender na lista.")
    else:
        cliente_atendido = lista_60.pop()
        print("Cliente atendido:", cliente_atendido.nome)

# Função para exibir o menu e realizar as operações selecionadas pelo usuário


def exibir_menu():
    while True:
        print("\n------ MENU ------")
        print("[a] Listar produtos de um determinado fabricante em ordem alfabética")
        print("[b] Apresentar o(s) estado(s) onde tenha(m) algum produto com o valor igual ao maior valor registrado no sistema")
        print("[c] Apresentar o(s) fabricante(s) onde tenha(m) algum produto com o valor igual ao menor valor registrado no sistema")
        print("[d] Listar todos os produtos em ordem crescente de valor")
        print(
            "[e] Listar todos os produtos em ordem crescente de maior 'valor do lucro'")
        print("[f] Cadastrar novo cliente para atendimento na lista")
        print("[g] Verificar se existe algum cliente para atendimento na lista com idade superior a 60 anos (busca sequencial)")
        print("[h] Verificar se existe algum produto com o valor especificado pelo usuário (busca binária)")
        print("[i] Usuário do sistema realizará o atendimento dos clientes que estão na lista original com 'ordem de acesso' baseado em fila")
        print("[j] Usuário do sistema realizará o atendimento dos clientes que estão na lista_60 com 'ordem de acesso' baseado em pilha")
        print("[s] Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "a":
            listar_produtos_fabricante()
        elif opcao == "b":
            apresentar_estados_maior_valor()
        elif opcao == "c":
            apresentar_fabricantes_menor_valor()
        elif opcao == "d":
            listar_produtos_ordem_valor()
        elif opcao == "e":
            listar_produtos_ordem_lucro()
        elif opcao == "f":
            cadastrar_cliente_lista()
        elif opcao == "g":
            verificar_cliente_idade()
        elif opcao == "h":
            verificar_produto_valor()
        elif opcao == "i":
            atender_clientes_fila()
        elif opcao == "j":
            atender_clientes_pilha()
        elif opcao == "s":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, digite uma opção válida.")


# Execução do programa
exibir_menu()
