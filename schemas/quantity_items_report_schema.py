"""Quantity items report schema.

This schema is used to report the specific overall file information,
in addition to the base report schema,
that should be reported for the quantity items schemas.

Section 3 in the regulations.
Item 13. Cards,
item 14. Payment accounts,
item 15. POS terminals,
item 16. E-money card terminals,
item 17. ATMs.
"""

from typing import Literal

from pydantic import (
    Field,
    PastDate,
    field_validator,
)

from ..enums.field_metadata_enums import (
    PeriodMeta,
    ReportedQuantityItemMeta,
    SchemaVersionMeta,
)
from ..enums.full_enums import QuantityItems
from ..schemas.base_report_schema import BaseReport
from ..utils.field_validaton_functions import (
    validate_half_year,
)


class QuantityItemsReport(BaseReport, extra="forbid"):
    """Quantity items report.

    Class Quantity items report consist of all attributes,
    in addition to the base report schemas attributes,
    that contains overall file information,
    and should be included in each file sent for the quantity items.
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

    reported_quantity_item: QuantityItems = Field(
        ...,
        description=ReportedQuantityItemMeta.description.value,
        examples=ReportedQuantityItemMeta.examples.value,
        json_schema_extra={"meta_class": "ReportedQuantityItemMeta"},
    )

    @field_validator("period", mode="before")
    @classmethod
    def validate_period(cls, period: str) -> str:
        """Make sure that period is the last day of each half year."""
        return validate_half_year(period)
