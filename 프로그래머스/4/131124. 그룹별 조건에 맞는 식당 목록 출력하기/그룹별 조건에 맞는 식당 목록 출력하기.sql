-- # 3

SELECT member_name, review_text, 
    DATE_FORMAT(review_date, '%Y-%m-%d') AS review_date
FROM member_profile JOIN rest_review USING(member_id)
WHERE member_id = (SELECT member_id 
                  FROM rest_review
                  GROUP BY member_id
                  ORDER BY COUNT(review_id) DESC
                  LIMIT 1)
GROUP BY member_id,review_text
ORDER BY review_date, review_text
; 