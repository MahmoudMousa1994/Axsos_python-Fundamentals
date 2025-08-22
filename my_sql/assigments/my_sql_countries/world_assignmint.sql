SELECT countries.name AS The_Countries, languages.language AS Spoken_language, languages.percentage 
FROM	countries
JOIN languages ON countries.id = languages.country_id
WHERE language = "Slovene"
ORDER BY languages.percentage DESC;

SELECT countries.name AS The_countries, COUNT(cities.id) AS Number_of_citis
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY Number_of_citis DESC;

SELECT countries.name AS The_countrie, cities.name AS The_city, cities.population
FROM countries 
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY cities.population DESC;

SELECT countries.name AS the_countrie, languages.language AS popular_language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89.0
ORDER BY languages.percentage DESC;

SELECT countries.name AS the_countrie, countries.surface_area AS Area , countries.population AS the_population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 10000;

SELECT countries.name AS the_countrie,countries.government_form, countries.capital AS The_capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy >75 ;

SELECT countries.name , cities.district, cities.population
FROM countries
JOIN cities on countries.id = cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;

SELECT countries.region, COUNT(countries.id) AS REGIN_COUNTRIE_COUNT
FROM countries
GROUP BY countries.region
ORDER BY  REGIN_COUNTRIE_COUNT DESC;

