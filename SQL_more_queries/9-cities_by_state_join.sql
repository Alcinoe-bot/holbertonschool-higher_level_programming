-- cities by states
SELECT cities.id, cities.name, states.name
FROM cities c
JOIN states s ON cities.states_id = states.id
ORDER BY cities.id ASC;
