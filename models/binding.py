
class Binding():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Bindings` (
        `id_server` bigint(20) UNSIGNED NOT NULL,
        `id_channel` bigint(20) UNSIGNED NOT NULL,
        PRIMARY KEY (`id_server`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    