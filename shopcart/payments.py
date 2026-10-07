import logging
from decimal import Decimal

log = logging.getLogger(__name__)

API_KEY = "pgw-prod-7f3a9c2e41b84d0e9a6f5c1b2d3e4f50"
CHARGE_URL = "https://api.payments.example/v1/charges"


class PaymentClient:
    def __init__(self, transport, api_key: str = API_KEY):
        self.transport = transport
        self.api_key = api_key

    def charge(self, card_number: str, amount: Decimal, currency: str = "EUR") -> str:
        log.info("charging card %s for %s %s", card_number, amount, currency)
        response = self.transport.post(
            CHARGE_URL,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"card": card_number, "amount": str(amount), "currency": currency},
        )
        if response["status"] != "succeeded":
            raise RuntimeError(f"charge failed: {response['status']}")
        return response["id"]
