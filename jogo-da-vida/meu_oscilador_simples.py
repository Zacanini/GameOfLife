import game_of_life

# oscila ate por volta da geraçao 320 , onde adota um padrão que se repete pra sempre 
# formando formas de quadrados e retangulos , como um oscilador
celulas_vivas = [
   (1,5),(1,6),(1,7),(1,8),(1,9),(1,10),
   (2,5),(2,6),(2,7),(2,8),(2,9),(2,10),
   (3,5),(3,6),(3,7),(3,8),(3,9),(3,10),
   (4,5),(4,6),(4,7),(4,8),(4,9),(4,10),
   (5,1) , (5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),
   (1,12) , (1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(1,21),
   (2,22) , (2,23),(2,24),(2,25),(2,26),(2,27),(2,28),(2,29),(2,20),(2,22),

] 

#aqui aumentando um pouco mais a largura das celulas vivas , vemos que por volta da geraçao 240 
#tudo parecia estar se estabilizando , mas a partir da geraçao 320 aproximadamente , ela começa a 'atacar'
#outras celulas vivas , formando um retangulo de 3 celulas que se repete pra sempre oscilando na vertical e horizontal 
celulas_vivas2 = [
   (1,5),(1,6),(1,7),(1,8),(1,9),(1,10),
   (2,5),(2,6),(2,7),(2,8),(2,9),(2,10),
   (3,5),(3,6),(3,7),(3,8),(3,9),(3,10), (3,15),(3,16),(3,17),(3,18),
   (4,5),(4,6),(4,7),(4,8),(4,9),(4,10), (4,15),(4,16),(4,17),(4,18),
   (5,1) , (5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),
   (1,12) , (1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(1,21),
   (2,22) , (2,23),(2,24),(2,25),(2,26),(2,27),(2,28),(2,29),(2,20),(2,22),

] 

#aqui dobrando as celuals vivas , repetindo o padrao a cima , percebe-se o padrao anterior de espalhar
#celulas vivas , mas a partir da geraçao 190 aproximadamente , elas começa a se 'atacar' ate que por bolta da geracao 220
# ela gera um unico planador que é disparado para a esquerda da tela e tudo se estabiliza ate aquele planador chegar na borda. 
celulas_vivas3 = [
   (1,5),(1,6),(1,7),(1,8),(1,9),(1,10),
   (2,5),(2,6),(2,7),(2,8),(2,9),(2,10),
   (3,5),(3,6),(3,7),(3,8),(3,9),(3,10), (3,15),(3,16),(3,17),(3,18),
   (4,5),(4,6),(4,7),(4,8),(4,9),(4,10), (4,15),(4,16),(4,17),(4,18),
   (5,1) , (5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),
   (1,12) , (1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(1,21),
   (2,22) , (2,23),(2,24),(2,25),(2,26),(2,27),(2,28),(2,29),(2,20),(2,22),
   (10,5),(10,6),(10,7),(10,8),(10,9),(10,10),
   (11,5),(11,6),(11,7),(11,8),(11,9),(11,10),
   (12,5),(12,6),(12,7),(12,8),(12,9),(12,10), (12,15),(12,16),(12,17),(12,18),
   (13,5),(13,6),(13,7),(13,8),(13,9),(13,10), (13,15),(13,16),(13,17),(13,18),
   (14,1) , (14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,9),(14,10),
   (10,12) , (10,13),(10,14),(10,15),(10,16),(10,17),(10,18),(10,19),(10,20),(10,21),
   (11,22) , (11,23),(11,24),(11,25),(11,26),(11,27),(11,28),(11,29),(11,20),(11,22),

] 

#aqui dobramos o tamanho das celulas vivas ocupando mais espaço na tela , percebe-se aqui que varias vezes ascelulas quase se estabilizam
#mas sempre acabam se atacando e formando novos padroes , mas no final , todas as celulas vivas se estabilizam e formam um padrao de retangulos e quadrados
#com uma celula morta no meio e 4 vivas na beirada , e 2 retangulos em loop de horizontal e vertical. 
celulas_vivas4 = [
   (1,5),(1,6),(1,7),(1,8),(1,9),(1,10),
   (2,5),(2,6),(2,7),(2,8),(2,9),(2,10),
   (3,5),(3,6),(3,7),(3,8),(3,9),(3,10), (3,15),(3,16),(3,17),(3,18),
   (4,5),(4,6),(4,7),(4,8),(4,9),(4,10), (4,15),(4,16),(4,17),(4,18),
   (5,1) , (5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),
   (1,12) , (1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(1,21),
   (2,22) , (2,23),(2,24),(2,25),(2,26),(2,27),(2,28),(2,29),(2,20),(2,22),
   (10,5),(10,6),(10,7),(10,8),(10,9),(10,10),
   (11,5),(11,6),(11,7),(11,8),(11,9),(11,10),
   (12,5),(12,6),(12,7),(12,8),(12,9),(12,10), (12,15),(12,16),(12,17),(12,18),
   (13,5),(13,6),(13,7),(13,8),(13,9),(13,10), (13,15),(13,16),(13,17),(13,18),
   (14,1) , (14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,9),(14,10),
   (10,12) , (10,13),(10,14),(10,15),(10,16),(10,17),(10,18),(10,19),(10,20),(10,21),
   (11,22) , (11,23),(11,24),(11,25),(11,26),(11,27),(11,28),(11,29),(11,20),(11,22),

   (30,5),(30,6),(30,7),(30,8),(30,9),(30,10),
   (31,5),(31,6),(31,7),(31,8),(31,9),(31,10),
   (32,5),(32,6),(32,7),(32,8),(32,9),(32,10), (32,15),(32,16),(32,17),(32,18),
   (33,5),(33,6),(33,7),(33,8),(33,9),(33,10), (33,15),(33,16),(33,17),(33,18),
   (34,1) , (34,2),(34,3),(34,4),(34,5),(34,6),(34,7),(34,8),(34,9),(34,10),
   (30,12) , (30,13),(30,14),(30,15),(30,16),(30,17),(30,18),(30,19),(30,20),(30,21),
   (31,22) , (31,23),(31,24),(31,25),(31,26),(31,27),(31,28),(31,29),(31,20),(31,22),
   (40,5),(40,6),(40,7),(40,8),(40,9),(40,10),
   (41,5),(41,6),(41,7),(41,8),(41,9),(41,10),
   (42,5),(42,6),(42,7),(42,8),(42,9),(42,10), (42,15),(42,16),(42,17),(42,18),
   (43,5),(43,6),(43,7),(43,8),(43,9),(43,10), (43,15),(43,16),(43,17),(43,18),
   (44,1) , (44,2),(44,3),(44,4),(44,5),(44,6),(44,7),(44,8),(44,9),(44,10),
   (40,12) , (40,13),(40,14),(40,15),(40,16),(40,17),(40,18),(40,19),(40,20),(40,21),
   (41,22) , (41,23),(41,24),(41,25),(41,26),(41,27),(41,28),(41,29),(41,20),(41,22),

] 

#Aqui temos no meio da tela 4 padroes que se repetem oscilando entre si , e em cima da tela coloquei celulas aleatorias para ver 
#se elas chegavam no padrao do meio e formavam um novo padrao , no final , o padrao do meio nao é tocado , porem as celulas que foram
#colocadas aleatoriamente se estabilizaram e formaram um padrao que formava varias formas geometricas repetidas no topo da tela oscilando entre si
celulas_vivas5 = [
   (1,5),(1,6),(1,7),(1,8),(1,9),(1,10),
   (2,5),(2,6),(2,7),(2,8),(2,9),(2,10),
   (3,5),(3,6),(3,7),(3,8),(3,9),(3,10),
   (4,5),(4,6),(4,7),(4,8),(4,9),(4,10),
   (5,1) , (5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),
   (1,12) , (1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(1,21),
   (2,22) , (2,23),(2,24),(2,25),(2,26),(2,27),(2,28),(2,29),(2,20),(2,22),
   (30 , 30), (30,31), (30,32), (31,30), (31,32), (32,30), (32,31), (32,32),
   (30 , 40), (30,41), (30,42), (31,40), (31,42), (32,40), (32,41), (32,42),
   (40 , 30), (40,31), (40,32), (41,30), (41,32), (42,30), (42,31), (42,32),
   (40 , 40), (40,41), (40,42), (41,40), (41,42), (42,40), (42,41), (42,42),
]

# Executa a simulação
game_of_life.executar_simulacao(celulas_vivas=celulas_vivas2)

#Mexendo e observando em todos esses padroes a cima , achei algo interessante e que parece que se repete sempre em estrturas como as a cima
#, que é a forma que as celulas vivas se comportam , elas sempre 'lutam' entre si no inicio , formam especies de bases e entao 
# é possivel ver um lado da tela 'guerreando' e o outro lado estabilizado , e logo entao a 'guerra' se espalha para o lado estabilizado
# como uma especie de virus , até que em algum momento tudo se estabiliza e forma um padrao que se repete pra sempre , e isso é muito interessante
# de se observar e pensar sobre , como a vida pode se comportar de forma tao simples e complexa ao mesmo tempo.