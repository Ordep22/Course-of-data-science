class Livros:

    def __init__(self,titulo, autor, paginas, genero):
        self.titulo  = titulo
        self.autor = autor
        self.paginas  = paginas
        self.genero  = genero

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
    
    def __len__(self):
        return self.paginas
    
def main():
    my_book  = Livros("Deep Learning Book", "DSA", 450, "Ciências & Tecnologia")
    type(my_book)
    print(f"O livro tem {len(my_book)} páginas") 

if __name__ == "__main__":
    main()