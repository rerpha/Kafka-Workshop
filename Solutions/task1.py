from pykafka import KafkaClient

client = KafkaClient("hinata.isis.cclrc.ac.uk:9092")

print(client.topics)
