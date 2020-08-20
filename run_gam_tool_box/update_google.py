"""
Kick off the gam update

"""


def run(file_path_to_csv):
    command = f"../bin/gam/gam csv {file_path_to_csv} gam ~Action " \
              f"user '~Email Address' " \
              f"firstname '~Preferred First Name' " \
              f"lastname '~Preferred Last Name' " \
              f"otheremail home '~Personal Email Address' " \
              f"Employee_Office_Location.Work_Location '~Building_ID' " \
              f"Employee_Office_Location.Work_Address '~Work Address' " \
              f"Employee_Office_Location.City '~City' " \
              f"Employee_Office_Location.State '~State' " \
              f"Employee_Office_Location.Country_Code '~Country Code' " \
              f"Employee_Record_Info.Legal_Last_Name '~Legal Last Name' " \
              f"Employee_Record_Info.Legal_First_Name '~Legal First Name' " \
              f"Employee_Record_Info.Hire_Date '~Hire Date' " \
              f"Employee_Record_Info.Employee_ID '~Workday Employee ID' " \
              f"Employee_Record_Info.Manager_ID '~Workday Manager ID' " \
              f"Employee_Record_Info.Is_a_Manager '~IsManager' " \
              f"relation manager '~Managers Email' " \
              f"location type default area '~Building_ID' endlocation " \
              f"organization title '~Employee Title' " \
              f"description '~Employee Type' " \
              f"costCenter '~Cost Center ID' " \
              f"department '~Cost Center Name' primary"

    return command

