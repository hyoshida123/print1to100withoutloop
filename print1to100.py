def print1to100(n):
    if n == 100:
        print(n)
        return

    print(n)
    print1to100(n+1)

if __name__ == "__main__":
    print1to100(1)