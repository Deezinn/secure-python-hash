from passlib.hash import pbkdf2_sha256, md5_crypt

other_hash: str = md5_crypt.hash(secret='senha')

# para previnir o erro, existe o metodo identify

print(pbkdf2_sha256.identify(hash=other_hash))
# False

# erro
print(pbkdf2_sha256.verify(secret='senha', hash=other_hash))