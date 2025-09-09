"""Direct debits report schema.

This schema is used to report the specific overall file information,
in addition to the base report schema,
that should be reported for direct debits item 7 in the regulations.
"""

from typing import Literal

from pydantic import (
    Field,
    PastDate,
    field_validator,
)

from payment_statistics_utils.enums.direct_debits_enums import (
    PaymentTypeDirectDebits,
)
from payment_statistics_utils.enums.field_metadata_enums import (
    PeriodMeta,
    ReportedPaymentTypeDDMeta,
    SchemaVersionMeta,
)
from payment_statistics_utils.schemas.base_report_schema import BaseReport
from payment_statistics_utils.utils.field_validaton_functions import (
    validate_date,
    validate_last_day_of_month,
)


class DirectDebitsReport(BaseReport, extra="forbid"):
    """Direct debits report.

    Class Direct debits report consist of all attributes,
    in addition to the base report schemas attributes,
    that contains overall file information,
    and should be included in each file sent for direct debits.
    """

    schema_version: Literal["1.0"] = Field(
        ...,
        description=SchemaVersionMeta.description.value,
        examples=SchemaVersionMeta.examples.value,
        json_schema_extra={"meta_class": "SchemaVersionMeta"},
    )

    reported_payment_type: PaymentTypeDirectDebits = Field(
        ...,
        description=ReportedPaymentTypeDDMeta.description.value,
        examples=ReportedPaymentTypeDDMeta.examples.value,
        json_schema_extra={"meta_class": "ReportedPaymentTypeDDMeta"},
    )

    period: PastDate = Field(
        ...,
        description=PeriodMeta.description.value,
        examples=PeriodMeta.examples.value,
        json_schema_extra={"meta_class": "PeriodMeta"},
    )

    @field_validator("period", mode="before")
    @classmethod
    def validate_period(cls, period: str) -> str:
        """Validates that period is valid date and last day of month."""
        _ = validate_date(period)
        return validate_last_day_of_month(period)
