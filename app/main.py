from fastapi import FastAPI
from app.services.mikrotik import test_connection

app = FastAPI(
    title="MirkoVPN Manager API",
    description="REST API for managing OpenVPN server on MikroTik RouterOS v7",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "MirkoVPN Manager API is running"}


@app.get("/api/mikrotik/test-connection")
def mikrotik_test_connection():
    """
    Test the connection to the MikroTik router.
    Returns the router identity if connected successfully.
    """
    return test_connection()
