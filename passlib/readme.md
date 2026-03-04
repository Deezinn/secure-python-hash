
---

# 🔐 Algoritmos de Hash de Senha Recomendados

Atualmente existem quatro opções seguras e amplamente aceitas:

* `argon2`
* `bcrypt`
* `pbkdf2_sha256 / pbkdf2_sha512`
* `sha256_crypt / sha512_crypt`

Todos possuem:

* Nenhuma vulnerabilidade prática conhecida
* Salt ≥ 96 bits
* Custo configurável (work factor)
* Implementações abertas e auditáveis
* Amplo uso em produção

---

## argon2

Algoritmo moderno e **memory-hard** (usa CPU + memória).
Vencedor da Password Hashing Competition.

**Vantagens**

* Alta resistência contra GPU/ASIC
* Considerado o padrão atual para novas aplicações
* Parâmetros ajustáveis: `time_cost`, `memory_cost`, `parallelism`

**Indicado para:** aplicações modernas.

---

## bcrypt

Algoritmo consolidado desde 1999.
Baseado no cipher Blowfish.

**Vantagens**

* Extremamente testado
* Amplamente suportado
* Configuração simples via `cost`

**Indicado para:** sistemas que priorizam estabilidade e compatibilidade.

---

## pbkdf2_sha256 / pbkdf2_sha512

KDF padronizado pelo NIST.

**Vantagens**

* Padronizado
* Implementação disponível na biblioteca padrão do Python
* Ajuste via `iterations`

**Indicado para:** ambientes restritos ou requisitos corporativos.

---

## sha256_crypt / sha512_crypt

Extensão do `crypt()` tradicional usada em sistemas Unix/Linux.

**Vantagens**

* Compatível com `/etc/shadow`
* Suporte nativo via `crypt()` em sistemas Linux

**Indicado para:** integração com autenticação do sistema operacional.

---

# 📌 Resumo prático

| Algoritmo    | Melhor uso           |
| ------------ | -------------------- |
| Argon2       | Aplicações novas     |
| bcrypt       | Alta compatibilidade |
| PBKDF2       | Ambientes restritos  |
| sha512_crypt | Integração com Linux |

---