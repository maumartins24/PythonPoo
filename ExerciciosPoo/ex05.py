class Livro:
    def __init__(self,titulo,autor,num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

livro1 = Livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 264)
livro2 = Livro('Fundamentals of Database Systems','Elsmasri Navathe', 1171)
lista = [livro1, livro2]
for x in lista:
    print('-'*30)
    print(f'Titulo: {x.titulo} \nAutor: {x.autor} \nNumero de paginas: {x.num_paginas}')