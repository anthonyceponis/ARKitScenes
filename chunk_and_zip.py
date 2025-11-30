from pathlib import Path
import os
import subprocess
import shutil
from tqdm import tqdm

if __name__ == "__main__":
    val_dirpath = Path("data/upsampling/Validation")

    video_filepaths = list(val_dirpath.iterdir())

    chunk_size = 50

    for i in tqdm(range(0, len(video_filepaths), chunk_size)):
        chunk_i = i // chunk_size
        chunk_dirpath = Path(f"validation_arkitscenes_{chunk_i}")
        os.mkdir(chunk_dirpath)
        for filepath in video_filepaths[i : min(len(video_filepaths), i + chunk_size)]:
            shutil.move(filepath, chunk_dirpath)
        subprocess.run(
            f"tar -czf {chunk_dirpath.stem}.tar.gz {chunk_dirpath.stem}".split(" ")
        )
        shutil.rmtree(chunk_dirpath)
