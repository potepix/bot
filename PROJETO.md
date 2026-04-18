# 📋 Resumo do Projeto - Bot de Vendas PIX

## ✅ O que foi Criado

### 🤖 Bot Discord
- **`/pix`** - Cria transação com valor
  - Pede valor via interact interativo
  - Gera chave PIX formatada
  - Gera ID único para rastreamento
  - Envia embed com informações
  
- **`/status [ID]`** - Consulta status da transação
  - Mostra status com emojis
  - Exibe valor e datas
  - Mostra motivo se recusada

### 🌐 API Flask + Dashboard Web

**Endpoints da API:**
```
GET  /api/transacoes                    → Todas transações
GET  /api/transacoes?status=pendente    → Filtrar por status
GET  /api/transacao/<id>                → Detalhes de uma
GET  /api/stats                         → Estatísticas
POST /api/transacao/<id>/processar      → Marcar processando
POST /api/transacao/<id>/aprovar        → Aprovar
POST /api/transacao/<id>/recusar        → Rejeitar com motivo
```

**Dashboard Web (http://localhost:5000):**
- 📊 Cards de estatísticas (atualizam a cada 5s)
- 📋 Tabela de transações com busca por status
- ✅ Botão para aprovar
- ❌ Botão para rejeitar (com motivo)
- ⏳ Botão para processar
- 👁️ Ver detalhes em modal

### 💾 Banco de Dados SQLite

Estrutura da tabela:
```sql
CREATE TABLE transactions (
    id TEXT PRIMARY KEY,                  -- ID único (ex: a1b2c3d4)
    valor REAL NOT NULL,                  -- Valor em reais
    chave_pix TEXT NOT NULL,              -- Chave PIX QR Code
    status TEXT DEFAULT 'pendente',       -- pendente/processando/aprovada/recusada
    channel_id TEXT NOT NULL,             -- ID do canal Discord
    usuario_id TEXT NOT NULL,             -- ID do vendedor
    data_criacao TIMESTAMP,               -- Data/hora criação
    data_atualizacao TIMESTAMP,           -- Data/hora última atualização
    motivo_rejeicao TEXT                  -- Motivo da rejeição
)
```

### 📁 Estrutura de Arquivos

```
bot/
├── main.py                              # Launcher principal
├── config.py                            # Configurações
├── requirements.txt                     # Dependências Python
├── test.py                              # Script de teste
├── .env                                 # Variáveis (seu token)
├── .env.example                         # Template .env
├── .gitignore                           # Arquivos ignorados
├── payments.db                          # Banco SQLite (auto-criado)
│
├── README.md                            # Documentação principal
├── SETUP.md                             # Guia de setup
│
└── src/
    ├── __init__.py
    │
    ├── bot/
    │   ├── __init__.py
    │   └── discord_bot.py               # Lógica do bot Discord
    │
    ├── api/
    │   ├── __init__.py
    │   └── app.py                       # API Flask + rotas
    │
    ├── database/
    │   ├── __init__.py
    │   └── models.py                    # ORM SQLite
    │
    └── web/
        ├── __init__.py
        ├── templates/
        │   ├── index.html               # Dashboard principal
        │   └── transaction.html         # Página de detalhes
        │
        └── static/
            ├── style.css                # Estilos (responsivo)
            └── script.js                # Lógica do dashboard
```

---

## 🔧 Configuração Necessária

### 1. Token Discord
- [ ] Regenerar em: https://discord.com/developers/applications
- [ ] Colar em `.env` -> `DISCORD_TOKEN=`

### 2. Bot no Servidor
- [ ] OAuth2 URL Generator
- [ ] Scopes: `bot`, `applications.commands`
- [ ] Permissions: Send Messages, Read History, Embed Links
- [ ] Abrir URL de convite no navegador

### 3. Iniciar
```bash
python main.py
```

---

## 🚀 Como Usar

### Via Discord

**Criar Pagamento:**
```
Vendedor: /pix
Bot: "💰 Qual é o valor da venda?"
Vendedor: 150.00
Bot: 
  💳 PIX Gerado
  Transação ID: `a1b2c3d4`
  💰 Valor: R$ 150,00
  🔑 Chave PIX: [código QR]
  ID: a1b2c3d4
```

**Consultar Status:**
```
Vendedor: /status a1b2c3d4
Bot: Mostra status atual
```

### Via Dashboard Web

1. Abra http://localhost:5000
2. Veja estatísticas em tempo real
3. Para cada transação:
   - 👁️ Ver detalhes
   - ⏳ Processar (para análise)
   - ✅ Aprovar
   - ❌ Recusar (com motivo)

---

## 📊 Fluxo de uma Transação

```
1. Vendedor usa /pix
   ↓
2. Bot cria transação (status: pendente)
   ↓
3. Bot gera chave PIX com valor
   ↓
4. Cliente copia chave e paga no banco
   ↓
5. Vendedor vê no Discord ou Dashboard
   ↓
6. Vendedor aprova/rejeita no Dashboard
   ↓
7. Status atualiza em tempo real
   ↓
8. Bot mostra novo status no /status
```

---

## 🔐 Segurança

✅ Token protegido em `.env`
✅ `.gitignore` impede commits de arquivos sensíveis
✅ Banco local (sem nuvem)
✅ Validações de entrada
✅ CORS apenas para localhost

---

## 📦 Dependências Instaladas

- `discord.py==2.3.2` → Bot Discord
- `flask==3.0.0` → API Web
- `flask-cors==4.0.0` → CORS
- `python-dotenv==1.0.0` → Variáveis de ambiente

---

## 🎯 Próximas Melhorias Possíveis

- [ ] Autenticação para dashboard (login)
- [ ] Notificações por email
- [ ] API de integração com sistemas externos
- [ ] Webhook para confirmação automática
- [ ] Exportar relatório (PDF/Excel)
- [ ] Histórico de ações (log)
- [ ] Dark mode no dashboard

---

## 📞 Suporte

Se tiver problemas:
1. Rodar `python test.py` para diagnosticar
2. Verificar logs do terminal
3. Consultar [SETUP.md](SETUP.md) e [README.md](README.md)

---

**Status: ✅ PRONTO PARA USO**

*Desenvolvido com ❤️*
