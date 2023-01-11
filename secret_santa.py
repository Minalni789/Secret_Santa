import random as rand

names = input("Enter the names of the participants separated by space: ").split()


def santas_elves(santa_list):
    presents = rand.sample(names,len(names))


    while any(santa_list[i] == presents[i] for i in range(len(santa_list))):
        rand.shuffle(presents)

    for f in range(len(santa_list)):
        print(f'{santa_list[f]} gives a gift to --> {presents[f]}')

santas_elves(names)
