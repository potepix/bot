from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from src.database.models import db
import os

# Configurar caminhos absolutos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'src', 'web', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'src', 'web', 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
CORS(app)

# ==================== API Routes ====================

@app.route('/api/transacoes', methods=['GET'])
def get_all_transactions():
    """Retorna todas as transações"""
    status_filter = request.args.get('status')
    
    if status_filter:
        transacoes = db.obter_transacoes_por_status(status_filter)
    else:
        transacoes = db.obter_todas_transacoes()
    
    return jsonify(transacoes)

@app.route('/api/transacao/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """Obtém uma transação específica"""
    transacao = db.obter_transacao(transaction_id)
    
    if not transacao:
        return jsonify({'erro': 'Transação não encontrada'}), 404
    
    return jsonify(transacao)

@app.route('/api/transacao/<transaction_id>/aprovar', methods=['POST'])
def approve_transaction(transaction_id):
    """Aprova uma transação"""
    success = db.atualizar_status(transaction_id, 'aprovada')
    
    if not success:
        return jsonify({'erro': 'Erro ao aprovar transação'}), 400
    
    return jsonify({'mensagem': 'Transação aprovada com sucesso'})

@app.route('/api/transacao/<transaction_id>/recusar', methods=['POST'])
def reject_transaction(transaction_id):
    """Rejeita uma transação"""
    data = request.get_json()
    motivo = data.get('motivo', 'Sem motivo especificado') if data else 'Sem motivo especificado'
    
    success = db.atualizar_status(transaction_id, 'recusada', motivo)
    
    if not success:
        return jsonify({'erro': 'Erro ao recusar transação'}), 400
    
    return jsonify({'mensagem': 'Transação recusada com sucesso'})

@app.route('/api/transacao/<transaction_id>/processar', methods=['POST'])
def process_transaction(transaction_id):
    """Marca uma transação como em processamento"""
    success = db.atualizar_status(transaction_id, 'processando')
    
    if not success:
        return jsonify({'erro': 'Erro ao processar transação'}), 400
    
    return jsonify({'mensagem': 'Transação em processamento'})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Retorna estatísticas das transações"""
    todas = db.obter_todas_transacoes()
    
    # Calcular valor total apenas das transações aprovadas and processando
    approved = db.obter_transacoes_por_status('aprovada')
    processing = db.obter_transacoes_por_status('processando')
    total_valor = sum(t['valor'] for t in approved) + sum(t['valor'] for t in processing)
    
    pendentes = len(db.obter_transacoes_por_status('pendente'))
    processando = len(db.obter_transacoes_por_status('processando'))
    aprovadas = len(db.obter_transacoes_por_status('aprovada'))
    recusadas = len(db.obter_transacoes_por_status('recusada'))
    
    return jsonify({
        'total_transacoes': len(todas),
        'total_valor': total_valor,
        'pendentes': pendentes,
        'processando': processando,
        'aprovadas': aprovadas,
        'recusadas': recusadas
    })

# ==================== Web Routes ====================

@app.route('/')
def index():
    """Página principal do dashboard"""
    return render_template('index.html')

@app.route('/transacao/<transaction_id>')
def transaction_detail(transaction_id):
    """Página de detalhes de uma transação"""
    transacao = db.obter_transacao(transaction_id)
    
    if not transacao:
        return "Transação não encontrada", 404
    
    return render_template('transaction.html', transacao=transacao)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
