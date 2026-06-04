import shutil

def copy_file(src, dst):
    print(f"Copying {src} to {dst}")
    try:
        shutil.copy2(src, dst)
        print("Copy successful!")
    except Exception as e:
        print(f"Error copying file: {e}")

if __name__ == "__main__":
    # Copy from FACULDADE FILOS to FILOS TESTE 2
    copy_file(
        "/Users/shayenefreita/FACULDADE FILOS/assets/images/student-pink-isolated.png",
        "/Users/shayenefreita/FILOS TESTE 2/assets/images/student-pink-isolated.png"
    )
    copy_file(
        "/Users/shayenefreita/FACULDADE FILOS/assets/images/student-portrait.png",
        "/Users/shayenefreita/FILOS TESTE 2/assets/images/student-portrait.png"
    )
