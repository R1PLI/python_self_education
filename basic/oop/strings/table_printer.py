def print_table(input_list):
    col_widths = [0] * len(input_list)
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if len(input_list[i][j]) > col_widths[i]:
                col_widths[i] = len(input_list[i][j])

    for x in range(len(input_list[0])):
        for y in range(len(input_list)):
            print(input_list[y][x].rjust(col_widths[y]), end=' ')
        print('')


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)