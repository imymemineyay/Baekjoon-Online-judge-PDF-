-- #2

SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, i.tel, 
        ROUND(AVERAGE(r.review_score),2) AS score
    FROM rest_info AS i JOIN rest_review AS r USING (rest_id)
    GROUP BY i.rest_id
    HAVING i.address like '서울%'
    ORDER BY score DESC , favorites DESC; 