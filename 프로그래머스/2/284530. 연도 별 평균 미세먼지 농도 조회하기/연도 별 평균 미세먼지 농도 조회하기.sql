SELECT year(ym) YEAR, ROUND(avg(pm_val1),2) PM10, ROUND(avg(pm_val2),2) AS 'PM2.5'
    FROM air_pollution
    WHERE location2 = '수원'
    GROUP BY year(ym)
    ORDER BY YEAR ;