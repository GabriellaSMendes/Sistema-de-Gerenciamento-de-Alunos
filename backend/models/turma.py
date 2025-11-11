class Turma:
    
    #construtor
    def __init__(self, id, cod_turma, id_disciplina, id_professor, ano, semestre):
        self.id = id
        self.cod_turma = cod_turma
        self.id_disciplina = id_disciplina
        self.id_professor = id_professor
        self.ano = ano
        self.semestre = semestre
    
    
"""        
#bloco de teste
turma1 = Turma(
    id=1,
    cod_turma = "TADS2302"
    id_disciplina=10,
    id_professor=5,
    ano=2025,
    semestre=1
)

print("ID:", turma1.id)
print("Disciplina:", turma1.id_disciplina)
print("Código:", turma1.cod_turma)
print("Professor:", turma1.id_professor)
print("Ano:", turma1.ano)
print("Semestre:", turma1.semestre)
"""