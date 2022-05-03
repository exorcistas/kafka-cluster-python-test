import json
from kafka import KafkaProducer
from loguru import logger
import random
import string
import time

class MessageProducer:
    def __init__(self, broker):
        self.producer = KafkaProducer(bootstrap_servers=broker,
                        value_serializer = lambda v: json.dumps(v).encode('utf-8'),
                        acks='all',
                        retries = 3)
        logger.info(f'KafkaProducer initialized on broker: {broker}')

    def send_msg(self, topic, msg):
        logger.info(f'Sending {msg}')
        try:
            future = self.producer.send(topic, msg)
            self.producer.flush()
            future.get(timeout=60)
            logger.info('Message sent successfully!')
            return {'status_code':200, 'error':None}

        except Exception as ex:
            logger.exception(f'Error: {ex}')
            return ex

def generate_message(user_ids, recipient_ids) -> dict:
    generated_user_id = random.choice(user_ids)
    recipient_ids_copy = recipient_ids.copy()
    recipient_ids_copy.remove(generated_user_id)
    generated_recipient_id = random.choice(recipient_ids_copy)

    message = ''.join(random.choice(string.ascii_letters) for i in range(32))
    return {
        'user id': generated_user_id,
        'recipient id': generated_recipient_id,
        'message': message
    }


if __name__ == '__main__':
    broker = 'localhost:9092'
    topic = 'sample'
    producer = MessageProducer(broker)

    user_ids = list(range(1,101))
    recipient_ids = list(range(1,101))

    while True:
        data = generate_message(user_ids, recipient_ids)
        resp = producer.send_msg(topic, data)
        time.sleep(2)