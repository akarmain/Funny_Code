import random


def shows_one_task(total_tasks):
    random_index = []
    hou_complit = 0
    for i in range(total_tasks):
        ran = random.randint(1, total_tasks)
        while ran in random_index:
            ran = random.randint(1, total_tasks)
        random_index.append(ran)
    for i in range(len(random_index)):
        hou_complit += 1
        print(f"Your task number is: {random_index[i]}")
        if i != total_tasks:
            Y_or_N = input("next? Y/n")
            if Y_or_N == "n":
                break
            else:
                continue
    print(f"Good, you have completed {hou_complit} tasks")


if __name__ == "__main__":
    first_argument = int(input("total tasks?\n"))
    # Откомментировать если нужно сразу передавать агрумент код через консоль
    # import sys; first_argument = int(sys.argv[1])
    shows_one_task(first_argument)
