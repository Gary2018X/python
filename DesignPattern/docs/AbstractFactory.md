# 抽象工厂模式

我们先引入两个概念：

   (1) 产品等级结构：产品等级结构即产品的继承结构，如一个抽象类是电视机，其子类有海尔电视机、海信电视机、TCL电视机，则抽象电视机与具体品牌的电视机之间构成了一个产品等级结构，抽象电视机是父类，而具体品牌的电视机是其子类。

(2) 产品族：在抽象工厂模式中，产品族是指由同一个工厂生产的，位于不同产品等级结构中的一组产品，如海尔电器工厂生产的海尔电视机、海尔电冰箱，海尔电视机位于电视机产品等级结构中，海尔电冰箱位于电冰箱产品等级结构中，海尔电视机、海尔电冰箱构成了一个产品族。
抽象工厂模式是所有形式的工厂模式中最为抽象和最具一般性的一种形式。抽象工厂模式与工厂方法模式最大的区别在于，工厂方法模式针对的是一个产品等级结构，而抽象工厂模式需要面对多个产品等级结构，一个工厂等级结构可以负责多个不同产品等级结构中的产品对象的创建。当一个工厂等级结构可以创建出分属于不同产品等级结构的一个产品族中的所有对象时，抽象工厂模式比工厂方法模式更为简单、更有效率。

## 抽象工厂模式的定义

抽象工厂模式(Abstract Factory Pattern)：提供一个创建一系列相关或相互依赖对象的接口，而无须指定它们具体的类。抽象工厂模式又称为Kit模式。
在抽象工厂中声明了多个工厂方法，用于创建不同类型的产品，抽象工厂可以是接口，也可以是抽象类或者具体类

## 抽象工厂模式的示例

我的这个示例代码可能有点难懂 可以参考参考链接4和5

```python
# 抽象产品类
class Animal():
    name = ""
    weight = 0.0
    type = "Animal"

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.price = weight

    def get_name(self):
        return self.name

# 具体产品类
class dog(Animal):
    def __init__(self):
        self.name = "dog"
        self.weight = 40.0


# 具体产品类
class cat(Animal):
    def __init__(self):
        self.name = "cat"
        self.weight = 5.0

# 抽象产品类
class Animal1():
    name = ""
    weight = 0.0
    type = "Animal1"

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.price = weight

    def get_name(self):
        return self.name

# 具体产品类
class dog1(Animal1):
    def __init__(self):
        self.name = "dog1"
        self.weight = 410.0


# 具体产品类
class cat1(Animal1):
    def __init__(self):
        self.name = "cat1"
        self.weight = 51.0

# 抽象工厂类
class animalFactory():
    def create_dog(self):
        pass

    def create_cat(self):
        pass

# 具体工厂类
class Factory(animalFactory):

    def create_dog(self):
        animalIns = dog()
        return animalIns

    def create_cat(self):
        animalIns = cat()
        return animalIns

# 具体工厂类
class Factory1(animalFactory):

    def create_dog(self):
        animalIns = dog1()
        return animalIns

    def create_cat(self):
        animalIns = cat1()
        return animalIns


if __name__ == "__main__":
    DOG = Factory1()
    dog = DOG.create_cat()
    print(dog.get_name(), dog.get_weight())  # dog 40.0

```

## 抽象工厂模式的优点

(1) 抽象工厂模式隔离了具体类的生成，使得客户并不需要知道什么被创建。由于这种隔离，更换一个具体工厂就变得相对容易，所有的具体工厂都实现了抽象工厂中定义的那些公共接口，因此只需改变具体工厂的实例，就可以在某种程度上改变整个软件系统的行为。

 (2) 当一个产品族中的多个对象被设计成一起工作时，它能够保证客户端始终只使用同一个产品族中的对象。

(3) 增加新的产品族很方便，无须修改已有系统，符合“开闭原则”。

## 抽象工厂模式的缺点

增加新的产品等级结构麻烦，需要对原有系统进行较大的修改，甚至需要修改抽象层代码，这显然会带来较大的不便，违背了“开闭原则”。

## 抽象工厂模式的适用场景

 (1) 一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节，这对于所有类型的工厂模式都是很重要的，用户无须关心对象的创建过程，将对象的创建和使用解耦。

 (2) 系统中有多于一个的产品族，而每次只使用其中某一产品族。可以通过配置文件等方式来使得用户可以动态改变产品族，也可以很方便地增加新的产品族。

(3) 属于同一个产品族的产品将在一起使用，这一约束必须在系统的设计中体现出来。同一个产品族中的产品可以是没有任何关系的对象，但是它们都具有一些共同的约束，如同一操作系统下的按钮和文本框，按钮与文本框之间没有直接关系，但它们都是属于某一操作系统的，此时具有一个共同的约束条件：操作系统的类型。

 (4) 产品等级结构稳定，设计完成之后，不会向系统中增加新的产品等级结构或者删除已有的产品等级结构。

## 工厂模式总结

简单工厂 ： 用来生产同一等级结构中的任意产品。（不支持拓展增加产品）

工厂方法 ：用来生产同一等级结构中的固定产品。（支持拓展增加产品）

抽象工厂 ：用来生产不同产品族的全部产品。（支持拓展增加产品；支持增加产品族）  

简单工厂的适用场合：只有伦敦工厂（只有这一个等级），并且这个工厂只生产三种类型的pizza：chesse,pepper,greak（固定产品）。

工厂方法的适用场合：现在不光有伦敦工厂，还增设了纽约工厂（仍然是同一等级结构，但是支持了产品的拓展），这两个工厂依然只生产三种类型的pizza：chesse,pepper,greak（固定产品）。

抽象工厂的适用场合：不光增设了纽约工厂（仍然是同一等级结构，但是支持了产品的拓展），这两个工厂还增加了一种新的类型的pizza：chinese pizza（增加产品族）。
