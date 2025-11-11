from database import conectar

class NotasRepository:
     
    #funçao pra criar conexao com DB
    def abrirConexao(self):
        conexao = conectar()
        cursor = conexao. cursor()
        return conexao, cursor
    
    #buscar nota por ID de aluno
    def buscarNota(self, id_aluno):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "SELECT * FROM notas WHERE id_aluno = %s",
            (id_aluno,)
        )
        
        resultado = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        return resultado
        
    
    #lançar notas
    def lancarNotas(self, notas):
        conexao, cursor = self.abrirConexao()
        
        cursor.execute(
            "INSERT INTO notas (id_disciplina, id_aluno, id_turma, avaliacao, nota, data_lancamento) VALUES (%s, %s, %s, %s, %s, %s)",
            (notas.id_disciplina, notas.aluno_id, notas.turma_id, notas.avaliacao, notas.nota, notas.data_lancamento)
        )

        
        conexao.commit()
        cursor.close()
        conexao.close()
        
    