# # Exercise 2

# class Languege:
#     def gretting(self):
#         pass


# class English(Languege):
#     def gretting(self):
#         print("hello by english")


# class Spanish(Languege):
#     def gretting(self):
#         print("Hello by spanish")

    
# def hello_friend(languege1:Languege, languege2:Languege):
#     languege1.gretting()
#     languege2.gretting()


# english = English()
# spanish = Spanish()
# hello_friend(spanish,english)

#Exercise 4

# class Base:

#     def method():
#         print("Hello from Base")

#     @classmethod
#     def classmethod(cls):
#         cls.method()


# class Child(Base):

#     def method():
#         print("Hello from Child")

#     @classmethod
#     def classmethod(cls):
#         cls.method()


# Child.classmethod()
# Base.classmethod()


#Exircise 5 

# example_7.py
from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)
    
class Cone(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))
        self.draw1.polygon([(75, 150), (175, 150), (125, 300)], fill="yellow")
        self.draw1.polygon([(225, 150), (175, 150), (125, 300)], fill=self.back_color)
        self.draw1.polygon([(75, 150), (1, 150), (125, 300)], fill=self.back_color)
        # self.draw1.line((20,20,50,50), fill="yellow")

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with cone was created")
        return self.im.save('draw-cone.png', quality=95)
    
    
class Paraboloid(Shape):
    @staticmethod
    def pointTo2D(x:int, y:int):
            z = x**2 - y**2
            x_proj = x / (z + 100) + 210
            y_proj = y / (z + 100) + 210
            return (x_proj,y_proj)


    def draw(self):
        # self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))
        # self.draw1.polygon([(75, 150), (75,400), (175, 400), (175, 150)], fill="yellow")
        # self.draw1.polygon([(225, 150), (175, 150), (125, 300)], fill=self.back_color)
        # self.draw1.polygon([(75, 150), (1, 150), (125, 300)], fill=self.back_color)
        # self.draw1.line((20,20,50,50), fill="yellow")
        for x in range(-200,200,1):
            for y in range(-200,200,1):
                # point1 = Paraboloid.pointTo2D(x,y)
                # point2 = Paraboloid.pointTo2D(x+2,y)
                # point3 = Paraboloid.pointTo2D(x+2,y+2)
                # point4 = Paraboloid.pointTo2D(x,y+2)
                # self.draw1.polygon([point1, point2, point3, point4], outline=(255, 255, 255))
                z = x**2 - y**2
                if (z >= 0):
                    color = (int((z/30000)*255),0,0)
                if (z < 0):
                    color = (0,0,int((-z/30000)*255))

                self.draw1.point((x + 220,y + 220),fill = color)


                # z = x**2 - y**2
                # x_proj = x / (z + 5)
                # y_proj = y / (z + 5)
                # z = (x+5)**2 - (y)**2

                # x_proj1 = (x+5) / (z + 5)
                # y_proj1 = (y) / (z + 5)
                # self.draw1.polygon([(x_proj, y_proj), (x_proj,y_proj1), (x_proj1, y_proj1), (x_proj1, y_proj)], outline=(255, 255, 255))
                # self.draw1.rectangle
                # self.draw1.polygon
        # self.draw1.polygon([(20, 20), (20,30), (30, 30), (30, 20)], fill="yellow")



    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with cone was created")
        return self.im.save('draw-cone.png', quality=95)




def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                          '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник\n\t'
                          '8. Вихід з програми\nОберіть необхідний пункт меню: '))
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                c = Circle()
                update_obj(c)
            case 6:
                sq = Square()
                update_obj(sq)
            case 7:
                t = Triangle()
                update_obj(t)
            case 8:
                break
            case 9:
                co = Cone()
                work_with_obj(co)
            case 10:
                co = Cone()
                update_obj(co)
            case 11:
                pa = Paraboloid()
                work_with_obj(pa)
            case 12:
                pa = Paraboloid()
                update_obj(pa)
            case _:
                print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()
