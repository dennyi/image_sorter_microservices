from nats.aio.client import Client
import os



class MessageBroker():
    def __init__(self, nats_url):
        self.nats_url = nats_url
        self.nc = Client()

    async def connect(self):
        try:
            await self.nc.connect(self.nats_url,   
                                  reconnected_cb=self.reconnected_cb,
                                  disconnected_cb=self.disconnected_cb,
                                  max_reconnect_attempts=-1)
        except:
            print("Cannot connect")
            
    async def disconnect(self):
        if self.nc.is_closed:
            return
        await self.nc.close()

    async def listen_for_messages(self, subject, callback, workers=None):
        print("Listening for requests on {subject}".format(subject=subject))
        await self.nc.subscribe(subject, cb=self.__message_callback(callback), queue=workers)

    async def send_message(self, subject, data): 
        await self.nc.publish(subject, str.encode(data))
        print("Sent message on subject {subject}".format(subject=subject))

    def __message_callback(self, callback):
        async def original_callback(msg):
            subject = msg.subject
            data = msg.data.decode()
            callback(subject, data)
        return original_callback
    
    async def disconnected_cb():
        print("Got disconnected...")

    async def reconnected_cb():
        print("Got reconnected...")