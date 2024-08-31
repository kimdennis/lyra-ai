import os

def ensure_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def save_text_to_file(text, file_path):
    with open(file_path, "w") as f:
        f.write(text)
