
---

# 🔐 secure-python-hash

Repositório criado para **fins de estudo sobre hashing de senhas em Python**, com foco em aplicações reais em **APIs que exigem armazenamento seguro de credenciais**.

O objetivo é entender, na prática, como funcionam diferentes algoritmos de hash e como aplicá-los corretamente em projetos backend.

---

## 📚 Objetivo do Projeto

Este repositório foi criado para:

* Estudar hashing de senhas com a biblioteca **Passlib**
* Comparar diferentes algoritmos de hash
* Entender boas práticas de segurança para autenticação
* Aplicar esse conhecimento futuramente em APIs

---

### 📂 Pasta `passlib/`

Contém exemplos práticos de uso de diferentes algoritmos:

* `argon2_hash.py` → Implementação usando Argon2
* `pbkdf2_sha256.py` → Implementação com PBKDF2
* `oracle_10.py` → Exemplo do algoritmo Oracle 10g
* `crypt_context.py` → Uso do CryptContext para gerenciar múltiplos hashes
* `verificando_outros_hash.py` → Testes e validações de hashes

---

## 🔍 Algoritmos Estudados

### 🔹 Argon2 (Escolhido como principal)

Após análise, o algoritmo escolhido como padrão foi:

👉 **Argon2**

Motivos:

* Considerado o algoritmo mais moderno para hashing de senhas
* Vencedor do Password Hashing Competition (PHC)
* Usa **CPU + memória (RAM)** para gerar o hash
* Dificulta ataques com GPU
* Resistente a ataques de força bruta em larga escala

Esse fator de uso intensivo de memória limita significativamente ataques paralelos com hardware especializado.

---

### 🔹 PBKDF2-SHA256

* Algoritmo amplamente utilizado
* Compatível com diversos frameworks
* Seguro, mas menos resistente a ataques com GPU comparado ao Argon2

---

### 🔹 Oracle 10g

* Exemplo de algoritmo legado
* Utilizado para fins de estudo
* Exige parâmetros externos (ex: username) para gerar hash

---

## 🧠 O que estou aprendendo

* Diferença entre **hash e criptografia**
* Importância de usar **salt automático**
* Uso do `CryptContext` para versionamento de hashes
* Estratégia de migração de algoritmos
* Como verificar senhas corretamente
* Como evitar armazenar senhas em texto puro

---
