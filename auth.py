

from datetime import datetime,timedelta
from passlib.context import CryptContext
from jose import jwt,JWTError


Security_key="1234"
algorithm="HS256"
time_expires_in_mins=30

password_context=CryptContext(schemes=["bcrypt"])

def password_scrambler(password:str):
    hashed_password=password_context.hash(password)
    return hashed_password

def password_checker(password:str,hashed_password:str):
    return password_context.verify(password,hashed_password)

def token_generator(data:dict):
    expiry=datetime.utcnow()+timedelta(minutes= time_expires_in_mins)
    to_encode=data.copy()
    to_encode.update({"exp":expiry})
    new_token=jwt.encode(to_encode,Security_key,algorithm)
    return new_token



def token_verifier(token:str):
    try:
        payload=jwt.decode(token,Security_key,algorithms=[algorithm])
        username=payload.get("sub")
        if username is None:
            return None
        return username
    except JWTError:
        return None
        
