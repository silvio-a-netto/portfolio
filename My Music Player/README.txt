<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Music Player - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1a1c1f;
            color: white;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #222;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            text-align: left;
        }
        h1, h2 {
            color: #05ad17;
        }
        code {
            background: #333;
            padding: 5px;
            border-radius: 5px;
        }
        pre {
            background: #333;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>My Music Player</h1>
        <h2>Descrição</h2>
        <p>My Music Player é um projeto de um reprodutor de música desenvolvido em Python, utilizando as bibliotecas <strong>Pygame (mixer)</strong>, <strong>CustomTkinter</strong>, <strong>Threading</strong> e <strong>PIL</strong>. O aplicativo permite reproduzir, pausar e navegar entre faixas musicais, além de exibir a capa do álbum correspondente.</p>
        
        <h2>Funcionalidades</h2>
        <ul>
            <li>Reproduzir e pausar músicas.</li>
            <li>Exibir a capa do álbum da faixa em execução.</li>
            <li>Pular para a próxima faixa ou retornar à faixa anterior.</li>
            <li>Ajustar o volume da música.</li>
            <li>Barra de progresso para indicar o tempo da música.</li>
        </ul>
        
        <h2>Tecnologias Utilizadas</h2>
        <ul>
            <li>Python</li>
            <li>Tkinter & CustomTkinter - Interface Gráfica</li>
            <li>Pygame (mixer) - Reprodução de áudio</li>
            <li>PIL (Pillow) - Manipulação de imagens</li>
            <li>Threading - Execução de tarefas em segundo plano</li>
        </ul>
        
        <h2>Instalação e Execução</h2>
        <h3>1. Clone o repositório</h3>
        <pre><code>git clone https://github.com/seu-usuario/my-music-player.git
cd my-music-player</code></pre>
        
        <h3>2. Instale as dependências</h3>
        <pre><code>pip install pygame customtkinter pillow</code></pre>
        
        <h3>3. Execute o programa</h3>
        <pre><code>python music_player.py</code></pre>
        
        <h2>Estrutura do Projeto</h2>
        <pre><code>my-music-player/
│── img/                   # Pasta contendo as capas das músicas
│── music/                 # Pasta contendo os arquivos de música (.mp3)
│── music_player.py        # Arquivo principal do projeto
│── README.md              # Documentação do projeto</code></pre>
        
        <h2>Controles</h2>
        <ul>
            <li><strong>Play:</strong> Inicia a reprodução da música.</li>
            <li><strong>Skip Forward (>):</strong> Avança para a próxima música.</li>
            <li><strong>Skip Back (<):</strong> Retorna à faixa anterior.</li>
            <li><strong>Slider de Volume:</strong> Ajusta o volume da reprodução.</li>
        </ul>
        
        <h2>Contribuição</h2>
        <p>Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Para isso:</p>
        <ol>
            <li>Faça um fork do repositório</li>
            <li>Crie uma branch (<code>git checkout -b minha-nova-funcionalidade</code>)</li>
            <li>Commit suas alterações (<code>git commit -m 'Adicionando nova funcionalidade'</code>)</li>
            <li>Envie para o repositório (<code>git push origin minha-nova-funcionalidade</code>)</li>
            <li>Abra um Pull Request</li>
        </ol>
    </div>
</body>
</html>