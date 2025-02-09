# Avaliador de Locação de Imóveis

Este é um aplicativo simples desenvolvido com Python e Tkinter para avaliar imóveis com base em vários critérios, como localização, tamanho, segurança, e outros aspectos. O aplicativo permite que o usuário insira informações sobre diferentes imóveis e salve essas avaliações em um banco de dados SQLite.

## Funcionalidades

- Cadastro de imóveis com informações como:
  - Localização
  - Tamanho do imóvel
  - Aluguel
  - Segurança
  - Beleza
  - Postos de saúde
  - Escola
  - Mercado
  - Hospital
  - Área verde
- Armazenamento das avaliações no banco de dados SQLite.
- Interface gráfica utilizando Tkinter e PIL para exibir imagens e criar a interface.
- Validação dos dados inseridos para garantir que as notas estão dentro da faixa permitida (0 a 10).

### Estrutura do Banco de Dados
O aplicativo utiliza um banco de dados SQLite chamado avaliacoes.db para armazenar as avaliações dos imóveis. A tabela avaliacoes é criada automaticamente se não existir.

A tabela contém as seguintes colunas:

id (INTEGER) - Identificador único da avaliação.
nome (VARCHAR) - Nome ou link do imóvel.
localizacao, tamanho_do_imovel, aluguel, segurança, beleza, postos_de_saude, escola, mercado, hospital, area_verde (REAL) - Notas de 0 a 10 para os respectivos critérios de avaliação.
localizacao_two, tamanho_do_imovel_two, aluguel_two, segurança_two, beleza_two, postos_de_saude_two, escola_two, mercado_two, hospital_two, area_verde_two (REAL) - Notas de 0 a 10 para os mesmos critérios, mas considerando uma comparação com outro imóvel (por exemplo, a "esposa").
avaliacao_final (REAL) - Média das avaliações, calculada com base nos critérios.

## Requisitos

- Python 3.x
- Tkinter (geralmente vem pré-instalado com o Python)
- SQLite3 (incluso no Python por padrão)
- Pillow (biblioteca para manipulação de imagens)

## Instalação

### 1. Clonar o repositório

Clone este repositório para o seu computador:

```bash
git clone https://github.com/silvio-a-netto/avaliador-imoveis.git

## Instalando dependências
pip install pillow
pip install tk

## Executando o programa
python main.py


