"""Payment system operators report schema.

This schema is used to report the specific overall file information,
in addition to the base report schema,
that should be reported for all the items in Section 7 of the regulations.
"""

from typing import Literal

from pydantic import Field, PastDate, field_validator

from payment_statistics_utils.enums.field_metadata_enums import (
    PeriodMeta,
    ReportedPaymentSystemMetricMeta,
    SchemaVersionMeta,
)
from payment_statistics_utils.enums.full_enums import PaymentSystemMetric
from payment_statistics_utils.schemas.base_report_schema import BaseReport
from payment_statistics_utils.utils.field_validaton_functions import (
    validate_quarterly,
)


class PaymentSystemOperatorsReport(BaseReport, extra="forbid"):
    """Payment system operators report.

    Class Payment system operators report consist of all attributes,
    in addition to the base report schemas attributes,
    that contains overall file information,
    and should be included in each file sent for the items in Section 7 of the regulations.
    """

    schema_version: Literal["1.0"] = Field(
        ...,
        description=SchemaVersionMeta.description.value,
        examples=SchemaVersionMeta.examples.value,
        json_schema_extra={"meta_class": "SchemaVersionMeta"},
    )

    period: PastDate = Field(
        ...,
        description=PeriodMeta.description.value,
        examples=PeriodMeta.examples.value,
        json_schema_extra={"meta_class": "PeriodMeta"},
    )

    reported_payment_system_metric: PaymentSystemMetric = Field(
        ...,
        description=ReportedPaymentSystemMetricMeta.description.value,
        examples=ReportedPaymentSystemMetricMeta.examples.value,
        json_schema_extra={"meta_class": "ReportedPaymentSystemMetricMeta"},
    )

    @field_validator("period", mode="before")
    @classmethod
    def validate_period(cls, period: str) -> str:
        """Make sure that period is the last day of each quarter."""
        return validate_quarterly(period)
