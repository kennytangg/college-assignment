SELECT * 
FROM crime_scene_report
WHERE type = "murder"
    AND date = 20180115
    AND city = "SQL City";

-- Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". 
-- The second witness, named Annabel, lives somewhere on "Franklin Ave".

SELECT * 
FROM person
WHERE address_street_name = "Northwestern Dr"
ORDER BY address_number;

-- 14887 (id)
-- Morty Schapiro (name) 
-- 118009 (license_id)
-- 4919 (address_number)
-- Northwestern Dr (address_street_name)
-- 111564949 (ssn)

SELECT * 
FROM interview
WHERE person_id = "14887";

-- Transcript from the Interview
-- I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. 
-- The membership number on the bag started with "48Z". Only gold members have those bags. 
-- The man got into a car with a plate that included "H42W".

SELECT * 
FROM get_fit_now_member
WHERE membership_status = "gold" 
	AND id LIKE '48Z%';

-- 48Z7A	28819	Joe Germuska	20160305	gold
-- 48Z55	67318	Jeremy Bowers	20160101	gold

SELECT * 
FROM drivers_license
WHERE plate_number like '%H42W%';

-- 183779	21	65	blue	blonde	female	H42W0X	Toyota	Prius
-- 423327	30	70	brown	brown	male	0H42W2	Chevrolet	Spark LS
-- 664760	21	71	black	black	male	4H42WR	Nissan	Altima

SELECT * 
FROM person
WHERE id = 28819 or id = 67318;

-- MURDER 1 DONE ( Jeremy Bowers )-- 

SELECT * 
FROM interview
WHERE person_id = 67318;

-- I was hired by a woman with a lot of money. I don't know her name but 
-- I know she's around 5'5" (65") or 5'7" (67").
-- She has red hair and she drives a Tesla Model S. 
-- I know that she attended the SQL Symphony Concert 3 times in December 2017. 

SELECT * 
FROM drivers_license
where car_make = "Tesla"
	AND car_model = "Model S"
	AND gender = "female"
	AND hair_color = "red";

-- 202298	68	66	green	red	female	500123	Tesla	Model S
-- 291182	65	66	blue	red	female	08CM64	Tesla	Model S
-- 918773	48	65	black	red	female	917UU3	Tesla	Model S


SELECT * 
FROM person
WHERE license_id = 918773 
    OR license_id = 291182
    OR license_id = 202298;

-- 78881	Red Korb	918773	107	Camerata Dr	961388910
-- 90700	Regina George	291182	332	Maple Ave	337169072
-- 99716	Miranda Priestly	202298	1883	Golden Ave	987756388 

SELECT * 
FROM income
WHERE ssn = 961388910 
    OR ssn = 337169072
    OR ssn = 987756388;

-- MURDER 2 DONE ( Miranda Priestly ) -- 

SELECT * 
FROM person
WHERE address_street_name = "Franklin Ave"
	AND name LIKE "%Annabel%";

-- 16371	Annabel Miller	490173	103	Franklin Ave	318771143

SELECT * 
FROM interview
WHERE person_id = 16371;

-- I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.


