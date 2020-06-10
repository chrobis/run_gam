from sys import platform
import os
from pathlib import Path
import csv
import shutil

from run_gam_tool_box import run_gam_tools

newest_csv = run_gam_tools.oldest_workday_filename()


def test_workday_csv_path():
    sftp_path = run_gam_tools.workday_csv_path()
    if platform == "darwin":
        assert os.path.isdir(sftp_path)
    elif platform == "linux":
        assert os.path.isdir(sftp_path)
    else:
        assert not sftp_path


def test_oldest_workday_file():
    """
    When testing on macOS I have a mock folder of workday csv files, so i can predict the name that will result when
    running latest_workday_file().

    In production I have no automated way of predicting the outcome of the file name other than calling the function
    that's being tested here (latest_workday_file()).

    If the server is recently built this test will fail because there is no existing workday csv dump.

    """

    csv_file = run_gam_tools.oldest_workday_file_w_path()
    assert os.path.isfile(csv_file)

    if platform == "darwin":
        assert csv_file == "sftpuser/Lime_G_Suite_Identity_Management_File_01152020.csv"


def test_number_of_users_csv_file():
    # Acceptable number of users in csv file.
    acceptable_number_of_users = 1000
    csv_file = run_gam_tools.oldest_workday_file_w_path()
    acceptable_int_user_in_csv = run_gam_tools.number_of_users_in_csv_file(acceptable_number_of_users)
    assert acceptable_int_user_in_csv

    acceptable_number_of_users = 0
    acceptable_int_user_in_csv = run_gam_tools.number_of_users_in_csv_file(acceptable_number_of_users)
    assert not acceptable_int_user_in_csv


