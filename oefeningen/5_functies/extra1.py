def bereken_pi(aantal):
    total = 0
    for n in range(aantal):
        term = 1 / (2 * n + 1)
        if n % 2 == 0:
            total += term
        else:
            total -= term

    return total * 4


def main():
    print(bereken_pi(20))


if __name__ == '__main__':
    main()
