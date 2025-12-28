DROP TABLE IF EXISTS stats;

CREATE TABLE stats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  gender TEXT NOT NULL,
  state_id INTEGER NOT NULL,
  fType NOT NULL,
  qualification NOT NULL,
  degree NOT NULL,
  nationality NOT NULL,
  ageRange NOT NULL,
  jobType NOT NULL,
  jobSize NOT NULL,
  jobArea NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
);

