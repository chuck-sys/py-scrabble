class Move:
    '''
    A move is an array of formatted tuples:
        (posx, posy, letter)

    This is to simulate the (mostly) multiple tile placings you see in all
    scrabble play. Of course, these moves are constructed on a tile-by-tile
    basis.

    The tuples only include the ones placed by the player, and not the ones that
    are on the board already.
    '''
    def __init__(self):
        self.m = []

        # The type of move can be one of 3 characters:
        # 'M' -> Your standard move (placing tiles on board)
        # 'E' -> Exchange (the placed tiles on board get swapped with others in
        #        the deck
        # 'P' -> Pass (all placed tiles return to hand and the next turn
        #        happens)
        # Defaults to 'M'
        self.t = 'M'

        # If the move is chained together with other tiles on the board, it will
        # be true, otherwise, if nothing is adjacent to it, it will be false.
        self.is_chain = False

    def get_item(self, x, y):
        '''
        Finds the move with coordinates equal to (x, y). Raises ValueError if
        move doesn't exist.
        '''
        for i, j, l in self.m:
            if i == x and j == y:
                return (i, j, l)
        raise ValueError('invalid indices (%d, %d)' % (x, y))

    def add_move(self, x, y, letter):
        '''
        Appends the entire thing onto move array. Checks for letters that are in
        the same position.
        '''
        for i, j, l in self.m:
            if i == x and j == y:
                raise Exception("error: attempt to place letter in same position")

        self.m.append((x, y, letter))

    def remove_move(self, x, y):
        '''
        Returns the removed letter
        '''
        rem = None
        for i, j, l in self.m:
            if i == x and j == y:
                # A match!
                rem = (i, j, l)

        if rem is None:
            raise Exception("error: letter doesn't exist and cannot be removed")

        self.m.remove(rem)
        return rem[2]

    def validate(self):
        '''
        Checks to see if the move made by the player is valid.
        Only checks tile placement (vertical or horizontal), and not the words
        itself.

        Returns true if the move is valid in said direction, and false
        otherwise.
        '''
        return self.validate_vertical() or self.validate_horizontal()

    def validate_horizontal(self):
        '''
        Checks to see if the move made by the player is in a horizontal line (y
        coordinates the same).
        
        Returns true if it is, and false otherwise.
        '''
        # Empty/single item in list should always return true
        if len(self.m) <= 1: return True
        sety = self.m[0][1]
        for x, y, l in self.m:
            if y != sety:
                return False
        return True

    def validate_vertical(self):
        '''
        Checks to see if the move made by the player is in a vertical line (x
        coordinates the same).
        
        Returns true if it is, and false otherwise.
        '''
        # Empty/single item in list should always return true
        if len(self.m) <= 1: return True
        setx = self.m[0][0]
        for x, y, l in self.m:
            if x != setx:
                return False
        return True
