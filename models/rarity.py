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
        "INSERT INTO `rarities` (`id`, `name`, `translation_id`) VALUES (NULL, 'Common', 1)",
        "INSERT INTO `rarities` (`id`, `name`, `translation_id`) VALUES (NULL, 'Unusual', 2)",
        "INSERT INTO `rarities` (`id`, `name`, `translation_id`) VALUES (NULL, 'Rare', 3)",
        "INSERT INTO `rarities` (`id`, `name`, `translation_id`) VALUES (NULL, 'Epic', 4)",
        "INSERT INTO `rarities` (`id`, `name`, `translation_id`) VALUES (NULL, 'Unreal', 5)"
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
