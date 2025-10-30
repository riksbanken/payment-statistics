"""Payment system operator enums."""

from enum import StrEnum

from ..enums.full_enums import PaymentSystemMetric, PaymentType


class PaymentTypePaymentSystems(StrEnum):
    """Payment type for Payment Systems."""

    DD = PaymentType.DD

    CT0 = PaymentType.CT0

    CT1 = PaymentType.CT1


class PaymentSystemMetricTransactions(StrEnum):
    """Payment system metric for transactions."""

    T = PaymentSystemMetric.T


class PaymentSystemMetricConcentration(StrEnum):
    """Payment system metric for concentration."""

    C = PaymentSystemMetric.C


class PaymentSystemMetricParticipants(StrEnum):
    """Payment system metric for participants."""

    P = PaymentSystemMetric.P
