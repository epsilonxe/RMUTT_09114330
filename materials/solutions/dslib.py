def gen_traj(func=None, seed=0, num=10):
    '''
    Generate trajectory
    Argumenets:
        func       A function in the iteration
        seed       Initial value in the iteration
        num        Number of iteration
    '''
    x = [None] * (num+1)
    x[0] = seed
    for k in range(num):
        x[k+1] = func(x[k])
    return x

def gen_latex_table(*args, **kvargs):
    num_col = len(args)
    col_name = kvargs['colname']
    align = kvargs['align']
    header1 = r'\begin{tabular}{' + align + r'}' + '\n'
    header2 = r'\hline' + '\n'
    for j in range(num_col):
        if j != (num_col - 1) :
            header2 += col_name[j] + ' & '
        else:
            header2 += col_name[j] + r'\\' + '\n' + r'\hline' + '\n'

    footer =  r'\hline' + '\n' + r'\end{tabular}'
    
    rows = ''
    n = len(args[0])
    for k in range(n):
        r = ''
        for j in range(num_col):
            if j != (num_col - 1) :
                r += f'{args[j][k]}' + ' & '
            else:
                r += f'{args[j][k]}' + r'\\' + '\n'
        rows += r    
    text = header1 + header2 + rows + footer    
    return text