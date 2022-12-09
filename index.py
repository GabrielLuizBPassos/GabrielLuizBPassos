
def contador(i, f, p):
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont}', end='', flush=True)
            cont += p
        print('FIM!')       
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='', flush=True)
            cont -= p
        print('FIM!')





        


contador(1, 10, 1)