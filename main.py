from data_csv import read
from algorithme import optimized
from bruteforce import bruteforce

def main():
    choice_algorithme = input(f'Quel algorithme souhaitez-vous sélectionner ?'
                              f'\n 1 - Brute Force: '
                              f'\n 2 - Optimisé (1)'
                              f'\n 3 - Optimisé (2)'
                              f'\n Choix: ')

    if choice_algorithme == '1':
        data_brute_force = read('actions')
        bruteforce(data_brute_force)
    elif choice_algorithme == '2':
        data_algo_one = read('dataset1')
        optimized(data_algo_one)
    elif choice_algorithme == '3':
        data_algo_two = read('dataset2')
        optimized(data_algo_two)
    else:
        print('Le choix séléctionné n\'existe pas')


if __name__ == '__main__':
    main()
