CREATE TABLE `Worktime` (
    `id` bigint unsigned NOT NULL AUTO_INCREMENT,
    `date` datetime NOT NULL DEFAULT '1000-01-01 00:00:00',
    `start_time` time NOT NULL DEFAULT '00:00:00',
    `end_time` time NOT NULL DEFAULT '00:00:00',
    PRIMARY KEY (`id`) 
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;