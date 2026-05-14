import os
import pandas as pd
from pathlib import Path
import glob

def extrair_numero(arquivo):
    return int(arquivo.split('_Parte')[1].split('.pdf')[0])

def renomear_pdfs_com_excel(excel_path, pdf_folder, pdf_files):
    # Leia o arquivo Excel
    df = pd.read_excel(excel_path)

    # Obtenha os nomes da primeira coluna do Excel
    nomes = df.iloc[:, 0]

    print(len(nomes))

    # Verifique se há correspondência entre os nomes do Excel e os arquivos PDF
    if len(nomes) != len(pdf_files):
        print("O número de nomes no Excel não coincide com o número de arquivos PDF.")
        return

    # Itera pelos nomes e arquivos PDF e renomeia os arquivos
    for nome, pdf_file in zip(nomes, pdf_files):
        pdf_file_path = os.path.join(pdf_folder, pdf_file)
        novo_nome_pdf = os.path.join(pdf_folder, f"{nome}.pdf")

        # Renomeia o arquivo PDF
        os.rename(pdf_file_path, novo_nome_pdf)
        print(f"Arquivo renomeado: {pdf_file} -> {novo_nome_pdf}")

# Exemplo de uso
if __name__ == "__main__":
    excel_path = Path("C:/Renomear/excel/Planilha_nomes.xlsx")  
    pdf_folder = Path("C:/Renomear/pdfs")
    arquivos = [arquivo for arquivo in os.listdir(pdf_folder) if arquivo.startswith('Arquivos_Parte') and arquivo.endswith('.pdf')]
    arquivos_ordenados = sorted(arquivos, key=extrair_numero)
    print(len(arquivos_ordenados))
    renomear_pdfs_com_excel(excel_path, pdf_folder, arquivos_ordenados)

    

