from pykafka import KafkaClient


client = KafkaClient(hosts="hinata.isis.cclrc.ac.uk:9092")

topic = client.topics[b'ConsumeFromMe']

consumer = topic.get_simple_consumer(consumer_group=b"mygroup")

msg = consumer.consume()

print(msg.value)
