# My Music Player

## Descrição
My Music Player é um projeto de um reprodutor de música desenvolvido em Python, utilizando as bibliotecas Pygame (mixer), CustomTkinter, Threading e PIL. O aplicativo permite reproduzir, pausar e navegar entre faixas musicais, além de exibir a capa do álbum correspondente.

## Funcionalidades
- Reproduzir e pausar músicas.
- Exibir a capa do álbum da faixa em execução.
- Pular para a próxima faixa ou retornar à faixa anterior.
- Ajustar o volume da música.
- Barra de progresso para indicar o tempo da música.

## Tecnologias Utilizadas
- Python
- Tkinter & CustomTkinter - Interface Gráfica
- Pygame (mixer) - Reprodução de áudio
- PIL (Pillow) - Manipulação de imagens
- Threading - Execução de tarefas em segundo plano

## Instalação e Execução

### 1. Clone o repositório
```bash
git clone https://github.com/silvio-a-netto/my-music-player.git
cd my-music-player

## Instalando as dependências
pip install pygame customtkinter pillow

## Execute o programa
python music_player.py

## Estrutura do Projeto
my-music-player/
│── img/ # Pasta contendo as capas das músicas
│── music/ # Pasta contendo os arquivos de música (.mp3)
│── music_player.py # Arquivo principal do projeto
│── README.md # Documentação do projeto

## Controles
Play: Inicia a reprodução da música.
Skip Forward (>): Avança para a próxima música.
Skip Back (<): Retorna à faixa anterior.
Slider de Volume: Ajusta o volume da reprodução.


