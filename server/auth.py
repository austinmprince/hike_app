
from jose import JWTError, jwt
from passlib.context import CryptContext

def _validate_password(plan_password, hashed_password):
  pwd_context.verify(plan_password, hashed_password)
  return pwd_context.verify(plan_password,hashed_password)

def _get_user(username: str):
  curr_user = users_coll.find_one({"username": username})
  if not curr_user:
    return None
  return UserIn(**curr_user)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
  print(data, expires_delta)
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.now + timedelta(minutes=15)
  to_encode.update({'exp': expire})
  encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
  return encoded_jwt
  
def _authenticate(username: str, password: str) -> UserOut:
  curr_user = _get_user(username)
  if not curr_user or not _validate_password(password, curr_user.password):
    return False
  return curr_user

def get_current_user(token: str = Depends(oauth2_scheme)):
  not_valid_exception = HTTPException(status_code=401, detail="User is not allowed to see this data")
  try:
    payload = jwt.decode(token, secret_key, algorithm)
    username = payload.get('sub')
    if not username:
      raise not_valid_exception
  except JWTError:
    raise not_valid_exception
  user = _get_user(username)
  if not user:
    raise not_valid_exception
  return user