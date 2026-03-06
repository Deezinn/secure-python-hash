from passlib.context import CryptContext

myctx: CryptContext = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])

hash1: str = myctx.hash(secret='minha_senha')
print(hash1)

# método que verifica o hash
print(myctx.verify(secret='outra_senha', hash=hash1)) # false
print(myctx.verify(secret="minha_senha", hash=hash1)) # true

hash2: str = myctx.hash(secret='nome_do_cachorro', scheme='md5_crypt')
print(hash2)

# método que verifica o hash
print(myctx.verify(secret="nome_de_outro_cachorro", hash=hash2))  # false
print(myctx.verify(secret="nome_do_cachorro", hash=hash2))  # true

myctx2: CryptContext = CryptContext(
    schemes=["sha256_crypt", "md5_crypt", "des_crypt"],
    default='des_crypt' # Se não definir o 'default',
    # por padrão o algoritmo de hash a ser escolhido será o primerio da lista
    )

hash3 = myctx2.hash(secret='password')
print(hash3)

myctx3 = CryptContext(schemes=["sha256_crypt", "ldap_salted_md5"])

print(myctx3.hash(secret="password", scheme="sha256_crypt"))
print(myctx3.hash(secret="password", scheme="ldap_salted_md5"))

# método que modifica o atributos padrão da classe CryptContext
myctx3.update(sha256_crypt__default_rounds=91234,
             ldap_salted_md5__salt_size=16)

print(myctx3.hash(secret="password", scheme="sha256_crypt"))
print(myctx3.hash(secret="password", scheme="ldap_salted_md5"))


myctx4 = CryptContext(
    schemes=["sha256_crypt", "ldap_salted_md5"],
    sha256_crypt__default_rounds = 91234,
    ldap_salted_md5__salt_size = 16
    )

# Analise do obj cryptcontext, setando por default alguns parametros
print(myctx4.to_dict())