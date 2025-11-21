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
            "INSERT INTO turma (cod_turma, id_disciplina, id_professor, ano, semestre) VALUES (%s, %s, %s, %s, %s)",
            (turma.cod_turma, turma.id_disciplina, turma.id_professor, turma.ano, turma.semestre)
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