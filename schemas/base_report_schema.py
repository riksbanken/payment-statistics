"""Base report schema.

This schema is used to report the specific overall file information.
The information should be included in each file sent.
"""

from typing import Any

from pydantic import (
    BaseModel,
    Field,
    PastDatetime,
    field_validator,
)

from payment_statistics_utils.enums.field_metadata_enums import (
    EnvironmentMeta,
    ItemsMeta,
    ReportDatetimeMeta,
    ReporterIdMeta,
    ReportPartMeta,
)
from payment_statistics_utils.enums.full_enums import Environment
from payment_statistics_utils.utils.field_validaton_functions import (
    validate_timestamp,
)


class BaseReport(BaseModel, extra="forbid"):
    """Base report.

    Class Base report consist of all attributes that contains overall file information and that should be included in each file sent.
    """

    reporter_id: str = Field(
        ...,
        pattern=r"\b[2-9][0-9]{5}-[0-9]{4}\b",
        description=ReporterIdMeta.description.value,
        examples=ReporterIdMeta.examples.value,
        json_schema_extra={"meta_class": "ReporterIdMeta"},
    )

    environment: Environment = Field(
        ...,
        description=EnvironmentMeta.description.value,
        examples=EnvironmentMeta.examples.value,
        json_schema_extra={"meta_class": "EnvironmentMeta"},
    )

    report_datetime: PastDatetime = Field(
        ...,
        description=ReportDatetimeMeta.description.value,
        examples=ReportDatetimeMeta.examples.value,
        json_schema_extra={"meta_class": "ReportDatetimeMeta"},
    )
    report_part: str | None = Field(
        None,
        description=ReportPartMeta.description.value,
        examples=ReportPartMeta.examples.value,
        json_schema_extra={"meta_class": "ReportPartMeta"},
    )
    items: list[dict[str, Any]] = Field(
        ...,
        description=ItemsMeta.description.value,
        examples=ItemsMeta.examples.value,
        json_schema_extra={"meta_class": "ItemsMeta"},
    )

    @field_validator("report_datetime", mode="before")
    @classmethod
    def validate_report_datetime(cls, report_datetime: str) -> str | None:
        """Validate that report date is in correct format."""
        return validate_timestamp(report_datetime)

    @field_validator("items", mode="before")
    @classmethod
    def validate_items_length(cls, items: str) -> str:
        """Validate that lenght of items > 0."""
        if len(items) > 0:
            return items
        else:
            raise ValueError("There are no items in the report.")
