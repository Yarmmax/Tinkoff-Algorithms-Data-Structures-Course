def comp(s1,s2):
    if len(s1) > len(s2):
        temp2 = s2
        temp2 *= len(s1)
        if s1 < temp2:
            return 1
        else:
            return -1
    else:
        temp1 = s1
        temp1 *= len(s2)
        if s2 < temp1:
            return -1
        else:
            return 1

def main():
    from sys import stdin
    from functools import cmp_to_key
    # "456456459","456456450","45645649","45645640","4564569","4564560","456456"
    # "456456","4564560","4564569","45645640","45645649","456456450","456456459"
    # "99","98","990","980","099","098","0990","0980","09","89"
    # "2252", "225"
    # "1", "225", "1", "225", "1"
    # "231", "23124"
    # "199", "19991"
    # "2","20","004","66"
    lines = [i for i in ["199", "19991"]]
    print(19919991 < 19991199)
    import itertools
    combinations = []
    for i in range(len(lines)):
        for subset in itertools.combinations(lines, i + 1):
            combinations.append(int("".join(subset)))
    # lines = [line.rstrip() for line in stdin]
    ans = sorted(lines, key=cmp_to_key(comp))
    print(str(max(combinations)) + " < " + " ".join(ans), max(combinations) < int("".join(ans)), sep='\n')
if __name__ == "__main__":
    main()



