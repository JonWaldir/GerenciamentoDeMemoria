import os
def grava_arq(sequencia,pasta):
    
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    caminho_completo = os.path.join(pasta, "ex37.txt")

    with open(caminho_completo,'a') as arquivo:
        arquivo.write(f"{sequencia}\n")


def main():
    pasta_alvo = 'C:\\temp\\'
    nome_arquivo = 'ex37.txt'

    caminho_total = os.path.join(pasta_alvo, nome_arquivo)

    if os.path.exists(caminho_total):
        os.remove(caminho_total)

    contador = 1
    t1 = -1
    t2 = 1
    
    while contador < 100 :
        proximo = t1+t2
        grava_arq(proximo, pasta_alvo)
        t1 = t2
        t2 = proximo
        
        contador +=1


if __name__ == "__main__":
    main()
