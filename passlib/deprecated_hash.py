from passlib.context import CryptContext


myctx = CryptContext(
    schemes=["sha256_crypt", "md5_crypt", "des_crypt"],
    deprecated=["md5_crypt", "des_crypt"],
)

hash1 = "$5$rounds=80000$zWZFpsA2egmQY8R9$xp89Vvg1HeDCJ/bTDDN6qkdsCwcMM61vHtM1RNxXur."

# método que verifica se aquele tipo de hash precisa de um update
print(myctx.needs_update(hash=hash1))

hash2 = "$1$fmWm78VW$uWjT69xZNMHWyEQjq852d1"

# método que verifica se aquele tipo de hash precisa de um update
print(myctx.needs_update(hash=hash2))

