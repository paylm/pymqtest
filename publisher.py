#-*- coding:utf-8 -*-
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.206.126'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',# 声明广播管道
                         exchange_type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!123'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()