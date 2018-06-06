#-*- coding:utf-8 -*-
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.206.126'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')
#不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
# 获取随机的queue名字
queue_name = result.method.queue
print("random queuename:", queue_name)

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name, # queue绑定到转发器上
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
