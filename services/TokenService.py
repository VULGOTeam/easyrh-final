import datetime
import json
import os
import jwt
from errors.InvalidUsage import InvalidUsage


class TokenService:
    def __init__(self):
        self.secret = os.environ.get("JWT_SECRET")

    def generate(self, payload):
        payload.update({"exp": datetime.datetime.timestamp(datetime.datetime.now() + datetime.timedelta(hours=6))})
        return jwt.encode(json.loads(json.dumps(payload, sort_keys=True)), self.secret,
                          algorithm="HS256")

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.secret, algorithms=["HS256"])
            return decoded
        except Exception:
            raise InvalidUsage(status_code=401, message='Token inválido')
