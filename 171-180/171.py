# # pathlib is a built-in Python module used to work with: files, folders, file paths

# # Instead of treating a path as just a string, Python gives us a Path object.

from pathlib import Path

folder = Path("data")

folder.mkdir(exist_ok=True)

print("Folder is ready.")




