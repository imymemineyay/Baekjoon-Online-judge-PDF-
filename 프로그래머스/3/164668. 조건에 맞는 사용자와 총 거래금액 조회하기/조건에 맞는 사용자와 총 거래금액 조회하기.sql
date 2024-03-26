-- #3

SELECT user_id, nickname, SUM(price) AS total_sales
FROM used_goods_board AS b JOIN used_goods_user AS u ON b.writer_id = u.user_id
WHERE status = 'DONE'
GROUP BY user_id
HAVING total_sales >= 700000
ORDER BY 3;