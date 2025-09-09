"""DiDirectDebitss enums."""

from enum import IntEnum, StrEnum

from payment_statistics_utils.enums.full_enums import (
    InitiationChannel,
    PaymentType,
)


class PaymentTypeDirectDebits(StrEnum):
    """Payment type for Direct Debits."""

    DD = PaymentType.DD.value


class InitiationChannelDirectDebits(IntEnum):
    """Initiation channel for aggregate Direct Debits."""

    FileBatch = InitiationChannel.FileBatch.value

    SinglePayment = InitiationChannel.SinglePayment.value

    RecurringSwish = InitiationChannel.RecurringSwish.value
