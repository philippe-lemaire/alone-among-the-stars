from datetime import datetime
import os

home_dir = os.path.expanduser("~")
text_files_dir = "alone_among_the_stars"
export_path = os.path.join(home_dir, text_files_dir)
# create export folder
os.makedirs(export_path, exist_ok=True)

now = datetime.now()
filename = os.path.join(export_path, f"{now.date()}_{now.time()}.md")
editor = "vim"
