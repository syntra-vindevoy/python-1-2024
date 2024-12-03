from code_snippets.flask_psycopg import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection parameters
db_params = {
    'dbname': 'test',
    'user': 'postgres',
    'password': os.getenv('DB_PASSWORD'),
    # bash: export DB_PASSWORD='your_password'
    'host': '127.0.0.1',
    'port': '5432'
}

# Initialize PostgreSQL database
def init_db():
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
    print("Database initialized")

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            return jsonify(users)

# Route to get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
            user = cursor.fetchone()
            return jsonify(user)

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id', (new_user['name'], new_user['email']))
            user_id = cursor.fetchone()[0]
            conn.commit()
            return jsonify({'id': user_id}), 201

# Route to update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.get_json()
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cursor:
            cursor.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (updated_user['name'], updated_user['email'], user_id))
            conn.commit()
            return jsonify({'message': 'User updated'})

# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
            conn.commit()
            return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)