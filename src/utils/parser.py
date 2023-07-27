from uuid import uuid4
from hashlib import md5


def create_hash(text=None):
    if text:
        return md5(text.encode('utf-8')).hexdigest()
    else:
        return uuid4().hex
