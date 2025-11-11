from backend.models.turma import Turma
from backend.repositories.turma_repo import TurmaRepository

class TurmaService:
    def __init__(self):
        self.repo = TurmaRepository()   
        
    def criarTurma(self, id_disciplina, id_professor, sigla_curso, ano, semestre):
        
        #campos obrigatorios
        if not id_disciplina or not id_professor or not sigla_curso or not ano or not semestre:
            print("Existem campos obrigatórios.")
            return
        
        # gera código da turma
        ano_curto = str(ano)[2:]
        cod_turma = f"T{sigla_curso.upper()}{ano_curto}0{semestre}"
        
        turma = Turma(id, cod_turma, id_disciplina, id_professor, sigla_curso, ano, semestre)
        self.repo.criarTurma(turma)
        print(f"Turma {cod_turma} criada.")
