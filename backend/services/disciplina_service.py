from backend.models.disciplina import Disciplina
from backend.repositories.disciplina_repo import DisciplinaRepository

class DisciplinaService:
    def __init__(self):
        self.repo = DisciplinaRepository()
        
        
    #criar disciplina
    def criarDisciplina(self, id, nome, cod_disciplina, id_professor):
                
        #campos obrigatorios
        if not nome or not cod_disciplina or not id_professor:
            print("Existem campos obrigatórios.")
            return
        
        disciplinas = self.repo.listarDisciplina()
        for d in disciplinas:
            if d[2] == cod_disciplina:
                print("Já existe uma disciplina com esse código")
                return
            
        disciplina = Disciplina(id, nome, cod_disciplina, id_professor)
        self.repo.criarDisciplina(disciplina)
        print(f"Disciplina '{nome}' criada com sucesso!")