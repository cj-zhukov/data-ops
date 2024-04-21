import hashlib
from io import BytesIO
from PIL import Image
import imagehash
import numpy
import scipy.fftpack


def calc_image_phash(file_path: str) -> str:
    with open(file_path, mode='rb') as file:
        bin_img = file.read()
    pil_img = Image.open(BytesIO(bin_img))
    phash = imagehash.phash(pil_img, hash_size=16)
    return str(phash)


def calc_image_phash2(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


if __name__ == "__main__":
    file = "foo.jpg"
    h = calc_image_phash(file)
    print(h)
