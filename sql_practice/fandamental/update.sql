--WHEREの条件に当てはまるレコードの値を変更する
UPDATE
    users_table
SET
    age = 25
WHERE
    job_id = 1
;