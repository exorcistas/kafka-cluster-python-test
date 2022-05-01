from kafka import KafkaConsumer
from loguru import logger

producer = KafkaConsumer(
    bootstrap_servers = ['localhost:9092']
)

consumer = KafkaConsumer("sample")
logger.info(f'KafkaConsumer initialized under topic name: sample')

for msg in consumer:
    logger.info(f'Received message: {msg}')   #msg.value