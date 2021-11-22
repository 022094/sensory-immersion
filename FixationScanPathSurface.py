# DATE: March 11, 2021
# !/usr/bin/env python

import os
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import PupilFolderFileCheck as flchk

RECORDING = flchk.ask_location()
os.chdir(RECORDING)

#cleo_overlay = plt.imread('/home/fiza/Documents/SF_Immersion/cleooverlay.png')

def upload_reference():
	print("Please enter path to your reference image: ")
	reference = plt.imread(input())
	plt.figure(figsize=(8,8))
	plt.imshow(reference)
	plt.axis('off')
	return reference


def load_fixationdata():
	surface_fixation_export = Path(RECORDING).joinpath("surfaces").\
		joinpath("fixations_on_surface_Cleo.csv")
	surface_df = pd.read_csv(surface_fixation_export)
	fixation_on_surf = surface_df[surface_df.on_surf==True]
	return fixation_on_surf


# Visualize fixation data on surface

def draw_fixationpath():

	""" This function takes the fixations on surface csv file and the reference image as inputs,
	plots the fixation points as scan paths onto the reference images, and outputs the scatter plot."""

	fixation_on_surf = load_fixationdata()
	reference = upload_reference()
	grid = reference.shape[0:2] # width, height of the loaded image

	x = fixation_on_surf["norm_pos_x"]
	y = fixation_on_surf["norm_pos_y"]
	N = max(len(x), len(y))

	# flips the fixation point from the original coordinate system, where the origin
	# is at the bottom left, to the image coordinate system, where the origin is at top left
	y  = 1 - y

	# scale up the normalized coordinates for x and y
	x *= grid[1]
	y *= grid[0]

	point_scale = fixation_on_surf["duration"]
	id_labels = list(fixation_on_surf["fixation_id"])
	colors = np.random.rand(N)

	# display reference image
	plt.figure(figsize=(20, 20))
	plt.imshow(reference, alpha=0.5)

	# display the line and points for fixation
	polyline = plt.plot(x, y, "C3", lw=0.5)
	# use the duration to determine the scatter plot circle radius
	points = plt.scatter(x, y, s=point_scale * 0.05, c=colors, alpha=0.2)

	plt.xlabel("X position over time in seconds.")
	plt.ylabel("Y position over time in seconds.")
	plt.xlim([0, 1000])
	plt.ylim([520, 0])

	ax = plt.gca() # get plot current axes for annotation
	for i, l in enumerate(id_labels):
		ax.annotate(text=str(l), xy=(list(x)[i], list(y)[i]), fontsize=1)

	plt.show();

if __name__=="__main__":
	draw_fixationpath()
