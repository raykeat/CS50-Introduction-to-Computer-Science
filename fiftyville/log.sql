-- Keep a log of any SQL queries you execute as you solve the mystery.

--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
--Interviews were conducted today with three witnesses who were present at the time
--each of their interview transcripts mentions the bakery.
--Littering took place at 16:36. No known witnesses.

SELECT description FROM crime_scene_reports WHERE month=7 AND day=28 AND year=2021 AND street='Humphrey Street';

--Jose,Eugene, Barbara, ruth, raymond, lily were interviewed
SELECT name FROM interviews WHERE month=7 AND day=28 AND year=2021;

--Sometime within ten minutes of the theft, I saw the thief get into a car in
--the bakery parking lot and drive away. If you have security footage from the
--bakery parking lot, you might want to look for cars that left the parking lot
--in that time frame.I don't know the thief's name, but it was someone I recognized.
--Earlier this morning, before I arrived at Emma's bakery, I was walking by
--the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 | As the thief was leaving the bakery, they called someone who talked to them
--In the call, I heard the thief say that they were planning
--to take the earliest flight out of Fiftyville tomorrow. The thief then asked the
--person on the other end of the phone to purchase the flight ticket. |
--Our neighboring courthouse has a very annoying rooster that crows loudly at
--6am every day. My sons Robert and Patrick took the rooster to a city far, far away,
--so it may never bother us again. My sons have successfully arrived in Paris.

SELECT transcript FROM interviews WHERE month=7 AND day=28 AND year=2021;

--possible account numbers of thief
--28500762       |
--28296815       |
--76054385       |
--49610011       |
--16153065       |
--25506511       |
--81061156       |
--26013199
SELECT account_number FROM atm_transactions WHERE month=7 AND day=28 AND year=2021
AND atm_location ='Leggett Street' AND transaction_type='withdraw';

--possible person id of thief
--686048    |
--514354    |
--458378    |
--395717    |
--396669    |
--467400    |
--449774    |
--438727
SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE month=7 AND day=28 AND year=2021
AND atm_location ='Leggett Street' AND transaction_type='withdraw');


+---------+----------------+-----------------+---------------+
|  name   |  phone_number  | passport_number | license_plate |
+---------+----------------+-----------------+---------------+
| Kenny   | (826) 555-1652 | 9878712108      | 30G67EN       |
| Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
| Benista | (338) 555-6650 | 9586786673      | 8X428L0       |
| Taylor  | (286) 555-6063 | 1988161715      | 1106N58       |
| Brooke  | (122) 555-4581 | 4408372428      | QX4YZN3       |
| Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
| Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
| Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
+---------+----------------+-----------------+---------------+
--POSSIBLE SUSPECTS
SELECT name,phone_number,passport_number,license_plate FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE month=7 AND day=28 AND year=2021
AND atm_location ='Leggett Street' AND transaction_type='withdraw'));

--POSSIBLE SUSPECTS BASED ON PHONE CALL - BRUCE, DIANA, BROOKE,KENNY,BENISTA,TAYLOR
SELECT caller FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE month=7 AND day=28 AND year=2021
AND atm_location ='Leggett Street' AND transaction_type='withdraw')));

--POSSIBLE ACCOMPLICE BASED ON PHONE CALL - robin
SELECT name FROM people
WHERE phone_number=(SELECT receiver FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND caller IN (SELECT caller FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE month=7 AND day=28 AND year=2021
AND atm_location ='Leggett Street' AND transaction_type='withdraw')))));

--possible suspects based on cars leaving at 1015 to 1025 and also match phone call suspect
--kenny,brooke,diana,bruce
SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE minute IN(SELECT minute FROM bakery_security_logs WHERE year=2021 AND month=7 AND day=28 AND hour=10 AND activity='exit' LIMIT 8));

--flight id of flight that left earliest the following morning is 36
SELECT id FROM flights WHERE origin_airport_id=8 AND year=2021 AND month=7 AND day=29 AND hour=8;

--possible suspects - kenny, bruce
--possible accomplice - robin
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id=36);

--New York City
SELECT city FROM airports WHERE id=(SELECT destination_airport_id FROM flights WHERE id=36);




