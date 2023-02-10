
def move_all_doc():
    for dirpath, dirs, files in os.walk(raw_path):
        for filename in files:
            if filename.endswith('.docx'):
                move(f'{dirpath}\{filename}',f'{csv_path}\{filename}')