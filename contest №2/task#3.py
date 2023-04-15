def comp(s1,s2):
    return int(s1 + s2 < s2 + s1)

def main():
    from sys import stdin
    from functools import cmp_to_key
    # lines = [i for i in ["2", "20", "004", "66"]]
    lines = [line.rstrip() for line in stdin]
    ans = sorted(lines, key=cmp_to_key(comp))
    print("".join(ans))

if __name__ == "__main__":
    main()