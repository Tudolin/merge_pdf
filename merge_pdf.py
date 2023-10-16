import PyPDF2
import argparse
import os


def path_type(path_string):
    if os.path.isabs(path_string):
        return path_string
    else:

        return os.path.abspath(os.path.join(os.getcwd(), path_string))


def merge_pdfs(archive_path, nome_arquivo):
    directory = os.getcwd()

    absolute_archive_path = os.path.abspath(
        os.path.join(directory, archive_path))

    path_name = os.path.join(directory, nome_arquivo)

    merge = PyPDF2.PdfMerger()

    try:
        archive_list = os.listdir(absolute_archive_path)
    except FileNotFoundError:
        print(f"Error: Directory/Folder '{absolute_archive_path}' not found.")
        return
    except TypeError:
        print(f"Error")

    archive_list.sort()

    for archive in archive_list:
        if not archive.lower().endswith(".pdf"):
            print(f"Error: the archive '{archive}' isn't a pdf and can't be merged.")
            continue
        if archive.lower().endswith(".pdf"):
            archive_path = os.path.join(absolute_archive_path, archive)
            try:
                merge.append(archive_path)
            except Exception as e:
                print(f"Error: can't read the archive = '{archive}': {e}")
                continue


    merge.write(path_name)
    merge.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge PDF archives.")

    parser.add_argument("--folder", type=path_type, required=True,
                        help="The path of the PDF's to be merged. Obs: separated names or directorys should be in quotes '' :D .")

    parser.add_argument("--name", type=str, required=True,
                        help="Final file name.")
    args = parser.parse_args()

    merge_pdfs(args.folder, args.name+'.pdf')
