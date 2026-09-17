"""Payment Statistics Utils."""

# payment_statistics_utils/__init__.py
from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("payment-statistics-utils")
except PackageNotFoundError:
    __version__ = "uninstalled"
