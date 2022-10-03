# TODO : Maj Modèle.

class Rarity():

    print(f'Found {__name__}...')

    model = '''
        CREATE TABLE IF NOT EXISTS `Rarities` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL UNIQUE,
        `translation_id` tinyint(1) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    data = [
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Common')",
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Unusual')",
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Rare')",
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Epic')",
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Unreal')"
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
