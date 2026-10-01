CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100),
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users VALUES (1, 'Alex', 'alex@email.com', 20);
INSERT INTO users VALUES (2, 'Ben', 'ben@email.com', 21);
INSERT INTO users VALUES (3, 'Chris', 'chris@email.com', 19);
INSERT INTO users VALUES (4, 'David', 'david@email.com', 22);
INSERT INTO users VALUES (5, 'Emma', 'emma@email.com', 20);
INSERT INTO users VALUES (6, 'Faith', 'faith@email.com', 21);
INSERT INTO users VALUES (7, 'Grace', 'grace@email.com', 19);
INSERT INTO users VALUES (8, 'Henry', 'henry@email.com', 23);
INSERT INTO users VALUES (9, 'Isaac', 'isaac@email.com', 20);
INSERT INTO users VALUES (10, 'Jack', 'jack@email.com', 22);

INSERT INTO posts VALUES (1, 1, 'First Post', 'My first post');
INSERT INTO posts VALUES (2, 2, 'Hello', 'Hello everyone');
INSERT INTO posts VALUES (3, 3, 'School', 'Good day at school');
INSERT INTO posts VALUES (4, 4, 'SQL', 'Learning SQL');
INSERT INTO posts VALUES (5, 5, 'Data', 'Working with data');
INSERT INTO posts VALUES (6, 6, 'Python', 'Learning Python');
INSERT INTO posts VALUES (7, 7, 'College', 'College is going well');
INSERT INTO posts VALUES (8, 8, 'Weekend', 'Ready for the weekend');
INSERT INTO posts VALUES (9, 9, 'Study', 'Time to study');
INSERT INTO posts VALUES (10, 10, 'Last Post', 'My last post');
