
class Inventory():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `inventories` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `user_id_unique` bigint(20) UNSIGNED NOT NULL,
        `user_id_server` bigint(20) UNSIGNED NOT NULL,
        `item_id` int(10) UNSIGNED NOT NULL,
        `augmented` tinyint(4) UNSIGNED NOT NULL DEFAULT '0',
        `stackable` tinyint(1) UNSIGNED DEFAULT NULL,
        `quantity` int(10) UNSIGNED NOT NULL,
        `acquired` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`),
        UNIQUE KEY `ID_Item` (`user_id_unique`, `user_id_server`, `item_id`, `augmented`, `stackable`),
        CONSTRAINT `fk_inventory_item` FOREIGN KEY (`item_id`) REFERENCES `Items`(`id`) ON DELETE CASCADE,
        CONSTRAINT `fk_inventory_user` FOREIGN KEY (`user_id_unique`, `user_id_server`) REFERENCES `users` (`id_unique`, `id_server`) ON DELETE CASCADE
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    