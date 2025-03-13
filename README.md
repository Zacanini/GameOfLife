

🧬 Jogo da Vida em Python
Simulação do Jogo da Vida (John Conway), um autômato celular que demonstra como regras simples geram comportamentos complexos.

🔍 Sobre o Projeto
O Jogo da Vida opera em um grid bidimensional, onde cada célula pode estar viva (1) ou morta (0). A evolução das gerações segue regras baseadas na vizinhança de cada célula.

Regras do Jogo:
Superpopulação: Células vivas com mais de 3 vizinhos morrem.

Solidão: Células vivas com menos de 2 vizinhos morrem.

Reprodução: Células mortas com exatamente 3 vizinhos tornam-se vivas.

Estabilidade: Células vivas com 2 ou 3 vizinhos permanecem vivas.

🛠 Implementação
Funcionamento do Código:
Matriz NumPy: Armazena o estado atual (a) e o próximo estado (novo_a).

Loop Principal: Atualiza o grid iterando sobre cada célula e contando vizinhos.

Visualização: Usa matplotlib para exibir o grid em tempo real.

Exemplo de Estruturas Incluídas:

Arquivo	     | Descrição	   | Comportamento
gun.py	     | Glider Gun	   | Emite planadores periodicamente
planador.py	 | Planador	     | Move-se diagonalmente pelo grid
spaceship.py | Nave Espacial | Move-se em linha reta
pulsar.py	   | Pulsar	       | Oscila a cada 3 gerações
🚀 Como Executar
Instale as dependências:

bash
Copy
pip install numpy matplotlib
Execute um dos arquivos (ex: python gun.py).

Pressione Q para encerrar a simulação.
