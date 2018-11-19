# offsets


# offset reset

# partitions

from pykafka import KafkaClient


client = KafkaClient(hosts="hinata.isis.cclrc.ac.uk:9092")

topic = client.topics[b'workshop_task4']

consumer = topic.get_simple_consumer(consumer_group=b"mygroup")

partition = topic.partitions[0]
consumer.reset_offsets([(partition, 11)])

for i in range(4):
    msg = consumer.consume()
    print(msg.value)
