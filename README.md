# Gerador de Senhas Seguras em Python

Um script simples, porém robusto, desenvolvido em Python para gerar senhas altamente seguras utilizando conjuntos diversificados de caracteres (maiúsculas, minúsculas, números e símbolos), acompanhadas de um **Hash SHA-256 único** e salvamento automático em arquivo de texto.

## Funcionalidades

* **Geração Robusta:** Garante obrigatoriamente a inclusão de pelo menos uma letra maiúscula, uma minúscula, um número e um símbolo na senha.
* **Tamanho Configurável:** Permite definir o tamanho desejado (com restrição de segurança para um mínimo de 10 caracteres).
* **Hash SHA-256 Exclusivo:** Cria um identificador único combinando a senha gerada com o timestamp atual (`time.time()`).
* **Histórico em Arquivo (`.txt`):** Salva automaticamente o registro da data/hora, da senha e do hash correspondente em um arquivo `senhas_geradas.txt` usando o modo de adição (`append`), preservando os registros anteriores.

---

## Pré-requisitos

Certifique-se de ter o **Python 3** instalado em sua máquina. O projeto utiliza apenas bibliotecas nativas do Python, portanto **não é necessário instalar dependências externas** via `pip`.

---

## Como Executar

1. Clone o repositório ou baixe o arquivo principal (`.py`):
```bash
git clone https://github.com/LuizFabianoCDL/Code-Generator.git
cd Code-Generator

```

2. Execute o script através do terminal:
```bash
python nome-do-arquivo.py

```

# Observações:
- Main.py: os arquivos presentes no repositório são para fins de testes, ainda não há uma versão final até o momento. Quando houver, será sinalizado.


## Autores

Desenvolvido por **Gemini** e **Luiz Fabiano**.





