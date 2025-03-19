# Game of Live (Jogo da Vida)
####################################
import game_of_life

# Células vivas iniciais
celulas_vivas = [
    (4, 1), (4, 2), (6, 2), (5, 3), (5, 4), 
    (4, 5), (6, 5), (6, 1), (5, 6)
]

# Executa a simulação
game_of_life.executar_simulacao(celulas_vivas=celulas_vivas)
