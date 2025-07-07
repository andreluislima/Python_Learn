# 💳 Sistema Bancário: SantANDRÉ - V2

> Desafio da **DIO** focado na refatoração e expansão de um sistema bancário com boas práticas em funções, estruturação e cadastro de usuários e contas.

## ✅ Requisitos do Projeto

### 📌 Refatorar funções existentes

As funções de **saque**, **depósito** e **extrato** devem ser extraídas em funções separadas com as seguintes regras:

---

#### 💸 Saque

- **Chamada por nome apenas** (keyword-only).
- **Parâmetros sugeridos**:
  - `*, saldo, valor, extrato, limite, numero_saques, limite_saques`
- **Retorno sugerido**:
  - `saldo` atualizado e `extrato` atualizado

---

#### 💰 Depósito

- **Chamada por posição apenas** (positional-only).
- **Parâmetros sugeridos**:
  - `/ saldo, valor, extrato`
- **Retorno sugerido**:
  - `saldo` atualizado e `extrato` atualizado

---

#### 📄 Extrato

- Deve aceitar:
  - **Argumentos posicionais**: `saldo`
  - **Argumentos nomeados**: `*, extrato`

---

### 👤 Criar Usuário (Cliente)

- Os usuários devem ser armazenados em uma lista.
- Cada usuário deve conter:
  - `nome`
  - `data de nascimento`
  - `cpf` (apenas números)
  - `endereço` no formato: `logradouro, número - bairro - cidade - UF`
- **Regra de negócio**:
  - Não pode haver dois usuários com o mesmo CPF

---

### 🏦 Criar Conta Corrente

- As contas também devem ser armazenadas em uma lista.
- Cada conta deve conter:
  - `agência` (sempre `"0001"`)
  - `número da conta` (sequencial, começando em 1)
  - `usuário` (vinculado a um CPF existente na lista de usuários)
- **Um usuário pode ter mais de uma conta, mas cada conta pertence a um único usuário.**

---

### 🧠 Dica

Para vincular um usuário a uma conta:
> Filtre a lista de usuários pelo CPF informado no momento da criação da conta.

---

## 💡 Possíveis Extensões

Você pode adicionar funcionalidades como:
- Listar contas cadastradas
- Buscar usuário por CPF
- Relatórios de movimentação
- Interface com menu interativo

---

## 📞 Contato

**André Lima**  
📧 andreluislima@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/andreluislima89)  
💻 [GitHub](https://github.com/andreluislima)
