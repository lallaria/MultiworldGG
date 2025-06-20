from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from CommonClient import CommonContext
from worlds.AutoWorld import MultiWorld

class Client_Builder(ABC):
    @property
    @abstractmethod
    def client(self) -> None:
        pass
    @abstractmethod
    def produce_client_cli(self) -> None:
        pass
    @abstractmethod
    def produce_client_gui(self) -> None:
        pass
    @abstractmethod
    def produce_client_context(self) -> None:
        pass
    @abstractmethod
    def produce_client_world_data(self) -> None:
        pass
    @abstractmethod
    def produce_client_connector(self) -> None:
        pass

class Implement_Initial_Client(Client_Builder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._client = Client()

    @property
    def client(self) -> Client:
        client = self._client
        self.reset()
        return client
    
    def produce_client_cli(self) -> None:
        self._client.add("CLI")

    def produce_client_gui(self) -> None:
        self._client.add("GUI")

class Implement_Game_Client(Client_Builder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._client = Client()

    @property
    def client(self) -> Client:
        client = self._client
        self.reset()
        return client
    
    def produce_client_cli(self) -> None:
        self._client.add("CLI")

    def produce_kivy_client(self) -> None:
        self._client.add("asyncio.Task[None]")

    def produce_client_gui(self) -> None:
        self._client.add("asyncio.Task[None]")

    def produce_client_context(self, ctx: CommonContext) -> None:
        self._client.add("Context")
    
    def produce_ctx_server_task(self) -> None:
        self._client.add("asyncio.Task[None]")

    def produce_ctx_keep_alive_task(self) -> None:
        self._client.add("asyncio.Task[None]")

    def produce_client_autoreconnect(self) -> None:
        self._client.add("asyncio.Task[None]")

class Client():
    def __init__(self):
        self.features = []
    def add(self, feature: str) -> None:
        self.features.append(feature)
    def __str__(self) -> str:
        return "Client with features: " + ", ".join(self.features)
    
class Client_Director():

    def __init__(self) -> None:
        self._client_builder = None

    @property
    def client_builder(self) -> Client_Builder:
        return self._client_builder

    @client_builder.setter
    def client_builder(self, client_builder: Client_Builder) -> None:
        self._client_builder = client_builder

    def build_cli_client(self) -> None:
        self._client_builder.produce_client_cli()
        self._client_builder.produce_client_context()
        self._client_builder.produce_client_world_data()
        self._client_builder.produce_client_connector()
    
    def build_gui_client(self) -> None:
        self._client_builder.produce_client_gui()
        self._client_builder.produce_client_context()
        self._client_builder.produce_client_world_data()
        self._client_builder.produce_client_connector()

    def build_client(self) -> None:
        self._client_builder.produce_client_cli()
        self._client_builder.produce_client_gui()
        self._client_builder.produce_client_context()
        self._client_builder.produce_client_world_data()
        self._client_builder.produce_client_connector()

if __name__ == "__main__":
    director = Client_Director()
    director.client_builder = Implement_Initial_Client()
    director.build_cli_client() #if args.cli
    director.client_builder = Implement_Game_Client()
    director.build_client() #all other scenarios
    print(director.client_builder.client)
