if __name__ == "__main__":
    file = open("octowateranimaluses.txt", "r")
    file_in_list = file.read()
    list_string = file_in_list.split("\n")
    for i in range(1, len(list_string), 2):
        one_str = list_string[i].split()
        for j in range(len(one_str)):
            if not(one_str[j] == "/||||||\\"):
                print(f"он: {one_str[j]} его номер {(j*i)+1}")
