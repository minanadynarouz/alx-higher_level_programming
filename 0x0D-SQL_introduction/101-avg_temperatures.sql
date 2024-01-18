-- displays the average temperature
SELECT city, AVG(`value`) as tmp_val
FROM temperature
GROUP BY city
ORDER BY tmp_val DESC;
