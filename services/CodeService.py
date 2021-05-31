import random
import string


class CodeService:
    @staticmethod
    def generate():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))