from pykafka import KafkaClient
from pykafka.common import OffsetType

client = KafkaClient(hosts="hinata.isis.cclrc.ac.uk:9092")

topic = client.topics[b"test_jack_workshop"]

consumer = topic.get_simple_consumer(consumer_group=b"mygroup", auto_offset_reset=OffsetType.LATEST,
                                     reset_offset_on_start=True)

# Set up the producer
producer = topic.get_producer()

# Produce a message onto a specified topic
producer.produce(b"hello world")

# Poll the topic - returns a msg object which has a key, value, timestamp etc
msg = consumer.consume()

print(msg.value)
