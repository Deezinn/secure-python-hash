from passlib.hash import argon2

hash: str = argon2.hash(secret='minha_senha')

# exemplo
print(hash)
# $argon2id$v=19$m=65536,t=3,p=4$eO/d+79Xam2t1br3HoNQag$QT+VJI9Pz4ncaJyYb5Ycpmm0/k5XayJ5TdsAkbMAMg8

print(argon2.verify(secret='minha_senha', hash=hash))
print(argon2.verify(secret='outra_senha', hash=hash))