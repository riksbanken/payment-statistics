"""Aggregate report schema.

This schema is used to report the specific overall file information,
in addition to the base report schema,
that should be reported for the aggregate items schemas.

Section 3 in the regulations.
Item 8. Money remittances,
item 9. E-money payment transactions,
item 10. Payment initiation services,
item 11. Over the counter (OTC) cash deposits,
item 12. Over the counter (OTC) cash withdrawals.
"""

from typing import Literal

from pydantic import (
    Field,
    PastDate,
    field_validator,
)

from ..enums.aggregates_enums import (
    PaymentTypeAggregates,
)
from ..enums.field_metadata_enums import (
    DateFromMeta,
    DateToMeta,
    ReportedPaymentTypeAggregateMeta,
    SchemaVersionMeta,
)
from ..schemas.base_report_schema import BaseReport
from ..utils.field_validaton_functions import (
    validate_date,
)


class AggregateReport(BaseReport, extra="forbid"):
    """Aggregate report.

    Class Aggregate report consist of all attributes,
    in addition to the base report schemas attributes,
    that contains overall file information,
    and should be included in each file sent for the aggregate items.
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

    reported_payment_type: PaymentTypeAggregates = Field(
        ...,
        description=ReportedPaymentTypeAggregateMeta.description.value,
        examples=ReportedPaymentTypeAggregateMeta.examples.value,
        json_schema_extra={"meta_class": "ReportedPaymentTypeAggregateMeta"},
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
