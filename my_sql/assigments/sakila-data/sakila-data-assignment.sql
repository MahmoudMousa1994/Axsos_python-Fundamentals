SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city_id
FROM customer
JOIN address on address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
WHERE city.city_id = 312;

SELECT film.film_id,title , description , release_year , rating , special_features, category.name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = "Comedy";

SELECT actor.actor_id ,first_name AS actor_name , film.title,description,release_year
FROM  film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;


SELECT store.store_id,city.city_id, customer.first_name,customer.last_name ,customer.email, address
FROM customer
JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
JOIN store ON store.store_id = customer.store_id
WHERE store.store_id= 1 and city.city_id  in ( 1,42,312,459);


SELECT film.title , film.description,film.release_year , film.rating , film.special_features
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 15 and  rating = "G" and special_features LIKE "%Behind the Scenes%";

SELECT film.film_id, actor.actor_id, concat(actor.first_name," ",actor.last_name) AS actor_name , actor.first_name
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

SELECT film.film_id,title , description , release_year , rating , special_features, category.name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = "Drama" and rental_rate = 2.99;

SELECT film.film_id,title , description , release_year , rating , special_features, category.name ,
concat(" ",actor.first_name," ",actor.last_name) AS actor_name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE category.name = "Action" and actor.first_name = "SANDRA" and actor.last_name = "KILMER"
