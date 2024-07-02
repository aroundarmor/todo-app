from flask import Flask, request, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

# PostgreSQL connection
pg_conn = psycopg2.connect(
    dbname=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT')
)

# Redis connection
redis_client = redis.StrictRedis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    password=os.getenv('REDIS_PASSWORD'),
    decode_responses=True
)


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        task = request.json['task']
        with pg_conn.cursor() as cursor:
            cursor.execute("INSERT INTO tasks (description) VALUES (%s) RETURNING id", (task,))
            task_id = cursor.fetchone()[0]
            pg_conn.commit()
            redis_client.set(f"task:{task_id}", task)
            return jsonify({"id": task_id, "task": task}), 201

    elif request.method == 'GET':
        with pg_conn.cursor() as cursor:
            cursor.execute("SELECT id, description FROM tasks")
            tasks = cursor.fetchall()
            return jsonify([{"id": task[0], "task": task[1]} for task in tasks])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)