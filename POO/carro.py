# A palavra "class" é usada para criar uma classe.
# Uma classe funciona como um molde para criar objetos
class Carro:

    # Método Construtor
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    # Métodos
    # Método acelerar
    # "aumento" sera o valor recebido para aumentar a velocidade.
    def acelerar(self, aumento):
        # self.velocidade = self.velocidade + aumento 
        self.velocidade += aumento
        print(f"O carro acelerou para {self.velocidade} km/h")

    #Metodo frear 
    def frear(self, reducao):
        # self.velocidade = self.velocidade + aumento 
        self.velocidade -= reducao
        print(f"O carro freou para {self.velocidade} km/h")

    # Metodo para exibir informacoes 
    def exibir_info(self):
        print("=== INFORMAOES DO CARRO ===")

        # Exibe os atributos do objeto
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"ano: {self.ano}")
        print(f"velocidade atual: {self.velocidade}")


# Criando um objeto da Classe Carro

# "carro1" é uma variável que recebe um objeto
carro1 = Carro("Chevrolet", "S10", 2013)
 
# Exibir informações do carro 1
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")

# O valor 50 sera enviado para o parametro "aumento"
carro1.acelerar(50)

# O valor 20 sera enviado para o parametro "redução"
# carro1.frear(redução)
carro1.frear(20)

# exibindo as informacoes do carro
carro1.exibir_info()






# # # "carro2" é uma variável que recebe um objeto
# carro2 = Carro("BYD", "Dolphin Mini", 2025)

# # # Exibir informações do carro 2
# print(f"Marca: {carro2.marca}")
# print(f"Modelo: {carro2.modelo}")
# print(f"Ano: {carro2.ano}")


