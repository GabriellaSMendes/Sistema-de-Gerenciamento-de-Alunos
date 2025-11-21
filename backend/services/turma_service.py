from backend.models.turma import Turma
from backend.repositories.turma_repo import TurmaRepository

class TurmaService:
    def __init__(self):
        self.repo = TurmaRepository()   
        
    def criarTurma(self, cod_turma, id_disciplina, id_professor, ano, semestre):
        
        #campos obrigatorios
        if not id_disciplina or not id_professor or not ano or not semestre:
            print("Existem campos obrigatórios.")
            return
        
                
        turma = Turma(None, cod_turma, id_disciplina, id_professor, None, ano, semestre)
        self.repo.criarTurma(turma)
        print(f"Turma {cod_turma} criada.")
