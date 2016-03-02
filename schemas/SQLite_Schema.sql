CREATE TABLE "Form" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "Sensor" (
  "name" TEXT NOT NULL PRIMARY KEY,
  "classtype" TEXT NOT NULL,
  "form" INTEGER REFERENCES "Form" ("id")
);

CREATE INDEX "idx_sensor__form" ON "Sensor" ("form");

CREATE TABLE "User" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "first" TEXT NOT NULL,
  "last" TEXT NOT NULL,
  "phone" TEXT NOT NULL,
  "address" TEXT NOT NULL,
  "classtype" TEXT NOT NULL
);

CREATE TABLE "UserUser" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "active" BOOLEAN NOT NULL,
  "created_on" DATETIME NOT NULL,
  "user_from" INTEGER NOT NULL REFERENCES "User" ("id"),
  "user_to" INTEGER NOT NULL REFERENCES "User" ("id"),
  "classtype" TEXT NOT NULL
);

CREATE INDEX "idx_useruser__user_from" ON "UserUser" ("user_from");

CREATE INDEX "idx_useruser__user_to" ON "UserUser" ("user_to");

CREATE TABLE "Value" (
  "sensor" TEXT NOT NULL REFERENCES "Sensor" ("name"),
  "user" INTEGER NOT NULL REFERENCES "User" ("id"),
  "time" DATETIME NOT NULL,
  "value" DECIMAL(12, 2),
  PRIMARY KEY ("sensor", "user", "time")
);

CREATE INDEX "idx_value__user" ON "Value" ("user")