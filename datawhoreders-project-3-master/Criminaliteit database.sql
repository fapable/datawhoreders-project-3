CREATE TABLE criminaliteit (
jaar INT,
wijk VARCHAR(255),
diefstal FLOAT,
drugsoverlast FLOAT,
geweld FLOAT,
inbraak FLOAT,
vandalisme FLOAT,
overlast FLOAT,
vervuiling FLOAT,
verkeer FLOAT,
average FLOAT);

INSERT INTO criminaliteit (jaar, wijk, diefstal, drugsoverlast, geweld, inbraak, vandalisme, overlast, vervuiling, verkeer, average)
VALUES (2009, 'Charlois', 20.03, 16.00, 6.50, 14.40, 17.75, 15.43, 32.63, 18.15, 17.66),
(2011, 'Charlois', 19.83, 15.50, 8.00, 15.30, 16.15, 15.23, 30.65, 16.85, 17.19),
(2009, 'Delfshaven', 20.16, 15.10, 7.56, 9.40, 14.00, 17.00, 34.78, 20.30, 17.29),
(2011, 'Delfshaven', 20.10, 16.60, 7.57, 14.30, 13.15, 18.23, 33.83, 19.90, 17.96),
(2009, 'Feijenoord', 20.60, 15.10, 6.43, 13.70, 20.40, 16.93, 33.78, 19.15, 18.26),
(2011, 'Feijenoord', 19.20, 15.4, 7.20, 16.20, 17.25, 16.90, 30.78, 17.55, 17.56),
(2009, 'Hillegersberg-Schiebroek', 9.63, 2.90, 1.03, 10.10, 9.07, 4.63, 18.05, 8.25, 7.96),
(2011, 'Hillegersberg-Schiebroek', 11.30, 3.70, 1.77, 11.60, 9.25, 4.47, 17.77, 8.35, 8.53),
(2009, 'Ijsselmonde', 15.33, 7.20, 4.63, 11.30, 18.25, 9.03, 22.58, 14.45, 12.85),
(2011, 'Ijsselmonde', 17.30, 9.60, 8.60, 21.70, 16.45, 12.27, 22.68, 14.60, 15.4),
(2009, 'Kralingen-Crooswijk', 22.33, 9.60, 3.27, 11.50, 14.25, 13.47, 30.75, 15.55, 15.09),
(2011, 'Kralingen-Crooswijk', 18.73, 9.30, 3.37, 10.50, 9.90, 13.10, 26.58, 13.90, 13.17),
(2009, 'Noord', 18.80, 10.10, 4.37, 10.20, 13.55, 12.80, 29.17, 18.00, 14.62),
(2011, 'Noord', 18.93, 9.40, 4.43, 8.30, 10.45, 11.70, 27.13, 15.70, 13.26),
(2009, 'Overschie', 19.27, 4.20, 2.60, 14.10, 16.80, 6.77, 22.55, 10.00, 12.04),
(2011, 'Overschie', 17.07, 4.60, 1.70, 13.90, 12.25, 6.97, 22.03, 22.10, 12.58),
(2009, 'Prins-Alexander', 13.53, 3.70, 1.67, 11.00, 20.00, 8.00, 22.42, 9.90, 11.28),
(2011, 'Prins-Alexander', 10.70, 3.20, 1.53, 13.80, 12.70, 7.53, 19.05, 8.45, 9.62),
(2009, 'Centrum', 23.63, 20.7, 6.067, 8.2, 15.1, 20.467, 32.767, 18.2, 18.14),
(2011, 'Centrum', 19.00, 11.8, 5.167, 9.4, 11.167, 19.867, 29.2, 17.1, 15.34);
