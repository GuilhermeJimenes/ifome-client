from time import sleep

import pika

from src.domain.constants import HOST_MESSAGE_BROKER
from src.exceptions.custom_exceptions import RabbitMQError


class RabbitMQ:
    def __init__(self):
        self.host = HOST_MESSAGE_BROKER
        self.connection, self.channel = self.connect()
        self.method_frame = None

    def connect(self):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
            channel = connection.channel()
            return connection, channel
        except Exception as error:
            print(error)
            raise RabbitMQError("Error connecting to RabbitMQ.") from error

    def validate_connection(self):
        if self.connection is None or self.channel is None:
            raise RabbitMQError("Connection and channel must be configured before consuming")

    def new_queue(self, queue_name):
        try:
            self.channel.queue_declare(queue=queue_name)
        except Exception as error:
            print(error)
            raise RabbitMQError("Error creating queue in RabbitMQ.") from error

    def publish(self, queue_name, message):
        try:
            self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)
            print("Published message.")
        except Exception as error:
            print(error)
            raise RabbitMQError("Error publishing message to RabbitMQ.") from error

    def consume_success(self):
        """if not called, the message goes back to the queue"""
        self.channel.basic_ack(delivery_tag=self.method_frame.delivery_tag)

    def consumer(self, queue_name):
        try:
            while True:
                sleep(2)
                if not self.method_frame:
                    self.method_frame, header_frame, body = self.channel.basic_get(queue=queue_name)
                else:
                    return body.decode()
        except Exception as error:
            print(error)
            raise RabbitMQError("Error consuming message from RabbitMQ.")

    def start_consuming(self, queue_name):
        try:
            self.validate_connection()
            message_received = self.consumer(queue_name)
            self.stop_consuming()
            return message_received
        except Exception as error:
            print(error)
            raise RabbitMQError("Error consuming message from RabbitMQ.")

    def stop_consuming(self):
        if self.channel is not None:
            self.channel.stop_consuming()

    def close_connection(self):
        if self.channel is not None:
            self.channel.stop_consuming()
            self.channel = None
        if self.connection is not None:
            self.connection.close()
            self.connection = None
