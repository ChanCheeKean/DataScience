
--Reward the 5 longest users
SELECT * FROM users 
ORDER BY created_at 
LIMIT 5;

--Campaign on most popular registration date
SELECT DAYNAME(created_at) AS day, COUNT(*)
FROM users 
GROUP BY day ORDER BY day;

--Identify inactive member (those who never posted photo)
SELECT username, image_url 
FROM users LEFT JOIN photos ON  user_id=users.id
WHERE photos.id IS NULL;

--Most likes photo , find the winners and photos
SELECT photos.id, photos.image_url, COUNT(*) AS total, username 
FROM photos 
INNER JOIN likes ON likes.photo_id=photos.id
INNER JOIN users ON photos.user_id=users.id
GROUP BY photos.id
ORDER BY total DESC LIMIT 5;

--See who like the photo
SELECT photos.id, photos.image_url, username, likes.user_id 
FROM photos 
INNER JOIN likes ON likes.photo_id=photos.id
INNER JOIN users ON photos.user_id=users.id
WHERE photos.id=20;

--How many times the user post in average
--Amount of photos divided by amount of users

SELECT  (   (SELECT COUNT(*) from photos)/
            (SELECT COUNT(*) from users)
        ) AS average;
        
--Most common hashtag
SELECT photo_tags.tag_id, COUNT(*) AS TOTAL
FROM photo_tags
GROUP BY tag_id
ORDER BY total DESC LIMIT 5;

--OR 

SELECT tags.id, tags.tag_name, COUNT(*) AS total
FROM photo_tags
INNER JOIN tags ON tags.id=photo_tags.tag_id
GROUP BY tags.id
ORDER BY total DESC LIMIT 5;

--Find users that like every photo (bot)
SELECT COUNT(*) FROM photos;

SELECT username, user_id, COUNT(*) AS total_like
FROM users  INNER JOIN likes ON likes.user_id=users.id
GROUP BY users.id
HAVING total_like=(SELECT COUNT(*) FROM photos);

--Do a trigger by not letting people to follow themselve, refer to tutorial 9
DELIMITER $$
CREATE TRIGGER prevent_self_follow
     BEFORE INSERT ON follows FOR EACH ROW
     BEGIN
          IF NEW.follower_id = NEW.followee_id
          THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'You cannot follow yourself!';
          END IF;
     END;
$$ DELIMITER ;

--not able to follow
INSERT INTO follows(follower_id,followee_id)
VALUES (8,8);
SHOW TRIGGERS;
DROP TRIGGER prevent_self_follow;



--Keep track/Logging when somebody unfollow
--Create unfollow table
CREATE TABLE unfollows (
    follower_id INTEGER NOT NULL,
    followee_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(follower_id) REFERENCES users(id),
    FOREIGN KEY(followee_id) REFERENCES users(id),
    PRIMARY KEY(follower_id, followee_id));

--Once delete from follows table, auto recorded in unfollow table
--Set can be replaced by insert into unfollows(follower_id, followee_id)value(old.follower_id, old.followee_id)

DELIMITER $$
CREATE TRIGGER record_unfollow
     AFTER DELETE ON follows FOR EACH ROW
     BEGIN
          INSERT INTO unfollows
          SET
          follower_id = OLD.follower_id,
          followee_id = OLD.followee_id;
     END;
$$ DELIMITER;

--MUST USE AND not coma after WHERE
DELETE FROM follows WHERE follower_id=3 AND followee_id=1;
SELECT * FROM unfollows;









