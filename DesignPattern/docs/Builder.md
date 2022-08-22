# 建造者模式

## 建造者模式的定义

建造者模式(Builder Pattern)：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。

## 建造者模式的示例

```python
class Burger():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0


class Snack():
    name = ""
    price = 0.0
    type = "SNACK"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class orderBuilder():
    # 抽象建造类
    bBurger = ""
    bSnack = ""
    bBeverage = ""

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return order(self)


class orderDirector():
    # 指挥类
    order_builder = ""

    def __init__(self, order_builder):
        self.order_builder = order_builder

    def createOrder(self, burger, snack, beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()


class order():
    # 具体建造类
    burger = ""
    snack = ""
    beverage = ""

    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print("Burger:%s" % self.burger.getName())
        print("Snack:%s" % self.snack.getName())
        print("Beverage:%s" % self.beverage.getName())


if __name__ == "__main__":
    order_builder = orderBuilder()
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())
    order_1 = order_builder.build()
    order_1.show()
    # 引入指挥者
    order_director = orderDirector(order_builder=order_builder)
    order_2 = order_director.createOrder(spicyChickenBurger(), chips(), milk())
    order_2.show()

```

## 建造者模式的优点

(1) 在建造者模式中，客户端不必知道产品内部组成的细节，将产品本身与产品的创建过程解耦，使得相同的创建过程可以创建不同的产品对象。

(2) 每一个具体建造者都相对独立，而与其他的具体建造者无关，因此可以很方便地替换具体建造者或增加新的具体建造者，用户使用不同的具体建造者即可得到不同的产品对象。由于指挥者类针对抽象建造者编程，增加新的具体建造者无须修改原有类库的代码，系统扩展方便，符合“开闭原则”

(3) 可以更加精细地控制产品的创建过程。将复杂产品的创建步骤分解在不同的方法中，使得创建过程更加清晰，也更方便使用程序来控制创建过程。

## 建造者模式的缺点

(1) 建造者模式所创建的产品一般具有较多的共同点，其组成部分相似，如果产品之间的差异性很大，例如很多组成部分都不相同，不适合使用建造者模式，因此其使用范围受到一定的限制。

(2) 如果产品的内部变化复杂，可能会导致需要定义很多具体建造者类来实现这种变化，导致系统变得很庞大，增加系统的理解难度和运行成本。

## 建造者模式的适用场景

(1) 需要生成的产品对象有复杂的内部结构，这些产品对象通常包含多个成员属性。

(2) 需要生成的产品对象的属性相互依赖，需要指定其生成顺序。

(3) 对象的创建过程独立于创建该对象的类。在建造者模式中通过引入了指挥者类，将创建过程封装在指挥者类中，而不在建造者类和客户类中。

(4) 隔离复杂对象的创建和使用，并使得相同的创建过程可以创建不同的产品。
