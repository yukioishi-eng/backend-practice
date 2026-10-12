SELECT 
    --結合するキーを表示させるときはどちらのキーなのか示す
    user.job_id,
    user_name,
    job_name
FROM
    --実務ではデータベースが複数あることで、テーブル名を書くときにパスの指定も必要になるが、今回は1つのデータベースを用いるので、省略する
    users_table AS user
INNER JOIN
    --INNER JOIN（内部都合）とは結合に使うキーが両方一致するレコードだけで結合すること
    jobs_table AS job
    --ASを使うことで、名前をこのコード内で付けなおせる
ON
    user.job_id = job.job_id
