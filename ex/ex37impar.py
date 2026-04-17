import os
def grava_arq(sequencia,par,pasta,):

    
    
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    caminho_completo = os.path.join(pasta, "ex37.txt")

    with open(caminho_completo,'a') as arquivo:
        arquivo.write(f"{sequencia}\n")
        arquivo.write(f"{par} -1\n")


def main():
    pasta_alvo = 'C:\\temp\\'
    nome_arquivo = 'ex37.txt'

    caminho_total = os.path.join(pasta_alvo, nome_arquivo)

    if os.path.exists(caminho_total):
        os.remove(caminho_total)

    contador = 1
    t1 = -1
    t2 = 1
    impar: int = 0
    nao_impar: int =0
    
    while contador < 100 :
        proximo = t1+t2
        if proximo %2 == 0 :
        
            nao_impar = proximo
        else:
            impar = proximo
        
        grava_arq(impar,nao_impar, pasta_alvo)
        t1 = t2
        t2 = proximo
        
        contador +=1


if __name__ == "__main__":
    main()
