from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


def configure_cors(app: FastAPI) -> None:
    # origins = [
    #     "http://localhost.tiangolo.com",
    #     "https://localhost.tiangolo.com",
    #     "http://127.0.0.1:3000",
    #     "http://localhost:3000",
    # ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
