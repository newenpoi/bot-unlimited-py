
class Waifu():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Waifus` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL,
        `gender` varchar(1) NOT NULL,
        `origin` varchar(32) DEFAULT NULL,
        `price` int(11) UNSIGNED NOT NULL,
        `date_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `source` varchar(128) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE (`name`, `origin`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    data = [
        "INSERT INTO `waifus` (`id`, `name`, `gender`, `origin`, `price`, `date_added`, `source`) VALUES (NULL, 'Fischl', 'F', 'Genshin Impact', 3000, NOW(), 'https://media.discordapp.net/attachments/577914680282972170/993568617671163934/85267485_p0_master1200.png')",
        "INSERT INTO `waifus` (`id`, `name`, `gender`, `origin`, `price`, `date_added`, `source`) VALUES (NULL, 'Ichigo', 'M', 'Bleach', 2000, NOW(), 'https://cdn.discordapp.com/attachments/577914680282972170/993591092983369918/ichigo.jpg')",
        "INSERT INTO `waifus` (`id`, `name`, `gender`, `origin`, `price`, `date_added`, `source`) VALUES (NULL, 'Yae Miko', 'F', 'Genshin Impact', 3000, NOW(), 'https://cdn.discordapp.com/attachments/577914680282972170/993591060414611586/99188724_p0_master1200.jpg')",
        "INSERT INTO `waifus` (`id`, `name`, `gender`, `origin`, `price`, `date_added`, `source`) VALUES (NULL, 'Vista', 'F', 'Soul Worker', 3000, NOW(), 'https://cdn.discordapp.com/attachments/577914680282972170/1002697953078685776/i13370836147.jpg')",
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    