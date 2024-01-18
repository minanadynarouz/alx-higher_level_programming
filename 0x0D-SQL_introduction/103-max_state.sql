-- Select max temp in table
SELECT state, MAX(state) as max_val
FROM temperatures
GROUP BY state
ORDER BY max_val DESC;
