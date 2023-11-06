#+------------------------+
#|         Aluno          |
#+------------------------+
#| nome: String           |
#| sexo: String           |
#| matrícula: Int         |
#| nascimento: Date       |
#+------------------------+
#| Registrar(n, s, m, na) |
#| Atualizar(n, s, m, na) |
#| Consultar(n, m)        |
#| Excluir(m)             |
#+------------------------+

class Aluno:
    def __init__(self, nome, sexo, matricula, nascimento):
        self.nome = nome
        self.sexo = sexo
        self.matricula = matricula
        self.nascimento = nascimento

    def Registrar(self,nome,sexo,matricula,nascimento):
        
        
