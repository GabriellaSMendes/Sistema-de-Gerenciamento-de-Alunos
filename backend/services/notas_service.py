from backend.models.notas import Notas
from backend.repositories.notas_repo import NotasRepository
from backend.repositories.usuario_repo import UsuarioRepository

class NotasService:
    
    def __init__(self):
        self.repo = NotasRepository()
        self.usuario_repo = UsuarioRepository() 
       
    #lançar notas
    def lancarNotas(self, id_disciplina, aluno_id, turma_id, avaliacao, nota, data_lancamento):
        
        #campos obrigatórios
        if not id_disciplina or not aluno_id or not turma_id or not avaliacao or not nota or not data_lancamento:
            print("Existem campos obrigatórios.")
            return
            
        #verifica se é aluno
        usuario = self.usuario_repo.buscarPorID(aluno_id)
        if usuario[5] != "ALUNO":
            print("Usuário não é aluno. Não é possível lançar nota.")
            return
        
        nota = round(float(nota), 2)
        
        nota = Notas(None, id_disciplina, aluno_id, turma_id, avaliacao, nota, data_lancamento)
        self.repo.lancarNotas(nota)
        print(f"Nota lançada para o aluno {usuario[1]}")