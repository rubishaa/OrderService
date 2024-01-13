import pika, json
import config as config

params = pika.URLParameters(config.MQ_URL) 
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange='orders', exchange_type="fanout",
                                      passive=False,
                                      durable=False,
                                      auto_delete=False)

def publish_orderMsg(method, body):
    try:
        properties = pika.BasicProperties(method)
        channel.basic_publish(exchange='orders', routing_key='created_order', body=json.dumps(body), properties=properties)
        return True
    except Exception as e:
        print(f"The error '{e}' occurred.")
        return False