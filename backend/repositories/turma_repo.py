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
            "INSERT INTO turma (id_disciplina, cod_turma, id_professor, ano, semestre) VALUES (%s, %s, %s, %s, %s)",
            (turma.id_disciplina, turma.cod_turma, turma.id_professor, turma.ano, turma.semestre)
        )
        
        conexao.commit()
        cursor.close()
        conexao.close()
        
        
    #deletar turma
    def deletarTurma(self, id):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "DELETE FROM turma WHERE id = %s",
            (id,)
        )
        
        conexao.commit()
        cursor.close()
        conexao.close()