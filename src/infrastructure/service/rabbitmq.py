import pika
from pika.exceptions import AMQPConnectionError, AMQPError

from src.domain.constants import HOST_MESSAGE_BROKER_USER
from src.exceptions.custom_exceptions import RabbitMQError


class RabbitMQ:
    def __init__(self):
        self.host = HOST_MESSAGE_BROKER_USER
        self._connection, self._channel = self.connection(self.host)
        self.message = []

    def connection(self, host):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host))
            channel = connection.channel()
            return connection, channel
        except AMQPConnectionError as error:
            print(error)
            raise RabbitMQError("Erro ao conectar ao RabbitMQ.") from error

    def channel(self, connection):
        try:
            if not self._channel:
                return connection.channel()
        except AMQPConnectionError as error:
            print(error)
            raise RabbitMQError("Erro ao conectar ao RabbitMQ.") from error

    def new_queue(self, queue_name):
        try:
            self._channel.queue_declare(queue=queue_name)
        except AMQPError as error:
            print(error)
            raise RabbitMQError("Erro ao criar a fila no RabbitMQ.") from error

    def publish(self, queue_name, message):
        try:
            self._channel.basic_publish(exchange='', routing_key=queue_name, body=message)
            print("Mensagem enviada.")
        except AMQPError as error:
            print(error)
            raise RabbitMQError("Erro ao publicar a mensagem no RabbitMQ.") from error

    def callback_unitary(self, channel, method, properties, body):
        message = body.decode('utf-8')
        print(f"Mensagem recebida: {message}")
        self.message.append(message)
        self._channel.stop_consuming()

    def callback_forever(self, channel, method, properties, body):
        message = body.decode('utf-8')
        print(f"Mensagem recebida: {message}")
        self.message.append(message)

    def consume(self, queue_name):
        try:
            self._channel.basic_consume(queue=queue_name, on_message_callback=self.callback_unitary, auto_ack=True)
            print('Aguardando mensagens...')
            self._channel.start_consuming()
        except AMQPError as error:
            print(error)
            raise RabbitMQError("Erro ao consumir mensagens do RabbitMQ.") from error

    def connection_close(self):
        try:
            if self._connection:
                self._connection.close()
                self._connection = None
        except Exception as error:
            print(error)
            raise RabbitMQError("Erro ao fechar conexao com RabbitMQ.") from error
