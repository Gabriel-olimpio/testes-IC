# Testes de Nivelamento da Intuitive Care

Os testes 1 e 2 se encontram na branch ```main```. Já o teste 4 está na outra branch do repositório, na qual se chama ``` test4```

# 📋 Testes 1 e 2 - IntuitiveCare

Repositório contendo as soluções para os Testes 1 (Web Scraping) e 2 (Transformação de Dados) do processo seletivo da IntuitiveCare.

## 🛠️ Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)
- Git (opcional)

## ⚙️ Configuração do Ambiente

### 1. Clone o repositório
```bash
git clone https://github.com/Gabriel-olimpio/testes-ic.git
cd Testes-Intuitive
```

### 2. Crie e ative um ambiente virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

## 📂 Estrutura do Projeto
```
/
├── teste1/              # Código do Teste 1 - Web Scraping
│   ├── teste_1.py         # Script principal
│   ├── anexos/          # PDFs baixados (gerado automaticamente)
│   
│
├── teste2/              # Código do Teste 2 - Transformação de Dados
│   ├── teste_2.py          # Script principal
│   ├── data/            # Arquivos CSV (gerados automaticamente)
│   
│
├── README.md            # Este arquivo
└── requirements.txt     # Dependências gerais
```

## 🚀 Como Executar

### Teste 1 - Web Scraping
```bash
python teste_1.py
```

**Saída esperada:**
- PDFs dos Anexos I e II baixados na pasta `anexos/`
- Arquivo `Teste_[Nome].zip` com os PDFs compactados

### Teste 2 - Transformação de Dados
```bash
python teste_2.py
```

**Saída esperada:**
- Arquivo `rol_procedimentos.csv` com os dados transformados
- Arquivo `Teste_[Nome].zip` com o CSV compactado

## 📦 Dependências

### Dependências Gerais (raiz do projeto)
- `pdfkit==1.0.0`
- `tabula-py==2.7.0`
- `beautifulsoup4==4.13.3`
- `pandas==2.2.3`
- `requests==2.32.3`
- `tabula-py==2.10.0`

