def collide(player,enemy):
        if ((player[0]-enemy[0])**2 + (player[0]-enemy[1])**2)**0.5 <= 63:
            return True