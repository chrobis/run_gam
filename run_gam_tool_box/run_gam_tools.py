from datetime import datetime
from sys import platform
from pathlib import Path
import os
import csv
import getpass
import sys
from typing import Union
sys.path.insert(0, "g_directory/")


def workday_csv_path() -> Union[bool, str]:
    """ Find the correct path to csv files from workday.

    In production the csv files coming from workday will be dumped at /home/sftpuser. In testing the mock workday dump
    files will be at "PROJECT_ROOT/sftpuser". As of now macOS is only used when developing the software. So if the OS is
    macOS then use the mock file path "sftpuser". If the OS is linux then use the production path "/home/sftpuser/".

    Returns:
        Union[bool, str]: If OS is linux or darwin (macOS) then return a str of a file path, else return False.
    """
    if platform == "darwin":
        sftp_file_path = Path("sftpuser")
    elif platform == "linux":
        sftp_file_path = Path("/home/sftpuser/")
    else:
        sftp_file_path = False

    return sftp_file_path


def oldest_workday_file_w_path() -> str:
    """Get the oldest workday csv file

    Workday dumps the csv files at /home/sftpuser. This function loops through all of the files that start with
    "Lime_G_Suite_Identity_Management_File_" and end in ".csv". It parses the timestamp in the file name and returns the
     latest file.

    Returns:
        str: Filename with path to the oldest workday csv file.
    """
    oldest = []
    path = workday_csv_path()
    for file in os.listdir(path):
        if "Lime_G_Suite_Identity_Management_File_" in file and ".csv" in file:
            time_stamp = str(file).split("_")[-1].replace(".csv", "")
            file_date = datetime.strptime(time_stamp, '%m%d%Y')
            if not oldest:
                oldest.append(f"{path}/{file}")
                oldest.append(file_date)
            elif file_date < oldest[1]:
                oldest[0] = f"{path}/{file}"
                oldest[1] = file_date

    return oldest[0]


def oldest_workday_filename() -> str:
    oldest_csv = []
    for file in os.listdir(workday_csv_path()):
        if "Lime_G_Suite_Identity_Management_File_" in file and ".csv" in file:
            time_stamp = str(file).split("_")[-1].replace(".csv", "")
            file_date = datetime.strptime(time_stamp, '%m%d%Y')
            if not oldest_csv:
                oldest_csv.append(file)
                oldest_csv.append(file_date)
            elif file_date < oldest_csv[1]:
                oldest_csv[0] = file
                oldest_csv[1] = file_date

    return oldest_csv[0]


def number_of_users_in_csv_file(approved_int_of_users: int) -> bool:
    """Confirm that the number of users in csv file is acceptable.

    Open the csv file and count the number of users. If the number of users is higher than the approved_int_of_users
    then return as False else return as true.

    Args:
        approved_int_of_users: The number of users that are allowed in the csv file.

    Returns:
        bool: If the number of users is higher than the approved_int_of_users then return as False else return as true.

    """
    #
    read = 'r'
    int_of_users_in_csv_file = 0
    csv_file = oldest_workday_file_w_path()
    with open(csv_file, mode=read) as csv_file:
        line_count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for user_row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                int_of_users_in_csv_file += 1

    if int_of_users_in_csv_file <= approved_int_of_users:
        acceptable_user_count = True
    else:
        acceptable_user_count = False

    return acceptable_user_count


def create_action_csvs(src_filename, off_board_users_dst_filename, on_board_update_users_dst_filename):
    read = 'r'
    headers = None
    delete_users = []
    create_update_users = []
    with open(src_filename, mode=read) as csv_file:
        line_count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for user_row in csv_reader:
            if line_count == 0:
                headers = user_row
                line_count += 1
            else:
                action = user_row[0]
                if action == "delete":
                    delete_users.append(user_row)
                elif action == "create" or action == "update":
                    create_update_users.append(user_row)

    write = "w"
    with open(off_board_users_dst_filename, mode=write) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for del_user in delete_users:
            csv_writer.writerow(del_user)

    with open(on_board_update_users_dst_filename, mode=write) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(headers)
        for create_update_user in create_update_users:
            csv_writer.writerow(create_update_user)









