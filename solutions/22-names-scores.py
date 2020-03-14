import csv

if __name__ == '__main__':
    names = []
    with open('p022_names.txt') as f:
        for row in csv.reader(f):
            names.extend(row)
    sorted_names = sorted(names)
    scores = (sum(map(lambda x: ord(x) - 64, name))
              for name
              in sorted_names)
    ans = sum(
            (place + 1) * score
            for place, (name, score)
            in enumerate(zip(sorted_names, scores))
    )
