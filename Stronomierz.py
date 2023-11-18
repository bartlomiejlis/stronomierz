import math


def podzial_tlumaczenia():
    """Funkcja obliczająca ilość tłumaczy potrzebnych do realizacji tłumaczenia oraz
    liczbę stron przypadającą na każdego z nich na podstawie wprowadzonych danych."""
    print('Program obliczający ilość tłumaczy potrzebnych do realizacji tłumaczenia na dany język oraz\n'
          'liczbę stron przypadającą na każdego z nich na podstawie wprowadzonych danych.\n')
    while True:
        print('1. Start programu')
        print('2. Wyjście')
        choice = input('Wybierz opcję z menu: ')

        if choice == '1':
            all_pages = float(input("\nPodaj całkowitą liczbę stron dla tłumacza w zleceniu: "))
            deadline = int(input("Podaj liczbę dni roboczych na realizację zlecenia: "))
            pages_per_day = all_pages / deadline
            pages_per_day_for_translator = int(input('Podaj liczbę stron dla tłumacza na dzień: '))
            no_of_translators = pages_per_day / pages_per_day_for_translator
            no_of_translators = math.ceil(no_of_translators)
            print(f'\nAby wyrobić się w terminie potrzebujesz {no_of_translators} tłumaczy z danego języka.')
            pages_per_translator = all_pages / no_of_translators
            pages_per_translator = math.ceil(pages_per_translator)
            print(f'Każdemu z tłumaczy zleć {pages_per_translator} stron.\n')
        elif choice == '2':
            break
        else:
            print('\nWybierz prawidłowy numer\n')


podzial_tlumaczenia()
