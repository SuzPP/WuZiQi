from Players import Player


class Board(object):
    ROW = [' '+chr(a)+' ' for a in range(65, 80)]
    BOARD = {}
    def __init__(self):
        self._piece = Player(1,'X').get_player_piece()


    def create_board(self):
        for i in self.ROW:
            self.BOARD[str(i)] = {}
            for j in range(1, 16):
                self.BOARD[str(i)][j] = '   '
        return self.BOARD

    def show_board(self):
        b = self.ROW.copy()
        b.insert(0,'    ')
        print('|'.join(b) + '|')
        print('-'*(4*16+1))
        for n in range(15):
            # print (n)
            for r in range(0,16):
                # print (r)
                if r != 0:
                    b[r] = self.BOARD[self.ROW[r-1]][n+1]
                else:
                    b[r] = ' %s '%(str((n+1)//10)+str((n+1)%10))
            print ('|'.join(b) + '|')
            print('-' * (4 * 16 + 1))



    def place_piece(self,location):
        row = int(location[0])
        col = ' ' + str(location)[1] + ' '
        # print (row)
        try:
            if self.BOARD[col][row] != '   ':
                print ('Cannot Place Here')
            else:
                self.BOARD[col][row] = ' X '
                print ('Placed!')
        except KeyError:
            raise 'Invalid Location!'

        return
if __name__ == '__main__':
    board = Board()
    board.BOARD = board.create_board()
    # print(board.create_board())
    board.place_piece( '1A')
    board.place_piece('1A')
    board.place_piece('3A')
    # board.create_board()
    print(board.BOARD)
    print(board.show_board())
