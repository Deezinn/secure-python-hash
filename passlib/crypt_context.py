from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256", "des_crypt"],
    # deprecated='auto',  caso eu tenha um hash antigo e queria atualizar, aplicar
)

hash: str = pwd_context.hash(secret='hash_qualquer')

print(hash)

print(pwd_context.verify(secret='hash_qualquer', hash=hash))
print(pwd_context.verify(secret="hash_qualquer_outro", hash=hash))