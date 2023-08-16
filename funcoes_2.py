def criar_carro(modelo,ano,placa,/, marca,motor,combustivel):#passado por posição, e nomeado depois da barra
      print (modelo,ano, placa, marca, motor, combustivel)
    
criar_carro("palio",1990,"ABC-1990",marca="Fiat",motor="1.0",combustivel="Gasolina") #deu certo o codigo
criar_carro(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")#vai dar erro no codigo


def criar_carro(*,modelo,ano,placa,marca,motor,combustivel):#passado por chave  
    print (modelo,ano, placa, marca, motor, combustivel)
    
criar_carro("palio",1990,"ABC-1990",marca="Fiat",motor="1.0",combustivel="Gasolina") #dmodelo invalido  
criar_carro(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")#deu certo o codigo


def criar_carro(modelo,ano,placa,/,marca,*,motor,combustivel):#modelo hibrido 
    print (modelo,ano, placa, marca, motor, combustivel)
    
criar_carro("palio",1990,"ABC-1990",marca="Fiat",motor="1.0",combustivel="Gasolina") #modelo valido 
criar_carro(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")#modelo invalido


#modelo de função de primeira classe

def somar (a,b):
    return a + b

def exibir_função (a,b,func):
     resultado = func (a,b)
     print (f"O resultado da operação {a} + {b} = {resultado}")
     
exibir_função(10,10,somar')

