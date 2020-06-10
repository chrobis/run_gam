"""

Steps:
    Find the newest workday export.

    Define the number of acceptable users in the csv file.

    If the number of users in the csv is more or equal to acceptable number of users. Then the code is allowed to run
    without any human intervention.

    Else a human must look at the csv and then change the number of acceptable number of users.


    * create a folder with todays date to be used to dump files to it.

    Move csv to g drive.

    open csv and move all delete action rows to a separate csv.
    move the delete csv to g drive.

    run gam on the original csv that no longer has delete actions

    move the original csv that no longer has delete actions to g drive
"""
from datetime import datetime
import os
import sys
import shutil
from sys import platform
from pathlib import Path
from subprocess import Popen, PIPE
from run_gam_tool_box import update_google

from run_gam_tool_box import run_gam_tools


# Acceptable number of users in csv file.
acceptable_number_of_users = 25

if run_gam_tools.number_of_users_in_csv_file(acceptable_number_of_users):

    # Get the filename of the oldest csv file from workday
    oldest_csv_filename = run_gam_tools.oldest_workday_filename()

    # Create the name for the staging folder
    staging_base_folder = Path(oldest_csv_filename.replace(".csv", f"_{datetime.utcnow().strftime('%H_%M_%S')}"))
    print(staging_base_folder)
    # Create the base folder that will get GAM related files
    os.mkdir(staging_base_folder)
    # Copy the newest workday csv to the base_folder
    shutil.copy(run_gam_tools.oldest_workday_file_w_path(), staging_base_folder)

    # CLEAN UP STAGING AREA
    if platform == "darwin":
        shutil.rmtree(staging_base_folder)
    elif platform == "linux":
        staged_file = f"{staging_base_folder}/{run_gam_tools.oldest_workday_filename()}"
        os.system(f"{update_google.run(staged_file)}")
        os.remove(run_gam_tools.oldest_workday_file_w_path())


else:
    path_to_workday_dump = run_gam_tools.oldest_workday_file_w_path()
    print(f"There are too many users in the {path_to_workday_dump}. "
          f"Check the file and make sure its correct before increasing the number of acceptable users.")






