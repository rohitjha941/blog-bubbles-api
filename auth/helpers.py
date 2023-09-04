# from urllib import response
# from passlib.context import CryptContext
# from auth import schemas, helpers, exceptions
# from jose import jwt, JWTError
# from datetime import datetime, timedelta
# from app.core.config import settings
# from fastapi import Header
# from auth.models.all import *


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def generateHash(password):
#     return pwd_context.hash(password)


# async def validatePassword(plain_password, email):

#     user = await User.get_or_none(email=email)
#     if user is None:
#         raise exceptions.loginException

#     hashverify = pwd_context.verify(plain_password, user.password)

#     if not hashverify:
#         raise exceptions.loginException

#     return user


# def generateToken(data, expires_delta=None):
#     data = {"email": data}
#     to_encode = data.copy()

#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(days=30)

#     to_encode.update({"exp": expire})

#     encoded_jwt = jwt.encode(
#         to_encode, settings.SECERET_KEY, algorithm=settings.ALGORITHM
#     )

#     return encoded_jwt


# def jwtDecodetoken(token):
#     return jwt.decode(token, settings.SECERET_KEY, algorithms=[settings.ALGORITHM])


# def returnUser(user):
#     user = user.__dict__
#     del user["password"]
#     user["token"] = helpers.generateToken(user["email"])
#     return user


# async def validateToken(token: str = Header(None)):
#     try:
#         payload = helpers.jwtDecodetoken(token)
#         email: str = payload.get("email")
#         if email is None:
#             raise exceptions.credentialsException
#         user = await User.get_or_none(email=email)
#         if user is None:
#             raise exceptions.credentialsException
#         return user
#     except JWTError:
#         raise exceptions.credentialsException
