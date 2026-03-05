from passlib.hash import oracle10

hash:str = oracle10.hash(secret='secret', user='admin')

print(hash)

print(oracle10.verify(secret="secret", hash=hash, user="wronguser"))

print(oracle10.verify(secret="wrongpassword", hash=hash, user="admin"))
