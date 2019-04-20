# Código bastante simples, para servir de referência para quem está aprendendo a programar 
# conforme as boas práticas, cada método tem apenas uma função! by Clean Code 

def calcula_imc(altura,peso):
    # Algoritmo básico que cálcula o IMC (Índice de massa corporal!)
    # Outra forma de calcular, (peso / (altura * altura)), o ** é o operador de potenciação!
    return (peso / (altura ** 2))

def get_altura_peso():
    # Método para pegar a altura e o peso via console!
    # Antes do input definimos o tipo do input nesse caso float
    altura = float(input("Informe sua altura: "))
    peso = float(input("Informe seu peso: "))
    
    # Retornamos a altur e o peso da forma que o próximo método esta aguardando o retorno
    return altura,peso

def gera_imc():

    # Atribuindo os valores conforme o método get_altura_peso!
    altura, peso = get_altura_peso()
    # Escrevendo o resultado, conforme a coleta e apuração das informações
    print ("Seu IMC (Índice de massa corporal) é: %s " % calcula_imc(altura,peso))

# Chamada do método final que conforme o nome gera o LMC! :D 
gera_imc()