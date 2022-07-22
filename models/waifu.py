
class Waifu():

    print(f'Found {__name__}...')
    
    model = '''
        CREATE TABLE IF NOT EXISTS `Waifus` (
        `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` varchar(32) NOT NULL,
        `price` int(11) NOT NULL,
        `date_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `source` varchar(128) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
    '''

    data = [
        "INSERT INTO `waifus` (`id`, `name`, `price`, `date_added`, `source`) VALUES (NULL, 'Fischl', 90000, NOW(), 'https://media.discordapp.net/attachments/577914680282972170/993568617671163934/85267485_p0_master1200.png')",
        "INSERT INTO `waifus` (`id`, `name`, `price`, `date_added`, `source`) VALUES (NULL, 'Ichigo', 60000, NOW(), 'https://cdn.discordapp.com/attachments/577914680282972170/993591092983369918/ichigo.jpg')",
        "INSERT INTO `waifus` (`id`, `name`, `price`, `date_added`, `source`) VALUES (NULL, 'Yae Miko', 90000, NOW(), 'https://cdn.discordapp.com/attachments/577914680282972170/993591060414611586/99188724_p0_master1200.jpg')",
    ]

    def __init__(self):
        print("Please do not instanciate this class (yet).")
    