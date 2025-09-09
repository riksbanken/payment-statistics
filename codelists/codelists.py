"""Codelists."""

import pycountry as pc

from payment_statistics_utils.enums.full_enums import (
    CardFunction,
    CardType,
    ConcentrationRatioType,
    Contactless,
    ContactlessFunction,
    EmoneyFunction,
    Environment,
    InitiationChannel,
    ParticipantSector,
    ParticipantType,
    PaymentScheme,
    PaymentServiceUser,
    PaymentSystem,
    PaymentSystemMetric,
    PaymentType,
    PispInitiatedTransaction,
    QuantityItems,
    RemoteInitiation,
    RoleInTransaction,
    TerminalFunction,
    TransactionType,
    TypeOfAccount,
)


type Codelist = dict[str | int, str]

country: Codelist = {c.alpha_2: c.name for c in pc.countries}

currency: Codelist = {c.alpha_3: c.name for c in pc.currencies}

environment: dict[Environment, str] = {
    Environment.T: "Test",
    Environment.P: "Production",
}

payment_type: dict[PaymentType, str] = {
    PaymentType.CT0: "Credit transfer",
    PaymentType.CT1: "Instant credit transfer",
    PaymentType.DD: "Direct debits",
    PaymentType.CPI: "Card-based payment transactions issuer",
    PaymentType.CPA: "Card-based payment transactions acquirer",
    PaymentType.CWI: "ATM cash withdrawal issuer",
    PaymentType.CW0: "ATM cash withdrawal",
    PaymentType.CD0: "ATM cash deposits",
    PaymentType.CADVI: "Cash advance at POS terminals issuer",
    PaymentType.CADVA: "Cash advance at POS terminals acquirer",
    PaymentType.EMP0: "E-money payment transactions",
    PaymentType.MREM: "Money remittance",
    PaymentType.PI: "Payment initiation services",
    PaymentType.CWOTC: "OTC cash withdrawals",
    PaymentType.CDOTC: "OTC cash deposits",
}

quantity_item: dict[QuantityItems, str] = {
    QuantityItems.CARD: "Cards",
    QuantityItems.PA: "Payment accounts",
    QuantityItems.POS: "POS terminals",
    QuantityItems.EMT: "E-money card terminals",
    QuantityItems.ATM: "ATMs",
}

initiation_channel: dict[InitiationChannel, str] = {
    InitiationChannel.NonElectronic: "Non-electronic",
    InitiationChannel.PaperBased: "Paper-based form",
    InitiationChannel.FileBatch: "File/batch",
    InitiationChannel.SinglePayment: "Single payment basis",
    InitiationChannel.OnlineBanking: "Online banking based",
    InitiationChannel.ECommerce: "E-commerce payments",
    InitiationChannel.MerchantInitiated: "Merchant initiated payments",
    InitiationChannel.OtherOnline: "Other online based payments",
    InitiationChannel.Terminal: "Terminal",
    InitiationChannel.ATM: "ATM",
    InitiationChannel.POSTerminal: "POS terminal",
    InitiationChannel.MobilePayment: "Mobile payment solution",
    InitiationChannel.P2PMobile: "P2P mobile payment solution",
    InitiationChannel.OtherMobile: "Other mobile payment solutions",
    InitiationChannel.EMoneyStoredCard: "E-money stored direct on a card",
    InitiationChannel.EMoneyAccountCard: "E-money account accessed via a card",
    InitiationChannel.EMoneyOther: "E-money payment initiated from account other than through a card or mobile payment",
    InitiationChannel.RecurringSwish: "Recurring Swish",
    InitiationChannel.Other: "Other",
    InitiationChannel.PISP: "PISP",
}

payment_scheme: dict[PaymentScheme, str] = {
    PaymentScheme.PCS_MCRD: "Mastercard",
    PaymentScheme.PCS_VISA: "VISA",
    PaymentScheme.PCS_CUP: "Union Pay",
    PaymentScheme.PCS_JCB: "JCB",
    PaymentScheme.PCS_AMEX: "American Express",
    PaymentScheme.PCS_DINE: "Diners and Discover",
    PaymentScheme.PCS_OTH: "Other card schemes",
    PaymentScheme.CTS_NPCI: "NPC Instant credit transfer scheme",
    PaymentScheme.CTS_SEPAI: "The SEPA instant credit transfer (SCT Inst)",
    PaymentScheme.CTS_NPCOLO: "NPC One-leg out instant credit transfer",
    PaymentScheme.CTS_EPCOLO: "EPC One-leg out instant credit transfer",
    PaymentScheme.CTS_OTHSIP: "Other-Swish",
    PaymentScheme.CTS_SEPA: "The SEPA Credit Transfer (SCT)",
    PaymentScheme.CTS_NPC: "NPC Credit transfer",
    PaymentScheme.CTS_OTHRIX: "Other - RIX RTGS",
    PaymentScheme.CTS_OTHXB: "Other - Cross-border",
    PaymentScheme.CTS_ONUS: "Other - On us",
    PaymentScheme.CTS_OTHO: "Other-other",
}

payment_service_user: dict[PaymentServiceUser, str] = {
    PaymentServiceUser.P: "Private persons",
    PaymentServiceUser.NMFIXP: "Non-MFI excl. private persons",
    PaymentServiceUser.MFI: "Monetary financial institutions",
}

transaction_type: dict[TransactionType, str] = {
    TransactionType.PUR: "Purchase",
    TransactionType.RET: "Returns",
    TransactionType.ORC: "Original credits",
    TransactionType.P2P: "P2P Card-to-card",
    TransactionType.REV: "Reversals",
    TransactionType.CHB: "Charge-back",
    TransactionType.REP: "Representments",
}

card_type: dict[CardType, str] = {
    CardType.Debit: "Debit card",
    CardType.DebitOnlyConsumer: "Debit card (only consumer card)",
    CardType.DelayedDebit: "Delayed debit card",
    CardType.Credit: "Credit card",
    CardType.CreditOnlyConsumer: "Credit card (only consumer card)",
    CardType.Corporate: "Corporate cards",
}

card_function: dict[CardFunction, str] = {
    CardFunction.CF1: "Payment function (except e-money function only)",
    CardFunction.CF2: "Cash function",
    CardFunction.CF3: "E-money function",
    CardFunction.CF4: "Payment and cash function",
    CardFunction.CF5: "Cash and e-money function",
    CardFunction.CF6: "Payment, Cash and e-money function",
}

emoney_function: dict[EmoneyFunction, str] = {
    EmoneyFunction.Stored: "Cards on which e-money can be stored directly",
    EmoneyFunction.Access: "Cards that give access to e-money stored on an e-money account",
}

terminal_function: dict[TerminalFunction, str] = {
    TerminalFunction.AcceptingEMoney: "Accepting e-money cards",
    TerminalFunction.NotAcceptingEmoney: "Not accepting e-money cards",
    TerminalFunction.EMoneyLoadUnload: "E-money cards loading and unloading",
    TerminalFunction.EMoneyAndCard: "Accepting both e-money transactions and card loading/unloading",
    TerminalFunction.CashWithdrawal: "Cash withdrawals",
    TerminalFunction.CashDeposit: "Cash deposits",
    TerminalFunction.CreditTransfer: "Credit transfers",
    TerminalFunction.CashWithdrawalAndDeposit: "Both cash withdrawals and -deposits",
    TerminalFunction.CashDepositAndCreditTransfer: "Both cash deposits and credit transfers",
    TerminalFunction.CashWithdrawalAndCreditTransfer: "Both cash withdrawals and credit transfer",
    TerminalFunction.CashWitdrawalDepositsAndCreditTransfer: "Both cash withdrawals, -deposits and credit transfers",
}

role_in_transaction: dict[RoleInTransaction, str] = {
    RoleInTransaction.PayersPSP: "Payer's PSP",
    RoleInTransaction.PayeesPSP: "Payee's PSP",
}

remote_initiation: dict[RemoteInitiation, str] = {
    RemoteInitiation.R: "Initiated via remote channel",
    RemoteInitiation.NR: "Initiated via non-remote channel",
}

contactless: dict[Contactless, str] = {
    Contactless.CNT: "Contact chip",
    Contactless.CNTL1: "Contactless chip NFC",
    Contactless.MAG: "Magstripe",
    Contactless.OTH: "Other",
}

contactless_function: dict[ContactlessFunction, str] = {
    ContactlessFunction.ContactFunction: "Contact function",
    ContactlessFunction.ContactlessFunction: "Contactless function",
    ContactlessFunction.Both: "Both contact and contactless function",
}

pisp_initiated_transaction: dict[PispInitiatedTransaction, str] = {
    PispInitiatedTransaction.ICT0: "Credit transfer",
    PispInitiatedTransaction.ICT1: "Instant credit transfer",
    PispInitiatedTransaction.OTH: "Other",
}

type_of_account: dict[TypeOfAccount, str] = {
    TypeOfAccount.PA: "Payment account",
    TypeOfAccount.EMA: "E-money account",
}

concentration_ratio_type: dict[ConcentrationRatioType, str] = {
    ConcentrationRatioType.ConcentrationByValue: "Concentration ratio by value",
    ConcentrationRatioType.ConcentrationByVolume: "Concentration ratio by volume",
}

payment_system: dict[PaymentSystem, str] = {
    PaymentSystem.RIX: "RIX",
    PaymentSystem.RIXI: "RIXInst",
    PaymentSystem.BG: "Bankgirot",
    PaymentSystem.DC: "Dataclearingen",
}

participant_type: dict[ParticipantType, str] = {
    ParticipantType.DirectParticipant: "Direct participant",
    ParticipantType.IndirectParticipant: "Indirect participant",
}

participant_sector: dict[ParticipantSector, str] = {
    ParticipantSector.S122C: "Credit institution",
    ParticipantSector.S121: "Central bank",
    ParticipantSector.S13: "General Government",
    ParticipantSector.S125D1: "Clearing and settlement organisation",
    ParticipantSector.S12P: "Other financial institutions",
    ParticipantSector.SZP: "Other than general government, clearing and settlement organisations and other financial institutions",
}

payment_system_metric: dict[PaymentSystemMetric, str] = {
    PaymentSystemMetric.C: "Concentration ratio for payment systems.",
    PaymentSystemMetric.P: "Participants per payment system.",
    PaymentSystemMetric.T: "Transactions per payment system",
}
