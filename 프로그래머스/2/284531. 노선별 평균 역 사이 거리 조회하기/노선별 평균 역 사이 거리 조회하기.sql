SELECT route, 
       concat(round(sum(D_BETWEEN_DIST),1),'km') total_distance, 
       concat(round(avg(D_BETWEEN_DIST),2),'km') average_distance
    FROM subway_distance
    GROUP BY route
    ORDER BY round(sum(D_BETWEEN_DIST),2) DESC;