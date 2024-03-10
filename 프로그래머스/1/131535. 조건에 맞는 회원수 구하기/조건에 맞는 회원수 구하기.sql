-- #2 
SELECT count(user_id) AS users
    FROM user_info
    WHERE YEAR(joined) = 2021 AND age BETWEEN 10 AND 29;