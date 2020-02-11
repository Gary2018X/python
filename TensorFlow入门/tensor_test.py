#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gary
import tensorflow as tf
import matplotlib.pyplot  as plt#数据可视化
import numpy as np#数据格式化
import datetime
class LeNet(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.conv_layer_1=tf.keras.layers.Conv2D(filters=6,kernel_size=(5,5),padding='valid',activation=tf.nn.relu)#卷积层一
        self.pool_layer_1=tf.keras.layers.MaxPooling2D(pool_size=(2,2),padding='same')#池化层一
        self.conv_layer_2=tf.keras.layers.Conv2D(filters=16,kernel_size=(5,5),padding='valid',activation=tf.nn.relu)#卷积层二
        self.pool_layer_2=tf.keras.layers.MaxPooling2D(padding='same')#池化层二
        self.flatten=tf.keras.layers.Flatten()#展平
        self.fc_layer_1=tf.keras.layers.Dense(units=120,activation=tf.nn.relu)#连接层
        self.fc_layer_2 = tf.keras.layers.Dense(units=84, activation=tf.nn.relu)#连接层
        self.output_layer = tf.keras.layers.Dense(units=10, activation=tf.nn.softmax)#输出层

    def call(self,inputs):#batch_size28*28*1
        x=self.conv_layer_1(inputs)
        x=self.pool_layer_1(x)
        x=self.conv_layer_2(x)
        x=self.pool_layer_2(x)
        x=self.flatten(x)
        x=self.fc_layer_1(x)
        x=self.fc_layer_2(x)
        output=self.output_layer (x)
        return output
class recon():
    # 初始化数据
    def __init__(self):
        self.mnist = tf.keras.datasets.mnist
        (self.x_train, self.y_train), (self.x_test, self.y_test) = self.mnist.load_data()#加载数据
        # 查看图片是否加载正确
        # image_index=1234#
        # plt.imshow(x_train[image_index])
        # plt.show()
        # print(y_train[image_index])

        # 填充数据集28*28变为32*32
        self.x_train = np.pad(self.x_train, ((0, 0), (2, 2), (2, 2)), 'constant', constant_values=0)  # 设置填充值为0
        self.x_test = np.pad(self.x_test, ((0, 0), (2, 2), (2, 2)), 'constant', constant_values=0)  # 设置填充值为0
        # print(x_train.shape)

        # 数据类型转化为float32
        self.x_train = self.x_train.astype('float32')
        self.x_test = self.x_test.astype('float32')

        # 数据正则化
        self.x_train /= 255
        self.x_test /= 255

        # 数据维度转换（n，h，w，c）
        self.x_train = self.x_train.reshape(self.x_train.shape[0], 32, 32, 1)
        self.x_test = self.x_test.reshape(self.x_test.shape[0], 32, 32, 1)
        # print(x_train.shape)

        self.model=None
        # 超参数训练
        self.num_epochs = 10
        self.batch_size = 64  # 需要调整
        self.learning_rate = 0.001

    #实例化
    def create_model(self):
        # 模型实例化
        # self.model=LeNet()#可以自建model，也可以使用Sequential方式
        self.model = tf.keras.models.Sequential([
            # 第一层卷积层 卷积核核数为6,卷积核大小为5*5.填充方式为舍弃,激活函数,输入数据格式为32,32,1
            tf.keras.layers.Conv2D(filters=6, kernel_size=(5, 5), padding='valid', activation=tf.nn.relu,
                                   input_shape=(32, 32, 1)),  # padding,valid是舍弃,same是增加
            # 第二层 池化层,池化层大小2*2,strides步长2
            tf.keras.layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'),
            tf.keras.layers.Conv2D(filters=16, kernel_size=(5, 5), padding='valid', activation=tf.nn.relu),
            tf.keras.layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'),
            # 展平类,多维数据变为一维
            tf.keras.layers.Flatten(),
            # 全连接层
            tf.keras.layers.Dense(units=120, activation=tf.nn.relu),
            tf.keras.layers.Dense(units=84, activation=tf.nn.relu),
            tf.keras.layers.Dense(units=10, activation=tf.nn.softmax)
        ])
        # 模型展示
        self.model.summary()
        # return model

    # 编译
    def compile_model(self):
        # 第二部分 模型训练

        # 优化器
        adam_optimizer=tf.keras.optimizers.Adam(self.learning_rate)
        #编译模型
        self.model.compile(optimizer=adam_optimizer,loss=tf.keras.losses.sparse_categorical_crossentropy,metrics=['accuracy'])

    #训练
    def fit_model(self):
        # 训练模型
        start = datetime.datetime.now()
        self.model.fit(x=self.x_train, y=self.y_train, batch_size=self.batch_size, epochs=self.num_epochs)
        end = datetime.datetime.now()
        time_cost = end - start
        print('time cost={}'.format(time_cost))

    # 保存
    def save_model(self):
        # 保存模型
        self.model.save(filepath='my_model.h5')

    # 加载
    def restore_model(self):
        # 加载模型
        self.model = tf.keras.models.load_model('my_model.h5')
        self.model.summary()

    # 评估
    def evaluate_model(self):
        # 模型评估
        print(self.model.evaluate(self.x_test, self.y_test))  # 输出损失率和准确率

    # 预测
    def predict_model(self,image_index):
        # 模型预测
        print(self.x_test[image_index].shape)
        plt.imshow(self.x_test[image_index].reshape(32, 32), cmap='Greys')
        plt.show()
        pred = self.model.predict(self.x_test[image_index].reshape(1, 32, 32, 1))
        print(pred.argmax())

if __name__ == '__main__':
        con=recon()
        con.create_model()#模型实例化
        con.compile_model()#新建模型训练
        # con.restore_model()#加载模型训练
        con.fit_model()#训练模型
        con.save_model()#保存模型
        con.evaluate_model()#评估模型
        con.predict_model(image_index = 5200)#预测模型
