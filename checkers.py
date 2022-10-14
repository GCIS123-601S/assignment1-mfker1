import Asignment3.pixart as pixart

def draw_row(red,black):
    for i in range(10):
        for color in (red, black):
            pixart.draw_pixel(color)

def draw_checker():
        draw_row("red","black")
        pixart.move(1,0)
        draw_row("black","red")
        pixart.move(2,0)
        draw_row("red","black")
        pixart.move(3,0)
        draw_row("black","red")
        pixart.move(4,0)
        draw_row("red","black")
        pixart.move(5,0)
        draw_row("black","red")
        pixart.move(6,0)
        draw_row("red","black")
        pixart.move(7,0)
        draw_row("black","red")
        pixart.move(8,0)
        draw_row("red","black")
        pixart.move(9,0)
        draw_row("black","red")
        pixart.move(10,0)
        draw_row("red","black")
        pixart.move(11,0)
        draw_row("black","red")
        pixart.move(12,0)
        draw_row("red","black")
        pixart.move(13,0)
        draw_row("black","red")
        pixart.move(14,0)
        draw_row("red","black")
        pixart.move(15,0)
        draw_row("black","red")
        pixart.move(16,0)
        draw_row("red","black")
        pixart.move(17,0)
        draw_row("black","red")
        pixart.move(18,0)
        draw_row("red","black")
        pixart.move(19,0)
        draw_row("black","red")
        pixart.move(20,0)

def main():
    pixart.initialize()
    draw_checker()

main()