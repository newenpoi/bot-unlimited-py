
class Bid():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Bids` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `id_server` bigint(20) UNSIGNED NOT NULL,
        `waifu_id` int(10) UNSIGNED NOT NULL,
        `user_id_unique` bigint(20) UNSIGNED DEFAULT NULL COMMENT 'User with the highest bid (can be null).',
        `highest` int(10) UNSIGNED DEFAULT NULL COMMENT 'The highest bid for this waifu (can be null).',
        `date_last_bid` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT 'This is null by default.',
        PRIMARY KEY (`id`),
        CONSTRAINT `fk_waifu_bid` FOREIGN KEY (`waifu_id`) REFERENCES `Waifus`(`id`),
        CONSTRAINT `fk_user_bid` FOREIGN KEY (`user_id_unique`) REFERENCES `Users`(`id_unique`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    