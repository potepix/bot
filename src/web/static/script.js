let filtroAtual = 'todas';

// Carregar dados ao abrir a página
document.addEventListener('DOMContentLoaded', function() {
    carregarDados();
    // Atualizar a cada 5 segundos
    setInterval(carregarDados, 5000);
});

async function carregarDados() {
    try {
        // Carregar estatísticas
        const statsRes = await fetch('/api/stats');
        const stats = await statsRes.json();
        
        document.getElementById('total-transacoes').textContent = stats.total_transacoes;
        document.getElementById('pendentes-count').textContent = stats.pendentes;
        document.getElementById('processando-count').textContent = stats.processando;
        document.getElementById('aprovadas-count').textContent = stats.aprovadas;
        document.getElementById('recusadas-count').textContent = stats.recusadas;
        document.getElementById('valor-total').textContent = `R$ ${stats.total_valor.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
        
        // Carregar transações
        let url = '/api/transacoes';
        if (filtroAtual !== 'todas') {
            url += `?status=${filtroAtual}`;
        }
        
        const transRes = await fetch(url);
        const transacoes = await transRes.json();
        
        renderizarTabela(transacoes);
    } catch (error) {
        console.error('Erro ao carregar dados:', error);
        document.getElementById('transactions-tbody').innerHTML = `
            <tr>
                <td colspan="5" class="loading">❌ Erro ao carregar dados</td>
            </tr>
        `;
    }
}

function renderizarTabela(transacoes) {
    const tbody = document.getElementById('transactions-tbody');
    
    if (transacoes.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="5" class="loading">Nenhuma transação encontrada</td>
            </tr>
        `;
        return;
    }
    
    tbody.innerHTML = transacoes.map(t => `
        <tr>
            <td><code>${t.id}</code></td>
            <td>R$ ${t.valor.toLocaleString('pt-BR', {minimumFractionDigits: 2})}</td>
            <td><span class="status-badge status-${t.status}">${getStatusEmoji(t.status)} ${getStatusText(t.status)}</span></td>
            <td>${new Date(t.data_criacao).toLocaleString('pt-BR')}</td>
            <td>
                <div class="actions">
                    <button class="btn-action btn-detalhes" onclick="abrirModal('${t.id}')">👁️ Ver</button>
                    ${t.status === 'pendente' ? `
                        <button class="btn-action btn-processar" onclick="processarTransacao('${t.id}')">⏳</button>
                        <button class="btn-action btn-aprovar" onclick="aprovarTransacao('${t.id}')">✅</button>
                        <button class="btn-action btn-recusar" onclick="mostrarRecusoModal('${t.id}')">❌</button>
                    ` : ''}
                    ${t.status === 'processando' ? `
                        <button class="btn-action btn-aprovar" onclick="aprovarTransacao('${t.id}')">✅</button>
                        <button class="btn-action btn-recusar" onclick="mostrarRecusoModal('${t.id}')">❌</button>
                    ` : ''}
                </div>
            </td>
        </tr>
    `).join('');
}

function getStatusEmoji(status) {
    const emojis = {
        'pendente': '🟡',
        'processando': '⏳',
        'aprovada': '✅',
        'recusada': '❌'
    };
    return emojis[status] || '❓';
}

function getStatusText(status) {
    const textos = {
        'pendente': 'Pendente',
        'processando': 'Processando',
        'aprovada': 'Aprovada',
        'recusada': 'Recusada'
    };
    return textos[status] || 'Desconhecido';
}

function filtrar(status) {
    filtroAtual = status;
    
    // Atualizar botões ativos
    document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    carregarDados();
}

async function abrirModal(transactionId) {
    try {
        const res = await fetch(`/api/transacao/${transactionId}`);
        const transacao = await res.json();
        
        const modalBody = document.getElementById('modal-body');
        const statusEmoji = getStatusEmoji(transacao.status);
        
        modalBody.innerHTML = `
            <h2>${statusEmoji} ${getStatusText(transacao.status)}</h2>
            <div class="modal-info">
                <p><strong>ID:</strong> <code>${transacao.id}</code></p>
                <p><strong>Valor:</strong> <span class="valor">R$ ${transacao.valor.toLocaleString('pt-BR', {minimumFractionDigits: 2})}</span></p>
                <p><strong>Data:</strong> ${new Date(transacao.data_criacao).toLocaleString('pt-BR')}</p>
                <p><strong>Chave PIX:</strong></p>
                <div class="pix-key">${transacao.chave_pix}</div>
                ${transacao.motivo_rejeicao ? `<p><strong>Motivo da Rejeição:</strong> ${transacao.motivo_rejeicao}</p>` : ''}
            </div>
            <div class="modal-buttons">
                ${transacao.status === 'pendente' ? `
                    <button class="btn-action btn-processar" onclick="processarTransacao('${transacao.id}'); fecharModal()">⏳ Processar</button>
                    <button class="btn-action btn-aprovar" onclick="aprovarTransacao('${transacao.id}'); fecharModal()">✅ Aprovar</button>
                    <button class="btn-action btn-recusar" onclick="mostrarRecusoModal('${transacao.id}')">❌ Recusar</button>
                ` : ''}
                ${transacao.status === 'processando' ? `
                    <button class="btn-action btn-aprovar" onclick="aprovarTransacao('${transacao.id}'); fecharModal()">✅ Aprovar</button>
                    <button class="btn-action btn-recusar" onclick="mostrarRecusoModal('${transacao.id}')">❌ Recusar</button>
                ` : ''}
                <button class="btn-action btn-fechar" onclick="fecharModal()">Fechar</button>
            </div>
        `;
        
        document.getElementById('modal').style.display = 'block';
    } catch (error) {
        alert('Erro ao carregar transação');
        console.error(error);
    }
}

function fecharModal() {
    document.getElementById('modal').style.display = 'none';
}

async function aprovarTransacao(transactionId) {
    if (!confirm('Tem certeza que deseja aprovar esta transação?')) return;
    
    try {
        const res = await fetch(`/api/transacao/${transactionId}/aprovar`, {
            method: 'POST'
        });
        
        if (res.ok) {
            alert('✅ Transação aprovada com sucesso!');
            carregarDados();
        } else {
            alert('❌ Erro ao aprovar transação');
        }
    } catch (error) {
        alert('❌ Erro ao aprovar transação');
        console.error(error);
    }
}

async function processarTransacao(transactionId) {
    if (!confirm('Marcar como em processamento?')) return;
    
    try {
        const res = await fetch(`/api/transacao/${transactionId}/processar`, {
            method: 'POST'
        });
        
        if (res.ok) {
            alert('⏳ Transação marcada como processando!');
            carregarDados();
        } else {
            alert('❌ Erro ao processar transação');
        }
    } catch (error) {
        alert('❌ Erro ao processar transação');
        console.error(error);
    }
}

function mostrarRecusoModal(transactionId) {
    const motivo = prompt('Digite o motivo da rejeição:');
    
    if (motivo === null) return; // Cancelou
    
    if (motivo.trim() === '') {
        alert('❌ Por favor, digite um motivo');
        return;
    }
    
    recusarTransacao(transactionId, motivo);
}

async function recusarTransacao(transactionId, motivo) {
    try {
        const res = await fetch(`/api/transacao/${transactionId}/recusar`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ motivo: motivo })
        });
        
        if (res.ok) {
            alert('❌ Transação recusada com sucesso!');
            fecharModal();
            carregarDados();
        } else {
            alert('❌ Erro ao recusar transação');
        }
    } catch (error) {
        alert('❌ Erro ao recusar transação');
        console.error(error);
    }
}

// Fechar modal ao clicar fora
window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
