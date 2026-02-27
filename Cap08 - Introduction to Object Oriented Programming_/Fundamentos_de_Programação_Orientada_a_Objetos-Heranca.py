#Classe pai
class Veiculo:

    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo 
        self.mode  = False
    
    def ligado(self):
        
        if self.mode == False:
            self.mode = True
            print(f"O {self.mode} foi ligado.")

        elif self.mode == True:
            print(f"O {self.mode} está ligado.")

        else:
            self.mode = False
            print(f"O {self.mode} será desligado por erro.")

    def deslig(self):
        
        if self.mode == True:
            self.mode = False
            print(f"O {self.mode} foi desligado.")

        elif self.mode == False:
            print(f"O {self.mode} está desligado.")

        else:
            self.mode = False
            print(f"O {self.mode} será desligado por erro.")



class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas  = portas

    def exibir_info_carro(self):
        print(f"\nCarro{self.marca} {self.modelo}, Portas: {self.portas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas  = cilindradas

    def empinar(self):
        print(f"\nA moto {self.mode} está empinando! Cuidado!")
    

def main():

    meu_carro  = Carro("Ford","Focus", "2025")

    meu_carro.exibir_info_carro()

    minha_moto  = Moto("Honda","Hornet",500)

    minha_moto.empinar()


if __name__ == "__main__":

    main()
