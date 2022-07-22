from datetime import date, datetime

class User():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Users` (
        `id_unique` bigint(20) UNSIGNED NOT NULL,
        `id_server` bigint(20) UNSIGNED NOT NULL,
        `nickname` varchar(32) NOT NULL,
        `gold` int(11) NOT NULL DEFAULT '500',
        `tick` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        `element` int(10) UNSIGNED NOT NULL DEFAULT '1',
        `date_birth` DATE,
        `health` int(11) NOT NULL DEFAULT 100,
        `show_date_birth` tinyint(1) DEFAULT NULL,
        PRIMARY KEY (`id_unique`, `id_server`),
        CONSTRAINT `fk_user_element` FOREIGN KEY (`element`) REFERENCES `Elements`(`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    