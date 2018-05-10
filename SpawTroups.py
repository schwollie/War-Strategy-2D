import Troups


def spawn_Troup(pos_x, pos_y, sort):
    if sort == "Swordsman":
        sw = Troups.Swordsman(pos_x, pos_y)
        Troups.all_troups.append(sw)
