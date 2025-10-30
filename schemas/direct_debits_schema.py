"""Direct debits schema is used to report direct debits, Section 3 item 7 in the regulations."""

from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from ..enums.direct_debits_enums import (
    InitiationChannelDirectDebits,
    PaymentTypeDirectDebits,
)
from ..enums.field_metadata_enums import (
    IdMeta,
    InitiationChannelMeta,
    NumberOfMeta,
    PaymentTypeDDMeta,
    TransactionCurrencyMeta,
    TransactionValueOtherMeta,
)
from ..utils.field_validaton_functions import validate_currency
from ..utils.types import Currency


class DirectDebits(BaseModel, extra="forbid"):
    """Direct debits.

    Class direct debits consist of all attributes that should be reported for direct debits (item 7).
    """

    id: str = Field(
        ...,
        description=IdMeta.description.value,
        examples=IdMeta.examples.value,
        json_schema_extra={"meta_class": "IdMeta"},
    )

    number_of: int = Field(
        ge=1,
        description=NumberOfMeta.description.value,
        examples=NumberOfMeta.examples.value,
        json_schema_extra={"meta_class": "NumberOfMeta"},
    )

    transaction_value: Decimal = Field(
        ge=0.00,
        decimal_places=2,
        description=TransactionValueOtherMeta.description.value,
        examples=TransactionValueOtherMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionValueOtherMeta"},
    )

    transaction_currency: Currency = Field(
        ...,
        description=TransactionCurrencyMeta.description.value,
        examples=TransactionCurrencyMeta.examples.value,
        json_schema_extra={"meta_class": "TransactionCurrencyMeta"},
    )

    payment_type: PaymentTypeDirectDebits = Field(
        ...,
        description=PaymentTypeDDMeta.description.value,
        examples=PaymentTypeDDMeta.examples.value,
        json_schema_extra={"meta_class": "PaymentTypeDDMeta"},
    )

    initiation_channel: InitiationChannelDirectDebits = Field(
        ...,
        description=InitiationChannelMeta.description.value,
        examples=InitiationChannelMeta.examples.value,
        json_schema_extra={"meta_class": "InitiationChannelMeta"},
    )

    @field_validator("transaction_currency", mode="after")
    @classmethod
    def validate_transaction_currency(cls, transaction_currency: str) -> str:
        """Validate that transaction_currency is alpha-3."""
        return validate_currency(transaction_currency)
