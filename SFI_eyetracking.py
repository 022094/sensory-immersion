# Date: May 30 2021
# !/usr/bin/env python

import csv
import os

import matplotlib.pyplot as plt
import numpy as np

import FixationScanPathSurface as fsp
import PupilFolderFileCheck as flchk

RECORDING = flchk.ask_location()
os.chdir(RECORDING)

# LOAD EXPORTED DATA

# ref = fsp.upload_reference() ?

def main():

    '''
    This program makes sure all of the functions within it are run. Make sure to specify parameters of functions that
    require them.
    @return: output of created functions.
    '''

    load_file(filename = 'export_info.csv')
    get_export_duration()
    select_fixations_data()
    define_AOI_dict()


def load_file(filename):

    '''
    @param filename: specify name of file you want to load
    @return: loaded dataframe.
    '''

    with open(filename, "r") as file:
        reader = list(csv.reader(file))
        return reader


def get_export_duration():

    '''
    Calculates the duration of the task based on its export info
    @return: duration of the entire task.
    '''

    x = load_file(filename='export_info.csv')
    y = x[14]
    y = y[1:]
    print(y)

    time1 = float(input('Enter absolute start time (displayed in seconds) of the task export printed above: '))
    time2 = float(input('Enter absolute end time (displayed in seconds) of the task export printed above: '))
    Duration = time2 - time1
    return Duration


def select_fixations_data():
    fixations = fsp.load_fixationdata()
    fixations = fixations[['world_timestamp', 'world_index', 'fixation_id', 'start_timestamp',
                           'duration', 'dispersion', 'norm_pos_x', 'norm_pos_y', 'x_scaled', 'y_scaled']]
    return fixations


a = fixations['x_scaled'].between(aoi_reels['reels'][0][0], aoi_reels['reels'][1][0], inclusive=True)
fixations['fixation_id'][a]
fixations['fixation_id'][a].values
plt.figure(); plt.plot(fixations['fixation_id'][a].values)
np.unique(fixations['fixation_id'][a].values)

# use function above to get all values within dataframe that match all values of the key.


'''
    AOI = {'reels' : [(fixations.norm_pos_x >= 0.116211) & (fixations.norm_pos_x <= 0.883789) 
    & (fixations.norm_pos_y >= 0.161538) & (fixations.norm_pos_y <= 0.95)], 
    'win' : [(fixations.norm_pos_x >= 0.661133) & (fixations.norm_pos_x <= 0.864258) 
    & (fixations.norm_pos_y >= 0.007692) & (fixations.norm_pos_y <= 0.136538)], 
    'credit' : [(fixations.norm_pos_x >= 0.478516) & (fixations.norm_pos_x <= 0.648438) 
    & (fixations.norm_pos_y >= 0.026923) & (fixations.norm_pos_y <= 0.111538)]}

    def define_AOI_dict():


    This function creates a dictionary of pre-defined AOIs.
    @return: defined AOI dictionary
    

    xr, yr = [np.arange(0.116211, 0.883789+0.000001, 0.000001), np.arange(0.161538, 0.95+0.000001, 0.0000001)]
    xw, yw = [np.arange(0.661133, 0.864258+0.000001, 0.000001), np.arange(0.00769, 0.136538+0.000001, 0.000001)]
    xc, yc = [np.arange(0.478516, 0.648438+0.000001, 0.000001), np.arange(0.026923, 0.111538+0.000001, 0.000001)]
    AOI = {'reels' : [xr, yr], 'win' : [xw, yw], 'credit' : [xc, yc]}
    df = pd.DataFrame(list(AOI.items()), columns = ['Region', 'Coordinates'])
    return AOI 


    def filter_fixation_export():
    
    The goal of this function is to filter exported fixation data based
    @return:
    
    AOI_dict = define_AOI_dict()
    fixations = select_fixations_data()
    x, y = [fixations.norm_pos_x, fixations.norm_pos_y] 


Goals:
    1. Define an AOI dictionary (DONE)
    2. Use coordinates to filter data?
    3. Loop through csv.
    4. Compare coordinates with dictionary
    
'''



# Define AOIs (on an image) and otherwise
# Get x, y coordinates from the uploaded csv file
# Divide those coordinates to different AOIs based on pre-defined AOIs
# Calculate dwell time and fixations
# dwell time: percentage of task time spent fixating on an AOI.






if __name__=="__main__":
	main()
