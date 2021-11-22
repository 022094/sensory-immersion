# Date: March 23, 2021
# !/usr/bin/env python

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import PupilFolderFileCheck as flchk

# LOAD EXPORTED DATA

RECORDING_LOCATION = flchk.ask_location()
os.chdir(RECORDING_LOCATION)


def load_surf_3dfixation():

    """ This function loads surface fixations. """

    exported_surf_fixations = os.path.join(RECORDING_LOCATION, "surfaces/fixations_on_surface_Cleo.csv")
    # load "_unix_datetime.csv" file after running TimeSync pyton file.
    surf_fixations_pd_frame = pd.read_csv(exported_surf_fixations)
    surf_fixations_pd_frame = surf_fixations_pd_frame[surf_fixations_pd_frame.on_surf==True]
    return surf_fixations_pd_frame


def filter_surf_3dfixation():

    """ This function loads the imported surface fixations data and stores the data post the first 5 seconds. """

    surf_fixations_pd_frame = load_surf_3dfixation()

    # skip first 5 seconds to allow for the 3D model of converge
    start_time = surf_fixations_pd_frame.start_timestamp.iloc[0] + 5
    detect_surf_fixation = surf_fixations_pd_frame[surf_fixations_pd_frame.start_timestamp > start_time]

    return detect_surf_fixation
