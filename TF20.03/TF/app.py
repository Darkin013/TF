from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configuração da conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )
    return conn

# Listar os alunos cadastrados
@app.route('/alunos', methods=['GET'])
def get_alunos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM alunos;')
    alunos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(alunos)

# Cadastrar novos alunos
@app.route('/alunos', methods=['POST'])
def add_aluno():
    new_aluno = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    ''', (new_aluno['aluno_id'], new_aluno['nome'], new_aluno['endereco'], new_aluno['cidade'], new_aluno['estado'], new_aluno['cep'], new_aluno['pais'], new_aluno['telefone']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_aluno), 201

# Alterar dados de alunos cadastrados
@app.route('/alunos/<aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    updated_aluno = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        UPDATE alunos
        SET nome = %s, endereco = %s, cidade = %s, estado = %s, cep = %s, pais = %s, telefone = %s
        WHERE aluno_id = %s;
    ''', (updated_aluno['nome'], updated_aluno['endereco'], updated_aluno['cidade'], updated_aluno['estado'], updated_aluno['cep'], updated_aluno['pais'], updated_aluno['telefone'], aluno_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(updated_aluno)

# Excluir alunos
@app.route('/alunos/<aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM alunos WHERE aluno_id = %s;', (aluno_id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)