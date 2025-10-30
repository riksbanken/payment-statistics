"""Quantity intems enums."""

from enum import IntEnum, StrEnum

from ..enums.full_enums import (
    CardType,
    PaymentScheme,
    PaymentServiceUser,
    QuantityItems,
    TerminalFunction,
)


class QuantityItemsCard(StrEnum):
    """Quantity items for Cards."""

    CARD = QuantityItems.CARD.value


class QuantityItemsPosTerminal(StrEnum):
    """Quantity Items for Pos Terminal."""

    POS = QuantityItems.POS.value


class QuantityItemsEMoneyTerminal(StrEnum):
    """Quantity Items for E-MoneyTerminal."""

    EMT = QuantityItems.EMT.value


class QuantityItemsATMs(StrEnum):
    """Quantity items for ATMs."""

    ATM = QuantityItems.ATM.value


class QuantityItemsPaymentAccounts(StrEnum):
    """Quantity items for Payment Accounts."""

    PA = QuantityItems.PA.value


class PaymentSchemeCard(StrEnum):
    """Payment scheme for Card."""

    PCS_MCRD = PaymentScheme.PCS_MCRD.value

    PCS_VISA = PaymentScheme.PCS_VISA.value

    PCS_AMEX = PaymentScheme.PCS_AMEX.value

    PCS_DINE = PaymentScheme.PCS_DINE.value

    PCS_OTH = PaymentScheme.PCS_OTH.value


class PaymentServiceUserCard(StrEnum):
    """Payment service user for Card."""

    P = PaymentServiceUser.P.value

    NMFIXP = PaymentServiceUser.NMFIXP.value


class PaymentServiceUserPaymentAccounts(StrEnum):
    """Payment service user of Payment Accounts."""

    P = PaymentServiceUser.P.value

    NMFIXP = PaymentServiceUser.NMFIXP.value


class CardTypeCard(IntEnum):
    """Card type for Card."""

    Debit = CardType.Debit.value

    DelayedDebit = CardType.DelayedDebit.value

    Credit = CardType.Credit.value


class TerminalFunctionPosTerminal(IntEnum):
    """Terminal function for Pos Terminal."""

    AcceptingEMoney = TerminalFunction.AcceptingEMoney.value

    NotAcceptingEmoney = TerminalFunction.NotAcceptingEmoney.value


class TerminalFunctionEMoneyTerminals(IntEnum):
    """Terminal function for E-Money Terminals."""

    AcceptingEMoney = TerminalFunction.AcceptingEMoney.value

    EMoneyLoadUnload = TerminalFunction.EMoneyLoadUnload.value

    EMoneyAndCard = TerminalFunction.EMoneyAndCard.value


class TerminalFunctionATMs(IntEnum):
    """Terminal function for ATMs."""

    CashWithdrawal = TerminalFunction.CashWithdrawal.value

    CashDeposit = TerminalFunction.CashDeposit.value

    CreditTransfer = TerminalFunction.CreditTransfer.value

    CashWithdrawalAndDeposit = TerminalFunction.CashWithdrawalAndDeposit.value

    CashDepositAndCreditTransfer = TerminalFunction.CashDepositAndCreditTransfer.value

    CashWithdrawalAndCreditTransfer = (
        TerminalFunction.CashWithdrawalAndCreditTransfer.value
    )

    CashWitdrawalDepositsAndCreditTransfer = (
        TerminalFunction.CashWitdrawalDepositsAndCreditTransfer.value
    )
