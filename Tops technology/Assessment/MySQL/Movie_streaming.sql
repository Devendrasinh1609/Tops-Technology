CREATE DATABASE movie_streaming;
USE movie_streaming;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

INSERT INTO users (name, city) VALUES
('Devang Patel', 'Ahmedabad'),
('Hetal Joshi', 'Baroda'),
('Rajesh Rana', 'Gandhinagar'),
('Karan Vaghela', 'Ahmedabad'),
('Mihir Mehta', 'Baroda'),
('Priya Shah', 'Gandhinagar'),
('Nirav Parmar', 'Ahmedabad'),
('Riya Trivedi', 'Baroda'),
('Harsh Patel', 'Gandhinagar'),
('Jatin Solanki', 'Ahmedabad');

CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    genre VARCHAR(50),
    release_year INT
);
INSERT INTO movies (title, genre, release_year) VALUES
('3 Idiots', 'Comedy', 2009),
('Bahubali 2', 'Action', 2017),
('KGF 2', 'Action', 2022),
('Dangal', 'Sports', 2016),
('Chhello Show (Last Film Show)', 'Drama', 2021),
('RRR', 'Action', 2022),
('Golmaal', 'Comedy', 2006),
('Pathaan', 'Action', 2023),
('Sanju', 'Drama', 2018),
('Simmba', 'Action', 2018);

CREATE TABLE ratings (
	user_id INT,
    movie_id INT,
    rating INT CHECK(rating BETWEEN 1 AND 5),
    rating_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE
);

INSERT INTO ratings (user_id, movie_id, rating, rating_date) VALUES
(1, 1, 5, '2023-01-01'),
(2, 2, 4, '2023-01-05'),
(3, 3, 5, '2023-01-10'),
(4, 4, 3, '2023-01-12'),
(5, 5, 5, '2023-01-15'),
(6, 6, 4, '2023-01-18'),
(7, 7, 5, '2023-01-20'),
(8, 8, 5, '2023-01-22'),
(9, 9, 4, '2023-01-25'),
(10, 10, 3, '2023-01-28');

CREATE TABLE watch_history (
    user_id INT,
    movie_id INT,
    watch_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE
);

INSERT INTO watch_history (user_id, movie_id, watch_date) VALUES
(1, 1, '2023-02-01'),
(2, 2, '2023-02-02'),
(3, 3, '2023-02-03'),
(4, 4, '2023-02-04'),
(5, 1, '2023-02-05'),
(6, 2, '2023-02-06'),
(7, 3, '2023-02-07'),
(8, 4, '2023-02-08'),
(9, 5, '2023-02-09'),
(10, 6, '2023-02-10');


-- Assessment
-- 1) Top 3 most-watched genres per country
SELECT u.city, m.genre, COUNT(*) AS total_watched
FROM watch_history w
JOIN users u ON w.user_id = u.user_id
JOIN movies m ON w.movie_id = m.movie_id
GROUP BY u.city, m.genre
ORDER BY u.city, total_watched DESC;

-- 2) Identify users who rated more than 20 movies.
SELECT user_id, COUNT(*) AS total_ratings
FROM ratings
GROUP BY user_id
HAVING total_ratings > 20;

-- 3) Find movies released after 2020 that have never been watched.
SELECT movie_id, title
FROM movies
WHERE release_year > 2020
AND movie_id NOT IN (SELECT movie_id FROM watch_history);

-- 4) Compute the average rating per genre.
SELECT m.genre, AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON r.movie_id = m.movie_id
GROUP BY m.genre;

-- 5) List users who gave 5-star ratings to all movies in a genre
SELECT u.user_id, u.name, m.genre
FROM users u
INNER JOIN ratings r ON u.user_id = r.user_id
INNER JOIN movies m ON r.movie_id = m.movie_id
GROUP BY u.user_id, m.genre
HAVING MIN(r.rating) = 5;

-- 6) Identify movies watched by users from at least 5 different cities
SELECT m.movie_id, m.title, COUNT(DISTINCT u.city) AS city_count
FROM watch_history w
JOIN users u ON w.user_id = u.user_id
JOIN movies m ON w.movie_id = m.movie_id
GROUP BY m.movie_id
HAVING COUNT(DISTINCT u.city) >= 5;

-- 7) Find the average number of movies watched per user per month.
SELECT count(*) / count(distinct user_id) FROM watch_history;
select *from watch_history;

-- 8) List users who watched the same movie more than once.
SELECT user_id, movie_id, COUNT(*) AS watch_count
FROM watch_history
GROUP BY user_id, movie_id
HAVING watch_count > 1;

-- 9) Count how many movies have ratings but were never watched.
SELECT DISTINCT r.movie_id
FROM ratings r
WHERE r.movie_id NOT IN (SELECT movie_id FROM watch_history);

-- 10) Identify the genre with the highest average 5-star rating count.
SELECT m.genre, COUNT(*) AS five_star_count
FROM ratings r
JOIN movies m ON r.movie_id = m.movie_id
WHERE r.rating = 5
GROUP BY m.genre
ORDER BY five_star_count DESC
LIMIT 1;
