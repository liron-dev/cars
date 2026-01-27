CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    hp INTEGER,
    engine VARCHAR(50),
    description TEXT,
    image VARCHAR(100),
    tags TEXT
);

INSERT INTO cars (name, hp, engine, description, image, tags) 
VALUES 
('Porsche 911 GT3 RS', 518, '4.0L Flat-6', 'The pinnacle of 911 performance. Built for the track.', 'images/porsche.jpeg', 'German,Track-Tool,Naturally Aspirated'),
('DeLorean DMC-12', 130, '2.85L V6', 'The stainless steel icon. Flux capacitor included.', 'images/delorean.jpeg', 'Movie Icon,Stainless Steel,Gull-wing');
