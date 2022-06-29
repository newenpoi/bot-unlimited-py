
class Interaction():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Interactions` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL,
        `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        `user_id_unique` bigint(20) UNSIGNED NOT NULL,
        `user_id_server` bigint(20) UNSIGNED NOT NULL,
        PRIMARY KEY (`id`),
        CONSTRAINT `fk_user_interaction` FOREIGN KEY (`user_id_unique`, `user_id_server`) REFERENCES `Users`(`id_unique`, `id_server`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    