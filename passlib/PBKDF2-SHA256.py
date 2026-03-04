from passlib.hash import pbkdf2_sha256

# criando hash de senha
hash = pbkdf2_sha256.hash(secret='minha_senha')
print(hash)

# verificando hash de senha
# Aqui verificamos se o input sem hash bate com o valor que foi criado o hash
print(pbkdf2_sha256.verify(secret='minha_senha', hash=hash))

print(pbkdf2_sha256.verify(secret='outra_senha', hash=hash))
