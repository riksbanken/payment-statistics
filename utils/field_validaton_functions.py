"""Functions for field validation."""

import calendar
import re
from datetime import datetime

from payment_statistics_utils.codelists.codelist_mcc import merchant_category_code
from payment_statistics_utils.codelists.codelist_sni import sni_codes
from payment_statistics_utils.codelists.codelists import country, currency
from payment_statistics_utils.codelists.locality import localities


def validate_currency(v: str) -> str:
    """Validates that currencies are part of codelist."""
    if v.upper() in currency.keys():
        return v.upper()
    else:
        raise ValueError(
            f"Currency code is incorrect. Got {v}, expected ISO 4217-1 alpha-3 currency code."
        )


def validate_country(v: str) -> str:
    """Validates that countries are part of codelist."""
    if v.upper() in country.keys():
        return v.upper()
    else:
        raise ValueError(
            f"Country code is incorrect. Got {v}, expected ISO 3166-1 alpha-2 country code."
        )


def validate_date(v: str) -> str:
    """Validate date format.

    Allowed format is date.
    Example "2025-01-31".
    """
    try:
        datetime.strptime(v, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(  # noqa: B904
            f"Date has to be in format '%Y-%m-%d', got {type(v)}: {v}"
        )
    return v


def validate_timestamp(v: str | None) -> str | None:
    """Validate timestamp or None.

    Allowed timestamp format is datetime.
    Example "2025-01-10 14:00:01."
    """
    if v is None:
        return v

    try:
        datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(  # noqa: B904
            f"Timestamp has to be in format '%Y-%m-%d %H:%M:%S' got {type(v)}: {v}"
        )
    return v


def validate_sni_code(v: str) -> str:
    """Validate sni code."""
    if v.upper() in sni_codes.keys():
        return v.upper()
    else:
        raise ValueError(f"Sni code is incorrect. Got {v}.")


def validate_locality(v: str) -> str:
    """Validate locality."""
    if not v:
        return v
    elif v in localities:
        return v.upper()
    else:
        raise ValueError(f"Locality is in incorrect. Got {v}.")


def validate_merchant_category_code(v: str) -> str:
    """Validate that merchant_category code is valid."""
    if v.upper() in merchant_category_code:
        return v.upper()
    else:
        raise ValueError(f"Merchant category code is incorrect. Got {v}.")


def validate_half_year(v: str) -> str:
    """Validate that perdiod is one of YYYY-06-30 and YYYY-12-31."""
    pattern = r"^\d{4}-(06-30|12-31)$"
    if not re.match(pattern, v):
        raise ValueError(
            f"The period should be one of YYYY-06-30 and YYYY-12-31. Got {v}."
        )

    return v


def validate_quarterly(v: str) -> str:
    """Validate that perdiod should be the last day in any quarter."""
    pattern = r"^\d{4}-(03-31|06-30|09-30|12-31)$"
    if not re.match(pattern, v):
        raise ValueError(
            f"The period should be the last day in the reported quarter. Got {v}."
        )

    return v


def validate_last_day_of_month(v: str) -> str:
    """Validates that reported date is last day of month."""
    v_date = datetime.strptime(v, "%Y-%m-%d")
    last_day = calendar.monthrange(v_date.year, v_date.month)[1]

    if v_date.day != last_day:
        raise ValueError(  # noqa: B904
            f"Date is not the last day of month, got {v}."
        )

    return v
