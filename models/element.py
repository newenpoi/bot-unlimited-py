
class Element():

    print(f'Found {__name__}...')

    model = '''
        CREATE TABLE IF NOT EXISTS `Elements` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL UNIQUE,
        PRIMARY KEY (`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    data = [
        "INSERT INTO `elements` (`id`, `name`) VALUES (NULL, 'Haine')",
        "INSERT INTO `elements` (`id`, `name`) VALUES (NULL, 'Clémence')",
        "INSERT INTO `elements` (`id`, `name`) VALUES (NULL, 'Pêché')",
        "INSERT INTO `elements` (`id`, `name`) VALUES (NULL, 'Vertu')",
        "INSERT INTO `elements` (`id`, `name`) VALUES (NULL, 'Supplice')",
        "INSERT INTO `elements` (`id`, `name`) VALUES (NULL, 'Consolation')"
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
