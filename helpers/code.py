#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert


def get_man(coord_house, coord_battery):
    manhattan_dist = abs(coord_house[0] - coord_battery[0]) + abs(coord_house[1] - coord_battery[1])
    return manhattan_dist
