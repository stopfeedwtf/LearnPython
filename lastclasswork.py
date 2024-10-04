# Dawson (a réparer)
# def new_board(n):
#     return [0] * n

# def display (board,n):
#     for i in range(n):
#         if board[i] == 0:
#             print(".", end=" ")
#         elif board[i] == 1:
#             print("x", end=" ")
#         else:
#             print("o", end=" ")
#     print("\n")
#     for i in range (n):
#         print(i+1, end=" ")
#     print("\n")

# def possible (board, n, i):
#     return 0 <= i and i < n and board[i]==0

# def select (board, n):
#     i = -1
#     while not possible(board, n, i):
#         i = int(input("Choisissez une case où jouer.")) - 1
#     return i
    
# def put (board, n, i):
#     board[i] = 1
#     if i != 0:
#         board[i-1]= -1
#     elif i != len(board-1) :
#         board[i+1]= -1

# def again (board, n):
#     for i in range(n):
#         if board[i] == 0:
#             return True
#     return False

# def dawson (n):
#     board = new_board(n)
#     player = 1
#     while again(board,n):
#         display(board,n)
#         i = select(board,n)
#         put(board,n,i)
#         display(board,n)
#         player = 1 if player == 2 else 2
#     player = 1 if player == 2 else 2
#     print("Le vainqueur est", player)

# dawson(int(input("Indiquez un nombre de cases.")))

# Toads and frogs

def init_board(n,p):
    if p >= n//2:
        p = n//2-1
    board = n * [0]
    for i in range(p):
        board[i] = 1
        board[n-i-1] = 2
    return board

def display (board,n):
    for i in range(n):
        if board[i] == 0:
            print(".", end=" ")
        elif board[i] == 1:
            print("x", end=" ")
        else:
            print("o", end=" ")
    print("\n")
    for i in range (n):
        print(i+1, end=" ")
    print("\n")

def possible(board, n, i, player):
    if i>=n or i < 0:
        return False
    if board[i] != player:
        return False
    if player == 1:
        if i+1<n and board[i+1]==0:
            return True
        else:
            if i+2<n and board[i+2]==0 and board [i+1]==2:
                return True
    else:
        if i-1>=0 and board[i-1]==0:
            return True
        else:
            if i-2>=0 and board[i-2]==0 and board [i-1]==1:
                return True
    return False

def select(board, n, player):
    i=-1
    while not possible(board, n, i, player):
        i = int(input("Choisissez une case où jouer.")) - 1
    return i

def move(board, player, i):
    board[i]=0
    if player == 1:
        if board[i+1]==0:
            board[i+1]=1
        else:
            board[i+2]=1
    else:
        if board[i-1]==0:
            board[i-1]=2
        else:
            board[i-2]=2

def again(board, n, player):
    for i in range(n):
        if possible(board,n,i,player):
            return True
    return False

def toads_and_frogs(n,p):
    player = 1
    board = init_board(n,p)
    while again(board,n,player):
        display(board,n)
        i = select(board,n,player)
        move(board,player,i)
        player = 1 if player == 2 else 2
        if not again(board,n,player):
            print("Le vainqueur est", player)

toads_and_frogs(int(input("Indiquez le nombre de cases. ")),int(input("Indiquez le nombre de pions.")))