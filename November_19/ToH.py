import sys


def toh(n, src, dest, temp):
    if n == 0:
        return

    toh(n - 1, src, temp, dest)
    print(f"move {n} from {src} to {dest}")
    toh(n - 1, temp, dest, src)


if __name__ == '__main__':
    disks = int(sys.argv[1])
    toh(disks, "A", "C", "B")