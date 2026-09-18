import hashlib
import random
import string
import time

def gerar_senha(tamanho=12):
    # Conjunto de caracteres
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Todo os caracteres em um único pool
    todos_caracteres = maiusculas + minusculas + numeros + simbolos

    # Garantia de pelo menos um tipo para mais segurança
    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Preenchimento aleatório do que sobrar
    for _ in range(max(0, tamanho - 4)):
        senha.append(random.choice(todos_caracteres))

    # Embaralhamento para evitar padrões previsíveis
    random.shuffle(senha)
    senha_str = "".join(senha)

    # Irá gerar um hash único para cada senha
    conteudo_unico = f"{senha_str}-{time.time()}"
    hash_senha = hashlib.sha256(conteudo_unico.encode()).hexdigest()

    return senha_str, hash_senha

def salvar_em_txt(senha, hash_senha):
    nome_arquivo = "senhas_geradas.txt"
    data_hora = time.strftime("%d/%m/%Y %H:%M:%S")

    # O parâmetro 'a' (append) faz com que as novas senha sejam adicionadas
    # ao final do arquivo sem apagar oas anteriores
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"Data/Hora: {data_hora}\n")
        arquivo.write(f"Senha: {senha}\n")
        arquivo.write(f"Hash SHA-256: {hash_senha}\n")
        arquivo.write("=" * 50 + "\n\n")

    print(f"[Sucesso] Informações salvas no arquivo '{nome_arquivo}'.", flush=True)

if __name__ == "__main__":
        print("Inicio do programa")
        print(" --- Gerador de senhas seguras com Hash e txt ---", flush=True
        ) # Adicionado flush=True
        try:
            entrada = input("Digite o tamanho desejado para a senha (mínimo 10): ")
            tamanho_usuario = int(entrada) if entrada.strip() else 12

            if tamanho_usuario < 10: 
                print("Para maior segurança, o tamanho mínimo recomendo é 10. Ajustando para 10.", flush=True)
                tamanho_usuario = 10

                # Gerando senha e hash (fora do if de aviso para rodar sempre corretamente)
                senha_gerada, hash_gerado = gerar_senha(tamanho_usuario)

                print(f"Senha gerada: {senha_gerada}", flush=True)
                print(f"Hash SHA-256 único: {hash_gerado}", flush=True)

                salvar_em_txt(senha_gerada, hash_gerado)

        except ValueError:
            print("Por favor, digite apenas números inteiros válidos", flush=True)