#-*- coding:utf-8 -*-

import pika,time,json

def sendToMQ(queueName='',body=''):

    #make a subj
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.206.126'))

    # 声明一个管道，在管道里发消息
    channel = connection.channel()

    # 在管道里声明queue
    channel.queue_declare(queue=queueName)
    # RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
    channel.basic_publish(exchange='',
                          routing_key='msg_pyque',
                          body=body,
                          properties=pika.BasicProperties(
                             delivery_mode=2,  # make message persistent
                              #correlation_id=corr_id
                          )
                          )
    print("[x] Send %s",body)
    connection.close() # 队列关闭


if __name__ == '__main__':

    for i in range(1,50):
        body = json.dumps({ 'a' : i, 'b' : i*10, 'c' : 3, 'd' : 4, 'e' : 5 })
        sendToMQ('msg_pyque',body)
        time.sleep(5)
