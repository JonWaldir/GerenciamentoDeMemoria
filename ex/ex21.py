import os

# --- b. Variáveis Globais ---
nome: str = ''
nota1 = nota2 = nota3 = nota4 = valor_media = 0.0
dir: str = ''
arq: str = ''

# --- e. Função que calcula a média ---
def med(n1, n2, n3, n4):
    media_local = (n1 + n2 + n3 + n4) / 4
    return media_local

# --- g. Função técnica de escrita ---
def escreveArq(caminho, arquivo, linha_arq):
    file = ''; tipo = ''; enc = ''
    caminho_completo = os.path.join(caminho, arquivo)
    
    if os.path.exists(caminho) and os.path.isdir(caminho):
        # Define se cria novo (w) ou adiciona ao final (a)
        if os.path.exists(caminho_completo):
            tipo = 'a'
        else:
            tipo = 'w'
            
        with open(caminho_completo, tipo) as f:
            f.write(linha_arq)

# --- f. Procedimento de cadastro ---
def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq
    dir = '/tmp/exercicios'
    arq = 'ex21.txt'
    
    # Monta a linha com ponto e vírgula e quebra de linha
    linha = str(nm) + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';' + str(nt4) + ';' + str(vlr_med) + '\n'
    escreveArq(dir, arq, linha)

# --- d. Procedimento de entrada de dados ---
def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    
    nome = input("\nDigite o nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    
    valor_media = med(nota1, nota2, nota3, nota4)
    
    print(f"Média calculada: {valor_media:.2f}")
    
    if valor_media >= 6.0:
        print("Mensagem: APROVADO")
    elif valor_media >= 3.0:
        print("Mensagem: EXAME")
    else:
        print("Mensagem: RETIDO")
        
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

# --- c. Procedimento principal ---
def main():
    # a. Cria a pasta e ajusta permissão para 744
    pasta_alvo = '/tmp/exercicios'
    if not os.path.exists(pasta_alvo):
        os.makedirs(pasta_alvo)
    os.chmod(pasta_alvo, 0o744)

    contador = 0
    while contador < 5:
        print(f"\n--- Cadastro {contador + 1} de 5 ---")
        entrada()
        contador += 1

if __name__ == "__main__":
    main() 