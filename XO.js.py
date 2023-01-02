INFINITE=5
def is_empty_place(x, y, table):
    if table[x][y]!=0:
        return False
    else: return True


def enter_input(table,input_text):
    x=INFINITE
    y=INFINITE
    while x >= 3 or y >= 3:

        x = int(input('the row is:'))
        y =int(input('the col is:'))

    while not is_empty_place(x, y, table):
        print('this place is taken')
        x = INFINITE
        y = INFINITE
        while x>=3 or y>=3:
            x = int(input('the row is:'))
            y = int(input('the col is:'))

    table[x][y] = input_text
    return table
def check_won(table):
    # algorithm need to be checked
    for row in table:
        print(row)
        if len(set(row))==1 and row[0]!=0:
            return row[0]
    return False
def main():
    won =False
    x_o_table=[[0,0,0],[0,0,0],[0,0,0]]
    while not won:
        print('Enter the X with the place that needed to be added, from 0,0 to 9,9')
        x_o_table=enter_input(x_o_table,'x')
        won=check_won(x_o_table)
        print('Enter the O with the place that needed to be added, from 0,0 to 9,9')
        x_o_table=enter_input(x_o_table,'o')
        won=check_won(x_o_table)
    print('{} WON!'.format(won))

main()