import datetime
import json
import os
import jwt


class TokenService:
    @staticmethod
    def generate(payload):
        payload.update({"exp": datetime.datetime.timestamp(datetime.datetime.now() + datetime.timedelta(hours=6))})
        return jwt.encode(json.loads(json.dumps(payload, sort_keys=True)), os.environ.get("JWT_SECRET"),
                          algorithm="HS256")

    @staticmethod
    def decode(token):
        return jwt.decode(token, os.environ.get("JWT_SECRET"))
