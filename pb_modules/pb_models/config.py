import os
from pb_config import ConfigDev, ConfigProd, ConfigLocal

match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- pb_models/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- pb_models/config: Production')
    case _:
        config = ConfigLocal()
        print('- pb_models/config: Local')
    