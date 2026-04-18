# 💰 Bot de Vendas com PIX

Um bot Discord combinado com uma API web para gerenciar pagamentos via PIX. O vendedor cria transações via `/pix` e confirma/rejeita via dashboard web.

---

## 🚀 Funcionalidades

### 🤖 Bot Discord
- **`/pix`** - Cria transação com valor enviando chave PIX
- **`/status [ID]`** - Consulta status do pagamento em tempo real

### 🌐 Dashboard Web (http://localhost:5000)
- 📊 Estatísticas de transações
- 📋 Tabela com todos os pagamentos
- ✅ Aprovar pagamentos
- ❌ Rejeitar com motivo
- ⏳ Marcar como em processamento
- 🔄 Auto-atualização a cada 5 segundos

### 💾 Banco de Dados
- SQLite com histórico completo
- Rastreamento de datas e motivos

---

## ⚙️ Instalação

### 1️⃣ Pré-requisitos
- Python 3.8+
- pip

### 2️⃣ Clonar o Repositório
```bash
cd /workspaces/bot
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Discord Bot

#### Criar o Bot:
1. Acesse [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em "New Application"
3. Dê um nome (ex: "Bot Vendas PIX")
4. Vá na aba "Bot" → "Add Bot"
5. Em "TOKEN", clique em "Copy" para copiar o token
6. Clique em "Reset Token" para gerar um novo (segurança)

#### Coletar Permissões:
1. Em "Bot" → "OAuth2 URL Generator"
2. Scopes: `bot`
3. Permissions: 
   - `Send Messages`
   - `Read Message History`
   - `Use Slash Commands`
4. Copie a URL gerada e abra no navegador para adicionar o bot ao seu servidor

### 5️⃣ Configurar Variáveis de Ambiente

Abra o arquivo `.env` e preencha:
```env
DISCORD_TOKEN=seu_token_aqui
PIX_KEY=sua_chave_pix_aqui
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=True
DB_PATH=payments.db
```

---

## ▶️ Iniciar a Aplicação

Execute no terminal:
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
🤖 Iniciando Bot Discord...
🌐 Iniciando API Web...

✅ Sistema iniciado!
📊 Dashboard: http://localhost:5000
🤖 Bot Discord: Conectado ao Discord

Pressione Ctrl+C para parar
```

---

## 📖 Como Usar

### No Discord:

#### 1. Criar Pagamento
```
/pix
→ Bot pergunta: "💰 Qual é o valor da venda?"
→ Você responde: "150.00"
→ Bot envia:
   💳 PIX Gerado
   Transação ID: `a1b2c3d4`
   💰 Valor: R$ 150,00
   🔑 Chave PIX: [chave]
   ID: a1b2c3d4
```

#### 2. Verificar Status
```
/status a1b2c3d4
→ Bot mostra o status atual da transação
```

### No Dashboard Web:

1. Abra http://localhost:5000
2. Veja estatísticas em tempo real
3. Use os botões para cada transação:
   - 👁️ **Ver** - Detalhes completos
   - ⏳ **Processar** - Marcar como em análise
   - ✅ **Aprovar** - Confirmar pagamento
   - ❌ **Recusar** - Rejeitar com motivo
4. Filtros: Todas, Pendentes, Processando, Aprovadas, Recusadas

---

## 📂 Estrutura do Projeto

```
bot/
├── main.py                      # Launcher (Bot + API)
├── config.py                    # Configurações
├── requirements.txt             # Dependências
├── .env                         # Variáveis (não commitar)
├── .env.example                 # Template do .env
├── .gitignore                   # Git ignore
├── payments.db                  # Banco SQLite (auto-criado)
│
└── src/
    ├── bot/
    │   └── discord_bot.py       # Bot Discord com /pix e /status
    │
    ├── api/
    │   └── app.py               # API Flask (endpoints)
    │
    ├── database/
    │   └── models.py            # Modelos SQL + operações
    │
    └── web/
        ├── templates/
        │   ├── index.html        # Dashboard principal
        │   └── transaction.html   # Detalhes da transação
        │
        └── static/
            ├── style.css         # Estilos (gradientes, responsivo)
            └── script.js         # Lógica do dashboard
```

---

## 🔐 Segurança

✅ Token do Discord em `.env` (protegido por `.gitignore`)
✅ Banco de dados local (sem uploads)
✅ CORS habilitado apenas para localhost
✅ Validações de entrada

---

## 🛠️ Troubleshooting

### "DISCORD_TOKEN não configurado"
→ Adicione o token regenerado ao arquivo `.env`

### "Porta 5000 já em uso"
→ Mude em `.env`: `FLASK_PORT=5001`

### "Banco de dados corrompido"
→ Delete `payments.db` e reinicie (irá recriar)

### Bot não responde aos comandos
→ Verifique se o bot tem permissão no servidor
→ Verifique se o token é válido

---

## 📝 API Endpoints

```
GET  /api/transacoes                    # Todas as transações
GET  /api/transacoes?status=pendente    # Filtrar por status
GET  /api/transacao/<id>                # Detalhes de uma
GET  /api/stats                         # Estatísticas
POST /api/transacao/<id>/processar      # Marcar processando
POST /api/transacao/<id>/aprovar        # Aprovar
POST /api/transacao/<id>/recusar        # Rejeitar
```

---

## 📞 Suporte

Qualquer dúvida, verifique:
1. Logs do terminal
2. Console do navegador (F12)
3. Permissões do servidor Discord

---

**Desenvolvido com ❤️**
