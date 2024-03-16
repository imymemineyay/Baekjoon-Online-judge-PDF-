-- #2 
SELECT user_id, nickname, SUM(price) AS total_sales
FROM used_goods_board JOIN used_goods_user ON writer_id = user_id
WHERE status = 'done'
GROUP BY user_id
HAVING SUM(price) >= 700000
ORDER BY 3;
