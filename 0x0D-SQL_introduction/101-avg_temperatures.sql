-- displays the average temperature
SELECT `city`, AVG(`value`) AS `temp_val`
FROM `temperatures`
GROUP BY `city`
ORDER BY `temp_val` DESC;
