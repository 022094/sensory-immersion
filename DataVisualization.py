# Data: Jan 31, 2021
# !/usr/bin/env python

import os

import pandas as pd
from IPython.display import display

import PupilFolderFileCheck as flchk

# LOAD EXPORTED DATA

RECORDING_LOCATION = flchk.ask_location()
os.chdir(RECORDING_LOCATION)

def load_3Ddata():

	''' This function imports pupil positions data and loads data. '''

	exported_pupil_csv = os.path.join(RECORDING_LOCATION, 'pupil_positions_unix_datetime.csv')	# load "_unix_datetime.csv" file after running TimeSync pyton file.
	pupil_pd_frame = pd.read_csv(exported_pupil_csv)
	return pupil_pd_frame


def filter_3Ddata():

	''' This function loads imports and stores data post the first 5 seconds. '''

	pupil_pd_frame = load_3Ddata()

	# filter for 3D data
	detector_3d_data = pupil_pd_frame[pupil_pd_frame.method == '3d c++']

	# skip first 5 seconds to allow for the 3D model of converge
	start_time = detector_3d_data.pupil_timestamp.iloc[0] + 5
	detector_3d_data = detector_3d_data[detector_3d_data.pupil_timestamp > start_time]

	return detector_3d_data


def display_filtered_3Ddata():

	''' This function takes in the filtered 3D data and then prints that data. '''

	pupil_pd_frame = load_3Ddata()
	detector_3d_data = filter_3Ddata()
	

	# split in right eye
	eye0_df = detector_3d_data[detector_3d_data.eye_id == 0]
	pd.options.display.float_format = '{:.3f}'.format

	print("Columns present in pupil data: ")
	print(list(pupil_pd_frame.columns))

	print("eye0 (right eye) data: ")
	display(eye0_df[['pupil_timestamp', 'eye_id', 'confidence', 'norm_pos_x', 'norm_pos_y', 'diameter_3d']].head(10))


# VISUALIZE PUPILLOMETRY DATA

import matplotlib.pyplot as plt

# Plot Pupil Diameter

def draw_plots():

	''' This function plots pupil positions and diameter using Pupil timestamps. After running TimeSync python file,
	you can plot using the System Time, i.e. Unix timestamps. '''

	pupil_pd_frame = load_3Ddata()
	detector_3d_data = filter_3Ddata()


	eye0_df = detector_3d_data[detector_3d_data.eye_id == 0]

	plt.figure(figsize=(16, 5))
	plt.plot(eye0_df['pupil_timestamp_unix'], eye0_df['diameter_3d'])
	plt.legend(['eye0'])
	plt.xlabel('Unix Timestamps [s]')
	plt.ylabel('Diameter [mm]')
	plt.title('Pupil Diameter')
	plt_pupil_diameter = plt.show()
	plt_pupil_diameter

# Plotting values with CI of over 0.95

	eye0_high_conf_df = eye0_df[eye0_df['confidence'] > 0.90]  # you can change confidence interval

	plt.figure(figsize=(16, 5))
	plt.plot(eye0_high_conf_df['pupil_timestamp_unix'], eye0_high_conf_df['diameter_3d'])
	plt.legend(['eye0'])
	plt.xlabel('Unix Timestamps [s]') # change x-axis to pupil_timestamp_unix column in the file.
	plt.ylabel('Diameter [mm]')
	plt.title('Pupil Diameter (only high confidence values)')
	plt.show()

# Plot Pupil Positions

	plt.figure(figsize=(16, 5))

	# plot right eye
	plt.plot(eye0_high_conf_df['pupil_timestamp_unix'], eye0_high_conf_df['norm_pos_x'])
	plt.plot(eye0_high_conf_df['pupil_timestamp_unix'], eye0_high_conf_df['norm_pos_y'])
	plt.xlabel('Unix Timestamps')
	plt.ylabel('norm_pos')
	plt.title('Pupil Position of Right Eye')
	plt.legend("xy")
	plt.show()

# Plot Spatial Distribution

	plt.figure(figsize=(16, 5))

	# plot right eye
	plt.plot(eye0_high_conf_df['pupil_timestamp'], eye0_high_conf_df['norm_pos_x'])
	plt.plot(eye0_high_conf_df['pupil_timestamp'], eye0_high_conf_df['norm_pos_y'])
	plt.xlabel('System Timestamps')
	plt.ylabel('norm_pos')
	plt.title('Spatial Distribution of Pupil Position of Right Eye')
	plt.legend("xy")
	plt.show()

if __name__ == '__main__': 

	''' Lets call all of the above functions and look at our data! '''

	display_filtered_3Ddata()
	draw_plots()
