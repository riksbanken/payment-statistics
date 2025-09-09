"""Type definitions."""

from typing import NewType


# Defines simple custom types with a doc string.
Country = NewType("Country", str)
"""ISO 3166-1 alpha-2 country code (e.g., 'SE', 'US')"""

Currency = NewType("Currency", str)
"""ISO 4217-1 alpha-3 currency code (e.g., 'SEK', 'USD')"""

MerchantCategory = NewType("MerchantCategory", str)
"""A Merchant Category Code (MCC) is a four-digit number assigned to businesses by credit card networks (Visa, MasterCard, American Express, Discover) to classify the type of goods or services they provide."""

Locality = NewType("Locality", str)
"""A "postort" (postal locality) is a defined area with its own postal address."""

SniCode = NewType("SniCode", str)
"""SNI codes (Swedish Standard Industrial Classification - Svensk Näringsgrensindelning) are used in Sweden to classify businesses and organizations according to the type of economic activity they perform."""
