# 🚀 Deploy no Railway

Railway é a melhor opção para hospedar bots Discord. Aqui está como fazer:

## ✅ Passo 1: Criar Conta

1. Acesse: https://railway.app
2. Clique em "Sign Up"
3. Faça login com GitHub (recomendado)

## ✅ Passo 2: Conectar Repositório GitHub

1. Clique em "New Project"
2. Selecione "Deploy from GitHub"
3. Autorize Railway a acessar seus repositórios
4. Selecione o repositório `potepix/bot`

## ✅ Passo 3: Configurar Variáveis de Ambiente

1. Na aba "Variables", clique em "Add Variable"
2. Adicione:

```
DISCORD_TOKEN=seu_token_aqui
PIX_KEY=sua_chave_pix_aqui
FLASK_HOST=0.0.0.0
FLASK_PORT=8080
FLASK_DEBUG=False
DB_PATH=/tmp/payments.db
```

⚠️ Importante: Use `/tmp/payments.db` no Railway (não use `payments.db`)

## ✅ Passo 4: Deploy

Railway fará o deploy automaticamente quando você:
1. Fizer um push para GitHub em `main`
2. Ou clicar no botão "Deploy" manualmente

---

## 📊 URLs de Acesso:

Após deploy, Railway fornecerá:
- **Bot Discord:** Rodando 24/7  ✅
- **Dashboard Web:** `https://seu-projeto.up.railway.app`
- **API:** `https://seu-projeto.up.railway.app/api/...`

---

## 🎯 Próximos Passos:

1. Crie conta em https://railway.app
2. Conecte GitHub
3. Configure as variáveis (DISCORD_TOKEN)
4. Clique "Deploy"
5. Pronto! Bot rodando 24/7

---

## 💡 Dicas:

- Railway é **grátis** com $5/mês de créditos
- Você só usa créditos quando usar recursos (CPU, memória)
- Para bots simples como esse, é praticamente FREE
- O bot fica 24/7 online (diferente de localhost)

---

## 📞 Problemas?

Se der erro, verifique:
1. `DISCORD_TOKEN` configurado corretamente
2. `Procfile` existe e está na raiz
3. `requirements.txt` tem todas as dependências
4. Seu repositório está public ou você tem acesso

---

**Pronto! Seu bot vai ficar ONLINE 24/7!** 🎉
