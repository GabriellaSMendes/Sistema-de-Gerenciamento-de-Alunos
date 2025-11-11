class Disciplina:
    
    #construtor
    def __init__(self, id, nome, cod_disciplina, professor_id):
        self.id = id
        self.nome = nome
        self.cod_disciplina = cod_disciplina
        self.professor_id = professor_id
        

"""
# Bloco de teste
disciplina1 = Disciplina(
    id=1,
    nome="Matemática",
    cod_disciplina="MAT101",
    professor_id=5
)

print("ID:", disciplina1.id)
print("Nome:", disciplina1.nome)
print("Código:", disciplina1.cod_disciplina)
print("Professor ID:", disciplina1.professor_id)
"""