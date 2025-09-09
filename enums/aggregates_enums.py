"""Aggregate enmus."""

from enum import IntEnum, StrEnum

from payment_statistics_utils.enums.full_enums import (
    InitiationChannel,
    PaymentServiceUser,
    PaymentType,
)


class PaymentTypeEMoney(StrEnum):
    """Payment type for E-Money."""

    EMP0 = PaymentType.EMP0.value


class PaymentTypeMoneyRemittances(StrEnum):
    """Payment type for Money Remittances."""

    MREM = PaymentType.MREM.value


class PaymentTypeOTC(StrEnum):
    """Payment type for OTC."""

    CWOTC = PaymentType.CWOTC.value

    CDOTC = PaymentType.CDOTC.value


class PaymentTypePaymentInitiationServices(StrEnum):
    """Payment type for Payment Initiated Services."""

    PI = PaymentType.PI.value


class PaymentTypeAggregates(StrEnum):
    """Payment types for all Aggregates."""

    EMP0 = PaymentType.EMP0.value

    MREM = PaymentType.MREM.value

    CWOTC = PaymentType.CWOTC.value

    CDOTC = PaymentType.CDOTC.value

    PI = PaymentType.PI.value


class InitiationChannelEMoney(IntEnum):
    """Initiation channel for aggregate E-Money."""

    P2PMobile = InitiationChannel.P2PMobile.value

    OtherMobile = InitiationChannel.OtherMobile.value

    EMoneyStoredCard = InitiationChannel.EMoneyStoredCard.value

    EMoneyAccountCard = InitiationChannel.EMoneyAccountCard.value

    EMoneyOther = InitiationChannel.EMoneyOther.value


class PaymentServiceUserEMoney(StrEnum):
    """Payment service user for E-Money."""

    P = PaymentServiceUser.P.value

    NMFIXP = PaymentServiceUser.NMFIXP.value


class PaymentServiceUserOTC(StrEnum):
    """Payment service user for OTC."""

    P = PaymentServiceUser.P.value

    NMFIXP = PaymentServiceUser.NMFIXP.value
