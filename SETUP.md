# 🚀 Guia de Setup - Bot de Vendas PIX

## ⚠️ IMPORTANTE: Regenere seu Token Discord!

Você compartilhou um token de bot Discord **em texto plano**! Este foi **INVALIDADO por segurança**. Você precisa gerar um novo token.

---

## 📋 Passos para Gerar um Novo Token

### 1️⃣ Acesse o Discord Developer Portal
- Abra: https://discord.com/developers/applications
- Faça login com sua conta Discord

### 2️⃣ Encontre seu Bot ou Crie um Novo
- Se já existe "Bot Vendas PIX", clique nele
- Caso contrário, clique em "New Application" e nomeie como "Bot Vendas PIX"

### 3️⃣ Regenerar o Token
- Na aba **"Bot"** (lado esquerdo), localize a seção **"TOKEN"**
- Clique no botão **"Reset Token"** (ícone de 🔄)
- Confirme que deseja regenerar
- Clique em **"Copy"** para copiar o novo token

### 4️⃣ Adicionar o Token ao `.env`
- Abra o arquivo `.env` na raiz do projeto `/workspaces/bot/.env`
- Procure por `DISCORD_TOKEN=`
- Cole o token copiado após o `=`:

```env
DISCORD_TOKEN=MTQ5NDgxMjUwMDQzOTQ3MDI4MQ.GsJWDo.O0Ru1W0sHs59hf_45NoFZBzakf9kG_7dUQI4N8
```

exemplo real (não use este!):
```env
DISCORD_TOKEN=MjE2NDkwMjU1NjU4OTcyMjI0.CHjZ3g.wHJo1qoD85Ud7_Q6dQaOK8Fw4v4
```

- Salve o arquivo

---

## 🤖 Configurar Permissões do Bot

### 1️⃣ Gerar URL de Convite
- Ainda em "Bot", vá para **"OAuth2 URL Generator"** (side bar esquerdo)

### 2️⃣ Selecionar Scopes e Permissões
- Em **"Scopes"**, marque:
  - ✅ `bot`
  - ✅ `applications.commands`

- Em **"Permissions"**, marque:
  - ✅ `Send Messages`
  - ✅ `Read Message History`
  - ✅ `Embed Links`
  - ✅ `Mention Everyone`

### 3️⃣ Copiar e Abrir URL
- Copie a URL gerada pelo gerador
- Abra a URL em um navegador
- Selecione o servidor Discord onde deseja adicionar o bot
- Clique em "Autorizar"

---

## ✅ Testar a Configuração

Depois de colocar o token no `.env`, execute:

```bash
python test.py
```

Você verá:
```
✅ discord.py OK
✅ Flask OK
✅ python-dotenv OK
✅ Todas as importações OK
✅ Banco de dados OK
✅ Bot Discord OK
✅ API Flask OK
✅ TUDO OK! Você pode executar: python main.py
```

---

## 🎯 Iniciar o Bot

Quando tudo estiver configurado:

```bash
python main.py
```

Você verá:
```
╔════════════════════════════════════════╗
║  💰 BOT DE VENDAS COM PIX 💰          ║
║  Discord Bot + Web Dashboard           ║
╚════════════════════════════════════════╝

🚀 Iniciando aplicação...

✅ Sistema iniciado!
📊 Dashboard: http://localhost:5000
🤖 Bot Discord: Conectado ao Discord

Pressione Ctrl+C para parar
```

---

## 🌐 Acessar o Dashboard

Abra seu navegador e vá para: **http://localhost:5000**

Você verá:
- Estatísticas em tempo real
- Tabela de transações
- Botões para aprovar/rejeitar pagamentos

---

## 🤖 Usar no Discord

### Criar Transação
```
/pix
```
O bot pedirá o valor, você responde, e ele gera uma chave PIX com ID.

### Verificar Status
```
/status [ID da transação]
```

---

## ❌ Troubleshooting

### "DISCORD_TOKEN não está configurado"
→ Certifique-se de que preencheu o `.env` corretamente

### "Bot não aparece no servidor"
→ Verifique se autorizado o bot no link de convite
→ Verifique se o bot tem permissões no servidor

### "Erro de conexão"
→ Verifique sua conexão de internet
→ Verifique se o token é válido

### "Porta 5000 em uso"
→ Mude em `.env`: `FLASK_PORT=5001`

---

## 🔒 Segurança

✅ **Nunca compartilhe seu token de bot**
✅ **Mantenha `.env` no `.gitignore`** (já está configurado)
✅ **Regenere o token se vazar** (já fez isso!)

---

## 📚 Próximos Passos

1. ✅ Regenerar token
2. ✅ Preencher `.env`
3. ✅ Rodar `python test.py`
4. ✅ Adicionar bot ao servidor
5. ✅ Rodar `python main.py`
6. ✅ Acessar http://localhost:5000

**Pronto! Seu bot está pronto para usar!** 🎉

---

*Qualquer dúvida, verifique o [README.md](README.md)*
