from passlib.context import CryptContext

myctx = CryptContext(
    schemes=["sha256_crypt", "md5_crypt", "des_crypt"]
)

hash1: str = myctx.hash(secret='minha_senha')
print(hash1)

# método que verifica o hash
print(myctx.verify(secret='outra_senha', hash=hash1)) # false
print(myctx.verify(secret="minha_senha", hash=hash1)) # true

