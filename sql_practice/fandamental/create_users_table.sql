CREATE TABLE users_table(
    user_id INT PRIMARY KEY,
    --PRIMARY KEYは主キー
    user_name STRING,
    age INT,
    job_id INT UNIQUE
    --UNIQUEは重複しないカラム(主キーにも言える)
);
