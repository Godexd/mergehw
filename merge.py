def read_files(file, count):
    for a in range(1, count + 1):
        name = str(a) + '.txt'
        lines = 0

        for line in open(file + str(a) + '.txt'):
            lines += 1

        data_files.append({'name': name, 'lines': lines})


def write_solution(file):
    file_solution = open(file + 'solution.txt', 'w')

    for a in range(len(data_files)):

        min_lines = data_files[0]['lines']
        min_name = data_files[0]['name']
        min_index = 0

        for index, item in enumerate(data_files):
            if item['lines'] < min_lines:
                min_lines = item['lines']
                min_name = item['name']
                min_index = index

        data_files.pop(min_index)

        file_solution.write(min_name + '\n')
        file_solution.write(str(min_lines) + '\n')

        for line in open(file + min_name):
            file_solution.write(line)
        else:
            file_solution.write('\n')


data_files = []

def main():
    read_files('Files/', 3)
    write_solution('Files/')


if __name__ == '__main__':
    main()