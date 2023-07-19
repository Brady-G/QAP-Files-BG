import datetime

def date(text):
    """
    Asks a user to input a date in YYYY-MM-DD format
    :param text: The text prefix for the input line.
    :return: The date that was inputted.
    """
    while True:
        try:
            Input = input(f"{text} (YYYY-MM-DD): ")
            return datetime.datetime.strptime(Input, "%Y-%m-%d")
        except:
            print_error("Could not read date, make sure its in (YYYY-MM-DD) format")

def currentOrPastDate(text, futureError):
    """
    Asks a user to input a date but requires the date to be in the past or the current date.
    :param text: The text prefix for the input line.
    :param futureError: The error message for if the date is in the future.
    :return: The date that was inputted.
    """
    CurrentDate = datetime.datetime.now()
    while True:
        Date = date(text)
        if (CurrentDate - Date).days < 0:
            print_error(futureError)
        else:
            return Date


def phoneNumber(text):
    """
    Asks a user to input a phone number in (123-123-1234) format.
    :param text: The text prefix for the input line.
    :return: The phone number entered.
    """
    while True:
        PhoneNumber = input(f"{text} (123-456-7890): ")
        PhoneNumberNoDash = PhoneNumber[:3] + PhoneNumber[4:7] + PhoneNumber[8:]

        if len(PhoneNumber) != 12:
            print_error("Phone number must be 10 digits with 2 dashes")
        elif PhoneNumber[3] != "-" or PhoneNumber[7] != "-":
            print_error("Phone number must contain 2 dashes")
        elif not PhoneNumberNoDash.isnumeric():
            print_error("Phone number must only contain digits in addition to the 2 dashes")
        else:
            return PhoneNumber

def number(text, min, max):
    """
    Asks a user to input an int between to ints.
    :param text: The text prefix for the input line.
    :param min: The minimum int allowed.
    :param max: The maximum int allowed.
    :return: The int number in between the min and max
    """
    while True:
        try:
            value = int(input(f"{text} ({min}-{max}): "))
            if value < min or value > max:
                print_error(f"Input was not between {min}-{max}")
            else:
                return value
        except:
            print_error("Input was not a number")

def number(text, min):
    """
    Asks a user to input an int between to ints.
    :param text: The text prefix for the input line.
    :param min: The minimum int allowed.
    :param max: The maximum int allowed.
    :return: The int number in between the min and max
    """
    while True:
        try:
            value = int(input(f"{text} (>={min}): "))
            if value < min:
                print_error(f"Input was not >={min}")
            else:
                return value
        except:
            print_error("Input was not a number")

def decimal(text, min, max):
    """
    Asks a user to input a float between to floats.
    :param text: The text prefix for the input line.
    :param min: The minimum float allowed.
    :param max: The maximum float allowed.
    :return: The float number in between the min and max
    """
    while True:
        try:
            value = float(input(f"{text} ({min}-{max}): "))
            if value < min or value > max:
                print_error(f"Input was not between {min}-{max}")
            else:
                return value
        except:
            print_error("Input was not a number")

def nonEmptyText(text, error):
    """
    Asks a user to input non empty text.
    :param text: The text line prefixing a colon and space.
    :param error: The error if the text inputted was empty.
    :return: The inputted text.
    """
    while True:
        Name = input(f"{text}: ")
        if Name == "":
            print_error(error)
        else:
            return Name

def name(text, error):
    """
    Asks a user to input non empty text and then capitalizes it.
    :param text: The text line prefixing a colon and space.
    :param error: The error if the text inputted was empty.
    :return: The inputted text capitalized.
    """
    return nonEmptyText(text, error).capitalize()

def firstName():
    """
    Asks a user to input their first name.
    :return: The first name inputted.
    """
    return name("Please Enter First Name", "First name cannot be blank.")

def lastName():
    """
    Asks a user to input their last name.
    :return: The last name inputted.
    """
    return name("Please Enter Last Name", "Last name cannot be blank.")


def province(text):
    ValidProvinces = ["ON", "QC", "NS", "NB", "MB", "BC", "PE", "SK", "AB", "NL", "NT", "YT", "NU"]
    while True:
        Province = input(f"{text} (NL): ").upper()

        if Province in ValidProvinces:
            return Province
        else:
            print_error("Province must be valid.")

def postalCode(text):
    while True:
        PostalCode = input(f"{text} (A1B 2C3): ")
        if len(PostalCode) != 7:
            print_error("Postal code must be 6 digits with 1 space")
        elif not PostalCode[0].isalpha() or not PostalCode[1].isnumeric() or not PostalCode[2].isalpha():
            print_error("Postal code first 3 characters must be letter number letter.")
        elif not PostalCode[4].isnumeric() or not PostalCode[5].isalpha() or not PostalCode[6].isnumeric():
            print_error("Postal code last 3 characters must be number letter number.")
        else:
            return PostalCode

def yesOrNo(text):
    while True:
        Answer = input(f"{text} (Y/N): ").upper()
        if Answer == "Y":
            return True
        elif Answer == "N":
            return False
        else:
            print_error("Answer must be [Y]es or [N]o")


def print_error(error):
    """
    Print an error in a certain format.
    :param error: The error message
    """
    print(f"[Error]: {error}")
