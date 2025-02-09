# Avaliador de Locação de Imóveis

Este aplicativo é um CRUD simples desenvolvido com Python e Tkinter para avaliar imóveis com base em vários critérios, como localização, tamanho, segurança, e outros aspectos. O aplicativo permite que o usuário insira informações sobre diferentes imóveis e salve essas avaliações em um banco de dados SQLite.

📋 Funcionalidades <br>

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

🗄️ Estrutura do Banco de Dados <br>
O aplicativo utiliza um banco de dados SQLite chamado avaliacoes.db para armazenar as avaliações dos imóveis. A tabela avaliacoes é criada automaticamente se não existir.

A tabela contém as seguintes colunas: <br>

id (INTEGER) - Identificador único da avaliação. <br>
nome (VARCHAR) - Nome ou link do imóvel. <br>
localizacao, tamanho_do_imovel, aluguel, segurança, beleza, postos_de_saude, escola, mercado, hospital, area_verde (REAL) - Notas de 0 a 10 para os respectivos critérios de avaliação. <br>
localizacao_two, tamanho_do_imovel_two, aluguel_two, segurança_two, beleza_two, postos_de_saude_two, escola_two, mercado_two, hospital_two, area_verde_two (REAL) - Notas de 0 a 10 para os mesmos critérios, mas considerando uma comparação com outro imóvel (por exemplo, a "esposa"). <br>
avaliacao_final (REAL) - Média das avaliações, calculada com base nos critérios. <br>

📂 Estrutura do Projeto <br>
Alocação-de-casa/ <br>
│── img/ # Pasta contendo as imagens utilizadas <br>
│── main.py # Arquivo principal do projeto <br>
│── README.md # Documentação do projeto <br>

📝 Requisitos <br>

- Python 3.x <br>
- Tkinter (geralmente vem pré-instalado com o Python) <br>
- SQLite3 (incluso no Python por padrão) <br>
- Pillow (biblioteca para manipulação de imagens) <br>

🚀 Instalação

### 1. Clonar o repositório

Clone este repositório para o seu computador:

```bash
git clone https://github.com/silvio-a-netto/portfolio.git

## Instalando dependências
pip install pillow
pip install tk (se necessario)

🎮 Executando o programa
python main.py

👤 Autor

- **E-mail**: silvio.alex.netto@gmail.com
- **LinkedIn**: [linkedin.com/in/silvio-alexandre](https://www.linkedin.com/in/silvio-alexandre-1a8088312/)
- **GitHub**: [github.com/silvio-a-netto](https://github.com/silvio-a-netto)
