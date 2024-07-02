# todo-app
this one deploys to-do app

#### Configuring PostgreSQL and Redis on AWS

Assuming you've already set up PostgreSQL and Redis on AWS, you’ll need to update the docker-compose.yml file with the endpoint details for these services:



## For PostgreSQL:

your_postgres_host should be the endpoint of your RDS instance.

your_db_name, your_db_user, and your_db_password should be the credentials of your database.



## For Redis:

your_redis_host should be the endpoint of your ElastiCache instance.

5. Initialize Your PostgreSQL Database

Before you start using the app, you'll need to create the tasks table in your PostgreSQL database:


##### sql

```
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL
);
```
You can run these commands via any PostgreSQL client or psql utility:


##### bash

```
psql -h your_postgres_host -U your_db_user -d your_db_name -p 5432
```

##### After connecting to the DB, run:
```
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL
);
```

## Running the Application

With Docker installed, navigate to the root of your project directory and run:


```docker-compose up --build```

## Testing Your Application

#### Add a new task:
```curl -X POST http://localhost:80/tasks -H "Content-Type: application/json" -d '{"task": "Buy groceries"}'```

or 

#### Get all tasks:
```curl http://localhost:80/tasks```
