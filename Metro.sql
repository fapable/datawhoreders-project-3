CREATE TABLE metro (
wijk VARCHAR(255),
wijkoppervlakte_km2 FLOAT,
aantal_stations INT,
aantal_markten INT);

INSERT INTO metro (wijk, wijkoppervlakte_km2, aantal_stations)
VALUES ('Centrum', 4.81, 9, 3),
('Delfshaven', 5.8, 5, 1),
('Overschie', 15.80, NULL, 1),
('Noord', 5.37, 1, 0),
('Hillegersberg_Schiebroek', 13.26, 2, 0),
('Kralingen_Crooswijk', 12.9, 3, 0),
('Feijenoord', 6.44, 4, 1),
('Ijsselmonde', 13.12, NULL, 1),
('Prins_Alexander', 20.24, 10, 1),
('Charlois', 10.0, 2, 1);
