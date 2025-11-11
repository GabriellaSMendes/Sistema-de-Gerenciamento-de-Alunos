class Turma:
    
    #construtor
    def __init__(self, id, disciplina_id, professor_id, ano, semestre):
        self.id = id
        self.disciplina_id = disciplina_id
        self.professor_id = professor_id
        self.ano = ano
        self.semestre = semestre
    
    
"""        
#bloco de teste
turma1 = Turma(
    id=1,
    disciplina_id=10,
    professor_id=5,
    ano=2025,
    semestre=1
)

print("ID:", turma1.id)
print("Disciplina:", turma1.disciplina_id)
print("Professor:", turma1.professor_id)
print("Ano:", turma1.ano)
print("Semestre:", turma1.semestre)
"""