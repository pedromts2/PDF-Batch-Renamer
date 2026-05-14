# 📄 PDF Merge Automation

Projeto em Python para combinação automática de múltiplos arquivos PDF em um único documento organizado por pasta.

O sistema percorre diretórios automaticamente, identifica arquivos PDF e gera um único PDF combinado para cada pasta encontrada.

---

# 🚀 Funcionalidades

* Combinação automática de PDFs
* Processamento de múltiplas pastas
* Geração automática de arquivos combinados
* Organização inteligente de documentos
* Automação de tarefas repetitivas
* Criação automática da pasta de saída

---

# 🛠 Tecnologias utilizadas

* Python
* PyMuPDF (`fitz`)
* OS Library

---

# ▶ Como executar

## Instale as dependências

```bash id="r63d36"
pip install -r requirements.txt
```

## Execute o projeto

```bash id="j7vx8r"
python main.py
```

---

# 📂 Configuração

Defina os diretórios desejados:

```python id="hrv1ne"
pasta_entrada = "C:/PASTAS"
pasta_saida = "C:/PASTAS COMBINADAS"
```

---

# 📌 Estrutura esperada

```text id="7p8l4w"
PASTAS/
│
├── Cliente_A/
│   ├── arquivo1.pdf
│   ├── arquivo2.pdf
│
├── Cliente_B/
│   ├── contrato.pdf
│   ├── documentos.pdf
```

---

# 📌 Resultado gerado

```text id="5bgx6k"
PASTAS COMBINADAS/
│
├── Cliente_A.pdf
├── Cliente_B.pdf
```

---

# 📖 Objetivo

Automatizar processos de organização e união de documentos PDF utilizando Python.
