"""
Abstract Adapters — VoIP/SMS/Email providers interface.
"""
from abc import ABC, abstractmethod
from typing import Any


class VoIPProviderAdapter(ABC):
    @abstractmethod
    async def connect(self) -> None: ...
    @abstractmethod
    async def disconnect(self) -> None: ...
    @abstractmethod
    async def get_channel_status(self, channel_id: str) -> dict[str, Any]: ...
    @abstractmethod
    async def get_call_metrics(self) -> dict[str, Any]: ...


class SMSServiceAdapter(ABC):
    @abstractmethod
    async def send_sms(self, to: str, body: str) -> dict[str, Any]: ...
    @abstractmethod
    async def get_delivery_status(self, message_id: str) -> dict[str, Any]: ...


class EmailServiceAdapter(ABC):
    @abstractmethod
    async def send_email(self, to: str, subject: str, body: str) -> dict[str, Any]: ...
    @abstractmethod
    async def get_inbox_metrics(self) -> dict[str, Any]: ...
