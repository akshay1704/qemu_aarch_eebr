import os

filenames = ["qemu-images/disk.img","qemu-images/efi-part.vfat","qemu-images/rootfs.ext2","qemu-images/rootfs.ext4"]
chunk_size = 100 * 1024 * 1024  # 100 MB in bytes

for filename in filenames:
    with open(filename, "rb") as infile:
        index = 0
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break
            chunk_filename = f"{filename}.part{index}"
            with open(chunk_filename, "wb") as outfile:
                outfile.write(chunk)
            index += 1

