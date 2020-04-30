from random import randint
#dedico ao meu amigo fidel, tbm conhecido como Thiago fidel
#Primeiro desafio
""" 
def ta_na_lista(num, lista):
    achou = False
    if num in lista:
        lista_original = lista
        while True:    
            metade = int(len(lista)/2)
            num_do_meio = lista[metade]
            if num_do_meio == num:
                return True, lista_original.index(num)
            if num>num_do_meio:
                nova_lista = lista[metade:len(lista)]
            elif num<num_do_meio:
                nova_lista = lista[:metade]
            lista = nova_lista 
        return False


lista = list(range(300))
num = 77

resultado = ta_na_lista(num,lista)
if resultado[0]:
    print(f"o numero {num} ta na posição {resultado[1]} da lista")
 """



def ta_na_listaA(num, lista):
    try:
        return True, lista.index(num)
    except:
        return False, 0


def desafio1():
    lista = list(range(0, 400, 4))
    print('############ Desafio 1: ############')
        
    print("Digite um número")
    num = int(input())

    resultado = ta_na_listaA(num, lista)
    if resultado[0]:
        print(f'O número está na posição {resultado[1]} da lista ')
    else:
        print("O número não está na lista")

#Segundo desafio

 

def ta_na_listaB(lista_pequena, lista_grande):
    lista = list()
    for i in lista_grande:
        if i in lista_pequena:
            lista.append(i)
    if not lista == []:
        print(lista)
    else:
        print('Não há números da lista grande na lista pequena')


def desafio2():
    print("############### Desafio 2: ###############")
    lista1 = [randint(0, 5000000) for x in range(500)]
    lista2 = [randint(0, 5000000) for x in range(50000)]    
    ta_na_listaB(lista1, lista2)


def eh_primo(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def todos_primos(final_num):
    for i in range(final_num+1):
        if eh_primo(i):
            print(i)

            

def desafio3():
    print("############### Desafio 3: ###############")
    print("Digite um número")
    number = int(input())
    todos_primos(number)

def soma_palavra(palavra):
    maiuscula = 26
    soma = 0
    dic = {'a': 1, 
        'b':2, 
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8,
        'i':9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,
        'o':15,
        'p':16,
        'q':17,
        'r':18,
        's':19,
        't':20,
        'u':21,
        'v':22,
        'w':23,
        'x':24,
        'y':25,
        'z':26,       
         }    
    for letra in palavra:
        if letra.lower() not in dic.keys():
            print(f"O caracter '{letra}' é inválido. Digite apenas letras de a-z ou A-Z")
            return None
        if letra.islower(): 
            soma += dic[letra]
        else:
            letra_minuscula = letra.lower()
            soma += maiuscula + dic[letra_minuscula]
    return soma

def desafio4():
    print('Quantas palavras deseja digitar?')
    num_palavras = int(input())
    
    palavras = []
    for i in range(num_palavras):
        palavra_input = input()
        palavras.append(palavra_input)

    for palavra in palavras:
        resultado = soma_palavra(palavra)
        if eh_primo(resultado):
            print(f"A soma da palavra {palavra} resulta numa soma de {resultado} que é um numero primo ")
        else:
            print(f"A soma da palavra {palavra} resulta numa soma de {resultado} que não é um numero primo ")


    
if __name__ == "__main__":
    desafio1()
    desafio2()
    desafio3()
    desafio4()
    



    