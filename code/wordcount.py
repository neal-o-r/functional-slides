from toolz.curried import *
from toolz.dicttoolz import merge_with
from string import punctuation
from collections import defaultdict
from glob import glob

punc = str.maketrans({p: None for p in punctuation})


def col_print(l, cols=5, width=12):

    group = zip(*[l[i::cols] for i in range(cols)])
    for row in group:
        print("".join(word.ljust(width) for word in row))


def stem(word: str) -> str:
    return word.lower().translate(punc)


def drop_word(word: str) -> bool:
    return len(word) >= 4


def normalise(d: dict, sign: int = 1) -> dict:
    s = sum(d.values())
    return {k: sign * v / s for k, v in d.items()}


def wordcount_imp(directory):

    d = defaultdict(int)
    for f in glob(directory):
        for line in open(f, "r"):
            line = line.split()
            line = [stem(i) for i in line]
            for s in line:
                d[s] += 1

    return {k: d[k] for k in d.keys() if not drop_word(k)}


if __name__ == "__main__":

    workflow = (
        glob,
        mapcat(open),
        mapcat(str.split),
        map(stem),
        frequencies,
        keyfilter(drop_word),
    )

    wordcount = compose(*reversed(workflow))

    billboard = wordcount("lyrics/billboard/*")
    dylan = wordcount("lyrics/dylan/*")

    m = merge_with(sum, normalise(dylan), normalise(billboard, sign=-1))

    print("\nDylan:")
    col_print(sorted(m, key=m.get)[-50:])
    print("\nBillboard:")
    col_print(sorted(m, key=m.get)[:50])
