# pymqtest

for rabbitmq demo

1 . RabbitMQ 消息分发轮询
  上面的只是一个生产者、一个消费者，能不能一个生产者多个消费者呢？ 
  可以上面的例子，多启动几个消费者consumer，看一下消息的接收情况。 
  采用轮询机制；把消息依次分发
  假如消费者处理消息需要15秒，如果当机了，那这个消息处理明显还没处理完，怎么处理？ 
  （可以模拟消费端断了，分别注释和不注释 no_ack=True 看一下） 
  你没给我回复确认，就代表消息没处理完。
  上面的效果消费端断了就转到另外一个消费端去了，但是生产者怎么知道消费端断了呢？ 
  因为生产者和消费者是通过socket连接的，socket断了，就说明消费端断开了。


  上述例术未实现queue 队列持久化，故重启rabbitmq 时会导致未消费的消息丢失

  此模型见producer.py 和 consumer.py


2 . 消息播模式：
  前面的效果都是一对一发，如果做一个广播效果可不可以，这时候就要用到exchange了 
  exchange必须精确的知道收到的消息要发给谁。exchange的类型决定了怎么处理， 
  类型有以下几种：

  fanout: 所有绑定到此exchange的queue都可以接收消息
  direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
  topic： 所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息
  
  topic 例子见 publisher.py和subscriber.py
