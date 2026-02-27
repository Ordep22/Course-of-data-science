class carro:
    def __init__(self, marca:str, modelo:str, ano:int) -> None:

        self.marca  = marca
        self.modelo = modelo
        self.ano = ano
        self.veiculo_mode = False
        self._velocidade = 0 
        self.__horsepower = 300
     
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


    def get_velocidade(self):

        print(f"O {self.modelo} está a {self._velocidade} Km/h")
        
        return self._velocidade

    def acelera(self,valor):
        if valor > 0:
            self._velocidade += valor
        else:
            print("O valor de aceleração deve ser positivo!!!")
    
    def frear(self, valor):
        if valor > 0:
            self._velocidade -= valor
            if self._velocidade < 0:
                self._velocidade = 0
            print(f"O {self.modelo} freou para {self._velocidade} Km/h")
        else:
            print("O valor de frenagem deve ser positivo!!!")
        


    def exibir_informacao(self):
         
         print("\n")
         print(f"Modelo do veículo : {self.modelo}")
         print(f"Ano do veículo : {self.ano}")
         print(f"Marca do veículo : {self.marca}")
         print("\n")
    
def main():

    meu_carro  = carro("Ford","Focus", "2025")

    print(f"Dict: {meu_carro.__dict__}")

    meu_carro.exibir_informacao()

    meu_carro.marca = "Ford"
    meu_carro.modelo = "Fiesta"
    meu_carro.ano = 2025

    meu_carro.exibir_informacao()

    meu_carro.get_velocidade()

    meu_carro.acelera(25)

    meu_carro.get_velocidade()

    meu_carro.frear(5)

    meu_carro.get_velocidade()

    print(f"\n Testando o encapsulamento: {meu_carro._carro__horsepower}")

    print(f"\n Forcçando erro no encapsulamento")

    meu_carro._carro__horsepower = 450

    print(f"\n Testando o 'erro' do encapsulamento no python: {meu_carro._carro__horsepower}")

if __name__ == "__main__":

    main()
