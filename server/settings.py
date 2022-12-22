# MongoDB attributes

from decouple import Config, RepositoryEnv

DOTENV_FILE = '.env.local'
env_config = Config(RepositoryEnv(DOTENV_FILE))

username = env_config.get('USERNAME')
password = env_config.get('PASSWORD')
secret_key = env_config.get('SECRET_KEY')
algorithm = env_config.get('ALGORITHM')
access_token_expire_minutes = env_config.get('ACCESS_TOKEN_EXPIRE_MINUTES')

# MongoDB attributes

mongodb_uri = 'mongodb+srv://' + username + ':' + password + '@cluster0.3ltwrrh.mongodb.net/?retryWrites=true&w=majority'
port = 8000

