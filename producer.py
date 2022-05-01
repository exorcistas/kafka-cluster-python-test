from json import dumps
from kafka import KafkaProducer
from loguru import logger

def serializer(message):
    return json.dumps(message).encode('utf-8')

if __name__ == '__main__':
    # initializing the Kafka producer
    producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092'],
        value_serializer = serializer
    )

    url = 'https://www.internetwache-polizei-berlin.de/vdb/Fahrraddiebstahl.csv'
    with open('testdata.csv',encoding='utf-8') as infile:
        data = infile.readlines()
    logger.info('Sending data to kafka under topic name `biketheft`')
    for d in data:
        producer.send('biketheft', d)
        logger.info(f'Sending {d}')