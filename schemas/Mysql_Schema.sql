CREATE TABLE `form` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE `sensor` (
  `name` VARCHAR(255) PRIMARY KEY,
  `classtype` VARCHAR(255) NOT NULL,
  `form` INTEGER
);

CREATE INDEX `idx_sensor__form` ON `sensor` (`form`);

ALTER TABLE `sensor` ADD CONSTRAINT `fk_sensor__form` FOREIGN KEY (`form`) REFERENCES `form` (`id`);

CREATE TABLE `user` (
  `id` INTEGER PRIMARY KEY,
  `first` VARCHAR(255) NOT NULL,
  `last` VARCHAR(255) NOT NULL,
  `phone` VARCHAR(255) NOT NULL,
  `address` LONGTEXT NOT NULL,
  `classtype` VARCHAR(255) NOT NULL
);

CREATE TABLE `useruser` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `active` BOOLEAN NOT NULL,
  `created_on` DATETIME NOT NULL,
  `user_from` INTEGER NOT NULL,
  `user_to` INTEGER NOT NULL,
  `classtype` VARCHAR(255) NOT NULL
);

CREATE INDEX `idx_useruser__user_from` ON `useruser` (`user_from`);

CREATE INDEX `idx_useruser__user_to` ON `useruser` (`user_to`);

ALTER TABLE `useruser` ADD CONSTRAINT `fk_useruser__user_from` FOREIGN KEY (`user_from`) REFERENCES `user` (`id`);

ALTER TABLE `useruser` ADD CONSTRAINT `fk_useruser__user_to` FOREIGN KEY (`user_to`) REFERENCES `user` (`id`);

CREATE TABLE `value` (
  `sensor` VARCHAR(255) NOT NULL,
  `user` INTEGER NOT NULL,
  `time` DATETIME NOT NULL,
  `value` DECIMAL(12, 2),
  PRIMARY KEY (`sensor`, `user`, `time`)
);

CREATE INDEX `idx_value__user` ON `value` (`user`);

ALTER TABLE `value` ADD CONSTRAINT `fk_value__sensor` FOREIGN KEY (`sensor`) REFERENCES `sensor` (`name`);

ALTER TABLE `value` ADD CONSTRAINT `fk_value__user` FOREIGN KEY (`user`) REFERENCES `user` (`id`)