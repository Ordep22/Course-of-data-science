#Super Class
class Veiculos:
   def  __init__(self, marca, modelo):
      self.marca = marca
      self.modelo  = modelo

   def exibir_detalhes(self):
      print(f"O veiculo genérico: {self.marca} {self.modelo}")

#Cirar a Subclass
class Caro(Veiculos):
   def __init__(self, marca, modelo, porta):
      super().__init__(marca, modelo) #Isso indica que os elementos marca e modelo serão herdados da superclasse
      self.portas = porta
    
   def exibir_detalhes(self):
      print(f"Carro: {self.marca} {self.modelo} | Portas: {self.portas}")

class Moto(Veiculos):
   def __init__(self, marca, modelo, cilindradas):
      super().__init__(marca, modelo) #Isso indica que os elementos marca e modelo serão herdados da superclasse
      self.cilindradas = cilindradas
    
   def exibir_detalhes(self):
      print(f"Moto:  {self.marca} {self.modelo} | Cilindradas: {self.cilindradas}")




def main():
   
    minha_moto  = Moto("Honda", "Hornet", 500)
    meu_carro = Caro("Honda", "HRV", 5)
    minha_bike  = Veiculos("Bike: Cervelo","TT")

    minha_moto.exibir_detalhes()
    meu_carro.exibir_detalhes()
    minha_bike.exibir_detalhes()
   

if __name__ == "__main__":
   main()