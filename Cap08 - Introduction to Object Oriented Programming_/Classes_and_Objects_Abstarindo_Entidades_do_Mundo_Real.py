class carro:
    def __init__(self, marca:str, modelo:str, ano:int) -> None:

        self.marca  = marca
        self.modelo = modelo
        self.ano = ano
        self.veiculo_mode = False
        self.velocidade = 0
     
    def ligar(self):
         
        if self.veiculo_mode == True:
            print(f"O {self.modelo} está ligado")
        elif self.veiculo_mode == False:
            self.veiculo_mode = True
            print(f"O veiculo {self.modelo} será ligado em alguns instantes")
        else:
            self.veiculo_mode = False
            print(f"O veículo modelo {self.modelo} será desligado e parado por problemas!!!")
            

    def deligar(self):
        
        
        if self.veiculo_mode == True:
            self.veiculo_mode = False
            print(f"O veiculo {self.modelo} será desligado em alguns instantes")
        elif self.veiculo_mode == False:
            print(f"O veiculo {self.modelo} está desligado") 
        else:
            self.veiculo_mode = False
            print(f"O veículo modelo {self.modelo} será desligado e parado por problemas!!!")

    def acelerar(self):
        pass


    def exibir_informacao(self):
         
         print("\n")
         print(f"Modelo do veículo : {self.modelo}")
         print(f"Ano do veículo : {self.ano}")
         print(f"Marca do veículo : {self.marca}")
         print("\n")
    
def main():

    meu_carro  = carro("Ford","Focus", "2025")

    meu_carro.exibir_informacao()

    meu_carro.marca = "Ford"
    meu_carro.modelo = "Fiesta"
    meu_carro.ano = 2025

    meu_carro.exibir_informacao()




if __name__ == "__main__":

    main()