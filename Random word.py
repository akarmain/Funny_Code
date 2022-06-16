import random


def main():
    leters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'y',
              'v', 'w', 'x', 'u', 'z']
    len_leters = random.randint(0, len(leters))
    while len_leters > 15:
        len_leters = random.randint(0, len(leters))
    for i in range(len_leters):
        print(random.choice(leters), end="")
    print(random.choice(leters))


if __name__ == "__main__":
    main()
    print("Random word")
