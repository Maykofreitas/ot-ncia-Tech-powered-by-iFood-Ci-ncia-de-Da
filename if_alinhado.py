saldo = 2000
saque = 100
cheque_especial = 100
conta = 0
opção = 0

opcao = int(input("informe o tipo de conta:\n 1:conta_normal \n 2:Conta Universitaria\n"))

if opção == 1:
     if saldo >= saque:
         print("saque realizado com sucesso")
     elif saque <= (saldo + cheque_especial):
         print ("saque realizado com uso do cheque especial")
         
elif opção == 2:
    if saldo >=saque:
        print ("saque realizado com sucesso ")
    else: 
        print ("saldo insuficiente")