select * from posts;
select * from user_languages;
SELECT * FROM posts JOIN users ON users.id = posts.user_id;
SELECT * FROM users;
SELECT * FROM user_languages JOIN users ON users.id = user_languages.user_id;
select * from messages;
SELECT * FROM messages 
JOIN users ON sender_id = users.id
WHERE receiver_id = 1;

