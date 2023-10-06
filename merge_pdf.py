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

    try:
        lista_arquivos = os.listdir(caminho_arquivo_absoluto)
    except FileNotFoundError:
        print(f"Error: Directory '{caminho_arquivo_absoluto}' not found.")
        return
    except TypeError:
        print(f"Error")

    lista_arquivos.sort()

    for arquivo in lista_arquivos:
        if arquivo.lower().endswith(".pdf"):
            arquivo_path = os.path.join(caminho_arquivo_absoluto, arquivo)
            try:
                merge.append(arquivo_path)
            except Exception as e:
                print(f"Error: can't read the archive = '{arquivo}': {e}")
                continue

    merge.write(caminho_com_nome)
    merge.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge PDF archives.")

    parser.add_argument("--folder", type=path_type, required=True,
                        help="The path of the PDF's to be merged.")

    parser.add_argument("--name", type=str, required=True,
                        help="Final file name.")
    args = parser.parse_args()

    merge_pdfs(args.folder, args.name+'.pdf')
