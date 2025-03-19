import numpy as np
import matplotlib.pyplot as fig
from matplotlib import animation, cm

def executar_simulacao(celulas_vivas=None, matriz_inicial=None, n=80, m=80, pausa=0.5):
    """
    Executa a simulação do Jogo da Vida.
    
    Parâmetros:
    -----------
    celulas_vivas : list, opcional
        Lista de tuplas (i, j) representando as posições das células vivas iniciais
    matriz_inicial : ndarray, opcional
        Matriz numpy com configuração inicial (tem precedência sobre celulas_vivas)
    n : int
        Número de linhas da matriz
    m : int
        Número de colunas da matriz
    pausa : float
        Tempo de pausa entre cada geração em segundos
    """
    # Inicializa as matrizes
    a = np.zeros((n+1, m+1))
    novo_a = np.zeros((n+1, m+1))
    
    # Configura células vivas iniciais
    if matriz_inicial is not None:
        a = matriz_inicial.copy()
    elif celulas_vivas is not None:
        for i, j in celulas_vivas:
            a[i, j] = 1
    
    # Variáveis para controle da simulação
    chave = [True]  # Lista para poder modificar dentro da função callback
    
    def tecla_pressionada(evento):
        if evento.key == 'q':
            print("Tecla 'q' pressionada. Encerrando simulação...")
            chave[0] = False
    
    # Configuração da figura
    fig.close('all')
    figura = fig.figure(figsize=(6, 6))
    figura.canvas.mpl_connect('key_press_event', tecla_pressionada)
    
    ger = 0
    while chave[0]:    # Iteração das gerações               
        for i in range(1, n):  # Percorre as linhas
            for j in range(1, m):  # Percorre as colunas
                vizinho = 0
                
                # Contagem de vizinhos (verificações de 8 células vizinhas)
                if a[i-1, j-1] == 1: vizinho += 1                       
                if a[i, j-1] == 1: vizinho += 1                          
                if a[i+1, j-1] == 1: vizinho += 1                       
                if a[i+1, j] == 1: vizinho += 1                       
                if a[i+1, j+1] == 1: vizinho += 1                       
                if a[i, j+1] == 1: vizinho += 1                       
                if a[i-1, j+1] == 1: vizinho += 1                      
                if a[i-1, j] == 1: vizinho += 1
                
                # Regras :
                if a[i, j] == 1:
                    if (vizinho == 2) or (vizinho == 3):  # Célula viva com 2 ou 3 vizinhos sobrevive
                        novo_a[i, j] = 1
                    else:
                        novo_a[i, j] = 0
                else:
                    if vizinho == 3:  # Célula morta com exatamente 3 vizinhos nasce
                        novo_a[i, j] = 1
                    else:
                        novo_a[i, j] = 0
        
        ger += 1
        
        a = novo_a.copy()
        novo_a = np.zeros((n+1, m+1))
        
        # Atualiza a visualização
        fig.clf()
        fig.title(f'GERAÇÃO {ger}', fontsize=20)
        fig.xticks([])
        fig.yticks([])
        im = fig.imshow(a, interpolation="nearest", cmap='Greys', animated=True)
        
        # mudei como a tela é gerada pois estava dando erro no windows
        try:
            fig.get_current_fig_manager().window.geometry(f"400x400+20+20")
        except:
            try:
                fig.gcf().set_size_inches(4, 4)
            except:
                pass
        
        fig.pause(pausa)
        
        if not chave[0]:
            break
    
    print(f"Simulação encerrada após {ger} gerações.")
    return ger