from classes.Grid import Grid
from classes.Battery import Battery
from classes.House import House
from classes.Cable import Cable

def main():
    kanaleneiland = Grid(1, 10, 10)
    coord_bat = [1, 3, 5, 7, 9]
    nr = 0
    for i in range(len(coord_bat)):
        id0 = f"B{nr}"
        kanaleneiland.add_battery(Battery(id0, coord_bat[i], coord_bat[i], 1500))
        nr += 1

    coord_house = [0, 2, 4, 6, 8, 10]
    nr1 = 0
    for i in range(len(coord_house)):
        id1 = f"H{nr1}"
        kanaleneiland.add_house(House(id1, coord_house[i], coord_house[i], 300))
        nr1 += 1

    C0 = Cable('C0')
    C0.add_route(1, 1)
    C0.add_route(1, 4)
    C0.add_route(4, 4)
    kanaleneiland.add_cable(C0)

    print(kanaleneiland)


if __name__ == "__main__":
    main()