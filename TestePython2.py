def menu ():
    menu = """"\n
    ______________Banco Lougan_______________________________
            
    [1]Depositar                     [4]Criar Usuario
    [2]Saque                         [5]Transferencia
    [3]Extrato                       [6]Abrir conta corrente
                       [0]Sair

    """

def menu ():
    
  opção = input (menu)

def depositar():
    valor =input("digite o valor a depositar: R$")
    if  valor >= "0":
        saldo += valor
        extrato += (f"deposito:\t{valor:.2f}\n")
        print("Deposito realizado com sucesso!")
    else :
        print ("Essa operação falhou! tente novamente mais tarde")
        
    return saldo, extrato
    
    
def sacar(*,saldo, valor, extrato, limite, numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques
    
    if excedeu_saldo:
        print("Operação falhou! Voce nao tem saldo suficiente")
        
    elif excedeu_limite:
        print ("Operação falhou! O Valor do saque excede o limite")
    
    elif excedeu_saque:
      print("Operação falhou! numero maximo de sauqes excedidos")
      
    elif valor>0:
       saldo -= valor 
       extrato+= f"saque :R$ {valor:.2f}"
       numero_saques += 1
       print ("saque realizado com sucesso!")
       
    else: print ("Operação falhou! o valor informado é invalido")
    
    return saldo,extrato
    
    
def exibir_extrato(saldo,/, extrato):
    print ("------------extrato--------------")
    print ("não foram realizados movimentações")
    print (f*saldo: R${saldo:.2f})
    print ("---------------------------------")

def criar_usuario():
    cpf: input("informe o cpf(somente numeros)")
    usuario = usuario (cpf , conta_corrente)
     
    if usuario: 
    print ("Usuario ja existe")
    return
    
    nome = input ("informe o nome completo")
    data_nascimento = input ("informe a data de nascimento(dd-mm-aaaa):")
    endereço = input ("informe o endereço(logradouro, numero- bairro - cidade - estado)")

    usuarios.append (["nome":nome, "data_nascimento": data_nascimento, "cpf": cpf])
    print ("Usuario criado com sucesso")

def criar_contas(agencia,numero_conta,usuario):
    cpf= input("informe o cpf do usuario:")
    
    print (" conta criada com sucesso")
    return ("agencia":agencia,"numero_conta": numero_conta,"usuario":usuario)

def main():
    limite_de_saques = 3
    Agencia:'00001'
    
    valor = 0
    saldo=0
    limite=5000
    extrato=""
    numero_de_saques=3
    usuario = []
    conta_corrente []

    while True:
    opção = menu()

    if opção == "1":
        valor = float(input("Informe o valor do deposito"))
        saldo, extrato = depositar (saldo, valor,extrato)
                
    elif opção == "2":
        valor = float (input("Qual o valor do saque:"))
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato = extrato,
            limite= limite,
            numero_saques =numero_saques
            limite_de_saques = limite_de_saques,
        
        )
    elif opção ="3":
        exibir_extrato(saldo, extrato+ extrato)
    
    elif opção= "4":
        criar_usuario(usuario)
    
    elif opção="5":
        transferencia(valor, conta_corrente)
        
    elif opção="6":
        numero_conta = len(contar) +1
        conta = criar_contas (agencia, numero_conta,usuario)
        if conta:
            contas.append(conta)
    
    elif opção = "0":
        break
        
    else ("opção invalida")
        
main()
        