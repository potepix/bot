import sqlite3
import uuid
from datetime import datetime
from typing import Optional, List, Dict

class Database:
    def __init__(self, db_path: str = "payments.db"):
        self.db_path = db_path
        self.init_db()
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id TEXT PRIMARY KEY,
                valor REAL NOT NULL,
                chave_pix TEXT NOT NULL,
                status TEXT DEFAULT 'pendente',
                channel_id TEXT NOT NULL,
                usuario_id TEXT NOT NULL,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                motivo_rejeicao TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def criar_transacao(self, valor: float, chave_pix: str, channel_id: str, usuario_id: str) -> str:
        """Cria uma nova transação e retorna o ID"""
        transaction_id = str(uuid.uuid4())[:8]
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO transactions (id, valor, chave_pix, status, channel_id, usuario_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (transaction_id, valor, chave_pix, 'pendente', channel_id, usuario_id))
        
        conn.commit()
        conn.close()
        return transaction_id
    
    def obter_transacao(self, transaction_id: str) -> Optional[Dict]:
        """Obtém uma transação pelo ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None
    
    def obter_todas_transacoes(self) -> List[Dict]:
        """Obtém todas as transações"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM transactions ORDER BY data_criacao DESC')
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def obter_transacoes_por_status(self, status: str) -> List[Dict]:
        """Obtém transações por status"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM transactions WHERE status = ? ORDER BY data_criacao DESC', (status,))
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def atualizar_status(self, transaction_id: str, novo_status: str, motivo_rejeicao: str = None) -> bool:
        """Atualiza o status de uma transação"""
        if novo_status not in ['pendente', 'aprovada', 'recusada', 'processando']:
            return False
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE transactions 
            SET status = ?, motivo_rejeicao = ?, data_atualizacao = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (novo_status, motivo_rejeicao, transaction_id))
        
        conn.commit()
        conn.close()
        return True

# Instância global do banco de dados
db = Database()
