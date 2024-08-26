from datetime import datetime
import os

home_dir = os.path.expanduser("~")
text_files_dir = "alone_among_the_stars"
now = datetime.now()
filename = os.path.join(home_dir, text_files_dir, f"{now.date()}_{now.time()}.md")
editor = "vim"
