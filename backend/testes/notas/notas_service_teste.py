from backend.services.notas_service import NotasService
from datetime import date

serv = NotasService()

print("\n🧩 TESTE 1 — Lançar nota válida para um aluno")
serv.lancarNotas(
    id_disciplina=2,
    aluno_id=1,        
    turma_id=1,
    avaliacao="P2",
    nota=6.0,
    data_lancamento=date.today()
)

print("\n🧩 TESTE 2 — Tentar lançar nota com campo obrigatório faltando (deve dar erro)")
serv.lancarNotas(
    id_disciplina="",
    aluno_id=1,
    turma_id=1,
    avaliacao="P2",
    nota=7.5,
    data_lancamento=date.today()
)

print("\n🧩 TESTE 3 — Tentar lançar nota para usuário que não é aluno (deve bloquear)")
serv.lancarNotas(
    id_disciplina=2,
    aluno_id=4,        
    turma_id=3,
    avaliacao="P3",
    nota=8.5,
    data_lancamento=date.today()
)
