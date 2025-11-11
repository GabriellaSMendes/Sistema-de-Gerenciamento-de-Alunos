from database import conectar

class TurmaRepository:
    
    #função pra criar conexao com DB
    def abrirConexao(self):
        conexao = conectar()
        cursor = conexao.cursor()
        return conexao, cursor
    
    #criar turma
    def criarTurma(self, turma):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "INSERT INTO turma (id_disciplina, cod_turma, id_professor, sigla_curso, ano, semestre) VALUES (%s, %s, %s, %s, %s, %s)",
            (turma.id_disciplina, turma.cod_turma, turma.id_professor, turma.sigla_curso, turma.ano, turma.semestre)
        )
        
        conexao.commit()
        cursor.close()
        conexao.close()
        
        
    #listar turma
    def listarTurma(self):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "SELECT * FROM turma",
        )
        
        resultados = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return resultados