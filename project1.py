import inputs
import datetime

DataFile = open("OSICDef.dat", "r")

NEXT_POLICY_NUMBER = int(DataFile.readline())
BASIC_PREMIUM = float(DataFile.readline())
ADDITIONAL_DISCOUNT = float(DataFile.readline())
LIABILITY = float(DataFile.readline())
COST_OF_GLASS = float(DataFile.readline())
LOANER_COVERAGE = float(DataFile.readline())
HST_RATE = float(DataFile.readline())
MONTHLY_PROCESSING = float(DataFile.readline())

BASIC_PREMIUM_DISCOUNTED = BASIC_PREMIUM * ADDITIONAL_DISCOUNT

DataFile.close()

while True:
    FirstName = inputs.firstName()
    LastName = inputs.lastName()
    Address = inputs.nonEmptyText("Input Address", "Address can not be blank")
    City = inputs.nonEmptyText("Input City", "City can not be blank").title()
    Province = inputs.province("Input Province")
    PostalCode = inputs.postalCode("Input postal code")
    PhoneNumber = inputs.phoneNumber("Input phone number")

    CarsInsured = inputs.number("Enter number of cars being insured", 0)
    Liability = inputs.yesOrNo("Extra liability up to $1M")
    GlassCoverage = inputs.yesOrNo("Glass Coverage")
    LoanerCar = inputs.yesOrNo("Loaner car")

    ValidPaymentTypes = ["Full", "Monthly"]
    while True:
        PaymentType = input(f"Enter how you would like to pay ({','.join(ValidPaymentTypes)}): ").title()

        if not PaymentType in ValidPaymentTypes:
            inputs.print_error("Payment type not valid.")
        else:
            break

    InsuranceCost = 0
    if CarsInsured > 0:
        InsuranceCost += BASIC_PREMIUM

    for i in range(1, CarsInsured):
        InsuranceCost += BASIC_PREMIUM_DISCOUNTED

    ExtraLiabilityCost = min(LIABILITY * CarsInsured, 1000000) if Liability else 0
    GlassCoverageCost = COST_OF_GLASS * CarsInsured if GlassCoverage else 0
    LoanerCarCost = LOANER_COVERAGE * CarsInsured if LoanerCar else 0

    TotalExtraCosts = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost

    TotalInsurancePremium = InsuranceCost + TotalExtraCosts

    TotalCost = TotalInsurancePremium * (1 + HST_RATE)
    TotalCost += MONTHLY_PROCESSING



    PolicyFile = open("Policies.dat", "a")
    PolicyFile.write(f"{NEXT_POLICY_NUMBER}, {datetime.date.today().strftime('%Y-%m-%d')}, {FirstName}, {LastName}, {Address}, {Province}, {PostalCode}, {PhoneNumber}, {CarsInsured}, {Liability}, {GlassCoverage}, {LoanerCar}, {PaymentType}, {TotalCost}\n")
    PolicyFile.close()

    # PRINT INFO HERE

    NEXT_POLICY_NUMBER += 1

    if input("Enter another policy (Y/N): ").upper() == "N":
        break

DataFile = open("OSICDef.dat", "w")
DataFile.writelines([
    f"{NEXT_POLICY_NUMBER}\n",
    f"{BASIC_PREMIUM}\n",
    f"{ADDITIONAL_DISCOUNT}\n",
    f"{LIABILITY}\n",
    f"{COST_OF_GLASS}\n",
    f"{LOANER_COVERAGE}\n",
    f"{HST_RATE}\n",
    f"{MONTHLY_PROCESSING}\n"
])
DataFile.close()