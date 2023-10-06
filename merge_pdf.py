import PyPDF2
import argparse
import os


def path_type(path_string):
    if os.path.isabs(path_string):
        return path_string
    else:

        return os.path.abspath(os.path.join(os.getcwd(), path_string))


def merge_pdfs(caminho_arquivo, nome_arquivo):
    diretorio_atual = os.getcwd()

    caminho_arquivo_absoluto = os.path.abspath(
        os.path.join(diretorio_atual, caminho_arquivo))

    caminho_com_nome = os.path.join(diretorio_atual, nome_arquivo)

    merge = PyPDF2.PdfMerger()

    lista_arquivos = os.listdir(caminho_arquivo_absoluto)

    lista_arquivos.sort()

    for arquivo in lista_arquivos:
        if arquivo.lower().endswith(".pdf"):
            arquivo_path = os.path.join(caminho_arquivo_absoluto, arquivo)
            try:
                merge.append(arquivo_path)
            except Exception as e:
                print(f"Erro ao ler o arquivo '{arquivo}': {e}")
                continue

    merge.write(caminho_com_nome)
    merge.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unir arquivos PDF.")

    parser.add_argument("--path", type=path_type, required=True,
                        help="Caminho para o diretório contendo os arquivos PDF a serem mesclados")

    parser.add_argument("--name", type=str, required=True,
                        help="Nome do arquivo mesclado")
    args = parser.parse_args()

    merge_pdfs(args.path, args.name+'.pdf')
