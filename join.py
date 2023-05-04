import os


filenames = ["qemu-images/disk.img","qemu-images/efi-part.vfat","qemu-images/rootfs.ext2","qemu-images/rootfs.ext4"]
chunk_size = 100 * 1024 * 1024  # 100 MB in bytes

for filename in filenames:
    with open(filename, "wb") as outfile:
        index = 0
        while True:
            chunk_filename = f"{filename}.part{index}"
            if not os.path.exists(chunk_filename):
                break
            with open(chunk_filename, "rb") as infile:
                chunk = infile.read()
                outfile.write(chunk)
            index += 1

