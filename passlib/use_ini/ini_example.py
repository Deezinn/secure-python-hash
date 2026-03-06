from passlib.context import CryptContext

pwd_context: CryptContext = CryptContext.from_path(path="passlib_cfg.ini")

hash: str = pwd_context.hash(secret='minha_senha')
print(hash)