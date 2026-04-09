import os

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def divisao(fat):
    return 1 / fat

def escreve(total, caminho_origem):
    os.makedirs(caminho_origem, exist_ok=True)
    caminho_novo = f"{caminho_origem}/ex36.txt"
    arquivo = open(caminho_novo, 'a')
    arquivo.write(total + "\n")
    arquivo.close()

def main():
    pasta = '/tmp/exercicios'
    vezes = int(input('Digite um numero opara a soma de divisao sobre fatorial do numero: '))
    soma_total = 0
    
    for contador in range(1, vezes + 1):
        f = fatorial(contador)
        div = divisao(f)
        soma_total += div
        escreve(f"Termo {contador}: {div}", pasta)

    escreve(f"A soma total é: {soma_total}", pasta)
    print("Cálculo concluído e gravado com sucesso!")

if __name__ == '__main__':
    main()