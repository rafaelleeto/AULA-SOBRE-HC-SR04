import mysql.connector

class Banco:
    def conectar(self):
        return mysql.connector.connect(
            host = "paparella.com.br",
            user = "paparell_aluno_1",
            password = "@Senai2025",
            database = "paparell_python"
        )
   
    
    def inserir_ou_atualizar_estado(self,aluno,ultrassom,distancia):
        
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(''' SELECT id FROM ultrassom WHERE aluno = %s''',(aluno,))
        id = cursor.fetchone()
        if id:
            cursor.execute(''' UPDATE ultrassom  SET distancia = %s WHERE id = %s''',(distancia,id[0]))
            print(f"Estado do LED do Aluno: {aluno }, atualizado com sucesso")
        else:    
            cursor.execute(''' INSERT INTO ultrassom (aluno,ultrassom,distancia) VALUES (%s,%s,%s)''',(aluno,ultrassom,distancia))
            print(f"Estado do LED do Aluno: {aluno }, atualizado com sucesso")
        conexao.commit()
        cursor.close()
        conexao.close()
    
