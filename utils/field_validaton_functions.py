"""Functions for field validation."""

import calendar
import re
from datetime import datetime
from typing import Annotated

from pydantic import AfterValidator
from zoneinfo import ZoneInfo

from ..codelists.codelist_mcc import merchant_category_code
from ..codelists.codelist_sni import sni_codes
from ..codelists.codelists import country, currency
from ..codelists.locality import localities


_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$")


def validate_currency(v: str) -> str:
    """Validates that currencies are part of codelist."""
    upper = v.upper()
    if upper in currency:
        return upper
    raise ValueError(
        f"Currency code is incorrect. Got {v}, expected ISO 4217-1 alpha-3 currency code."
    )


def validate_country(v: str) -> str:
    """Validates that countries are part of codelist.

    Additional country codes:
        XK: Kosovo
        XX: Codes not in ISO 3166-1 alpha-2 and not in exceptions list.
    """
    exceptions = ["XK", "XX"]
    if v.upper() in country or v.upper() in exceptions:
        return v.upper()
    else:
        raise ValueError(
            f"Country code is incorrect. Got {v}, expected ISO 3166-1 alpha-2 country code."
        )


def validate_date(v: str) -> str:
    """Validate date format. Allowed format is date. Example "2025-01-31"."""
    if not _DATE_RE.match(v):
        raise ValueError(f"Date has to be in format '%Y-%m-%d', got {type(v)}: {v}")
    return v


def validate_timestamp(v: str) -> str:
    """Validate timestamp. Allowed format is datetime. Example "2025-01-10T14:00:01"."""
    if not _TIMESTAMP_RE.match(v):
        raise ValueError(
            f"Timestamp has to be in format '%Y-%m-%dT%H:%M:%S' got {type(v)}: {v}"
        )
    return v


def validate_optional_timestamp(v: str | None) -> str | None:
    """Validate timestamp or None."""
    if v is None:
        return v
    if not _TIMESTAMP_RE.match(v):
        raise ValueError(
            f"Timestamp has to be in format '%Y-%m-%dT%H:%M:%S' got {type(v)}: {v}"
        )
    return v


def validate_sni_code(v: str) -> str:
    """Validate sni code."""
    if v.upper() in sni_codes:
        return v.upper()
    else:
        raise ValueError(f"Sni code is incorrect. Got {v}.")


def validate_locality(v: str) -> str:
    """Validate locality."""
    if not v:
        return v
    elif v.upper() in localities:
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


def _past_in_stockholm(v: datetime) -> datetime:
    tz_sthlm = ZoneInfo("Europe/Stockholm")
    if v.replace(tzinfo=tz_sthlm) >= datetime.now(tz=tz_sthlm):
        raise ValueError("report_datetime must be in the past (Europe/Stockholm)")
    return v


StockholmPastDatetime = Annotated[datetime, AfterValidator(_past_in_stockholm)]
