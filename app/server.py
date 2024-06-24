from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.message import message

def get_application() -> FastAPI:

    application = FastAPI(docs_url="/swagger")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(message)

    return application

app = get_application()

@app.get("/")
def root():
    return {"message": "Hello Gen.View"}

@app.on_event("startup")
async def startup_event():
    print("Start up the server")
@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down the server")

