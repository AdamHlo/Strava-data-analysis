import gpxpy
import numpy as np
from functools import cached_property
from itertools import islice


def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def calculate_speed(distances, times):
    np_distances = np.array(distances)
    np_times = np.array(times)
    convolved_distances = np.convolve(np_distances, np.ones(60), mode='same')
    convolved_times = np.convolve(np_times, np.ones(60), mode='same')
    speeds = convolved_distances / convolved_times
    return speeds * 3.6


def calculate_slope(elevation_differences, distances):
    np_elev_differences = np.array(elevation_differences)
    np_distances = np.array(distances)
    convolved_elev_differences = np.convolve(np_elev_differences, np.ones(60), mode='same')
    convolved_distances = np.convolve(distances, np.ones(60), mode='same')
    slopes = (convolved_elev_differences / convolved_distances) * 100
    return slopes


class Activity:
    # TODO: class that merges all segments from all tracks into one (ofc consistently)
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.gpx = gpxpy.parse(file)

    @cached_property
    def distances(self):
        pass
