import os

def grava_arq(quadrado, pasta):
    # Primeiro: Garante que a pasta existe (apenas cria se não existir)
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    # SEGUNDO: O caminho e a gravação devem estar FORA do IF acima
    caminho_completo = os.path.join(pasta, "ex31.txt")
    
    # Modo 'a' adiciona conteúdo ao final do arquivo
    with open(caminho_completo, 'a') as arquivo:
        arquivo.write(f"{quadrado}\n")

def main():
    pasta_alvo = 'C:\\temp\\' 
    nome_arquivo = "ex31.txt"
    caminho_total = os.path.join(pasta_alvo, nome_arquivo)
    
    
    if os.path.exists(caminho_total):
        os.remove(caminho_total)
    
    contador = 11
    while contador < 150:
        resultado = contador * contador
        grava_arq(resultado, pasta_alvo)
        contador += 1
    
    


if __name__ == "__main__":
    main()
