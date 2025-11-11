from datetime import date

class Notas():
    
    #construtor
    def __init__(self, id, id_disciplina, aluno_id, turma_id, avaliacao, nota, data_lancamento: date):
        self.id = id
        self.id_disciplina = id_disciplina
        self.aluno_id = aluno_id
        self.turma_id = turma_id
        self.avaliacao = avaliacao
        self.nota = nota
        self.data_lancamento = data_lancamento

"""
# Bloco de teste
from datetime import date

nota1 = Notas(
    id=1,
    id_disciplina=2,
    aluno_id=1,
    turma_id=3,
    avaliacao=10,
    nota=9.5,
    data_lancamento=date.today()
)

print("ID:", nota1.id)
print("Disciplina:", nota1.id_disciplina)
print("Aluno:", nota1.aluno_id)
print("Turma:", nota1.turma_id)
print("Avaliação:", nota1.avaliacao)
print("Nota:", nota1.nota)
print("Data de Lançamento:", nota1.data_lancamento)
"""
