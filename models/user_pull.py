
class User_Pull():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Users_Pulls` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `user_id_unique` bigint(20) UNSIGNED NOT NULL,
        `user_id_server` bigint(20) UNSIGNED NOT NULL,
        `waifu_id` int(10) UNSIGNED NOT NULL,
        `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`),
        CONSTRAINT `fk_pull_user` FOREIGN KEY (`user_id_unique`, `user_id_server`) REFERENCES `users` (`id_unique`, `id_server`) ON DELETE CASCADE,
        CONSTRAINT `fk_pull` FOREIGN KEY (`waifu_id`) REFERENCES `Waifus`(`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    