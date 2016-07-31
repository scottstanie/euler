def is_pal(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    print max(a * b for a in range(1000) for b in range(1000) if is_pal(a * b))
