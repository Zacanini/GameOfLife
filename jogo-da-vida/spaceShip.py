import game_of_life

######## estrutura spaceship (espaçonave) ######
celulas_vivas = [
    (2,10), (3,10), (4,10), (1,11), 
    (4,11), (4,12), (4,13), (1,14), (3,14)
]
##############################################

game_of_life.executar_simulacao(celulas_vivas=celulas_vivas)
