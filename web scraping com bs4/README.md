Web Scraping

Este é um script em Python para realizar web scraping no site Books to Scrape e extrair informações sobre livros, incluindo título e preço. Os dados coletados são armazenados em um arquivo CSV para análise posterior.

📌 Funcionalidades

Coleta automática de títulos e preços de livros.

Navegação automática por todas as páginas do catálogo.

Armazenamento dos dados coletados em um arquivo CSV.

📋 Tecnologias Utilizadas

Python 3.x

Requests

BeautifulSoup4

Pandas

🛠️ Instalação e Configuração

Clone este repositório:

   git clone https://github.com/silvio-a-netto/portfolio.git

Navegue até o diretório do projeto:

   cd web scraping com bs4

## Instale as dependências necessárias:

   pip install pandas
   pip install requests
   pip install beautifulsoup4

## Estrutura do Projeto
web-scraping-com-bs4/
│── books_scraping/ # Planilha com dados coletados
│── scraping.py # Arquivo principal do projeto
│── README.md # Documentação do projeto

🚀 Como Executar

Basta rodar o seguinte comando no terminal:

   python scraping.py

Após a execução, os dados extraídos serão salvos no arquivo books_scraping.csv.

📂 Estrutura do Arquivo CSV

O script cria um arquivo CSV chamado books_scraping.csv com os seguintes campos:

Título: Nome do livro.

Preço: Preço do livro listado no site.

⚠️ Possíveis Problemas e Correções

Cabeçalhos User-Agent: Caso ocorra bloqueio de requisições, tente modificar o User-Agent nas requisições HTTP.

📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

👤 Autor

- **E-mail**: silvio.alex.netto@gmail.com
- **LinkedIn**: [linkedin.com/in/silvio-alexandre](https://www.linkedin.com/in/silvio-alexandre-1a8088312/)
- **GitHub**: [github.com/silvio-a-netto](https://github.com/silvio-a-netto)

