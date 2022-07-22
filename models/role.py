
class Role():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Roles` (
        `id_server` bigint(20) UNSIGNED NOT NULL,
        `id_channel` bigint(20) UNSIGNED NOT NULL,
        `id_message` bigint(20) UNSIGNED NOT NULL,
        `id_role` bigint(20) UNSIGNED NOT NULL,
        `emoji` varchar(32) NOT NULL,
        PRIMARY KEY (`id_server`, `id_channel`, `id_message`, `id_role`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    