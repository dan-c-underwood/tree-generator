import numpy as np
import math
import ConfigParser
import copy
import random
from collections import deque

from obj import ObjWriter


def deg2rad(degrees):
    radians = math.pi * degrees / 180
    return radians


def rot_x_matrix(x_rot):
    return np.array([[1, 0, 0, 0],
                         [0, math.cos(x_rot), -math.sin(x_rot), 0],
                         [0, math.sin(x_rot), math.cos(x_rot), 0],
                         [0, 0, 0, 1]])

def rot_y_matrix(y_rot):
    return np.array([[math.cos(y_rot), 0, math.sin(y_rot), 0],
                         [0, 1, 0, 0],
                         [-math.sin(y_rot), 0, math.cos(y_rot), 0],
                         [0, 0, 0, 1]])

def rot_z_matrix(z_rot):
    return np.array([[math.cos(z_rot), -math.sin(z_rot), 0, 0],
                         [math.sin(z_rot), math.cos(z_rot), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])


def translation_matrix(x_trans, y_trans, z_trans):
    return np.array([[1, 0, 0, x_trans],
                     [0, 1, 0, y_trans],
                     [0, 0, 1, z_trans],
                     [0, 0, 0, 1]])


def tree_matrix(matrix_stack):
    temp_stack = copy.copy(matrix_stack)
    matrix = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    while temp_stack:
        matrix = temp_stack.pop().dot(matrix)

    return matrix

def draw_leaf(matrix_stack):
    vertices = []


def draw_tree(depth, radius, length, matrix_stack):
    global writer
    global config

    faces = config.getfloat("params", "faces")
    stem_angle = deg2rad(config.getfloat("params", "stem_angle"))
    branch_ratio = config.getfloat("params", "branch_ratio")
    stem_ratio = config.getfloat("params", "stem_ratio")
    branch_per_stem = config.getint("params", "stem_per_branch")
    max_depth = config.getint("params", "max_depth")

    # Draw branch segment
    rad_per_face = (2 * math.pi) / faces

    trunk_face = 0
    current_rot = 0

    t_matrix = tree_matrix(matrix_stack)

    while trunk_face < faces:
        vertices = []
        coords = t_matrix.dot(np.array([[radius * math.sin(current_rot)],
                                        [0],
                                        [radius * math.cos(current_rot)],
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

        coords = t_matrix.dot(
            np.array([[(radius * stem_ratio) * math.sin(current_rot + rad_per_face)],
                      [length],
                      [(radius * stem_ratio) * math.cos(current_rot + rad_per_face)],
                      [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        coords = t_matrix.dot(np.array([[radius * math.sin(current_rot + rad_per_face)],
                                        [0],
                                        [radius * math.cos(current_rot + rad_per_face)],
                                        [1]]))
        vertices.append(writer.add_vertex(coords[0, 0],
                                          coords[1, 0],
                                          coords[2, 0]))

        writer.add_face(vertices)
        trunk_face += 1
        current_rot += rad_per_face

    if depth == max_depth:
        draw_leaf(matrix_stack)
        return
    else:
        # Continue stem
        # new_translation = [translation[0], translation[1] + (length * (math.sin(deg2rad(90) - rotation[0]))),
        #                    translation[2] + (length * (math.cos(deg2rad(90) - rotation[0])))]
        # new_rotation = [rotation[0], rotation[1], rotation[2]]
        new_matrix_stack = copy.copy(matrix_stack)
        new_matrix_stack.append(translation_matrix(0, length, 0))

        draw_tree(depth + 1, radius * stem_ratio, length * stem_ratio, new_matrix_stack)

        rads_per_branch = (2 * math.pi) / branch_per_stem
        current_angle = 0
        for branch in range(0, branch_per_stem):
            # Draw branch
            # new_translation = [translation[0], translation[1] + (length * (math.sin(deg2rad(90) - rotation[0]))),
            #                    translation[2] + (length * (math.cos(deg2rad(90) - rotation[0])))]
            # new_rotation = [rotation[0] + (random.random() * stem_angle), rotation[1] + (random.random() * current_angle), rotation[2]]

            new_matrix_stack = copy.copy(matrix_stack)
            new_matrix_stack.append(translation_matrix(0, length, 0))
            new_matrix_stack.append(rot_y_matrix(current_angle))
            new_matrix_stack.append(rot_x_matrix(stem_angle))

            draw_tree(depth + 1, radius * branch_ratio, length * branch_ratio, new_matrix_stack)
            current_angle += rads_per_branch


writer = ObjWriter("tree.obj")
config = ConfigParser.RawConfigParser()
config.read("tree.ini")

draw_tree(0, config.getfloat("params", "radius"), config.getfloat("params", "length"), deque([]))
writer.write_vertices()
writer.write_faces()
writer.close()