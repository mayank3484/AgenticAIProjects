from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import PSQL_DB,PSQL_HOST,PSQL_PASSWORD,PSQL_PORT,PSQL_USER,SECRET,ALGORITHM
import jwt
import datetime
import json
import psycopg2
from psycopg2.extras import RealDictCursor

class LoginRequest(BaseModel):
    username:str
    password:str

def get_user_details(username:str,password:str):
    connection=psycopg2.connect(dbname=PSQL_DB,user=PSQL_USER,password=PSQL_PASSWORD,host=PSQL_HOST,port=PSQL_PORT)
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("select * from users where username = %s and password = %s",(username,password))
        result=cursor.fetchone()
    connection.close()
    return result
app = FastAPI(title="MCP Demo application")

@app.post("/login")
def login(request: LoginRequest):
    user=get_user_details(request.username,request.password)
    if user is None:
        raise HTTPException(status_code=404,detail="invalid username or password")
    now=datetime.datetime.now()
    payload={
        "sub":user["username"],"permissions":user["permissions"],"aud":"mcp_demo"
    }
    token=jwt.encode(payload,SECRET,algorithm=ALGORITHM)
    return {"access_token":token,"permissions":user["permissions"]}