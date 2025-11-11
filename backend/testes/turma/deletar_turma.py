from backend.models.turma import Turma
from backend.repositories.turma_repo import TurmaRepository

repo = TurmaRepository()

repo.deletarTurma(2)

print("Turma deletada")