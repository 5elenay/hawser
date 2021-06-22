from dataclasses import dataclass
from hawser.utils import raise_error
from hawser.meta import __socket__
from aiohttp import ClientSession
from json import loads
from asyncio import sleep, get_event_loop


@dataclass
class Gateway:
    """Gateway class.

    Constants:
        EVENT: 0
        HELLO: 1
        INIT: 2
        HEARTBEAT: 3

    Public Functions:
        <Gateway>.on_ready(async function) -> True
        <Gateway>.on_message(async function) -> True
        <Gateway>.start() -> True
        <Gateway>.start_and_wait() -> None
    """

    EVENT: int = 0
    HELLO: int = 1
    INIT: int = 2
    HEARTBEAT: int = 3

    def __init__(self, *args) -> None:
        self.ids = [str(i) for i in args]

        self.ws = None
        self.heartbeat = 30
        self.session = None
        self.event_loop = get_event_loop()

        self.__init_function = lambda _: None
        self.__event_function = lambda _: None

    def on_ready(self, function) -> True:
        """Ready function for gateway.

        Parameters:
            function (async function): The function is runned when gateway is ready. Function needs to have one parameter (data) and should be async.

        Returns:
            True: Function added successfully.
        """

        raise_error(function, "function", type(lambda: True))

        self.__init_function = function

    def on_message(self, function) -> True:
        """Event function for gateway.

        Parameters:
            function (async function): The function is runned when receive a message. Function needs to have one parameter (data) and should be async.

        Returns:
            True: Function added successfully.
        """

        raise_error(function, "function", type(lambda: True))

        self.__event_function = function

    async def __connect_to_gateway(self):
        self.session = ClientSession()
        self.ws = await self.session.ws_connect(__socket__)

    async def __heartbeat(self):
        while True:
            await self.ws.send_json({
                "op": self.HEARTBEAT,
                "d": None
            })

            await sleep(self.heartbeat / 1000)

    async def __send_users(self, data):
        await self.ws.send_json({
            "op": self.INIT,
            "d": {
                "subscribe_to_ids": self.ids
            }
        })

        self.heartbeat = data["heartbeat_interval"]
        self.event_loop.create_task(self.__heartbeat())

    def __handle_event(self, packet):
        if packet["t"] == "INIT_STATE":
            self.event_loop.create_task(self.__init_function(packet["d"]))
        else:
            self.event_loop.create_task(self.__event_function(packet["d"]))

    async def __receive(self):
        while True:
            packet = await self.ws.receive()

            if isinstance(packet.data, int) and len(str(packet.data)) == 4:
                print("WebSocket Exception Found: {0} ({1})".format(
                    packet.data, packet.extra))
                continue
            elif isinstance(packet.data, type(None)):
                if packet.type == 0x101:
                    return None

            packet = loads(packet.data)

            if packet["op"] == self.HELLO:
                await self.__send_users(packet["d"])
            elif packet["op"] == self.EVENT:
                self.__handle_event(packet)

    async def __start_client(self):
        await self.__connect_to_gateway()
        await self.__receive()

    def start(self) -> True:
        """Start the connection.

        Returns:
            True: Connection started successfully.
        """
        self.event_loop.create_task(self.__start_client())
        return True

    def start_and_wait(self) -> None:
        """Start the connection without creating new task.

        Returns:
            None
        """
        self.event_loop.run_until_complete(self.__start_client())
