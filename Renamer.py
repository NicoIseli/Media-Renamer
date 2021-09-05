import Configuration

from datetime import date
import os
os.getcwd()


""" PATH ENTRY """

# VARIABLES OF PATH ENTRY
path = input("Path:\t\t").replace("\\", "/")


""" COUNTRY ENTRY """

# VARIABLES OF COUNTRY ENTRY
correct_country = False

# VALIDATION OF COUNTRY ENTRY
while not correct_country:
    country = input("\nCountry:\t").upper()

    if Configuration.MIN_LENGTH_OF_COUNTRY_CODE <= len(country) <= Configuration.MAX_LENGTH_OF_COUNTRY_CODE:
        correct_country = True
    else:
        print("\nERROR: The country code must contain between two and three letters. Please enter another one:")


""" YEAR ENTRY """

# VARIABLES OF YEAR ENTRY
correct_year = False

# VALIDATION OF YEAR ENTRY
while not correct_year:
    year = input("\nYear:\t\t")

    if int(year) <= date.today().year:
        correct_year = True
    else:
        print("\nERROR: The entered year is not in the given range. Please enter another one:")


""" FORMAT ENTRY """

# VARIABLES OF FORMAT ENTRY
correct_format = False

# VALIDATION OF FORMAT ENTRY
while not correct_format:
    input_format = input("\nFormat:\t\t").lower()

    for file_ending in Configuration.VALID_FORMATS:
        if input_format == file_ending:
            correct_format = True

    if not correct_format:
        print("\nERROR: This format does not exist. Please enter another one:")


""" LOOP FOR RENAMING THE FILES BASED ON A SPECIFIC NAME """
for i, filename in enumerate(os.listdir(path)):
    os.rename(path + "/" + filename, path + "/" + country + "_" + year + "_" + str(i+1) + "." + input_format)
