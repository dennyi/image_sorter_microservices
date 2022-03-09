import asyncio
from messagebroker import MessageBroker

import unittest
import unittest.mock as mock

class MessageBrokerTestCase(unittest.IsolatedAsyncioTestCase):

    @mock.patch("messagebroker.messagebroker.Client.connect")
    async def test_connect_called_once(self, mock_connect):
        broker = MessageBroker("test_url") 
        await broker.connect()
        mock_connect.assert_called_once()

    @mock.patch("messagebroker.messagebroker.Client.connect")
    async def test_connect_with_correct_url(self, mock_connect):
        broker = MessageBroker("test_url") 
        await broker.connect()
        args, kwargs = mock_connect.call_args_list[-1]
        self.assertTrue("test_url" in args)

if __name__ == '__main__':
    unittest.main()