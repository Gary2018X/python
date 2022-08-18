# 工厂模式

## 工厂模式的定义

工厂方法模式(Factory Method Pattern)：定义一个用于创建对象的接口，让子类决定将哪一个类实例化。工厂方法模式让一个类的实例化延迟到其子类。工厂方法模式又简称为工厂模式(Factory Pattern)，又可称作虚拟构造器模式(Virtual Constructor Pattern)或多态工厂模式(Polymorphic Factory Pattern)。
   与简单工厂模式相比，工厂方法模式最重要的区别是引入了抽象工厂角色，抽象工厂可以是接口，也可以是抽象类或者具体类。

## 工厂模式的示例

代码中抽象了一个公共类Animal抽象dog、cat公共的方法、两个具体类dog、cat实现Animal以及一个工厂类animalFactory控制具体类的生成。

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

# 抽象工厂类
class animalFactory():

    def create(self):
        pass

# 具体工厂类
class DogFactory(animalFactory):
    def create(self):
        return dog()

# 具体工厂类
class CatFactory(animalFactory):
    def create(self):
        return cat()


if __name__ == "__main__":
    DOG = DogFactory()
    dog = DOG.create(dog)
    print(dog.get_name(), dog.get_weight())  # dog 40.0



```

## 工厂模式的优点

(1) 在工厂方法模式中，工厂方法用来创建客户所需要的产品，同时还向客户隐藏了哪种具体产品类将被实例化这一细节，用户只需要关心所需产品对应的工厂，无须关心创建细节，甚至无须知道具体产品类的类名。

   (2) 基于工厂角色和产品角色的多态性设计是工厂方法模式的关键。它能够让工厂可以自主确定创建何种产品对象，而如何创建这个对象的细节则完全封装在具体工厂内部。工厂方法模式之所以又被称为多态工厂模式，就正是因为所有的具体工厂类都具有同一抽象父类。

(3) 使用工厂方法模式的另一个优点是在系统中加入新产品时，无须修改抽象工厂和抽象产品提供的接口，无须修改客户端，也无须修改其他的具体工厂和具体产品，而只要添加一个具体工厂和具体产品就可以了，这样，系统的可扩展性也就变得非常好，完全符合“开闭原则”。

## 工厂模式的缺点

(1) 在添加新产品时，需要编写新的具体产品类，而且还要提供与之对应的具体工厂类，系统中类的个数将成对增加，在一定程度上增加了系统的复杂度，有更多的类需要编译和运行，会给系统带来一些额外的开销。

 (2) 由于考虑到系统的可扩展性，需要引入抽象层，在客户端代码中均使用抽象层进行定义，增加了系统的抽象性和理解难度，且在实现时可能需要用到DOM、反射等技术，增加了系统的实现难度。

## 工厂模式的适用场景

 (1) 客户端不知道它所需要的对象的类。在工厂方法模式中，客户端不需要知道具体产品类的类名，只需要知道所对应的工厂即可，具体的产品对象由具体工厂类创建，可将具体工厂类的类名存储在配置文件或数据库中。

 (2) 抽象工厂类通过其子类来指定创建哪个对象。在工厂方法模式中，对于抽象工厂类只需要提供一个创建产品的接口，而由其子类来确定具体要创建的对象，利用面向对象的多态性和里氏代换原则，在程序运行时，子类对象将覆盖父类对象，从而使得系统更容易扩展。
