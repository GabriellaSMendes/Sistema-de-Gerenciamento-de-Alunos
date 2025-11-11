from backend.services.turma_service import TurmaService

serv = TurmaService()

print("\n🧩 TESTE 1 — Criar turma válida")
serv.criarTurma(
    id_disciplina=2,
    id_professor=1,
    sigla_curso="ADS",
    ano=2025,
    semestre=2
)

print("\n🧩 TESTE 2 — Criar turma com campo obrigatório faltando (deve dar erro)")
serv.criarTurma(
    id_disciplina="",
    id_professor=1,
    sigla_curso="ADS",
    ano=2025,
    semestre=2
)

print("\n🧩 TESTE 3 — Criar turma de outro curso (pra ver se muda o código)")
serv.criarTurma(
    id_disciplina=3,
    id_professor=1,
    sigla_curso="MAT",
    ano=2024,
    semestre=1
)
