import os
import pandas as pd
from pathlib import Path


def extrair_numero(arquivo):
    """
    Extrai o número do arquivo:
    Exemplo:
    Arquivos_Parte1.pdf -> 1
    """
    return int(arquivo.split('_Parte')[1].split('.pdf')[0])


def renomear_pdfs_com_excel(excel_path, pdf_folder):

    # Lê a planilha Excel
    df = pd.read_excel(excel_path)

    # Obtém nomes da primeira coluna
    nomes = df.iloc[:, 0].dropna().astype(str)

    # Lista arquivos PDF
    arquivos_pdf = [
        arquivo for arquivo in os.listdir(pdf_folder)
        if arquivo.startswith('Arquivos_Parte')
        and arquivo.endswith('.pdf')
    ]

    # Ordena os arquivos corretamente
    arquivos_ordenados = sorted(arquivos_pdf, key=extrair_numero)

    print(f"\n📄 PDFs encontrados: {len(arquivos_ordenados)}")
    print(f"📊 Nomes encontrados no Excel: {len(nomes)}")

    # Verifica se quantidade coincide
    if len(nomes) != len(arquivos_ordenados):
        print("\n❌ ERRO:")
        print("Quantidade de nomes no Excel não coincide com quantidade de PDFs.")
        return

    print("\n🚀 Iniciando renomeação...\n")

    # Renomeia arquivos
    for nome, arquivo_pdf in zip(nomes, arquivos_ordenados):

        caminho_antigo = os.path.join(pdf_folder, arquivo_pdf)

        # Remove caracteres inválidos
        nome_limpo = "".join(
            caractere for caractere in nome
            if caractere not in r'\/:*?"<>|'
        )

        novo_nome = f"{nome_limpo}.pdf"

        caminho_novo = os.path.join(pdf_folder, novo_nome)

        try:
            os.rename(caminho_antigo, caminho_novo)

            print(f"✅ {arquivo_pdf}")
            print(f"   ➜ {novo_nome}")

        except Exception as erro:
            print(f"❌ Erro ao renomear {arquivo_pdf}: {erro}")

    print("\n🎉 Processo concluído com sucesso!")


if __name__ == "__main__":

    # Caminho da planilha Excel
    excel_path = Path(
        r"C:\Renomear\excel\Planilha_nomes.xlsx"
    )

    # Pasta contendo PDFs
    pdf_folder = Path(
        r"C:\Renomear\pdfs"
    )

    renomear_pdfs_com_excel(excel_path, pdf_folder)
