import pika, json

params = pika.URLParameters('amqps://csmzdbia:5IGG1qeiX6ACePGZ8223WDt4SRn1lu11@albatross.rmq.cloudamqp.com/csmzdbia') 
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange='orders', exchange_type="fanout",
                                      passive=False,
                                      durable=False,
                                      auto_delete=False)

def callback(ch, method, properties, body):
    print('Received in User microservice')
    print(body)
   
channel.basic_consume(queue='orders', on_message_callback=callback, \
auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()