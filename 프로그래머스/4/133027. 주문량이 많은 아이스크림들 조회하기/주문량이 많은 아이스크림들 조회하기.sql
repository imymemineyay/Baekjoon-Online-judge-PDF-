WITH july_tot AS (
    SELECT flavor, SUM(total_order) AS total_order
    FROM july
    GROUP BY flavor
)

SELECT f.flavor
FROM first_half AS f
JOIN july_tot AS j ON f.flavor = j.flavor
GROUP BY f.flavor
ORDER BY SUM(f.total_order + j.total_order) DESC
LIMIT 3;