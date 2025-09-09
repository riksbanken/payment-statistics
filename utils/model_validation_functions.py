"""Model validation functions."""

from datetime import date, datetime
from enum import StrEnum

from pydantic_core import InitErrorDetails


def model_validation_error(
    loc: tuple[str, ...], input: object, msg: str
) -> InitErrorDetails:
    """Helper to create typed InitErrorDetails."""
    return {"type": "value_error", "loc": loc, "input": input, "ctx": {"error": msg}}


def validate_payment_type_and_reported_payment_type(
    payment_type: StrEnum,
    reported_payment_type: StrEnum,
) -> None | InitErrorDetails:
    """Validates that payment type is same as reported payment type."""
    if reported_payment_type.value != payment_type.value:
        return model_validation_error(
            ("payment_type",),
            f"{reported_payment_type}, {payment_type}",
            "Filed payment_type is not the same as reported_payment_type.",
        )

    return None


def valdate_transaction_cleared_between_dates(
    transaction_cleared: date,
    date_from: date,
    date_to: date,
) -> None | InitErrorDetails:
    """Validates that transaction cleared is between date_from and date_to."""
    if not (date_from <= transaction_cleared <= date_to):
        return model_validation_error(
            ("transaction_cleared", "date_from", "date_to"),
            f"{transaction_cleared}, {date_from}, {date_to}",
            "Filed transaction_cleared is not between date_from and date_to.",
        )
    return None


def valdate_transaction_day_between_dates(
    transaction_day: date,
    date_from: date,
    date_to: date,
) -> None | InitErrorDetails:
    """Validates that transaction day is between date_from and date_to."""
    if not (date_from <= transaction_day <= date_to):
        return model_validation_error(
            ("transaction_day", "date_from", "date_to"),
            f"{transaction_day}, {date_from}, {date_to}",
            "Filed transaction_day is not between date_from and date_to.",
        )
    return None


def valdate_transaction_time_between_dates(
    transaction_time: datetime,
    date_from: date,
    date_to: date,
) -> None | InitErrorDetails:
    """Validates that transaction time is between date_from and date_to."""
    if not (date_from <= transaction_time.date() <= date_to):
        return model_validation_error(
            ("transaction_time", "date_from", "date_to"),
            f"{transaction_time}, {date_from}, {date_to}",
            "Filed transaction_time is not between date_from and date_to.",
        )
    return None
