class Language():

    print(f'Found {__name__}...')

    # English does not use country code here.
    # It is the default language.

    model = '''
        CREATE TABLE IF NOT EXISTS `Languages` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL UNIQUE,
        `country_code` varchar(32) NOT NULL UNIQUE,
        PRIMARY KEY (`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    data = [
        "INSERT INTO `languages` (`id`, `name`, `country_code`) VALUES (NULL, 'English', '')",
        "INSERT INTO `languages` (`id`, `name`, `country_code`) VALUES (NULL, 'Français', 'fr')"
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
