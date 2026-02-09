PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE metadata (
        id INTEGER PRIMARY KEY,
        source TEXT NOT NULL,
        as_of TEXT NOT NULL
    );
 codex/create-epl-football-stats-analytics-site-d7kwnb
INSERT INTO metadata VALUES(1,'StatsBomb Open Data (локальный срез)','2026-02-05');

INSERT INTO metadata VALUES(1,'Демонстрационные агрегированные данные, вдохновленные StatsBomb Open Data','2026-02-05');
 main
CREATE TABLE standings (
        position INTEGER,
        team TEXT,
        played INTEGER,
        wins INTEGER,
        draws INTEGER,
        losses INTEGER,
        goals_for INTEGER,
        goals_against INTEGER,
        points INTEGER,
        form TEXT
    );
INSERT INTO standings VALUES(1,'Манчестер Сити',24,17,4,3,54,22,55,'ВВВНВ');
INSERT INTO standings VALUES(2,'Арсенал',24,16,5,3,49,21,53,'ВНВВП');
INSERT INTO standings VALUES(3,'Ливерпуль',24,15,6,3,50,24,51,'НВВВН');
INSERT INTO standings VALUES(4,'Тоттенхэм',24,13,6,5,45,30,45,'ВНПВВ');
INSERT INTO standings VALUES(5,'Ньюкасл',24,12,6,6,41,29,42,'ВПВНВ');
INSERT INTO standings VALUES(6,'Манчестер Юнайтед',24,11,7,6,38,31,40,'НВНПВ');
INSERT INTO standings VALUES(7,'Челси',24,10,8,6,36,29,38,'ВННВП');
INSERT INTO standings VALUES(8,'Брайтон',24,10,6,8,34,30,36,'ПВНВН');
INSERT INTO standings VALUES(9,'Астон Вилла',24,9,7,8,33,32,34,'ВНПВН');
INSERT INTO standings VALUES(10,'Вест Хэм',24,8,8,8,30,31,32,'НВПНВ');
INSERT INTO standings VALUES(11,'Вулверхэмптон',24,8,6,10,28,33,30,'ПВПНВ');
INSERT INTO standings VALUES(12,'Фулхэм',24,7,7,10,27,34,28,'НПВНП');
INSERT INTO standings VALUES(13,'Кристал Пэлас',24,7,6,11,25,35,27,'ПНВПН');
INSERT INTO standings VALUES(14,'Брентфорд',24,6,8,10,26,37,26,'ННВПП');
INSERT INTO standings VALUES(15,'Эвертон',24,6,7,11,24,35,25,'ПВНПН');
INSERT INTO standings VALUES(16,'Борнмут',24,6,6,12,23,36,24,'ППВНП');
INSERT INTO standings VALUES(17,'Ноттингем Форест',24,5,7,12,22,37,22,'НППВН');
INSERT INTO standings VALUES(18,'Лутон Таун',24,5,5,14,21,40,20,'ПВППН');
INSERT INTO standings VALUES(19,'Бернли',24,4,6,14,20,42,18,'ПНППВ');
INSERT INTO standings VALUES(20,'Шеффилд Юнайтед',24,3,5,16,18,45,14,'ППНПП');
CREATE TABLE fixtures (
        date TEXT,
        time TEXT,
        home TEXT,
        away TEXT,
        venue TEXT,
        status TEXT
    );
INSERT INTO fixtures VALUES('2026-02-05','15:30','Арсенал','Ньюкасл','Эмирейтс','Сегодня');
INSERT INTO fixtures VALUES('2026-02-05','18:00','Челси','Брайтон','Стэмфорд Бридж','Сегодня');
INSERT INTO fixtures VALUES('2026-02-06','21:45','Ливерпуль','Тоттенхэм','Энфилд','Завтра');
INSERT INTO fixtures VALUES('2026-02-07','17:00','Манчестер Сити','Вест Хэм','Этихад','Скоро');
INSERT INTO fixtures VALUES('2026-02-08','19:30','Астон Вилла','Манчестер Юнайтед','Вилла Парк','Скоро');
COMMIT;
