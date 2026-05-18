# ============================================================
# 🔐 FastAPI STUDENT App + JWT Authentication (Array Version)
# ============================================================

# ============================================================
# 🚀 WHAT WE ARE BUILDING
# ============================================================

'''
This project includes:

✅ FastAPI
✅ JWT Authentication
✅ CRUD Operations
✅ Temporary Storage using Python List
✅ Protected APIs using Token

No Database used here.
Data will be stored temporarily in array/list.
'''

# ============================================================
# 🚀 INSTALL REQUIRED PACKAGES
# ============================================================

'''
pip install fastapi uvicorn python-jose
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import List

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

'''
SECRET_KEY
-----------
Used to sign the token.

Think:
JWT Token = Locked Box
SECRET_KEY = Key to lock/unlock

If secret key changes:
- Old tokens become invalid
'''

SECRET_KEY = "|<>AtYkKern@S0ftWaRe!#_nov%^nErK"

# ------------------------------------------------------------

'''
ALGORITHM
-----------
Encryption algorithm used to create token.

HS256 = Most commonly used JWT algorithm
'''

ALGORITHM = "HS256"

# ------------------------------------------------------------

'''
TOKEN EXPIRY TIME
------------------
Defines how long token stays valid.

Examples:

timedelta(seconds=1)        -> 1 second
timedelta(seconds=30)       -> 30 seconds

timedelta(minutes=1)        -> 1 minute
timedelta(minutes=5)        -> 5 minutes
timedelta(minutes=15)       -> 15 minutes
timedelta(minutes=30)       -> 30 minutes

timedelta(hours=1)          -> 1 hour
timedelta(hours=2)          -> 2 hours
timedelta(hours=12)         -> 12 hours

timedelta(days=1)           -> 1 day
timedelta(days=7)           -> 7 days
timedelta(days=30)          -> 30 days
'''

ACCESS_TOKEN_EXPIRE = timedelta(hours=1)

# ============================================================
# 🧾 Pydantic Models
# ============================================================

'''
Used for:
- Request validation
- Data structure
- Auto API documentation
'''

class Student(BaseModel):

    id: int
    name: str
    email: str
    age: int = 0

# ------------------------------------------------------------

class Login(BaseModel):

    username: str
    password: str

# ============================================================
# 🗃️ TEMPORARY DATABASE (LIST)
# ============================================================

'''
Temporary array/list storage

⚠️ Data will be lost when server restarts
'''

students: List[Student] = []

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):

    '''
    Steps:
    1. Copy incoming data
    2. Add expiry time
    3. Encode token using secret key
    4. Return generated JWT token
    '''

    # Copy data
    to_encode = data.copy()

    # Create expiry time
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    '''
    Example:

    Current Time = 10:00 AM

    Expiry = 5 minutes

    Token Expiry = 10:05 AM
    '''

    # Add expiry into payload
    to_encode.update({"exp": expire})

    '''
    Final JWT Payload Example:

    {
        "sub": "admin",
        "exp": "10:05 AM"
    }
    '''

    # Generate encoded JWT token
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================

'''
OAuth2PasswordBearer
---------------------

Automatically:
- Reads Authorization header
- Extracts Bearer token

Example Header:

Authorization: Bearer eyJhbGc...
'''

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ------------------------------------------------------------

def verify_token(token: str = Depends(oauth2_scheme)):

    '''
    This function validates token.

    Steps:
    1. Read token
    2. Decode token
    3. Verify secret key
    4. Verify expiry time
    5. Extract user info
    '''

    try:

        '''
        jwt.decode() automatically checks:

        ✅ Secret key
        ✅ Token expiry
        ✅ Algorithm

        If expired:
            JWTError occurs
        '''

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        '''
        Example Payload:

        {
            "sub": "admin",
            "exp": "10:05 AM"
        }
        '''

        # Extract username
        username = payload.get("sub")

        # Check username exists
        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        '''
        Happens when:
        - Token expired
        - Wrong secret key
        - Invalid token
        '''

        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI + JWT + Array CRUD 🚀"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(user: Login):

    '''
    Dummy Login

    Username = admin
    Password = admin123
    '''

    if user.username != "admin" or user.password != "admin123":

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    '''
    Create token with username
    "sub" = subject/user
    '''

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }

# ============================================================
# ✅ CREATE STUDENT
# ============================================================

@app.post("/students")
def create_student(
    student: Student,
    user: str = Depends(verify_token)
):

    '''
    Depends(verify_token)

    Means:
    Before API executes:
        verify_token() runs first

    If token invalid:
        API stops immediately
    '''

    # Check duplicate ID
    for existing in students:

        if existing.id == student.id:

            raise HTTPException(
                status_code=400,
                detail="ID already exists"
            )

    # Add student into list
    students.append(student)

    return {
        "message": "Student created",
        "data": student
    }

# ============================================================
# ✅ READ ALL STUDENTS
# ============================================================

@app.get("/students")
def get_all_students(
    user: str = Depends(verify_token)
):

    '''
    Flow While Calling This API:

    1. Read Authorization Header
    2. Extract Bearer Token
    3. verify_token() runs
    4. jwt.decode() validates:
        - Secret key
        - Expiry
        - Algorithm
    5. If valid:
        Continue API
    6. If expired:
        Return 401 Error
    '''

    return {
        "count": len(students),
        "data": students
    }

# ============================================================
# ✅ READ SINGLE STUDENT
# ============================================================

@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    user: str = Depends(verify_token)
):

    for student in students:

        if student.id == student_id:

            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ============================================================
# ✅ UPDATE STUDENT
# ============================================================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated: Student,
    user: str = Depends(verify_token)
):

    for index, student in enumerate(students):

        if student.id == student_id:

            students[index] = updated

            return {
                "message": "Student updated successfully",
                "data": updated
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ============================================================
# ✅ DELETE STUDENT
# ============================================================

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    user: str = Depends(verify_token)
):

    for index, student in enumerate(students):

        if student.id == student_id:

            deleted = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "data": deleted
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ============================================================
# 🔥 FINAL JWT FLOW
# ============================================================

'''
LOGIN FLOW
------------

Client Login
    ↓
Generate JWT Token
    ↓
Return Token to Client


API ACCESS FLOW
----------------

Client Calls API
    ↓
Send Token in Header

Authorization: Bearer eyJhbGc...

    ↓
verify_token() runs
    ↓
jwt.decode() validates:
    ✅ Secret Key
    ✅ Expiry Time
    ✅ Algorithm

    ↓
If Valid:
    Continue API

If Expired:
    Return 401 Error
'''

# ============================================================
# 🌐 RUN SERVER
# ============================================================

'''
uvicorn main:app --reload
'''

# ============================================================
# 🌐 SWAGGER DOCS
# ============================================================

'''
http://127.0.0.1:8000/docs
'''
