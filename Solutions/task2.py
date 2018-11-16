from confluent_kafka import Producer, Consumer
import uuid

config = {'bootstrap.servers': 'hinata.isis.cclrc.ac.uk', 'default.topic.config': {'auto.offset.reset': 'earliest'}, 'group.id': uuid.uuid4()}

# Set up the consumer with the above configuration
cons = Consumer(config)

# Subscribe to list of topics
cons.subscribe(['test_jack_workshop'])

# Set up the producer
prod = Producer(config)

# Produce a message onto a specified topic
prod.produce('test_jack_workshop', "hello world")

# Poll the topic - returns a msg object which has a key, value, timestamp etc
msg = cons.poll()

print(msg.value)
