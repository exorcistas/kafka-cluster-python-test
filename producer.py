from kafka import KafkaProducer
#from json import dumps
import json
from loguru import logger


class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
                        value_serializer = lambda v: json.dumps(v).encode('utf-8'),
                        acks='all',
                        retries = 3)
        logger.info(f'KafkaProducer initialized under topic name: {topic}')

    def send_msg(self, msg):
        logger.info(f'Sending {msg}')
        try:
            future = self.producer.send(self.topic, msg)
            self.producer.flush()
            future.get(timeout=60)
            logger.info('Message sent successfully!')
            return {'status_code':200, 'error':None}

        except Exception as ex:
            logger.exception(f'Error: {ex}')
            return ex


if __name__ == '__main__':
    broker = 'localhost:9092'
    topic = 'sample'
    producer = MessageProducer(broker, topic)

    data = {'name':'abc', 'email':'abc@example.com'}
    resp = producer.send_msg(data)