from fastapi import HTTPException, status

loginException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=[{
        "type":"unauthorized",
        "msg":"User not Authorized"
    }],
    headers={"WWW-Authenticate": "Bearer"},
)

credentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=[{
        "type":"incorrect_password",
        "msg":"Incorrect email or password"
    }],
    headers={"WWW-Authenticate": "Bearer"},
)

userException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=[{
        "type":"user_not_found",
        "msg":"User cannot be validated"  
    }],
    headers={"WWW-Authenticate": "Bearer"},
)
