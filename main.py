from data_csv import read
from algorithme import optimized
from bruteforce import bruteforce

def main():
    choice_algorithme = input('Brute Force ou Optimisé (b/o1/o2): ')

    if choice_algorithme == 'b':
        data_brute_force = read('actions')
        bruteforce(data_brute_force)
    elif choice_algorithme == 'o':
        data_algo_one = read('dataset1')
        optimized(data_algo_one)
    else:
        data_algo_two = read('dataset2')
        optimized(data_algo_two)


if __name__ == '__main__':
    main()
