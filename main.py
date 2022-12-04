from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

binarios = []

def graficos():
    strbin = (entrada_bin.get())          # recebe o entrada do usuario 
    str2 = " " .join(strbin)              # adiciona um espaco entre cada numero digitado
    binariosTemp = list(str2.split(" "))  # separa cada elemento entre espacos para um indice da lista
    tamstr = len(binariosTemp)            # pega o tamanho da lista
    for i in range (tamstr):              # executa enquanto nao chegar ao final da lista
        aux = binariosTemp[i]             # recebe o valor do indice atual da lista
        intaux = int(aux)                 # trasnforma o valor recebido em um inteiro
        binarios.append(intaux)           # adiciona o inteiro na lista
    
    #Unipolar NRZ
    NRZUnipolar()                         # chama a funcao
    NRZpolar()                            # chama a funcao

    bin_text["text"] = binarios           # altera o texto de um label do tkinter
    plt.show() #mostra o grafico
    for x in range(len(binarios)):        # limpa a lista para poder receber outro numero
        binarios.clear()

def NRZpolar():
    graph = []
    graph2 = []
    anterior = 0                          #verifica se o numero anterior é 0, para pular para 1
    index = [0]
    i = 1                                 # precisa iniciar em 1 pq já temos a primeira posição no array de index
    for binario in binarios:
        if(not binario):                  # not 0 -> true --> verifica se o binário é ZERO
            if(anterior == 0):
                graph.extend((1,1))
                graph2.extend((0,0))
                anterior = 0
            else:
                graph.extend((-1,-1))
                graph2.extend((0,0))
                anterior = 1
        else: # binário é 1
            graph.extend((-1,-1))
            graph2.extend((0,0))
        index.extend((i,i)) if i != len(binarios) else index.append(i)
        i += 1
    plt.subplot(2,1,2)
    plt.xlabel("NRZ Polar" , fontdict= font)
    plt.plot(index,graph2, c = '#000000')
    plt.plot(index,graph)

def NRZUnipolar():
    graph = []
    anterior = 0                    # verifica se o numero anterior é 0, para pular para 1
    index = [0]
    i = 1                           # precisa iniciar em 1 pq já temos a primeira posição no array de index
    for binario in binarios:
        if(not binario):            # not 0 -> true --> verifica se o binário é ZERO
            if(anterior == 0):
                graph.extend((0,0))
                anterior = 0
            else:
                graph.extend((1,1))
                anterior = 1
        else: # binário é 1
            graph.extend((1,1))
        index.extend((i,i)) if i != len(binarios) else index.append(i)
        i += 1
    plt.subplot(2,1,1)
    plt.title("NRZ Unipolar", fontdict= font)
    plt.plot(index,graph)

font={'family':'serif','color':'black','size':12}

janela = Tk()
janela.title("Conversor Binario para Grafico")

texto_bin = Label(janela, text="Insira o Número Binario:")
texto_bin.grid(column=0, row=0)

entrada_bin = ttk.Entry(janela, width=15)
entrada_bin.grid(column=1, row=0)

bin_text = Label(janela, text="")
bin_text.grid(column=1, row=1)

botao1 = Button(janela, text="Gerar Graficos", command=graficos)
botao1.grid(column=0, row=1)
plt.show()

janela.mainloop()
