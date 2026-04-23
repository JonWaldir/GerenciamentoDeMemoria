import os

def valida_impar(numero):
    if numero % 2 != 0:
        return numero
    else:
        return -1

def procedimento_leitura(caminho):
    if not os.path.exists(caminho):
        print("Erro: Arquivo não encontrado.")
        return

    print("--- Números Ímpares ---")
    
    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            itens = linha.split()
            for i in itens:
                valor = int(i)
                resultado = valida_impar(valor)
                if resultado != -1:
                    print(resultado)

def main():
    pasta = 'C:\\temp\\'
    arquivo = 'ex37.txt'
    caminho_total = pasta + arquivo

    procedimento_leitura(caminho_total)

if __name__ == "__main__":
    main()
