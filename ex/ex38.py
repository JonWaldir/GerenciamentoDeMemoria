import os

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

    caminho  = os.path.join(pasta, 'ex38.txt')
    arq = open(caminho, 'w')


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
    print('O arquivo foi fechado e com os dados gravados')








if __name__ == '__main__':
    main()