from itertools import islice
from math import ceil
from pykafka import KafkaClient


client = KafkaClient(hosts="hinata.isis.cclrc.ac.uk:9092")

topic = client.topics[b'workshop_task4']

consumer = topic.get_simple_consumer(consumer_group=b"mygroup")

LAST_N_MESSAGES = 51
# how many messages should we get from the end of each partition?
MAX_PARTITION_REWIND = int(ceil(LAST_N_MESSAGES / len(consumer._partitions)))
# find the beginning of the range we care about for each partition
offsets = [(p, op.last_offset_consumed - MAX_PARTITION_REWIND)
           for p, op in consumer._partitions.items()]
# if we want to rewind before the beginning of the partition, limit to beginning
offsets = [(p, (o if o > -1 else -2)) for p, o in offsets]
# reset the consumer's offsets
consumer.reset_offsets(offsets)
for message in islice(consumer, LAST_N_MESSAGES):
    print(message.offset, message.value)
