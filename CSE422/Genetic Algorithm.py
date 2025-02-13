import random

def random_with_N_digits(n):
    key1 = ""
    for i in range(n):
        temp = str(random.randint(0, 1))
        key1 += temp
    return key1

def generate_chromosome(chromosomes, length):
    num_chromosomes = 10
    for i in range(num_chromosomes):
        chromosome = random_with_N_digits(length)
        if chromosome not in chromosomes:
            chromosomes.append(chromosome)
        else:
            num_chromosomes += 1

def fitness(chromosome, timeslot_num, course_num):
    timeslot = []
    x = 0
    y = course_num
    for i in range(timeslot_num):
        temp = chromosome
        timeslot.append(temp[x:y])
        x += course_num
        y += course_num
    #Overlapping
    error = 0
    for i in range(timeslot_num):
        count = 0
        for j in range(course_num):
            if timeslot[i][j] == "1":
                count += 1
        if count != 0:
            error += (count - 1)
    #Consistency
    for i in range(course_num):
        count = 0
        for j in range(timeslot_num):
            if timeslot[j][i] == "1":
                count += 1
        if count != 0:
            error += (count - 1)
        else:
            error += 1
    return (-1*error)

def crossover(f_chromosome, s_chromosome, length):
    crossover_p1 = random.randint(0, length - 2)
    crossover_p2 = random.randint(crossover_p1 + 1, length - 1)

    offspring1 = f_chromosome[:crossover_p1] + s_chromosome[crossover_p1:crossover_p2] + f_chromosome[crossover_p2:]
    offspring2 = s_chromosome[:crossover_p1] + f_chromosome[crossover_p1:crossover_p2] + s_chromosome[crossover_p2:]

    return offspring1, offspring2

def genetic_algorithm():
    NT = [int(i) for i in input().split(" ")]

    chromosome_len = NT[0]*NT[1]
    courses = []
    for i in range(0,NT[0]):
        courses.append(input())

    chromosomes = []
    generate_chromosome(chromosomes, chromosome_len)

    while True:
        for i in range(5):
            random_c1 = random.randint(0,9)
            random_c2 = random.randint(0,9)
            while random_c1 == random_c2:
                random_c2 = random.randint(0,9)
            offspring1, offspring2 = crossover(chromosomes[random_c1], chromosomes[random_c2], chromosome_len)
            chromosomes.extend([offspring1, offspring2])

        fitness_c = [0]*20
        for i in range(len(chromosomes)):
            error = fitness(chromosomes[i], NT[1], NT[0])
            fitness_c[i] = error

        for i in range(len(fitness_c)):
            if fitness_c[i] == 0:
                return chromosomes[i], courses

        for i in range(10):
            minimum_f_indx = fitness_c.index(min(fitness_c))
            fitness_c[minimum_f_indx] = 0
            chromosomes[minimum_f_indx] = 0

        chromosomes = [i for i in chromosomes if i != 0]
        fitness_c = [i for i in fitness_c if i != 0]

output, courses = genetic_algorithm()
def main(output, courses):
    part1 = output[:3]
    part2 = output[3:6]
    part3 = output[6:]
    for i in range(len(part1)):
        if part1[i] == "1":
            print(f"{courses[i]} ->", end="")
    for i in range(len(part2)):
        if part2[i] == "1":
            print(f"{courses[i]} ->", end="")
    for i in range(len(part3)):
        if part3[i] == "1":
            print(f"{courses[i]}")

main(output, courses)

