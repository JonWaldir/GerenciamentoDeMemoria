import os

# b. Declaração das variáveis globais
valor: int = 0
dir: str = ''
arq: str = ''

def mult(vlr, tab):
    # d. Calcula a multiplicação e retorna
    res = vlr * tab
    return res

def grava(c, rslt):
    # e. Procedimento de gravação com lógica de modo de arquivo
    global dir, arq
    dir = '/tmp/exercicios'
    arq = 'ex34.txt'
    
    file = ''; tipo = ''; enc = ''; linha = ''
    
    linha = str(rslt) + '\n'
    caminho_completo = os.path.join(dir, arq)
    
    # Verifica se o diretório existe e é um diretório
    if os.path.exists(dir) and os.path.isdir(dir):
        # Define o tipo: 'w' para o primeiro item (c=0) ou se arquivo não existir
        # 'a' (append) apenas se c > 0
        if os.path.exists(caminho_completo) and c > 0:
            tipo = 'a'
        else:
            tipo = 'w'
            
        with open(caminho_completo, tipo) as f:
            f.write(linha)

def main():
    # a. Criação da pasta e permissão 744
    pasta = '/tmp/exercicios'
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    os.chmod(pasta, 0o744)

    # c. Procedimento principal
    global valor
    contador = 1
    result = 0
    
    valor = int(input("Digite um valor entre 1 e 10: "))
    
    # Executa 10 vezes (tabuada do 1 ao 10)
    while contador <= 10:
        result = mult(valor, contador)
        # Passamos contador-1 para a lógica de 'w' ou 'a' funcionar no primeiro item
        grava(contador - 1, result)
        print(f"{valor} x {contador} = {result}")
        contador += 1

if __name__ == "__main__":
    main()