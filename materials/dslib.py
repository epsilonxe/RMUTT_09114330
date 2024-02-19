import numpy as np

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

def rk(func, ini, start=0, stop=1, h=0.01, *args, **kwargs):
    try:
        dim = np.size(ini)
    except:
        dim = 1
    t = np.arange(start, stop+h, h)
    n = np.size(t)
    x = np.zeros((n, dim))
    x[0, : ] = ini
    for i in range(n-1):
        k1 = func(t[i], x[i, : ], *args, **kwargs)
        k2 = func(t[i] + 0.5*h, x[i, : ] + 0.5*h*k1, *args, **kwargs)
        k3 = func(t[i] + 0.5*h, x[i, : ] + 0.5*h*k2, *args, **kwargs)
        k4 = func(t[i] + h, x[i, : ] + h*k3, *args, **kwargs)
        x[i+1, :] = x[i, :] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    return t, x
    
