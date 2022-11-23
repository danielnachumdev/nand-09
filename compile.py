from danielutils import get_files, acm, delete_file, cm, bytes_to_str
from LOCAL import COMPILER
if __name__ == "__main__":
    [delete_file(f) for f in get_files("./") if f.endswith(".vm")]
    _, stdout, stderr = cm(COMPILER)
    print(bytes_to_str(stdout))
    print(bytes_to_str(stderr))
