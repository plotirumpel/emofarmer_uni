class Drawing:
    def __init__(self, length, height, symbol):
        self.image = [[symbol] * length for i in range (height)]
        print (self.image)

    def print(self):
        for row in self.image:
            for elem in row:
                print(elem, end=' ')
            print()

    def setPoint(self, x, y, symb='x'):
        self.image[y-1][x-1] = symb
        return

    def drawVerticalLine(self, x, y1, y2, symb='x'):
        for y in range (y1-1, y2):
            self.image[y][x-1] = symb

    def drawHorizontalLine(self, y, x1, x2, symb='x'):
        for x in range(x1-1, x2):
            self.image[y-1][x] = symb

    def drawRectangle(self, length, height, symb='x'):
        self.drawVerticalLine(1, 1, height, symb)
        self.drawVerticalLine(length, 1, height, symb)
        self.drawHorizontalLine(1, 1, length, symb)
        self.drawHorizontalLine(height, 1, length, symb)

    def draw_line(self, x1=0, y1=0, x2=0, y2=0, symb='x'):
        delta_x = x2 - x1
        delta_y = y2 - y1
        if delta_x > 0:
            sign_x = 1
        elif delta_x == 0:
            sign_x = 0
        else:
            sign_x = -1
            delta_x = - delta_x
        if delta_y > 0:
            sign_y = 1
        elif delta_y == 0:
            sign_y = 0
        else:
            sign_y = -1
            delta_y = -delta_y
        if delta_x > delta_y:
            pdx, pdy = sign_x, 0
            es, el = delta_y, delta_x
        else:
            pdx, pdy = 0, sign_y
            es, el = delta_x, delta_y
        x, y = x1, y1
        error, t = el/2, 0
        self.setPoint(x, y, symb)
        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            self.setPoint(x, y, symb)

    def draw_circle (self,x1,y1,r,symb='x'):
        x, y = 0, r
        gap = 0
        delta = 2 - 2 * r
        while y >= 0:
            self.setPoint(x1 + x, y1 + y, symb)
            self.setPoint(x1 + x, y1 - y, symb)
            self.setPoint(x1 - x, y1 + y, symb)
            self.setPoint(x1 - x, y1 - y, symb)
            gap = 2 * (delta + y) - 1
            if delta < 0 and gap <= 0:
                x+=1
                delta += 2 * x + 1
                continue
            if delta > 0 and gap > 0:
                y -=1
                delta -= 2 * y + 1
                continue
            x +=1
            delta += 2 * (x - y)
            y -=1

img = Drawing(10, 9, '.')
img.draw_circle(5,5,2)
#img.drawHorizontalLine(2, 5, 7, 'x')
#img.drawVerticalLine(2, 5, 7, 'x')
img.print()
