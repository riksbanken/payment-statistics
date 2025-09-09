"""Transaction report.

This schema is used to report the specific overall file information,
in addition to the base report schema,
that should be reported for all the items that are reported transaction by transaction (card_transaction schemas and transaction_schemas).

Section 3 in the regulations.
Item 1. Instant credit transfers,
item 2. Credit transfers,
Item 3. Card based payment transactions,
item 4. ATM cash withdrawal,
item 5. Cash advance at point of sale (POS) terminals.
item 6. ATM cash deposit.
"""

from typing import Literal

from pydantic import (
    Field,
    PastDate,
    field_validator,
)

from payment_statistics_utils.enums.field_metadata_enums import (
    DateFromMeta,
    DateToMeta,
    ReportedPaymentTypeTransactionsMeta,
    SchemaVersionMeta,
)
from payment_statistics_utils.enums.transaction_enums import (
    PaymentTypeTransactions,
)
from payment_statistics_utils.schemas.base_report_schema import BaseReport
from payment_statistics_utils.utils.field_validaton_functions import (
    validate_date,
)


class TransactionReport(BaseReport, extra="forbid"):
    """Transaction report.

    Class Transaction report consist of all attributes,
    in addition to the base report schemas attributes,
    that contains overall file information,
    and should be included in each file sent for the items that are reported transaction by transaction.
    """

    schema_version: Literal["1.0"] = Field(
        ...,
        description=SchemaVersionMeta.description.value,
        examples=SchemaVersionMeta.examples.value,
        json_schema_extra={"meta_class": "SchemaVersionMeta"},
    )

    date_from: PastDate = Field(
        ...,
        description=DateFromMeta.description.value,
        examples=DateFromMeta.examples.value,
        json_schema_extra={"meta_class": "DateFromMeta"},
    )

    date_to: PastDate = Field(
        ...,
        description=DateToMeta.description.value,
        examples=DateToMeta.examples.value,
        json_schema_extra={"meta_class": "DateToMeta"},
    )

    reported_payment_type: PaymentTypeTransactions = Field(
        ...,
        description=ReportedPaymentTypeTransactionsMeta.description.value,
        examples=ReportedPaymentTypeTransactionsMeta.examples.value,
        json_schema_extra={"meta_class": "ReportedPaymentTypeTransactionsMeta"},
    )

    @field_validator("date_from", mode="before")
    @classmethod
    def validate_date_from(cls, date_from: str) -> str:
        """Validate format of date_from."""
        return validate_date(date_from)

    @field_validator("date_to", mode="before")
    @classmethod
    def validate_date_to(cls, date_to: str) -> str:
        """Validate format of date_to."""
        return validate_date(date_to)
