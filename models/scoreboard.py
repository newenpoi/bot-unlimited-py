
class Scoreboard():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Scoreboard` (
        `id_unique` bigint(20) UNSIGNED NOT NULL,
        `id_server` bigint(20) UNSIGNED NOT NULL,
        `value` int(11) NOT NULL,
        `unit` VARCHAR(32) NOT NULL,
        `scale` int(11) NOT NULL,
        PRIMARY KEY (`id_unique`, `id_server`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    