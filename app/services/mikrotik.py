import routeros_api
from app.config import (
    MIKROTIK_HOST,
    MIKROTIK_PORT,
    MIKROTIK_USERNAME,
    MIKROTIK_PASSWORD,
    MIKROTIK_USE_SSL,
)


def get_mikrotik_connection():
    """
    Create and return a connection to the MikroTik router.
    Uses plaintext_login=True (required for RouterOS >= 6.43).
    """
    connection = routeros_api.RouterOsApiPool(
        host=MIKROTIK_HOST,
        username=MIKROTIK_USERNAME,
        password=MIKROTIK_PASSWORD,
        port=MIKROTIK_PORT,
        use_ssl=MIKROTIK_USE_SSL,
        plaintext_login=True,
    )
    return connection


def test_connection():
    """
    Test the connection to MikroTik by fetching system identity.
    Returns the router identity name if successful.
    """
    connection = get_mikrotik_connection()
    try:
        api = connection.get_api()
        identity = api.get_resource("/system/identity")
        result = identity.get()
        return {"status": "connected", "identity": result[0]["name"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        connection.disconnect()
