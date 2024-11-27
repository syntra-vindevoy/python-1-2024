DROP TABLE IF EXISTS todos;

CREATE TYPE status_enum AS ENUM ('NEW', 'IDLE', 'DOING', 'DONE');

CREATE TABLE todos
(
    id          SERIAL PRIMARY KEY,
    title       VARCHAR(100),
    description TEXT,
    due_date    TIMESTAMP,
    priority    INT,
    status      status_enum DEFAULT 'NEW'
);

-- Optionally, you can ensure that the increment step is set to 1 explicitly.
ALTER SEQUENCE todos_id_seq INCREMENT BY 1;