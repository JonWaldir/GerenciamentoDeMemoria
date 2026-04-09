import os
def grava_diferente(caminho_origem, pasta):

    caminho_novo = f"{pasta}/mutltiplos.txt"

    lido = open(caminho_origem,'r')
    novo = open(caminho_novo,"w")

    for linha in lido:
        texto = linha.strip()

        if "maior" not in texto  and "menor " not in texto:
            num = int(texto)
            if num % 5 == 0:
                novo.write(f"Multiplo de 5: {num}\n")
    
    lido.close()
    novo.close()



def grava_final(grande, pequeno,arquivo ):


    arquivo.write("O maior numero digitado é : " + str(grande) + "\n")
    arquivo.write("O menor numero é: "+ str(pequeno) + "\n")
    

def main():
    pasta: str = ''
    numero: int = 0

    pasta = '/tmp/exercícios'
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    os.chmod(pasta, 0o744)

    caminho_ex38  = os.path.join(pasta, 'ex38.txt')
    arq = open(caminho_ex38, 'w')


    contador = 1
    maior: int  = 0
    menor: int  = 0
    

    for contador in range ( 1,11,1):
            
        numero = int(input('Digite 10 numeros: '))
        arq.write(str(numero) + "\n")

        
        if contador == 1:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
            
            
    grava_final(maior, menor,arq)
    arq.close()
    grava_diferente(caminho_ex38, pasta)

    print('O arquivo foi fechado e com os dados gravados')








if __name__ == '__main__':
    main()