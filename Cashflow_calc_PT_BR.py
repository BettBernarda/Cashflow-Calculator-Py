
#Entrada calculadora
print()
print("Bem vindo a calculadora de fluxo de caixa!")
print()

#Informações iniciais
Valor_Inicial = float(input("Informe o valor inicial: "))
Mes=(int(input("Informe o numero do mês (ex: Abril=4): ")))
if Mes <= 0 or Mes >12:
    print("Você Inseriu um valor incorreto, tente novamente")
    quit()
(print)

#Repositório de informações
Lista_entradas =[]
Dic_entradas={}
Lista_Saidas = []
Dic_Saidas={}
Contador_Entrada=1
Contador_Saida =1

#Operação de catalogação de itens
def Transacao(Nome_trasacao ,Contador,Lista,Dicionario):
    #Espaço para titulo
    print()
    print(20*"/", Nome_trasacao, 20*"/")
    print("Digite -1 para ir para o próximo menu")
    print()
    #Loop preenchimento de item
    #O loop se encerra ao digitar "-1"
    while True:
        print(f"{Contador}° Item:")
        #Nome
        Nome_Item = input(f"Nome {Nome_trasacao}: ")
        if Nome_Item == "-1":
            break
        else:
            #Valor
            Valor_Item = float(input("Valor: "))
            if Valor_Item == -1:
                break
            else:
                #Dia
                Dia= int(input("Dia: "))
                if Dia == -1:
                    break
                #Verificação dia correto
                elif  Dia>30 or Dia<1:
                    print("Você Inseriu um valor incorreto, tente novamente")
                else:
                    #Resultado final do item, ele é adicionado a lista  e logo após ao dicionario, sendo as chaves numeradas pelo contador de itens.
                    print()
                    Lista.append((Nome_Item,Valor_Item, Dia))
                    Dicionario.update({Contador:Lista[Contador -1]})
                    Contador+=1
                    
    #Return para adicionar valor ao Contador, desde que caso o usuário queira retornar a tela de adição, a contagem permança a mesma         
    return Contador
#Resumo de tudo, calculando todas as entradas e saidas registradas
def Resultados():

    global i , Mes, Valor_Inicial, Contador_Entrada, Contador_Saida, Lista_entradas , Lista_Saidas, Dic_entradas
    #Variaveis entras e saidas
    Entradas = 0
    Saidas = 0
    #For de soma e subtração de valores dentro das listas do dicionario
    for chave,Valor in Dic_entradas.items():
        Entradas += Valor[1]
    for chave,Valor in Dic_Saidas.items():
        Saidas += Valor[1]
    #Diferença entre entradas e saidas, ou seja, valor que sobrou ou deveu
    Saldo_Operacional= Entradas-Saidas
    #Soma sobra e saldo incial
    Saldo_Final = Valor_Inicial+Saldo_Operacional
    print("\n" * 130)
    print(20*"/", f"Resultados mês {Mes}", 20*"/")
    print()
    #Apresentação de resultados
    print(f"Saldo inicial: R${Valor_Inicial:.2f}")
    print(f"Valor de entradas: R${Entradas:.2f}")
    print(f"Valor de saidas: R${Saidas:.2f}")
    print(f'Valor do saldo operacional: R${Saldo_Operacional:.2f}')
    print(f'Saldo final: R${Saldo_Final:.2f}')
    print("\n"*7)
    #Menu de caminhos para edição e visualização
    Caminhos = input("Entradas[E] Saidas [S]")[0].upper()
    ###[0].upper() is a good way to make input works by words, even tho it can read every word that starts with the leatter, it can be very efficient
   
    if Caminhos == "S":
        Contador_Saida=Analise('Saida',Dic_Saidas,Contador_Saida,Lista_Saidas)
        
    elif Caminhos == "E":
        Contador_Entrada=Analise('Entrada',Dic_entradas,Contador_Entrada,Lista_entradas)
#Representação e menu de edição da lista de itens.
def Analise(Nome_Transacao, Dicionario,Contador,Lista_Transacao):
    print("\n" * 130)
    print(10*"/", Nome_Transacao , 10*"/")
    #For de listagem e apresentação de dados expesificos
    for Chave, lista in Dicionario.items(): 
        print(f"{Chave}. {lista[0]} - R$ {lista[1]} - Dia:{lista[2]}")
    #Menu de opção tela de analise
    Escolha=input("[V] Voltar [A] Adicionar [E] Excluir")[0].upper()
    while True:
        #voltar
        if Escolha == "V":
            Resultados()
            break
        #Adicionar
        elif Escolha == "A":
            Contador=Transacao(Nome_Transacao,Contador,Lista_Transacao,Dicionario)
            Resultados()
            return Dicionario
        #Excluir
        elif Escolha == "E":
            while True:
                delete = int(input("Qual da lsita deseja excluir? "))
                if delete not in Dicionario:
                    print("Valor invalido! Ensira novamente.")
                    print()
                else:
                    #Lógica de re-contage: O dicionario deleta o item da chave em questão,, o processom é recontado com a uma lista provisória , utiliozando dos dados dos itens do dicionario
                    Dicionario.pop(delete)
                    Lista_Escape={}
                    Contador_Dicionario=1
                    for chave,Lista_2 in Dicionario.items():
                        Lista_Escape.update ({Contador_Dicionario:Lista_2})
                        Contador_Dicionario+=1
                    #após isso, o ddicionario é limpado e são inseridas as informações da lista provisória
                    Dicionario.clear()
                    Dicionario.update(Lista_Escape)
                    #Após o processo completo, a lista provisoria é limpa, para futuro uso.
                    Lista_Escape.clear()
                    Contador-=1
                    print("item deletado com sucesso")
                    break
        
        Analise(Nome_Transacao, Dicionario,Contador,Lista_Transacao)
        break
      
## Catalogação de Entradas
Contador_Entrada=Transacao('Entrada',Contador_Entrada,Lista_entradas,Dic_entradas)

##Catalogação de Saidas
Contador_Saida=Transacao('Saida',Contador_Saida,Lista_Saidas,Dic_Saidas)

##Resultados

Resultados()
