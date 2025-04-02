# Teste 4: Busca de Operadoras com Flask e Vue.js

Este projeto é uma aplicação web que permite a busca de operadoras a partir de um arquivo CSV, utilizando um backend em Flask e um frontend em Vue.js.

## 📌 Tecnologias Utilizadas
- **Backend:** Flask (Python)
- **Frontend:** Vue.js com Vite
- **Dados:** CSV processado com Pandas
- **Requisições HTTP:** Axios
---

## 🚀 Como Rodar o Projeto

### 1️⃣ Clonar o Repositório
```bash
    git clone https://github.com/Gabriel-olimpio/testes-IC.git
    cd Testes_Intuitive
```

### 2️⃣ Configurar o Backend (Flask)
#### Criar e ativar um ambiente virtual:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

#### Instalar as dependências:
```bash
pip install -r requirements.txt
```

#### Executar o backend:
```bash
python app.py
```
O servidor Flask rodará em `http://127.0.0.1:5000/`.

### 3️⃣ Configurar o Frontend (Vue.js)
#### Instalar as dependências:
```bash
cd ../frontend
npm install
```

#### Rodar o frontend:
```bash
npm run dev
```
O frontend rodará em `http://localhost:5173/`.

---

## 🔥 Testando a API com Postman
1. Importe a coleção do Postman (`Teste API Flask - Operadoras.postman_collection.json`)
2. Utilize a rota:
   ```bash
   GET http://127.0.0.1:5000/buscar?termo=exemplo
   ```

---