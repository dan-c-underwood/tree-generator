"""
Module to generate a .obj 3D model of a tree recursively.
"""
import math
import ConfigParser
import copy
from collections import deque

import numpy as np

from obj import ObjWriter


random_en = None
writer = None
config = None


# Returns a random integer value from a normal distribution.
def _random_value_i(centre, scale=None):
    global random_en
    if random_en:
        if scale is None:
            return int(round(np.random.normal(centre, centre / 6 + np.nextafter(0, 1))))
        else:
            return int(round(np.random.normal(centre, scale)))
    else:
        return centre


# Returns a random float value from a normal distribution.
def _random_value_f(centre, scale=None):
    global random_en

    if random_en:
        if scale is None:
            return np.random.normal(centre, abs(centre / 6 + np.nextafter(0, 1)))
        else:
            return np.random.normal(centre, scale)
    else:
        return centre


# Convert degrees to radians.
def _deg2rad(degrees):
    radians = math.pi * degrees / 180
    return radians


# Creates a rotation matrix in the x axis
def _rot_x_matrix(x_rot):
    return np.array([[1, 0, 0, 0],
                     [0, math.cos(x_rot), -math.sin(x_rot), 0],
                     [0, math.sin(x_rot), math.cos(x_rot), 0],
                     [0, 0, 0, 1]])


# Creates a rotation matrix in the y axis
def _rot_y_matrix(y_rot):
    return np.array([[math.cos(y_rot), 0, math.sin(y_rot), 0],
                     [0, 1, 0, 0],
                     [-math.sin(y_rot), 0, math.cos(y_rot), 0],
                     [0, 0, 0, 1]])


# Creates a rotation matrix in the z axis
def _rot_z_matrix(z_rot):
    return np.array([[math.cos(z_rot), -math.sin(z_rot), 0, 0],
                     [math.sin(z_rot), math.cos(z_rot), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])


# Creates a translation matrix
def _translation_matrix(x_trans, y_trans, z_trans):
    return np.array([[1, 0, 0, x_trans],
                     [0, 1, 0, y_trans],
                     [0, 0, 1, z_trans],
                     [0, 0, 0, 1]])


# Creates a composite transformation matrix from all those in matrix_stack
def _tree_matrix(matrix_stack):
    temp_stack = copy.copy(matrix_stack)
    matrix = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    while temp_stack:
        matrix = temp_stack.pop().dot(matrix)

    return matrix


# Draws a leaf in the tree including the connecting segment of branch
def _draw_leaf(radius, length, matrix_stack):
    global writer
    global config

    faces = config.getfloat("params", "faces")
    leaf_length = _random_value_f(config.getfloat("params", "leaf_length"))
    leaf_width = _random_value_f(config.getfloat("params", "leaf_width"))

    rads_per_face = (2 * math.pi) / faces

    trunk_face = 0
    current_rot = 0

    t_matrix = _tree_matrix(matrix_stack)

    # Create the branch segment leading to the leaf
    while trunk_face < faces:
        vertices = []

        coords = t_matrix.dot(np.array([[radius * math.sin(current_rot + rads_per_face)],
                                        [0],
                                        [radius * math.cos(current_rot + rads_per_face)],
                                        [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        coords = t_matrix.dot(
            np.array([[0],
                      [length],
                      [0],
                      [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        coords = t_matrix.dot(np.array([[radius * math.sin(current_rot)],
                                        [0],
                                        [radius * math.cos(current_rot)],
                                        [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        writer.add_face(vertices, "stem")
        trunk_face += 1
        current_rot += rads_per_face

    # Create the leaf vertices
    vertices = []

    coords = t_matrix.dot(
        np.array([[0],
                  [length],
                  [0],
                  [1]]))
    vertices.append(writer.add_vertex(coords[0, 0],
                                      coords[1, 0],
                                      coords[2, 0]))

    coords = t_matrix.dot(np.array([[leaf_width],
                                    [length + 0.5 * leaf_length],
                                    [0],
                                    [1]]))
    vertices.append(writer.add_vertex(coords[0, 0],
                                      coords[1, 0],
                                      coords[2, 0]))

    coords = t_matrix.dot(
        np.array([[0],
                  [length + leaf_length],
                  [0],
                  [1]]))
    vertices.append(writer.add_vertex(coords[0, 0],
                                      coords[1, 0],
                                      coords[2, 0]))

    coords = t_matrix.dot(np.array([[-leaf_width],
                                    [length + 0.5 * leaf_length],
                                    [0],
                                    [1]]))
    vertices.append(writer.add_vertex(coords[0, 0],
                                      coords[1, 0],
                                      coords[2, 0]))

    writer.add_face(vertices, "leaf")


# Recursive function to draw tree stem and branches
def _draw_tree(depth, radius, length, matrix_stack):
    global writer
    global config

    faces = config.getfloat("params", "faces")
    branch_angle = _deg2rad(config.getfloat("params", "branch_angle"))
    branch_ratio = config.getfloat("params", "branch_ratio")
    stem_ratio = config.getfloat("params", "stem_ratio")
    branch_per_stem = _random_value_i(config.getint("params", "branch_per_stem"))
    max_depth = config.getint("params", "max_depth")

    # Draw branch segment
    rad_per_face = (2 * math.pi) / faces

    trunk_face = 0
    current_rot = 0

    t_matrix = _tree_matrix(matrix_stack)

    while trunk_face < faces:
        vertices = []

        coords = t_matrix.dot(np.array([[radius * math.sin(current_rot + rad_per_face)],
                                        [0],
                                        [radius * math.cos(current_rot + rad_per_face)],
                                        [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        coords = t_matrix.dot(
            np.array([[(radius * stem_ratio) * math.sin(current_rot + rad_per_face)],
                      [length],
                      [(radius * stem_ratio) * math.cos(current_rot + rad_per_face)],
                      [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        coords = t_matrix.dot(
            np.array([[(radius * stem_ratio) * math.sin(current_rot)],
                      [length],
                      [(radius * stem_ratio) * math.cos(current_rot)],
                      [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        coords = t_matrix.dot(np.array([[radius * math.sin(current_rot)],
                                        [0],
                                        [radius * math.cos(current_rot)],
                                        [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        writer.add_face(vertices, "stem")
        trunk_face += 1
        current_rot += rad_per_face

    # Once the max depth is reached then draw a leaf segment
    if depth == max_depth:
        matrix_stack.append(_translation_matrix(0, length, 0))
        _draw_leaf(radius * stem_ratio, length * stem_ratio, matrix_stack)
        return
    else:
        # Draw the stem
        new_matrix_stack = copy.copy(matrix_stack)
        new_matrix_stack.append(_translation_matrix(0, length, 0))

        _draw_tree(depth + 1, radius * stem_ratio, length * stem_ratio, new_matrix_stack)

        # Draw the branches that come from this segment of stem
        if branch_per_stem != 0:
            rads_per_branch = (2 * math.pi) / branch_per_stem
            current_angle = 0
            for branch in range(0, branch_per_stem):
                new_matrix_stack = copy.copy(matrix_stack)
                new_matrix_stack.append(_translation_matrix(0, _random_value_f(length), 0))
                new_matrix_stack.append(_rot_y_matrix(_random_value_f(current_angle, rads_per_branch * 2)))
                new_matrix_stack.append(_rot_x_matrix(_random_value_f(branch_angle)))

                _draw_tree(depth + 1, radius * branch_ratio, length * branch_ratio, new_matrix_stack)
                current_angle += rads_per_branch


def generate(pref_file, random, out_file="tree.obj"):
    """
    Base function that calls the recursive tree generation algorithm.

    :param pref_file: The name of the .ini file that contains the required parameters.
    :param random: Whether to apply randomness to the tree generation process (produces more "realistic" trees!).
    :param out_file: The name of the .obj file that the script will output into.
    """
    global writer
    writer = ObjWriter(out_file)
    global config
    config = ConfigParser.RawConfigParser()
    global random_en
    random_en = random

    config.read(pref_file.name)

    _draw_tree(0, config.getfloat("params", "radius"), config.getfloat("params", "length"), deque([]))
    writer.write_all()
    writer.close()