import game_of_life

######## escolha da estrutura Pulsar ######
celulas_vivas = [
    (15,30) ,(15,31), (15,32),(16,30) , 
    (17,30) , (18,30) , (19,30) , (19,31) , 
    (19,32) , (16,32) , (17,32) , (18,32) 
]

##############################################



game_of_life.executar_simulacao(celulas_vivas=celulas_vivas)