from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from api.routes.auth import router as auth_router
from api.routes.users import router as users_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    messages = [f"{'.'.join(str(l) for l in e['loc'][1:])}: {e['msg']}" for e in errors]
    return JSONResponse(status_code=422, content={"detail": "; ".join(messages)})

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    err_msg = str(exc.orig).lower()
    if "username" in err_msg:
        return JSONResponse(status_code=400, content={"detail": "Username already exists"})
    elif "email" in err_msg:
        return JSONResponse(status_code=400, content={"detail": "Email already exists"})
    return JSONResponse(status_code=400, content={"detail": "Database error"})

@app.get("/")
def root():
    return {"message": "API is running"}