from jose import jwt
import json
from urllib.request import urlopen
from functools import wraps


# configuration
AAD_AUDIENCE = "TO FILL"
AAD_TENANT = "TO FILL"
ALGORITHMS = ["RS256"]


def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        id_token, access_token = get_token_auth_header(
            kwargs.get("X_Api_Key"), kwargs.get("request")
        )
        payload = verify_decode_jwt(id_token, access_token)
        return f(*args, **kwargs)

    return wrapper


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header(X_Api_Key, request):
    """Obtains the Access Token from the Authorization Header
    """
    # auth = request.headers.get("X-Api-Key", None)
    auth = X_Api_Key
    if not auth:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected.",
            },
            401,
        )
    parts = auth.split(",")

    if len(parts) == 1:
        raise AuthError(
            {"code": "invalid_header", "description": "Token not found."}, 401
        )

    elif len(parts) > 2:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must be bearer token.",
            },
            401,
        )
    id_token, access_token = parts[:2]
    return id_token, access_token


def verify_decode_jwt(id_token, access_token):
    # GET THE PUBLIC KEY FROM AAD
    jwks_uri = f"https://login.microsoftonline.com/{AAD_TENANT}/discovery/v2.0/keys"
    jsonurl = urlopen(jwks_uri)
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN THE HEADER
    try:
        unverified_header = jwt.get_unverified_header(id_token)
    except:
        raise AuthError(
            {"code": "invalid_token", "description": "Token malformed."}, 401
        )
    # CHOOSE OUR KEY
    rsa_key = {}
    if "kid" not in unverified_header:
        raise AuthError(
            {"code": "invalid_header", "description": "Authorization malformed."}, 401
        )

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = key
    if rsa_key:
        issuer = f"https://login.microsoftonline.com/{AAD_TENANT}/v2.0"
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                id_token,
                rsa_key,
                algorithms=["RS256"],
                audience=AAD_AUDIENCE,
                issuer=issuer,
                access_token=access_token,
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "Token expired."}, 401
            )

        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer.",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token.",
                },
                400,
            )
    raise AuthError(
        {
            "code": "invalid_header",
            "description": "Unable to find the appropriate key.",
        },
        400,
    )
