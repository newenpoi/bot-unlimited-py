
class Quiz():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Quiz` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `user_id_unique` bigint(20) UNSIGNED NOT NULL,
        `user_id_server` bigint(20) UNSIGNED NOT NULL,
        `score` int(11) NOT NULL,
        `timing` int(11) DEFAULT NULL,
        PRIMARY KEY (`id`),
        KEY `guild_user` (`user_id_unique`, `user_id_server`),
        CONSTRAINT `fk_quiz_user` FOREIGN KEY (`user_id_unique`, `user_id_server`) REFERENCES `users` (`id_unique`, `id_server`) ON DELETE CASCADE
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    