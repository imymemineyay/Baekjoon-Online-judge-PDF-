-- # 3

-- 서울에 위치한 식당의 id, name, type, favorites, address, ROUND(AVG(review),2)

SELECT rest_id, rest_name, food_type, favorites, address, ROUND(AVG(review_score),2) AS score
FROM rest_info JOIN rest_review USING(rest_id)
WHERE address like '서울%'
GROUP BY rest_id
ORDER BY 6 DESC, 4 DESC;