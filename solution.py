import re  # Import the regular expression module

def parse_address(address):
    # Check if the input is a non-empty string
    if not isinstance(address, str) or not address.strip():
        raise ValueError("Invalid address input.")

    # Remove leading and trailing whitespace from the input string
    address = address.strip()

    # Define a list of regular expression patterns to match against the input string
    patterns = [
        r'^(?P<street>.*\D) (?P<housenumber>\d.*|\d)$',  # Matches "street name housenumber" or "street name housenumberA"
        r'^(?P<housenumber>\d+),? (?P<street>.*)$',  # Matches "housenumber, street name" or "housenumber,street name"
        r'^(?P<street>.*),? (?P<housenumber>\d.*)$',  # Matches "street name, housenumber" or "street name,housenumberA"
        r'^(?P<street>.*\D) (?P<housenumber>No \d.*)$',  # Matches "street name No housenumber" or "street name No housenumberA"
        r'^(?P<housenumber>[a-zA-Z]*\d+),? (?P<street>.*)$',  # Matches "housenumberA, street name" or "housenumberA,street name"
        r'^(?P<street>[^-]+)-(?P<housenumber>[^-]+)-(?P<extra>[^-]+)$',  # Matches "street name-housenumber-extra"
        r'^(?P<housenumber>\d+) (?P<street>.+ [NS][EW]?)$',  # Matches "housenumber street name direction"
        r'^(?P<street>.*),? (?P<housenumber>Floor \d+)$',  # Matches "street name, Floor number"
        r'^(?P<housenumber>\d+\/\d+) (?P<street>.*)$',  # Matches "housenumberA/housenumberB street name"
        r'^(?P<street>.*),? (?P<housenumber>\d+\/\d+)$',  # Matches "street name, housenumberA/housenumberB"
        r'^(?P<housenumber>\d+),? (?P<street>.*\D) (?P<extra>\d+\/\d+[a-zA-Z]?)$',  # Matches "housenumber, street name extra" or "housenumber,street name extra"
        r'^(?P<street>.*\D) (?P<housenumber>\d+[a-zA-Z]*\s?[a-zA-Z]*),? (?P<extra>[^-]+)$',  # Matches "street name housenumberAextra" or "street name housenumberA extra"
        r'^(?P<street>.*\D) (?P<housenumber>\d+),? (?P<extra>[^-]+)$',  # Matches "street name housenumberA extra" or "street name, housenumberA extra"
        r'^(?P<street>.*\D) (?P<housenumber>\d+[-:\/#]\d+)$',  # Matches "street name housenumberA-housenumberB"
        ]

    # Use a generator expression to iterate over the regular expression patterns
    # and try to match them against the input string using re.match
    match = next((re.match(pattern, address, re.IGNORECASE) for pattern in patterns if re.match(pattern, address, re.IGNORECASE)), None)

    # If a match is found, extract the street name, housenumber, and extra information (if any)
    if match:
        street = match.group("street").strip()
        housenumber = match.group("housenumber").strip()
        extra = match.group("extra") if "extra" in match.groupdict() else ""

        # Remove trailing comma from the street name, if present
        if street[-1] == ',':
            street = street[:-1]

        # If the address contains ", Haus" but the housenumber does not, add it to the housenumber
        if ", Haus" in address and ", Haus" not in housenumber:
            housenumber += ", " + extra.strip()

        # Handle the case with 'No' in the housenumber
        if "No " in address and "No " not in housenumber:
            no_index = address.find("No ")
            if no_index > 0 and address[no_index - 1].isspace():
                street = address[:no_index].strip()
                housenumber = address[no_index:].strip()

        # Return a dictionary containing the street name and housenumber (and extra information, if any)
        return {"street": street, "housenumber": housenumber}

    # If no match is found, raise a ValueError
    raise ValueError("Unable to parse the address.")

