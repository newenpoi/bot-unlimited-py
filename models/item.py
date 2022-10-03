class Item():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Items` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL,
        `description` varchar(32) DEFAULT NULL,
        `value` int(11) UNSIGNED NOT NULL DEFAULT '0',
        `rarity_id` int(10) UNSIGNED NOT NULL DEFAULT '1',
        `category_id` int(10) UNSIGNED NOT NULL DEFAULT '1',
        PRIMARY KEY (`id`),
        UNIQUE KEY `Name` (`name`),
        CONSTRAINT `fk_item_rarity` FOREIGN KEY (`rarity_id`) REFERENCES `rarities`(`id`),
        CONSTRAINT `fk_item_category` FOREIGN KEY (`category_id`) REFERENCES `categories`(`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;
    '''

    data = [
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Gravel', NULL, 1, 1, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Coal', NULL, 1, 1, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Copper', NULL, 1, 1, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Iron', NULL, 1, 1, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Silver', NULL, 1, 2, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Aluminium', NULL, 1, 2, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Gold', NULL, 1, 3, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Platinum', NULL, 1, 4, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Vanadium', NULL, 1, 3, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Iridium', NULL, 1, 3, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Palladium', NULL, 1, 3, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Tungsten', NULL, 1, 4, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Uranium', NULL, 1, 4, 1)",
        "INSERT INTO `items` (`id`, `name`, `description`, `value`, `rarity_id`, `category_id`) VALUES (NULL, 'Newenite', NULL, 1, 5, 1)",
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    