# i know qualllitii coooootteeeeeeeeeeeeeeeeeeee :D
f = open("../main.py", "w")
f.write('input_number = input("Wpisz liczbe: ")')
number = 1
# reppppeatttt 100x
while number < 100:
    if (number % 2) == 0:
        f.write(f'\nif(input_number == "{number}"):\n')
        f.write('    print("liczba jest parzysta")\n')
    else:
        f.write(f'\nif(input_number == "{number}"):\n')
        f.write('    print("liczba jest nieparzysta")\n')
    number += 1

f.close()
