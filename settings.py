from datetime import datetime
import os

base_dir = os.getcwd()
text_files_dir = "output"
export_path = os.path.join(base_dir, text_files_dir)
# create export folder
os.makedirs(export_path, exist_ok=True)

now = datetime.now()
filename = os.path.join(export_path, f"{now.date()}_{now.time()}.md")
editor = "vim"
