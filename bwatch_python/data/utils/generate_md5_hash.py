import hashlib


def generateMD5Hash(password: str):
    return hashlib.md5(password.encode()).hexdigest()
