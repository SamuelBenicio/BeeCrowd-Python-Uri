while(True):
    try:
        n1 = input()
        if(n1=='esquerda'):
            print('ingles')
        elif(n1=='direita'):
            print('frances')
        elif(n1=='nenhuma'):
            print('portugues')
        elif(n1=='as duas'):
            print('caiu')
    except EOFError:
        break
