--view para o relatorio de notas


CREATE OR REPLACE VIEW vw_relatorio_alunos AS
SELECT
    u.nome AS nome_aluno,
    u.matricula AS matricula_aluno,
    t.semestre AS semestre_atual,
    d.nome AS disciplina,
    r.media AS media,
    r.situacao AS situacao
FROM notas n
JOIN usuario u ON n.id_aluno = u.id
JOIN disciplina d ON n.id_disciplina = d.id
JOIN turma t ON n.id_turma = t.id
LEFT JOIN relatorio r ON r.id_aluno = u.id
ORDER BY
    u.nome, d.nome;
