"""Codelists descriptions."""

from ..enums.full_enums import (
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


environment_desc: dict[Environment, str] = {
    Environment.T: "Used when a reporter sends a file with data for test environment.",
    Environment.P: "Used when a reporter sends a file with data for production environment.",
}

payment_type_desc: dict[PaymentType, str] = {
    PaymentType.CT1: "Refers to item 3 § 1 in the regulations.",
    PaymentType.CT0: "Refers to item 3 § 2 in the regulations.",
    PaymentType.CPI: "Refers to item 3 § 3 in the regulations.",
    PaymentType.CPA: "Refers to item 3 § 3 in the regulations.",
    PaymentType.CWI: "Refers to item 3 § 4 in the regulations.",
    PaymentType.CW0: "Refers to item 3 § 4 in the regulations.",
    PaymentType.CADVI: "Refers to item 3 § 5 in the regulations.",
    PaymentType.CADVA: "Refers to item 3 § 5 in the regulations.",
    PaymentType.CD0: "Refers to item 3 § 6 in the regulations.",
    PaymentType.DD: "Refers to item 3 § 7 in the regulations.",
    PaymentType.MREM: "Refers to item 3 § 8 in the regulations.",
    PaymentType.EMP0: "Refers to item 3 § 9 in the regulations.",
    PaymentType.PI: "Refers to item 3 § 10 in the regulations.",
    PaymentType.CDOTC: "Refers to item 3 § 11 in the regulations.",
    PaymentType.CWOTC: "Refers to item 3 § 12 in the regulations.",
}

quantity_item_desc: dict[QuantityItems, str] = {
    QuantityItems.CARD: "Refers to item 3 § 13 in the regulations.",
    QuantityItems.PA: "Refers to item 3 § 14 in the regulations.",
    QuantityItems.POS: "Refers to item 3 § 15 in the regulations.",
    QuantityItems.EMT: "Refers to item 3 § 16 in the regulations.",
    QuantityItems.ATM: "Refers to item 3 § 17 in the regulations.",
}

initiation_channel_desc: dict[InitiationChannel, str] = {
    InitiationChannel.NonElectronic: "Includes card payments initiated via imprinters, post or telephone. Can be both remote and non-remote initiated.",
    InitiationChannel.PaperBased: "Includes paper-based initiations over the counter and post. Can be both remote and non-remote initiated.",
    InitiationChannel.FileBatch: "Each transaction included in a file/batch is counted as a separate transaction. Always reported as remotely initiated transactions.",
    InitiationChannel.SinglePayment: " An electronically initiated transaction that is independent from other transactions, i.e. that is not part of a group of transactions jointly initiated.",
    InitiationChannel.OnlineBanking: "Transactions via the internet bank, either via a web browser or the customer's banking app on the phone. Always reported as remotely initiated transactions.",
    InitiationChannel.ECommerce: "This includes all payments made online where the purchase is made via a web browser on a computer, mobile phone or other devices. Always reported as remotely initiated transactions.",
    InitiationChannel.MerchantInitiated: "Includes merchant-initiated payments (MIT) such as recurring card payments. Always reported as remotely initiated transactions.",
    InitiationChannel.OtherOnline: "Online-based transactions that are not part of e-commerce, internet- or mobile banking. Always reported as remotely initiated transactions.",
    InitiationChannel.Terminal: "Only includes transactions that occur at physical terminals. This also includes transactions where you scan a QR code or enter a phone number using your phone. Note that all Swish payments P2B are excluded here and are included under mobile payments (code 2232) even if you use, for example, the Swish app to scan a QR code. Always reported as non-remotely initiated transactions.",
    InitiationChannel.ATM: "Includes transactions initiated via an ATM. Can only include non-remote initiated transactions.",
    InitiationChannel.POSTerminal: "Only includes transactions that occur at physical POS-terminals. Including those that occur with contactless technology. For example, Apple Pay or similar. Always reported as non-remotely initiated transactions.",
    InitiationChannel.MobilePayment: "Includes card payments made in a merchant's app (not the bank app). This also includes payments made remotely via Apple Pay and Google Pay. If it is not possible to distinguish whether a payment is made via mobile or not, it is reported under e-commerce (code 2211). Always reported as remotely initiated transactions.",
    InitiationChannel.P2PMobile: "Includes P2P transactions that take place via a mobile payment solution. This includes, for example, Swish transactions P2P. Always reported as remotely initiated transactions.",
    InitiationChannel.OtherMobile: "Includes other transactions, except P2P, that are made via a mobile payment solution. This includes, for example, all P2B payments made via Swish. Always reported as remotely initiated transactions.",
    InitiationChannel.EMoneyStoredCard: "E-money held on a card in the e-money holder's possession.",
    InitiationChannel.EMoneyAccountCard: "Cards which give access to e-money stored on e-money accounts are cards linked to e-money (card) accounts.",
    InitiationChannel.EMoneyOther: "E-money payment initiated from account other than through a card or mobile payment",
    InitiationChannel.RecurringSwish: "Includes recurring Swish payments.",
    InitiationChannel.Other: "Includes transactions that do not belong to any of the other specified categories. For credit transfers other includes transactions initiated via email or phone. Can be both remote and non-remote initiated.",
    InitiationChannel.PISP: "Includes transactions initiated by PISP. If information is available about both the fact that the transaction is initiated via a PISP and what other initiation channel is used for the transaction, PISP takes precedence and is specified for the transaction. Always reported as remotely initiated transactions.",
}

payment_scheme_desc: dict[PaymentScheme, str] = {
    PaymentScheme.PCS_MCRD: "",
    PaymentScheme.PCS_VISA: "",
    PaymentScheme.PCS_CUP: "",
    PaymentScheme.PCS_JCB: "",
    PaymentScheme.PCS_AMEX: "",
    PaymentScheme.PCS_DINE: "",
    PaymentScheme.PCS_OTH: "If the payment scheme is not known, it should be reported as other. If the payment scheme is known but it is not included in the code list, contact the Riksbank and inform them about the payment scheme and the Riksbank will add a code for it.",
    PaymentScheme.CTS_NPCI: "Instant credit transfers in the Nordic currencies.",
    PaymentScheme.CTS_SEPAI: "Instant credit transfers in EUR.",
    PaymentScheme.CTS_NPCOLO: "Upcoming scheme, development in progress. Instant credit transfers that start in one currency and end in another. The scheme handles incoming/outgoing payments to any of the Nordic currencies. The scheme indicates that they should be instant in the Nordic currency.",
    PaymentScheme.CTS_EPCOLO: "Instant credit transfers that start in one currency and end in another, where EUR is one of the currencies. The immediacy is for the part of the payment that is in EUR.",
    PaymentScheme.CTS_OTHSIP: "Swish (also includes Swish transactions where both payer and payee have the same bank).",
    PaymentScheme.CTS_SEPA: "Credit transfers in EUR.",
    PaymentScheme.CTS_NPC: "Payments in the Nordics that go via NPC Credit transfer. No on us transactions are included here.",
    PaymentScheme.CTS_OTHRIX: "Payments that go individually directly via RIX RTGS.",
    PaymentScheme.CTS_OTHXB: "Includes other cross-border payments where knowledge of the payment scheme is lacking or the payment does not belong to any specific payment scheme. If knowledge about the payment scheme is available but it is not included in the code list, contact the Riksbank and inform about the payment scheme and the Riksbank will add a code for it.",
    PaymentScheme.CTS_ONUS: "Payments/transactions between two accounts in the same bank (if the account holder is the same on both accounts, the payment/transaction should also be included).",
    PaymentScheme.CTS_OTHO: "If the payment scheme is not known, it should be reported as other. If the payment scheme is known but it is not included in the code list, contact the Riksbank and inform them about the payment scheme and the Riksbank will add a code for it.",
}

payment_service_user_desc: dict[PaymentServiceUser, str] = {
    PaymentServiceUser.P: "Private persons include all private persons that are not sole proprietors or a HIO",
    PaymentServiceUser.NMFIXP: "Non-MFIs excl. private persons are defined as all non-MFIs excl. private persons. Note that self-employed households, i.e. sole proprietors, and Household Non-Profit Organizations (HIOs) are included in the sector Non-MFIs exc. private persons. The public sector is, for example, also included here.",
    PaymentServiceUser.MFI: "In payment statistics, MFIs refer to institutions that are traditionally considered MFIs and companies that are payment service providers. Transactions initiated by MFIs can be, for example, when an MFI purchases office equipment from a retailer or when another MFI initiates a payment (PSP that has an account with the reporting MFI).",
}

transaction_type_desc: dict[TransactionType, str] = {
    TransactionType.PUR: "The payer is a cardholder and the payee is a sales company (merchant)",
    TransactionType.RET: "The payer is the selling company and the payee is a cardholder. It does not have to be the entire original purchase that is returned; it can be a partial amount.",
    TransactionType.ORC: "The payer is the selling company and the payee is a cardholder. It essentially functions like a refund, more of a regulatory definition where certain selling companies are given the right to make a credit to cardholders without a prior purchase transaction. For example, gambling winnings.",
    TransactionType.P2P: "Payer is a cardholder and the payee is another cardholder within the same payment scheme.",
    TransactionType.REV: "Technical backing of a transaction, as a correction for a technical error. For example, a batch of transactions that has been read into clearing twice by mistake.",
    TransactionType.CHB: "When the payer claims that the completed transaction is legally (not technically) incorrect and the payer's payment service provider compensates the payer and then charges the payee's payment service provider for this in accordance with the scheme's rules. For example, fraud or when the payer has not received the goods or services he paid for.",
    TransactionType.REP: "The acquirer rejects a chargeback and takes back the money.",
}

card_type_desc: dict[CardType, str] = {
    CardType.Debit: "Pre paid cards are included here as long as there is no e-money on the card.",
    CardType.DebitOnlyConsumer: "",
    CardType.DelayedDebit: "",
    CardType.Credit: "",
    CardType.CreditOnlyConsumer: "",
    CardType.Corporate: "",
}

card_function_desc: dict[CardFunction, str] = {
    CardFunction.CF1: "",
    CardFunction.CF2: "",
    CardFunction.CF3: "",
    CardFunction.CF4: "",
    CardFunction.CF5: "",
    CardFunction.CF6: "",
}

emoney_function_desc: dict[EmoneyFunction, str] = {
    EmoneyFunction.Stored: "",
    EmoneyFunction.Access: "",
}

terminal_function_desc: dict[TerminalFunction, str] = {
    TerminalFunction.AcceptingEMoney: "",
    TerminalFunction.NotAcceptingEmoney: "",
    TerminalFunction.EMoneyLoadUnload: "",
    TerminalFunction.EMoneyAndCard: "",
    TerminalFunction.CashWithdrawal: "",
    TerminalFunction.CashDeposit: "",
    TerminalFunction.CreditTransfer: "",
    TerminalFunction.CashWithdrawalAndDeposit: "",
    TerminalFunction.CashDepositAndCreditTransfer: "",
    TerminalFunction.CashWithdrawalAndCreditTransfer: "",
    TerminalFunction.CashWitdrawalDepositsAndCreditTransfer: "",
}

role_in_transaction_desc: dict[RoleInTransaction, str] = {
    RoleInTransaction.PayersPSP: "Payers payment service provider.",
    RoleInTransaction.PayeesPSP: "Payees payment service provider.",
}

remote_initiation_desc: dict[RemoteInitiation, str] = {
    RemoteInitiation.R: "Remote payment transaction means a payment transaction initiated via internet or through a device that can be used for distance communication. This includes transactions initiated via email or telephone (both when you button/keys in on the phone and when you speak to customer service).",
    RemoteInitiation.NR: "Non-remote transactions are those initiated at physical terminals and over the counter, including transactions initiated using contactless technology.",
}

contactless_desc: dict[Contactless, str] = {
    Contactless.CNT: "",
    Contactless.CNTL1: "",
    Contactless.MAG: "",
    Contactless.OTH: "",
}

contactless_function_desc: dict[ContactlessFunction, str] = {
    ContactlessFunction.ContactFunction: "",
    ContactlessFunction.ContactlessFunction: "",
    ContactlessFunction.Both: "",
}

pisp_initiated_transaction_desc: dict[PispInitiatedTransaction, str] = {
    PispInitiatedTransaction.ICT0: "",
    PispInitiatedTransaction.ICT1: "",
    PispInitiatedTransaction.OTH: "",
}

type_of_account_desc: dict[TypeOfAccount, str] = {
    TypeOfAccount.PA: "",
    TypeOfAccount.EMA: "",
}

concentration_ratio_type_desc: dict[ConcentrationRatioType, str] = {
    ConcentrationRatioType.ConcentrationByValue: "",
    ConcentrationRatioType.ConcentrationByVolume: "",
}

payment_system_desc: dict[PaymentSystem, str] = {
    PaymentSystem.RIX: "",
    PaymentSystem.RIXI: "",
    PaymentSystem.BG: "",
    PaymentSystem.DC: "",
}

participant_type_desc: dict[ParticipantType, str] = {
    ParticipantType.DirectParticipant: "",
    ParticipantType.IndirectParticipant: "",
}

participant_sector_desc: dict[ParticipantSector, str] = {
    ParticipantSector.S122C: "",
    ParticipantSector.S121: "",
    ParticipantSector.S13: "",
    ParticipantSector.S125D1: "",
    ParticipantSector.S12P: "",
    ParticipantSector.SZP: "",
}

payment_system_metric_desc: dict[PaymentSystemMetric, str] = {
    PaymentSystemMetric.C: "",
    PaymentSystemMetric.P: "",
    PaymentSystemMetric.T: "",
}
