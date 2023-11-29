import pika
import json
from EmailSend import EmailSend

class RabbitConsumer:

    def __init__(self) -> None:
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = 'guest'
        self.__password = 'guest'
        self.__queue = 'email_que'
        self.__channel = self.__create_channel()
        self.__email_send = EmailSend()
    
        
    def __create_channel(self):
        connection = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )
        channel = pika.BlockingConnection(connection).channel()
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback= self.__callback
        )

        return channel
    
    def start(self):
        print('Listen...')
        self.__channel.start_consuming()
        
    def __callback(self, ch, method, properties, body):
        dados_agenda = body.decode("utf-8")
        print(dados_agenda)
        
        json_obj = json.loads(dados_agenda)
        email_message = f"""
        Ola, {json_obj["user"]}. 
        Seu Agendamento foi marcado. Dia {json_obj["date"]} as {json_obj["time"]}.
        Você será atendido pelo(a) {json_obj["barber"]}.
        Seu serviço selecionado foi {json_obj["servico"]}.
        Obrigado pela preferência!!
        """
        self.__email_send.send_email(email_message, json_obj["email"])

consumer = RabbitConsumer()
consumer.start() 
        