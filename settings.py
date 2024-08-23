from datetime import datetime
import os

home_dir = os.path.expanduser("~")

editor = "vim"
now = datetime.now()
filename = os.path.join(
    home_dir, f"tmp/alone_among_the_stars_{now.date()}_{now.time()}.md"
)
