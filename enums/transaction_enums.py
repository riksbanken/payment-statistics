"""Enums for transaction schemas."""

from enum import IntEnum, StrEnum

from payment_statistics_utils.enums.full_enums import (
    CardType,
    InitiationChannel,
    PaymentScheme,
    PaymentServiceUser,
    PaymentType,
)


class PaymentTypeCardPaymentIssuer(StrEnum):
    """Payment type for Card Payment Issuer."""

    CPI = PaymentType.CPI.value

    CWI = PaymentType.CWI.value

    CADVI = PaymentType.CADVI.value


class PaymentTypeCardPaymentAcquirer(StrEnum):
    """Payment type for Card Payment Acquirer."""

    CPA = PaymentType.CPA.value

    CADVA = PaymentType.CADVA.value


class PaymentTypeCashTransactionATMOwners(StrEnum):
    """Payment type for Cash Transactions ATM Owners."""

    CW0 = PaymentType.CW0.value

    CD0 = PaymentType.CD0.value


class PaymentTypeCreditTransfer(StrEnum):
    """Payment type for Credit Transfer."""

    CT0 = PaymentType.CT0.value


class PaymentTypeInstantCreditTransfer(StrEnum):
    """Payment type for Credit Transfer."""

    CT1 = PaymentType.CT1.value


class PaymentTypeTransactions(StrEnum):
    """Payment types for Transactions Report."""

    CPI = PaymentType.CPI.value

    CWI = PaymentType.CWI.value

    CADVI = PaymentType.CADVI.value

    CPA = PaymentType.CPA.value

    CADVA = PaymentType.CADVA.value

    CW0 = PaymentType.CW0.value

    CD0 = PaymentType.CD0.value

    CT0 = PaymentType.CT0.value

    CT1 = PaymentType.CT1.value


class PaymentServiceUserCardPaymentIssuer(StrEnum):
    """Payment service user for Card Payment Issuer."""

    P = PaymentServiceUser.P.value

    NMFIXP = PaymentServiceUser.NMFIXP.value


class InitiationChannelCardPaymentIssuer(IntEnum):
    """Initiation channel for Card Payment Issuer."""

    NonElectronic = InitiationChannel.NonElectronic.value

    ATM = InitiationChannel.ATM.value

    POSTerminal = InitiationChannel.POSTerminal.value

    Ecommerce = InitiationChannel.ECommerce.value

    MerchantInitiated = InitiationChannel.MerchantInitiated.value

    MobilePayment = InitiationChannel.MobilePayment.value

    Other = InitiationChannel.Other.value


class InitiationChannelCardPaymentAquierer(IntEnum):
    """Initiation channel for Card Payment Acquirer."""

    NonElectronic = InitiationChannel.NonElectronic.value

    POSTerminal = InitiationChannel.POSTerminal.value

    Ecommerce = InitiationChannel.ECommerce.value

    MerchantInitiated = InitiationChannel.MerchantInitiated.value

    MobilePayment = InitiationChannel.MobilePayment.value

    Other = InitiationChannel.Other.value


class InitiationChannelCreditTransfer(IntEnum):
    """Initiation channel for Credit transfer."""

    PaperBased = InitiationChannel.PaperBased.value

    FileBatch = InitiationChannel.FileBatch.value

    OnlineBanking = InitiationChannel.OnlineBanking.value

    ECommerce = InitiationChannel.ECommerce.value

    OtherOnline = InitiationChannel.OtherOnline.value

    Terminal = InitiationChannel.Terminal.value

    P2PMobile = InitiationChannel.P2PMobile.value

    OtherMobile = InitiationChannel.OtherMobile.value

    Other = InitiationChannel.Other.value

    PISP = InitiationChannel.PISP.value


class InitiationChannelInstantCreditTransfer(IntEnum):
    """Initiation channel for InstantCreditTransfer."""

    FileBatch = InitiationChannel.FileBatch.value

    OnlineBanking = InitiationChannel.OnlineBanking.value

    ECommerce = InitiationChannel.ECommerce.value

    OtherOnline = InitiationChannel.OtherOnline.value

    Terminal = InitiationChannel.Terminal.value

    P2PMobile = InitiationChannel.P2PMobile.value

    OtherMobile = InitiationChannel.OtherMobile.value

    Other = InitiationChannel.Other.value

    PISP = InitiationChannel.PISP.value


class PaymentSchemeCardPaymentIssuer(StrEnum):
    """Payment scheme for Card Payment Issuer."""

    PCS_MCRD = PaymentScheme.PCS_MCRD.value

    PCS_VISA = PaymentScheme.PCS_VISA.value

    PCS_AMEX = PaymentScheme.PCS_AMEX.value

    PCS_DINE = PaymentScheme.PCS_DINE.value

    PCS_OTH = PaymentScheme.PCS_OTH.value


class PaymentSchemeCardPaymentAcquirer(StrEnum):
    """Payment scheme for Card Payment Acquirer."""

    PCS_MCRD = PaymentScheme.PCS_MCRD.value

    PCS_VISA = PaymentScheme.PCS_VISA.value

    PCS_AMEX = PaymentScheme.PCS_AMEX.value

    PCS_DINE = PaymentScheme.PCS_DINE.value

    PCS_CUP = PaymentScheme.PCS_CUP.value

    PCS_JCB = PaymentScheme.PCS_JCB.value

    PCS_OTH = PaymentScheme.PCS_OTH.value


class PaymentSchemeCashTransactionsATMOwners(StrEnum):
    """Payment scheme for Cash Transactions ATM Owners."""

    PCS_MCRD = PaymentScheme.PCS_MCRD.value

    PCS_VISA = PaymentScheme.PCS_VISA.value

    PCS_CUP = PaymentScheme.PCS_CUP.value

    PCS_JCB = PaymentScheme.PCS_JCB.value

    PCS_AMEX = PaymentScheme.PCS_AMEX.value

    PCS_DINE = PaymentScheme.PCS_DINE.value

    PCS_OTH = PaymentScheme.PCS_OTH.value


class PaymentSchemeCreditTransfer(StrEnum):
    """Payment scheme for Credit Transfer."""

    CTS_SEPA = PaymentScheme.CTS_SEPA.value

    CTS_NPC = PaymentScheme.CTS_NPC.value

    CTS_OTHRIX = PaymentScheme.CTS_OTHRIX.value

    CTS_OTHXB = PaymentScheme.CTS_OTHXB.value

    CTS_ONUS = PaymentScheme.CTS_ONUS.value

    CTS_OTHO = PaymentScheme.CTS_OTHO.value


class PaymentSchemeInstantCreditTransfer(StrEnum):
    """Payment scheme for Instant Credit Transfer."""

    CTS_NPCI = PaymentScheme.CTS_NPCI.value

    CTS_SEPAI = PaymentScheme.CTS_SEPAI.value

    CTS_NPCOLO = PaymentScheme.CTS_NPCOLO.value

    CTS_EPCOLO = PaymentScheme.CTS_EPCOLO.value

    CTS_OTHSIP = PaymentScheme.CTS_OTHSIP.value

    CTS_OTHO = PaymentScheme.CTS_OTHO.value


class CardTypeCardPaymentIssuer(IntEnum):
    """Card type for Card Payment Issuer."""

    Debit = CardType.Debit.value

    DelayedDebit = CardType.DelayedDebit.value

    Credit = CardType.Credit.value


class CardTypeCardPaymentAcquirer(IntEnum):
    """Card type for Card Payment Acquirer."""

    DebitOnlyConsumer = CardType.DebitOnlyConsumer.value

    CreditOnlyConsumer = CardType.CreditOnlyConsumer.value

    Corporate = CardType.Corporate.value
