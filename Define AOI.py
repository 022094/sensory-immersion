# Date: August 12 2021
# !/usr/bin/env python

# Import Packages
import os
import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np
import FixationScanPathSurface as fsp


def main():

    """
    This program makes sure all of the functions within it are run. Make sure to specify parameters of functions that
    require them.
    @return: output of created functions.
    """

    AOI_ref(image = "/home/fiza/Documents/ClarkLabProjects/SF_Immersion/cleooverlay.png")
    select_fixations_data()


def AOI_ref(image):

    # Load Image and its Dimensions
    cleo = cv2.imread("/home/fiza/Documents/ClarkLabProjects/SF_Immersion/cleooverlay.png")
    (h, w, d) = cleo.shape
    print("width={}, height={}".format(w, h))
    cv2.imshow("Cleo", cleo)
    AOI_defined = cleo.copy()
    cv2.rectangle(AOI_defined, (77, 2), (946, 446), (255, 0, 0), 2)
    cv2.rectangle(AOI_defined, (77, 447), (483, 520), (100, 100, 100), 2)
    cv2.rectangle(AOI_defined, (484, 447), (669, 520), (0, 0, 255), 2)
    cv2.rectangle(AOI_defined, (670, 447), (946, 520), (0, 255, 0), 2)

    AOI_defined = cv2.imshow("AOI", AOI_defined)
    return AOI_defined


# Load fixation data
def select_fixations_data():
    fixations = fsp.load_fixationdata()
    fixations = fixations[['world_timestamp', 'world_index', 'fixation_id', 'start_timestamp',
                           'duration', 'dispersion', 'norm_pos_x', 'norm_pos_y', 'x_scaled', 'y_scaled']]
    return fixations


# Load data values onto pre-defined AOIs
def map_fixations():

    """
	This function takes the fixations on surface csv file and the reference image as inputs,
	plots the fixation points as scan paths onto the reference images, and outputs the scatter plot.
	"""

    fixations = select_fixations_data()
    reference = cv2.imread("/home/fiza/Documents/ClarkLabProjects/SF_Immersion/AOIsample_definedregions.png")[...,::-1]

    # tells you where/what the error is:
    assert not isinstance(reference, type(None)), 'image not found'

    grid = reference.shape[0:2] # width, height of the loaded image

    x = fixations["norm_pos_x"]
    y = fixations["norm_pos_y"]
    N = max(len(x), len(y))

    # flips the fixation point from the original coordinate system, where the origin
	# is at the bottom left, to the image coordinate system, where the origin is at top left
    y = 1 - y

    # scale up the normalized coordinates for x and y
    x *= grid[1]
    y *= grid[0]

    point_scale = fixations["duration"]
    id_labels = list(fixations["fixation_id"])

    # display reference image
    plt.figure(figsize=(16,16))
    plt.imshow(reference, alpha=0.5)

    # defining a colormap
    cdict = {'blue': [(77, 2), (946, 446)],
             'gray': [(77, 447), (483, 520)],
             'red': [(484, 447), (669, 520)],
             'green': [(670, 447), (946, 520)]}

    # OR create a colormap based on opencv edge detection?


    # use the duration to determine the scatter plot circle radius
    points = plt.scatter(x, y, s=point_scale * 0.05, c='black', alpha=0.2)

    plt.show()


if __name__=="__main__":
    AOI_ref(image = "/home/fiza/Documents/ClarkLabProjects/SF_Immersion/cleooverlay.png")
    select_fixations_data()
    map_fixations()
    draw_heatmap()
