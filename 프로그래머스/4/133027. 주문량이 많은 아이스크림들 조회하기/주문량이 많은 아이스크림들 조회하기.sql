-- #2

SELECT flavor
    FROM july AS j LEFT OUTER JOIN first_half AS h USING(flavor)
    GROUP BY h.flavor
    ORDER BY AVG(h.total_order) + SUM(j.total_order) DESC 
    LIMIT 3;
