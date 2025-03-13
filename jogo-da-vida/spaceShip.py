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

######## escolha da estrutura spaceship (espaçonave) ######
a[2,10]=1
a[3,10]=1
a[4,10]=1 
a[1,11]=1
a[4,11]=1
a[4,12]=1
a[4,13]=1
a[1,14]=1
a[3,14]=1
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
                # Resto do código igual
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
                   if (vizinho==2) or (vizinho==3):
                       novo_a[i,j]=1                
                   else:                            
                       novo_a[i,j]=0
                else:
                   if vizinho==3:                  
                      novo_a[i,j]=1                
                   else:
                      novo_a[i,j]=0                
      ger += 1
      
      a=novo_a                                      
      novo_a=np.zeros((n+1,m+1)) 
      fig.clf()  # Limpa a figura atual
      fig.title('GERAÇÃO %d' % ger, fontsize=20)
      fig.xticks([])           
      fig.yticks([])            
      im = fig.imshow(a, interpolation = "nearest",cmap='Greys',animated=True)
      
      try:
          fig.get_current_fig_manager().window.geometry(f"400x400+20+20")
      except:
          try:
              fig.gcf().set_size_inches(4, 4)
          except:
              pass
      
      fig.pause(0.5)                  
      
      if not chave:  
          break

print("Simulação encerrada após", ger, "gerações.")
