
class User_Waifu():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Users_Waifus` (
        `waifu_id` int(10) UNSIGNED NOT NULL,
        `user_id_unique` bigint(20) UNSIGNED NOT NULL,
        `user_id_server` bigint(20) UNSIGNED NOT NULL,
        `acquired` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`waifu_id`, `user_id_unique`, `user_id_server`),
        CONSTRAINT `fk_waifu` FOREIGN KEY (`waifu_id`) REFERENCES `Waifus`(`id`),
        CONSTRAINT `fk_waifu_user` FOREIGN KEY (`user_id_unique`, `user_id_server`) REFERENCES `users` (`id_unique`, `id_server`) ON DELETE CASCADE
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    