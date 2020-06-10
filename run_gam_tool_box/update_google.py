"""
Kick off the gam update

"""


def run(file_path_to_csv):
    command = f"../bin/gam/gam csv {file_path_to_csv} gam ~Action " \
              f"user '~Email Address' " \
              f"firstname '~First Name' " \
              f"lastname '~Last Name' " \
              f"Employee_Information.City '~City' " \
              f"Employee_Information.State '~Building_ID' " \
              f"Employee_Information.Country_Code '~State' " \
              f"Employee_Information.Country '~Country Code' " \
              f"Workday_Custom_Attribute.Workday_Employee_ID '~Workday Employee ID' " \
              f"Workday_Custom_Attribute.Workday_Manager_ID '~Workday Manager ID' " \
              f"relation manager '~Managers Email' " \
              f"organization title '~Employee Title' " \
              f"department '~Cost Center' primary"

    return command

