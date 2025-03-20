"""
Atividade Avaliativa MT2 - Geração de Números Pseudoaleatórios
Autores: Giselle Chaves, Marcius Moraes, Julia Agustini, Artur Lampert
"""

from Generator import linearCongruentGenerator
from Generator import uniformity

a = 7632
c = 6245
m = 2.83712893198237E+29
seed = 14

result = []
result = linearCongruentGenerator(a,c,m,seed)
resultUniformity = uniformity(result,m)

print(len(result))

print("Values:")
for i in result:
    print(i) 
    
print("Uniformity:")
for i in resultUniformity:
    print(i)