# 📄 PDF Batch Renamer

Projeto em Python para renomeação automática de arquivos PDF utilizando nomes extraídos de uma planilha Excel.

O sistema lê uma planilha `.xlsx`, identifica os nomes na primeira coluna e renomeia automaticamente arquivos PDF em sequência.

---

# 🚀 Funcionalidades

* Renomeação automática de PDFs
* Integração com Excel
* Processamento em lote
* Ordenação automática de arquivos
* Automação documental
* Organização rápida de arquivos

---

# 🛠 Tecnologias utilizadas

* Python
* Pandas
* OpenPyXL
* OS Library

---

# ▶ Como executar

## Instale as dependências

```bash id="f0l8fy"
pip install -r requirements.txt
```

## Execute o projeto

```bash id="3mq2xn"
python main.py
```

---

# 📂 Configuração

Defina os caminhos desejados:

```python id="t7j9gd"
excel_path = Path("C:/Renomear/excel/Planilha_nomes.xlsx")
pdf_folder = Path("C:/Renomear/pdfs")
```

---

# 📌 Estrutura esperada

## PDFs

```text id="e2m2hf"
Arquivos_Parte1.pdf
Arquivos_Parte2.pdf
Arquivos_Parte3.pdf
```

## Excel

| Nome   |
| ------ |
| João   |
| Maria  |
| Carlos |

---

# 📌 Resultado gerado

```text id="7kp6q0"
João.pdf
Maria.pdf
Carlos.pdf
```

---

# 📖 Objetivo

Automatizar processos de organização e renomeação de documentos PDF utilizando dados de planilhas Excel.
