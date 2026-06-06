import random


def generate_input(filename='input.txt', n=1000, max_cylinder=4999):
    requests = [random.randint(0, max_cylinder) for _ in range(n)]
    with open(filename, 'w') as f:
        for r in requests:
            f.write(f'{r}\n')
    print(f'Generated {n} requests in {filename}')


if __name__ == '__main__':
    generate_input()
