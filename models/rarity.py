# TODO : Maj Modèle.

class Rarity():

    print(f'Found {__name__}...')

    model = '''
        CREATE TABLE IF NOT EXISTS `Rarities` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL UNIQUE,
        PRIMARY KEY (`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    data = [
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Commun')",
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Inhabituel')",
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Rare')",
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Épique')",
        "INSERT INTO `rarities` (`id`, `name`) VALUES (NULL, 'Irréel')"
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
