import shutil
from pathlib import Path

source_dir = Path("./downloads")

packnames = [
	name.name for name in source_dir.iterdir() if name.is_dir()
]

for packname in packnames:
	source_path = source_dir / packname / "webp"
	dest_path = Path("./sorted") / packname


	print(packname)

	if not dest_path.exists():
		dest_path.mkdir(parents=True)

	for file_path in source_path.iterdir():
		shutil.copy(file_path, dest_path)
