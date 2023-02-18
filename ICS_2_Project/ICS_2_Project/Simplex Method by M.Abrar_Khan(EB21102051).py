objective = input('What is given objective (max/min)?')
max_chances = ['max', 'Max', 'MAX', 'maximization', 'Maximization', 'MAXIMIZATION', 'maximize', 'Maximize', 'MAXIMIZE',
               'maximum', 'Maximum', 'MAXIMUM']

def maximization(matrix):
    # for initial tableau
    initial_tab = matrix
    z = []
    for o in range(len(initial_tab[-1])):
        if initial_tab[-1][o] != 0:
            a = (initial_tab[-1][o]) * -1
            z.append(a)
    for i in range(cons_eq):
        z.append(float(0))
    initial_tab[-1] = z

    j = cons - 1
    for unit in range(len(initial_tab) - 1):
        u = initial_tab[unit]
        for i in range(cons_eq):
            u.insert(-1, float(0))
            initial_tab[unit] = u
        for k in range(cons):
            initial_tab[unit][j] = float(1)
        j += 1
    table=[]
    for k in range(len(initial_tab)):
        mat_3 = []
        for f in range(len(initial_tab[k])):
            mat_3.append(initial_tab[k][f])
        table.append(mat_3)

    def objective_fucntion(table):
        # final = []
        obj_func.clear()
        for k in range(len(table[-1])):
            obj_func.append(table[-1][k])
        # print(obj_func)
        try:
            minimum = obj_func[0]
            for i in range(len(obj_func)):
                if obj_func[i] < minimum:
                    minimum = obj_func[i]



            # final=[]
            while minimum<0:
                min_rat = []

                for calc in range(len(table)-1):
                    try:
                        piv_col = min(table[-1])
                        x = table[-1].index(piv_col)
                    except ValueError:
                        pass

                    try:
                        min_ratio = (table[calc][-1]) / (table[calc][x])
                        if min_ratio != 0:
                            min_rat.append(min_ratio)
                    except ZeroDivisionError:
                        pass
                table.append(min_rat)
            # print(a)
            # print(f"min_rat is {min_rat}")

                mini = min_rat[0]
                for i in range(len(min_rat)):
                    if min_rat[i] < mini:
                        mini = min_rat[i]
                piv_row = mini
            # print(f"min_ratio is {piv_row}")
                b = table[-1].index(piv_row)
                piv_ele = table[b][x]
            # print(b)
            # print(piv_ele)

                for cal_2 in range(len(table)):
                    pivot_row = []
                    for i in range(len(table[b])):
                        try:
                            new_piv_row = (table[b][i]) / piv_ele
                            pivot_row.append(new_piv_row)
                        except ZeroDivisionError:
                            pass
                    table[b] = pivot_row
                    break

                table.pop(-1)
                initial_tab_pos = []
                for pos in range(len(table)):
                    if pos != b:
                        initial_tab_pos.append(pos)

                another_tableau = []
                for k in range(len(table)):
                    mat_5 = []
                    for f in range(len(table[k])):
                        mat_5.append(table[k][f])
                    another_tableau.append(mat_5)
                table.pop(b)
            # print(table)
                for i in range(len(initial_tab_pos)):
                    d = initial_tab_pos[i]
                    n_r = []
                    for j in range(len(table[i])):
                        try:
                            new_rows = (table[i][j]) - ((table[i][x]) * another_tableau[b][j])
                            n_r.append(new_rows)
                        except IndexError:
                            pass
                    another_tableau[d] = n_r

                table.clear()
                table=[]
                for k in range(len(another_tableau)):
                    mat_6 = []
                    for f in range(len(another_tableau[k])):
                        mat_6.append(another_tableau[k][f])
                    table.append(mat_6)
                # final=[]
                for i in range(len(table[-1])):
                # while True:
                #     if table[-1][i]>=0:
                    if i >= len(table[-1])-1:
                        print(table)
                # print(jk)        # continue
                # final.append(table[-1])
                # print(final)
        except  IndexError:
            pass

        # print(table)

    objective_fucntion(table)

matrix_1 = []
DV = int(input("How many decision variables? "))
obj_func = []
for DV in range(1, DV + 1):
    obj_func.append(float(input(f"Enter value of Decision Varibale {DV} = ")))
cons_eq = int(input("How many equations of constraints? "))
for cons_eq in range(1, cons_eq + 1):
    matrix_2 = []
    cons = int(input(f"How many values of constraint equation {cons_eq}? "))
    for constraints in range(1, cons + 1):
        matrix_2.append(float(input(f"Enter value of constraint eqn {constraints} = ")))
    matrix_1.append(matrix_2)

if len(matrix_1[0]) != len(obj_func):
    obj_func.append(float(0))
    matrix_1.append(obj_func)
    if objective in max_chances:
        matrix = matrix_1
        maximization(matrix)
    else:
        rows = len(matrix_1)
        cols = len(matrix_1[0])
        transposed = []
        for i in range(cols):
            a = []
            for j in range(rows):
                a.append(matrix_1[j][i])
            transposed.append(a)
        matrix = transposed
        maximization(matrix)