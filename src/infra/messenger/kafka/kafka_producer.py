import os
import json

from src.application.interfaces.providers.messenger import ProducerMessenger

from kafka import KafkaProducer as KafkaProducerClient


class KafkaProducer(ProducerMessenger):
    """Inplementation of Producer Messenger for Kafka"""

    client: KafkaProducerClient

    def __init__(self):
        self.client = KafkaProducerClient(
            bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def produce(self, to: str, data: dict):
        """Produce an message to the given topic
        @paramns:
            - to: Kafka topic
            - data: message content. Must be type bytes, or be serializable to bytes

        @Returns:
            FutureRecordMetadata: resolves to RecordMetadata

        @Raises:
            KafkaTimeoutError: if unable to fetch topic metadata, or unable
                to obtain memory buffer prior to configured max_block_ms

        """
        return self.client.send(topic=to, value=data)
