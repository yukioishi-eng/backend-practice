SELECT 
    user_name,
    age, 
    job_id
FROM
    users_table
WHERE
    AGE >= 20
    AND job_id = 1;
    
--WHEREに入る条件はほかにもa is NULLやa BETWEEN 1 AND 4（aの値が1~4）、a IN (1, 2)(aが1か2)などがある