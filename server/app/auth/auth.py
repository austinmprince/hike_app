from models import UserOut, UserIn
import datetime
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"])

def _authenticate(username: str, password: str) -> UserOut:
  curr_user = _get_user(username)
  if not curr_user or not _validate_password(password, curr_user.password):
    return False
  return curr_user
 

def _validate_password(plan_password, hashed_password):
  pwd_context.verify(plan_password, hashed_password)
  return pwd_context.verify(plan_password,hashed_password)
∏
def _get_user(username: str):
  curr_user = users_coll.find_one({"username": username})
  if not curr_user:
    return None
  return UserIn(**curr_user)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.now + timedelta(minutes=15)
  to_encode.update({'exp': expire})
  encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
  return encoded_jwt
  