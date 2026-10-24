import requests
import json

# ==========================================
# DESAFIO DIO - RPA COM N8N E PYTHON
# ==========================================

# 1. URL do Webhook gerada no n8n (Método POST)
# Substitua pela sua Test URL ou Production URL
WEBHOOK_URL = "COLE_A_SUA_URL_DO_WEBHOOK_AQUI"

# 2. Dados dinâmicos do mercado financeiro para o portfólio do cliente
dados_mercado = {
    "ativo": "PETR4",
    "preco_atual": "38.50",
    "tendencia_percentual": "+2.5% (Alta volatilidade positiva)",
    "perfil_investidor": "Moderado",
    "email_cliente": "seu_email_de_teste@gmail.com" 
}

def disparar_fluxo_n8n():
    print("Iniciando comunicação com o webhook do n8n...")
    
    try:
        # 3. Disparo da requisição HTTP POST injetando os dados no n8n
        response = requests.post(WEBHOOK_URL, json=dados_mercado)
        
        # 4. Validação da resposta
        if response.status_code == 200:
            print("✅ Sucesso! Os dados foram injetados no fluxo de RPA.")
            print("Resposta do servidor n8n:", response.text)
        else:
            print(f"⚠️ Erro ao comunicar. Código de status: {response.status_code}")
            print("Detalhes:", response.text)
            
    except Exception as e:
        print(f"❌ Erro na execução do script: {e}")

if __name__ == "__main__":
    disparar_fluxo_n8n()
