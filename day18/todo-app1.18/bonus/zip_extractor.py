import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/home/bennie/Documents/development/python/ardit/60-Days-of-Python/day18/todo-app1.18/bonus/compressed.zip",
                    "/home/bennie/Documents/development/python/ardit/60-Days-of-Python/day18/todo-app1.18/bonus")