import turtle as tur


def make_grid(rows, columns):
    tur.color('black', 'white')
    tur.begin_fill()
    dir = 1
    tur.forward(20 * columns)
    for _ in range(rows):
        if dir > 0:
            tur.right(90)
            tur.forward(20)
            tur.right(90)
            tur.forward(20 * columns)
        else:
            tur.left(90)
            tur.forward(20)
            tur.left(90)
            tur.forward(20 * columns)
        dir *= -1
    tur.penup()
    tur.home()
    tur.pendown()
    tur.right(90)
    dir = 1
    tur.forward(20 * rows)
    for _ in range(columns):
        if dir > 0:
            tur.left(90)
            tur.forward(20)
            tur.left(90)
            tur.forward(20 * rows)
        else:
            tur.right(90)
            tur.forward(20)
            tur.right(90)
            tur.forward(20 * rows)
        dir *= -1
    tur.end_fill()
    tur.done()


make_grid(10, 10)
