# **8 Rainhas - Algoritmos de Busca**

Este projeto implementa o **problema das 8 Rainhas**, utilizando algoritmos de busca como **Busca em Profundidade (DFS)** e **Subida de Encosta** em uma aplicação **Django**. A interface permite visualizar o tabuleiro e navegar entre as soluções geradas.

---

## **Pré-requisitos**

Antes de executar o projeto, certifique-se de ter os seguintes componentes instalados na sua máquina:

1. **Python** (versão 3.7 ou superior):  
   - Verifique se está instalado:  
     ```bash
     python --version
     ```

2. **Pip** (gerenciador de pacotes do Python):  
   - Verifique se está instalado:  
     ```bash
     pip --version
     ```

3. **Virtualenv** (opcional, mas recomendado):  
   - Instale o `virtualenv` se necessário:  
     ```bash
     pip install virtualenv
     ```

---

## **Como executar o projeto**

### **1. Clone o repositório**
Faça o clone deste repositório no seu computador:

```bash
git clone https://github.com/seu-usuario/8-Rainhas-algoritmos-de-busca.git
cd 8-Rainhas-algoritmos-de-busca
```

---

### **2. Crie um ambiente virtual**
Crie e ative um ambiente virtual para isolar as dependências do projeto:

- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

---

### **3. Instale as dependências**
Com o ambiente virtual ativo, instale as dependências necessárias:

```bash
pip install django
```

---

### **4. Execute as migrações**
O projeto usa um banco de dados SQLite. Execute as migrações do Django:

```bash
python manage.py migrate
```

---

### **5. Execute o servidor**
Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

Se tudo estiver correto, você verá uma mensagem parecida com esta:

```
Starting development server at http://127.0.0.1:8000/
```

Abra o navegador e acesse **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** para usar a aplicação.

---

## **Como usar a aplicação**
1. Na interface inicial, escolha o algoritmo desejado:
   - **DFS (Busca em Profundidade)**  
   - **Subida de Encosta**
2. Clique em **Iniciar Busca** para gerar a primeira solução.
3. Utilize os botões para navegar entre as soluções encontradas.
4. O tabuleiro será atualizado dinamicamente conforme as soluções forem carregadas.

---

## **Estrutura do projeto**
```
8-Rainhas-algoritmos-de-busca/
├── manage.py
├── db.sqlite3
├── oito_rainhas/            <- Código principal da aplicação
│   ├── views.py             <- Lógica dos algoritmos
│   ├── models.py
│   ├── urls.py
│   └── templates/
│       └── tabuleiro.html   <- Interface do tabuleiro
├── tabuleiro/               <- Recursos do tabuleiro
│   └── static/
│       ├── queen.svg        <- Imagem das peças
│       └── tabuleiro.png    <- Imagem do tabuleiro
└── .gitignore
```

---

## **Tecnologias usadas**
- **Python 3.7+**
- **Django**
- **HTML/CSS** (para renderização do tabuleiro)

---
