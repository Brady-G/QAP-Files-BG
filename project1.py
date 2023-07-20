import inputs
import datetime
import calendar

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
    PostalCode = inputs.postalCode("Input postal code").upper()
    PhoneNumber = inputs.phoneNumber("Input phone number")

    CarsInsured = inputs.number("Enter number of cars being insured", 1)
    Liability = inputs.yesOrNo("Extra liability up to $1M")
    GlassCoverage = inputs.yesOrNo("Glass Coverage")
    LoanerCar = inputs.yesOrNo("Loaner car")

    ValidPaymentTypes = ["Full", "Monthly"]
    while True:
        PaymentType = input(f"Enter how you would like to pay ({', '.join(ValidPaymentTypes)}): ").title()

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

    FormattedInvoiceDate = datetime.date.today().strftime('%Y-%m-%d')
    FormattedNextPaymentDate = (datetime.date.today().replace(day=1) + datetime.timedelta(days=32)).replace(day=1).strftime('%Y-%m-%d')

    MonthlyCost = TotalCost / 8

    PolicyFile = open("Policies.dat", "a")
    PolicyFile.write(f"{NEXT_POLICY_NUMBER}, {FormattedInvoiceDate}, {FirstName}, {LastName}, {Address}, {Province}, {PostalCode}, {PhoneNumber}, {CarsInsured}, {Liability}, {GlassCoverage}, {LoanerCar}, {PaymentType}, {TotalCost}\n")
    PolicyFile.close()

    print("="*64)
    print("One Stop Insurance Company".center(64))

    print("="*64)
    print("Invoice Information".center(64))
    print(f"Invoice Date:                    {FormattedInvoiceDate:>31}")
    print(f"Policy Number:                    {NEXT_POLICY_NUMBER:>30}")
    if PaymentType == "Monthly":
        print(f"Next Payment Due:                 {FormattedNextPaymentDate:>30}")
    print("=" * 64)
    print("Policy Holder Information".center(64))
    print(f"Name:   {f'{FirstName} {LastName}':>56}")
    print(f"Address:   {Address:>53}")
    print(f"City:   {City:>56}")
    print(f"Province:   {Province:>52}")
    print(f"Postal Code:   {PostalCode:>49}")
    print(f"Phone Number:   {PhoneNumber:>48}")
    print("="*64)
    print("Policy Information".center(64))
    print(f"Number of Cars Insured:   {CarsInsured:>38}")
    print(f"Extra Liability:   {'Yes' if Liability else 'No':>45}")
    print(f"Glass Coverage:   {'Yes' if GlassCoverage else 'No':>46}")
    print(f"Loaner Car:   {'Yes' if LoanerCar else 'No':>50}")
    print(f"Payment Type:   {PaymentType:>48}")
    print("="*64)
    print("Cost Information".center(64))
    print()
    print("-" * 64)

    print(f"| {'Insurance Premium':<30}|{f'${InsuranceCost}.2f':>29} |")
    print(f"| {'Extra Liability':<30}|{f'${ExtraLiabilityCost}.2f':>29} |")
    print(f"| {'Glass Coverage':<30}|{f'${GlassCoverageCost}.2f':>29} |")
    print(f"| {'Loaner Car':<30}|{f'${LoanerCarCost}.2f':>29} |")
    print(f"| {'Total Extra Costs':<30}|{f'${TotalExtraCosts}.2f':>29} |")
    print(f"| {'Monthly Processing':<30}|{f'${MONTHLY_PROCESSING}.2f':>29} |")
    print(f"| {'Total Insurance Premium':<30}|{f'${TotalInsurancePremium}.2f':>29} |")
    print(f"| {'HST':<30}|{f'${TotalInsurancePremium * HST_RATE:.2f}':>29} |")
    print(f"| {'Total Cost':<30}|{f'${TotalCost:.2f}':>29} |")
    if PaymentType == "Monthly":
        print(f"| {'Monthly Cost':<30}|{f'${MonthlyCost:.2f}':>29} |")
    print("-" * 64)
    print()
    CostText = f"${TotalCost:.2f}" if PaymentType == "Full" else f"${MonthlyCost:.2f}"
    CostTextBox = len(CostText) + 4

    print(f"{'-' * CostTextBox:>64}")
    print(f"{f'Total Due | {CostText} |':>64}")
    print(f"{'-' * CostTextBox:>64}")

    print("="*64)

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
