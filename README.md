# 🚀 Plano de Execução do Pipeline de Engenharia de Dados

## 🎯 Objetivos do Desafio
1. **Consumir Dados**
   - Realizar uma requisição à API do TRE-RJ para obter a lista de todos os locais de votação.

2. **Armazenar Dados em MongoDB**
   - Armazenar os dados recebidos em um banco de dados MongoDB, mantendo a estrutura semi-estruturada.

3. **Transformação de Dados**
   - Realizar transformações nos dados armazenados para normalizar e limpar informações, como:
     - Remover duplicatas.
     - Padronizar nomes de municípios.
     - Extrair e separar informações relevantes de endereços.

4. **Armazenar Dados em MySQL**
   - Após a transformação, salvar os dados em um banco de dados MySQL em uma tabela estruturada.
   - Definir os tipos de dados adequados para cada coluna, considerando a estrutura dos dados.

5. **Análise e Relatórios**
   - Criar relatórios básicos que mostrem:
     - O número total de locais de votação por município.
     - A distribuição dos locais de votação em relação a áreas urbanas e rurais.
     - Quais municípios têm o maior número de locais de votação.

6. **Automatização do Pipeline**
   - Descrever como automatizar o processo de coleta e transformação de dados, garantindo que os dados sejam atualizados periodicamente.

7. **Documentação e Apresentação**
   - Preparar uma documentação clara e concisa do pipeline desenvolvido, incluindo:
     - Descrição das etapas realizadas.
     - Decisões tomadas durante o desenvolvimento.
     - Possíveis melhorias e extensões para o futuro.

---

## 🛠 Etapas do Pipeline

### 1️⃣ Coleta de Dados
- Fazer requisição para a API do TRE-RJ e obter os dados dos locais de votação.
- Utilizar `requests` (Python) para consumir a API e salvar os dados brutos em MongoDB.

### 2️⃣ Armazenamento em MongoDB
- Criar uma coleção no MongoDB para armazenar os dados brutos, mantendo a estrutura original.
- Inserir os dados utilizando `pymongo`.

### 3️⃣ Transformação e Normalização
- Remover duplicatas (usando índices no MongoDB ou scripts de limpeza).
- Padronizar nomes dos municípios (exemplo: acentos, maiúsculas/minúsculas).
- Separar informações de endereço (rua, número, bairro, etc.).

### 4️⃣ Armazenamento em MySQL
- Criar tabelas normalizadas no MySQL.
- Inserir os dados transformados no MySQL utilizando `sqlalchemy`.

### 5️⃣ Análise e Relatórios
- Criar consultas SQL para relatórios básicos:
  - Número total de locais de votação por município.
  - Distribuição por área urbana/rural.
  - Municípios com maior número de locais de votação.

### 6️⃣ Automatização do Pipeline
- Criar um script Python para executar todo o processo periodicamente.
- Usar `cron` (Linux) ou `Airflow` para agendar a execução.

### 7️⃣ Documentação
- Explicar cada etapa do pipeline e tecnologias utilizadas.
- Apontar melhorias futuras, como integração com ferramentas de BI (Power BI, Metabase, etc.).

---
