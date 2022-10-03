
class Category():

    print(f'Found {__name__}...')

    model = '''
        CREATE TABLE IF NOT EXISTS `Categories` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL UNIQUE,
        PRIMARY KEY (`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    data = [
        "INSERT INTO `categories` (`id`, `name`) VALUES (NULL, 'Raw')",
        "INSERT INTO `categories` (`id`, `name`) VALUES (NULL, 'Augment')",
        "INSERT INTO `categories` (`id`, `name`) VALUES (NULL, 'Weapon')",
        "INSERT INTO `categories` (`id`, `name`) VALUES (NULL, 'Organic')"
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
