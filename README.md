# 🚀 Assistente de Investimentos Automatizado (RPA com n8n e Python)

Este repositório contém o projeto final (MVP) do desafio **"Criando um Processo de RPA com N8N e Python"**, do bootcamp Santander 2026 - Automação com N8N da [DIO](https://www.dio.me/).

## 📌 Visão Geral do Projeto
O projeto consiste em um fluxo de RPA (Robotic Process Automation) que integra um script em Python, a orquestração no n8n e a Inteligência Artificial (OpenAI) para gerar e disparar briefings diários de investimentos personalizados.

### 🛠️ Tecnologias Utilizadas
- **Python:** Coleta de dados financeiros simulados e acionamento do fluxo via Webhook HTTP.
- **n8n:** Plataforma de orquestração do workflow.
- **OpenAI (ChatGPT):** Análise do cenário financeiro e redação do e-mail com base no perfil do investidor (via Advanced AI Nodes).
- **Google Docs:** Registro do histórico de execuções para fins de auditoria/compliance.
- **Gmail API:** Disparo automatizado do relatório gerado para o cliente final.

## 📂 Estrutura do Repositório
- `script_rpa.py`: Script desenvolvido em Python (com a biblioteca `requests`) para integrar o sistema externo ao Webhook do n8n.
- `workflow_n8n.json`: O pipeline completo estruturado no n8n exportado. *(Lembre-se de subir o seu arquivo exportado para o repositório)*
- `README.md`: Documentação do projeto.

## 🚀 Como Executar o Projeto
1. Importe o arquivo `workflow_n8n.json` na sua instância local ou cloud do n8n.
2. Configure suas credenciais (OAuth2) para o **Gmail** e **Google Docs**, além da API Key da **OpenAI**.
3. Certifique-se de que o nó inicial do n8n é um **Webhook** (Método POST) e copie a URL de Teste/Produção.
4. No arquivo `script_rpa.py`, insira a URL do Webhook na variável `WEBHOOK_URL`.
5. Execute o script Python (`python script_rpa.py`) para disparar a automação.

## 📜 Requisitos Atendidos no Desafio (Desafio Completo)
- [x] Repositório estruturado.
- [x] Workflow N8N exportado.
- [x] Script de RPA integrado ao Webhook do N8N.
- [x] Integração com Agente de IA no n8n.
- [x] Mensagens (e-mails) geradas dinamicamente com base nos dados e salvas no Docs.
