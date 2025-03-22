"""
Atividade Avaliativa MT2 - Geração de Números Pseudoaleatórios
Autores: Giselle Chaves, Marcius Moraes, Julia Agustini, Artur Lampert
"""
def main():
    from LinearCongruentGenerator import LinearCongruentGenerator

    a = 89
    c = 226
    m = 564
    seed = 14

    result = []
    result = LinearCongruentGenerator(a,c,m,seed)

    print("next_random:")
    print(result.next_random()) 
        

if __name__ == "__main__":
    main()
