CREATE TABLE Metro (
wijk VARCHAR(255),
wijkoppervlakte_km2 FLOAT,
aantal stations INT);

INSERT INTO Metro (wijk, wijkoppervlakte_km2, aantal stations)
VALUES ('Centrum', 4.81, 9),
('Delfshaven', 5.8, 5),
('Overschie', 15.80, NULL),
('Noord', 5.37, 1),
('Hillegersberg-Schiebroek', 13.26, 2),
('Kralingen-Crooswijk', 12.9, 3),
('Feijenoord', 6.44, 4),
('IJsselmonde', 13.12, NULL),
('Prins-Alexander', 20.24, 10),
('Charlois', 10.0, 2),
('Hoogvliet', 9.5, 3);