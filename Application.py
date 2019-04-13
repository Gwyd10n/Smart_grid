# Test classes
from Classes.Grid import Grid
from Classes.Battery import Battery
from Classes.House import House

def main():
    kanaleneiland = Grid(1, 500, 500)
    coord_bat = [50, 100, 200, 300, 400, 450]
    for i in range(len(coord_bat)):
        kanaleneiland.add_battery(Battery(i, coord_bat[i], coord_bat[i], 1500), i)

    coord_house = [5, 10, 20, 30, 40, 60, 80, 90, 110, 120, 130, 140, 150, 160, 170, 180, 190]
    for i in range(len(coord_house)):
        kanaleneiland.add_house(House(i, coord_house[i], coord_house[i], 300), i)

    print(kanaleneiland)

if __name__ == "__main__":
    main()