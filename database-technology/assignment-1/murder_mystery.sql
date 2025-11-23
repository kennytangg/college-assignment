SELECT * 
FROM crime_scene_report
WHERE type = "murder"
    AND date = 20180115
    AND city = "SQL City";

-- Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". 
-- The second witness, named Annabel, lives somewhere on "Franklin Ave".

SELECT p.*, i.transcript
FROM person p
JOIN interview i ON p.id = i.person_id
WHERE
    (p.address_street_name = 'Northwestern Dr' AND
     p.address_number = (
       SELECT MAX(address_number)
       FROM person
       WHERE address_street_name = 'Northwestern Dr'
     ))
  OR
    (p.name LIKE '%Annabel%' AND p.address_street_name = 'Franklin Ave');

-- 14887	Morty Schapiro	118009	4919	Northwestern Dr	111564949

-- Transcript from the Interview
-- I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. 
-- The membership number on the bag started with "48Z". Only gold members have those bags. 
-- The man got into a car with a plate that included "H42W".

-- 16371	Annabel Miller	490173	103	Franklin Ave	318771143

-- Transcript from the Interview
-- I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.

SELECT m.*, p.name, d.plate_number
FROM get_fit_now_member m
    JOIN person p ON m.person_id = p.id
    JOIN drivers_license d ON p.license_id = d.id
WHERE m.membership_status = 'gold'
    AND m.id LIKE '48Z%'
    AND d.plate_number LIKE '%H42W%';

-- 48Z55	67318	Jeremy Bowers	20160101	gold	Jeremy Bowers	0H42W2

-- MURDER 1 DONE ( Jeremy Bowers )-- 

SELECT * 
FROM interview
WHERE person_id = 67318;

-- I was hired by a woman with a lot of money. I don't know her name but 
-- I know she's around 5'5" (65") or 5'7" (67").
-- She has red hair and she drives a Tesla Model S. 
-- I know that she attended the SQL Symphony Concert 3 times in December 2017. 

SELECT p.*, d.car_make, d.car_model, d.hair_color, d.gender, f.event_name, f.date
FROM drivers_license d
    JOIN person p ON p.license_id = d.id
    JOIN facebook_event_checkin f ON f.person_id = p.id
WHERE d.car_make = 'Tesla'
    AND d.car_model = 'Model S'
    AND d.gender = 'female'
    AND d.hair_color = 'red'
    AND f.event_name = 'SQL Symphony Concert'
    AND f.date BETWEEN '20171201' AND '20171231'
GROUP BY p.id
HAVING COUNT(*) = 3;

-- 99716	Miranda Priestly	202298	1883	Golden Ave	987756388	Tesla	Model S	red	female	SQL Symphony Concert	20171229

-- MURDER 2 DONE ( Miranda Priestly ) -- 