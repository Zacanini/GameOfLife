# Game of Live (Jogo da Vida)
####################################
import numpy as np
import matplotlib.pyplot as fig
from matplotlib import animation, cm
import random

fig.close('all')  # fecha figuras existentes

n=80              # números de linhas
m=80              # número de colunas

##### inicializa com zeros  ###############
a=np.zeros((n+1,m+1))
novo_a=np.zeros((n+1,m+1))
############################################

######## escolha da estrutura inicial ######
a[4,1]=1
a[4,2]=1
a[6,2]=1 
a[5,3]=1
a[5,4]=1
a[4,5]=1
a[6,5]=1
a[6,1]=1
a[5,6]=1
##############################################

# Função para capturar o pressionamento da tecla
def tecla_pressionada(evento):
    global chave
    if evento.key == 'q':
        print("Tecla 'q' pressionada. Encerrando simulação...")
        chave = False

# Criar a figura antes do loop
figura = fig.figure(figsize=(6, 6))
# Conectar o evento de pressionar tecla
figura.canvas.mpl_connect('key_press_event', tecla_pressionada)

ger = 0
chave = True
while chave:    # <----------------- iteração das gerações               
      for i in range(1,n): # <-------------- percorre as linhas
           for j in range(1,m): #<---------- percorre as colunas
                vizinho=0
                if a[i-1,j-1]==1:
                          vizinho=vizinho+1                       
                if a[i,j-1]==1:
                          vizinho=vizinho+1                          
                if a[i+1,j-1]==1:
                          vizinho=vizinho+1                       
                if a[i+1,j]==1:
                          vizinho=vizinho+1                       
                if a[i+1,j+1]==1:
                          vizinho=vizinho+1                       
                if a[i,j+1]==1:
                          vizinho=vizinho+1                       
                if a[i-1,j+1]==1:
                          vizinho=vizinho+1                      
                if a[i-1,j]==1:
                          vizinho=vizinho+1                          
                if a[i,j]==1:
                   if (vizinho==2) or (vizinho==3): ### se célula viva com 2
                       novo_a[i,j]=1                ### ou 3 vizinhos, permanece
                   else:                            ### viva
                       novo_a[i,j]=0
                else:
                   if vizinho==3:                  ### se espaço vazio com 2
                      novo_a[i,j]=1                ### ou 3 vizinhos, nasce
                   else:
                      novo_a[i,j]=0                ### se espaço vazio com 1 ou 
      ger += 1
      
      a=novo_a                                      ### 4 viz, permanece vazio
      novo_a=np.zeros((n+1,m+1)) ### atualiza a regra
      fig.clf()  # Limpa a figura atual
      fig.title('GERAÇÃO %d' % ger, fontsize=20)
      fig.xticks([])            # esconde os numeros do eixo x
      fig.yticks([])            # esconde os números do eixo y
      im = fig.imshow(a, interpolation = "nearest",cmap='Greys',animated=True)
      
      # Usa try/except para lidar com diferentes backends
      try:
          fig.get_current_fig_manager().window.geometry(f"400x400+20+20")  # Reduzido ainda mais
      except:
          try:
              fig.gcf().set_size_inches(4, 4)    # Reduzido para 4x4 polegadas
          except:
              pass  # Ignora erros se não conseguir configurar o tamanho
      
      fig.pause(0.5)                  ### pausa para ver as células se mover
      
      if not chave:  # Verifica se a tecla 'q' foi pressionada
          break

print("Simulação encerrada após", ger, "gerações.")
