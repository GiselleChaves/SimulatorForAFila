"""
Atividade Avaliativa MT2 - Geração de Números Pseudoaleatórios
Autores: Giselle Chaves, Marcius Moraes, Julia Agustini, Artur Lampert
"""
def main():
    from Generator import Generator
    a = 89
    c = 226
    m = 564371982
    seed = 14

    result = []
    result = Generator(a,c,m,seed)

    print("next_random:")
    print(result.next_random()) 
    print(result.next_random()) 
    print(result.next_random()) 
    print(result.next_random()) 

    
        

if __name__ == "__main__":
    main()
