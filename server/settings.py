# MongoDB attributes

from decouple import Config, RepositoryEnv

DOTENV_FILE = '.env.local'
env_config = Config(RepositoryEnv(DOTENV_FILE))

username = env_config.get('USERNAME')
password = env_config.get('PASSWORD')
# MongoDB attributes

mongodb_uri = 'mongodb+srv://' + username + ':' + password + '@cluster0.3ltwrrh.mongodb.net/?retryWrites=true&w=majority'
port = 8000  

