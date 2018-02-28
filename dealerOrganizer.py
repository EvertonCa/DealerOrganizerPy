def imprimeOpcoes():
    print("1 - Veículos:")
    print("2 - Clientes:")
    print("3 - Vendedores:")
    print("4 - Acessórios:")
    print("5 - Serviços")

#---------------------------------------------

def cadastraCliente():
    aux = []
    aux.append(len(clientes) + 1)
    aux.append(input("Nome: "))
    aux.append(input("Endereço: "))
    aux.append(input("Telefone: "))
    aux.append(input("CPF: "))
    clientes.append(aux)
    print("Cliente cadastrado com sucesso!!\n")

def cadastraVeiculo():
    aux = []
    aux.append(len(veiculos) + 1)
    aux.append(input("Modelo: "))
    aux.append(input("Marca: "))
    aux.append(input("Ano: "))
    aux.append(input("Cor: "))
    aux.append(float(input("Preco: ")))
    aux.append(float(input("KM: ")))
    veiculos.append(aux)
    print("Veículo cadastrado com sucesso!!\n")

def cadastraVendedor():
    aux = []
    aux.append(len(vendedores) + 1)
    aux.append(input("Nome: "))
    aux.append(input("Endereco: "))
    aux.append(input("Telefone: "))
    aux.append(input("CPF: "))
    vendedores.append(aux)
    print("Vendedor cadastrado com sucesso!!\n")

def cadastraAcessorio():
    aux = []
    aux.append(len(acessorios) + 1)
    aux.append(input("Descricao: "))
    aux.append(input("Quantidade: "))
    aux.append(input("Valor Unitario: "))
    acessorios.append(aux)
    print("Acessório cadastrado com sucesso!!\n")

def cadastraServico():
    aux = []
    aux.append(len(servicos) + 1)
    aux.append(input("Descricao: "))
    aux.append(input("Valor: "))
    servicos.append(aux)
    print("Serviço cadastrado com sucesso!!\n")

def cadastraPedido():
    aux = []
    aux.append(len(pedidos) + 1)
    aux.append(input("Data: "))
    vID = int(input("Id Cliente: "))
    aux.append(clientes[vID - 1][1])
    vID = int(input("Id Veículo: "))
    aux.append(veiculos[vID - 1][5])
    aux.append(veiculos[vID - 1][6])
    vID = int(input("Id Vendedor: "))
    aux.append(vendedores[vID - 1][1])
    vID = int(input("Id Acessório: "))
    aux.append(acessorios[vID - 1][1])
    aux.append(acessorios[vID - 1][3])
    quant = int(input("Quantidade dos acessórios: "))
    aux.append(quant)
    pedidos.append(aux)
    print("Pedido cadastrado com sucesso!!\n")

#---------------------------------------------

def atualizaCliente():
    idCli = int(input("Digite o Id do Cliente que deseja atualizar: "))
    nomeCli = input("Digite o novo nome do cliente: ")
    endCli = input("Digite o novo endereco do cliente: ")
    telCli = input("Digite o novo telefone do cliente: ")
    cpfCli = input("Digite o novo cpf do cliente: ")
    clientes[idCli - 1][1] = nomeCli
    clientes[idCli - 1][2] = endCli
    clientes[idCli - 1][3] = telCli
    clientes[idCli - 1][4] = cpfCli
    print("Cliente atualizado com sucesso !!\n")

def atualizaVeiculo():
    idVei = int(input("Digite o Id do Veiculo que deseja atualizar: "))
    modVei = input("Digite o novo modelo do veiculo: ")
    nomeVei = input("Digite a nova marca do veiculo: ")
    anoVei = int(input("Digite o novo ano do veiculo: "))
    corVei = input("Digite a nova cor do veiculo: ")
    precoVei = float(input("Digite o novo preco do veiculo: "))
    kmVei = float(input("Digite a nova km do veiculo: "))
    veiculos[idVei - 1][1] = modVei
    veiculos[idVei - 1][2] = nomeVei
    veiculos[idVei - 1][3] = anoVei
    veiculos[idVei - 1][4] = corVei
    veiculos[idVei - 1][5] = precoVei
    veiculos[idVei - 1][6] = kmVei
    print("Veiculo atualizado com sucesso !!\n")

def atualizaVendedor():
    idVen = int(input("Digite o Id do Vendedor que deseja atualizar: "))
    nomeVen = input("Digite o novo nome do vendedor: ")
    endVen = input("Digite o novo endereco do vendedor: ")
    telVen = int(input("Digite o novo telefone do vendedor: "))
    cpfVen = input("Digite a nova cpf do vendedor: ")
    vendedores[idVen - 1][1] = nomeVen
    vendedores[idVen - 1][2] = endVen
    vendedores[idVen - 1][3] = telVen
    vendedores[idVen - 1][4] = cpfVen
    print("Vendedor atualizado com sucesso !!\n")

def atualizaAcessorio():
    idAce = int(input("Digite o Id do Acessorio que deseja atualizar: "))
    nomeAce = input("Digite a nova descricao do acessorio: ")
    qtdAce = input("Digite a nova quantidade do acessorio: ")
    valAce = int(input("Digite o novo valor unitario do acessorio: "))
    acessorios[idAce - 1][1] = nomeAce
    acessorios[idAce - 1][2] = qtdAce
    acessorios[idAce - 1][3] = valAce
    print("Acessorio atualizado com sucesso !!\n")

def atualizaServico():
    idServ = int(input("Digite o Id do Servico que deseja atualizar: "))
    nomeServ = input("Digite a nova descricao do servico: ")
    valServ = input("Digite o novo valor do servico: ")
    acessorios[idAce - 1][1] = nomeServ
    acessorios[idAce - 1][2] = valServ
    print("Servico atualizado com sucesso !!\n")

#---------------------------------------------

def deleta(vetor,obj):
    IdDel = int(input("Digite o ID do %s que deseja deletar: " %obj))
    del vetor[IdDel -1]
    print("%s deletado com sucesso!!\n" %obj)

#---------------------------------------------

def exibeVeiculos():
    for i in range (len(veiculos)):
        print(" ID: ",veiculos[i][0]," Modelo: ", veiculos[i][1]," Marca: ", veiculos[i][2], " Ano: ", veiculos[i][3], " Cor: ", veiculos[i][4], " Preço: ", veiculos[i][5], " Km: ", veiculos[i][6])

def exibeCLientes():
    for i in range (len(clientes)):
        print(" ID: ",clientes[i][0]," Nome: ", clientes[i][1]," Endereço: ", clientes[i][2], " Telefone: ", clientes[i][3], " CPF/CNPJ: ", clientes[i][4])

def exibeVendedor():
    for i in range (len(vendedores)):
        print(" ID: ",vendedores[i][0]," Nome: ", vendedores[i][1]," Endereço: ", vendedores[i][2], " Telefone: ", vendedores[i][3], " CPF: ", vendedores[i][4])

def exibeAcessorios():
    for i in range (len(acessorios)):
        print(" ID: ",acessorios[i][0]," Descrição: ", acessorios[i][1]," Quantidade: ", acessorios[i][2], " Valor unitário: ", acessorios[i][3])

def exibeServicos():
    for i in range (len(servicos)):
        print(" ID: ",servicos[i][0]," Descrição: ", servicos[i][1]," Valor: ", servicos[i][2])

#---------------------------------------------

def consultaCliente():
    idCli = int(input("Digite o id do cliente que deseja consultar: "))
    print("Nome do Cliente: %s\nEndereco do Cliente: %s\nTelefone do Cliente: %s" %(clientes[idCli - 1][1], clientes[idCli - 1][2], clientes[idCli - 1][3]))
    print("CPF/CNPJ do Cliente: %s" % clientes[idCli - 1][4])

def consultaVeiculo():
    idVei = int(input("Digite o id do veiculo que deseja consultar: "))
    print("Modelo do Veiculo: %s\nMarca do Veiculo: %s\nAno do Veiculo: %s" %(veiculos[idVei - 1][1], veiculos[idVei - 1][2], veiculos[idVei - 1][3]))
    print("Cor do Veiculo: %s\nPreco do Veiculo: %10.2f\nKM do Veiculo: %s" %(veiculos[idVei - 1][4], veiculos[idVei - 1][5], veiculos[idVei - 1][6]))

def consultaVendedor():
    idVen = int(input("Digite o id do vendedor que deseja consultar: "))
    print("Nome do Vendedor: %s\nEndereco do Vendedor: %s\nTelefone do Vendedor: %s\nCPF do Vendedor: %s" %(vendedores[idVen - 1][1], vendedores[idVen - 1][2], vendedores[idVen - 1][3], vendedores[idVen - 1][4]))

def consultaAcessorio():
    idAce = int(input("Digite o id do acessorio que deseja consultar: "))
    print("Descricao do Acessorio: %s\nQuantidade: %s\nValor Unitario do Acessorio: %s" %(acessorios[idAce - 1][1], acessorios[idAce - 1][2], acessorios[idAce - 1][3]))

def consultaServico():
    idSer = int(input("Digite o id do servico que deseja consultar: "))
    print("Descricao do Servico: %s\nValor do Servico:%s" % (servicos[idSer - 1][1], servicos[idSer - 1][2]))

def consultaPedido():
    idPed = int(input("Digite o id do pedido que deseja consultar: "))
    valTot = int(pedidos[idPed - 1][12]) * int(pedidos[idPed - 1][11])
    print("Data do pedido: %s\nNome do cliente: %s\nModelo do veiculo: %s" %(pedidos[idPed - 1][1], pedidos[idPed - 1][2], pedidos[idPed - 1][5]))
    print("Preco do veiculo: %s\nNome do Vendedor: %s\nDescricao do acessorio:%s" %(pedidos[idPed - 1][6], pedidos[idPed - 1][8], pedidos[idPed - 1][10]))
    print("Quantidade de acessorios: %s\nValor Unitario acessorio: %s\nValor total: %d" %(pedidos[idPed - 1][12], pedidos[idPed - 1][11], valTot))

#---------------------------------------------

veiculos = []
clientes = []
vendedores = []
acessorios = []
servicos = []
pedidos = []
continua = True
print("\n\n~~~~~~~~~~~~~~~~ BEM VINDO ao SuperControlator 3000 ~~~~~~~~~~~~~~~~")
while continua:
    print("~~~~~~~~~~~~~~~~~~ TUNcars - A sua concessionária! ~~~~~~~~~~~~~~~~~\n")
    print("Selecione a opção desejada:\n")
    print("1 - Cadastrar:")
    print("2 - Consultar:")
    print("3 - Editar:")
    print("4 - Deletar:")
    print("5 - Fazer pedido:")
    print("0 - Encerrar programa:")

    opcao = int(input())

    if opcao == 1:
        print("Selecione o que gostaria de cadastrar:\n")
        imprimeOpcoes()
        opcao2 = int(input())
        if opcao2 == 1:
            cadastraVeiculo()
        elif opcao2 == 2:
            cadastraCliente()
        elif opcao2 == 3:
            cadastraVendedor()
        elif opcao2 == 4:
            cadastraAcessorio()
        elif opcao2 == 5:
            cadastraServico()

    elif opcao == 2:
        print("Selecione o que gostaria de consultar:\n")
        imprimeOpcoes()
        print("6 - Pedido:")
        print("7 - Exibir tudo:")
        opcao2 = int(input())
        if opcao2 == 1:
            consultaVeiculo()
        elif opcao2 == 2:
            consultaCliente()
        elif opcao2 == 3:
            consultaVendedor()
        elif opcao2 == 4:
            consultaAcessorio()
        elif opcao2 == 5:
            consultaServico()
        elif opcao2 == 6:
            consultaPedido()
        elif opcao2 == 7:
            print("Veículos Cadastrados:")
            exibeVeiculos()
            print("Clientes Cadastrados:")
            exibeCLientes()
            print("Vendedores Cadastrados:")
            exibeVendedor()
            print("Acessórios Cadastrados:")
            exibeAcessorios()
            print("Serviços Cadastrados:")
            exibeServicos()

    elif opcao == 3:
        print("Selecione o que gostaria de editar:\n")
        imprimeOpcoes()
        opcao2 = int(input())
        if opcao2 == 1:
            atualizaVeiculo()
        elif opcao2 == 2:
            atualizaCliente()
        elif opcao2 == 3:
            atualizaVendedor()
        elif opcao2 == 4:
            atualizaAcessorio()
        elif opcao2 == 5:
            atualizaServico()

    elif opcao == 4:
        print("Selecione o que gostaria de deletar:\n")
        imprimeOpcoes()
        opcao2 = int(input())
        if opcao2 == 1:
            deleta(veiculos,'Veículo')
        elif opcao2 == 2:
            deleta(clientes,'Cliente')
        elif opcao2 == 3:
            deleta(vendedores,'Vendedor')
        elif opcao2 == 4:
            deleta(acessorios,'Acessório')
        elif opcao2 == 5:
            deleta(servicos,'Serviço')

    elif opcao == 5:
        cadastraPedido()

    elif opcao == 0:
        print("\n~~~~~~~~~~~~~~~~ OBRIGADO por usar o SuperControlator 3000 ~~~~~~~~~~~~~~~~")
        continua = False