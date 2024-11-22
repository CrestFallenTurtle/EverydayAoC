# Sections
VARIABLE_START_SECTION = "WAKE UP"
METHOD_START_SECTION = "EVERYDAY I WAKE UP"
MAIN_LOOP_SECTION = "PIECE OF SHIT"
END_LOOP_SECTION = "FUCK THIS SHIT"

# Sections that must appear in every file
REQUIRED_SECTIONS = {
    MAIN_LOOP_SECTION: False
}

# Sections that are optional, but will raise a warning if they
# are not present
OPTIONAL_SECTIONS = {
    VARIABLE_START_SECTION: False,
    METHOD_START_SECTION: False,
    END_LOOP_SECTION: False
}

# How comments look like
COMMENTS = "#"

# Library location
LIBS_LOCATION = "libs"