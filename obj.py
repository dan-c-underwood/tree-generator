class ObjWriter:
    """Class to handle the writing to a .obj file. """
    def __init__(self, filename):
        """
        Initialise a file to be written to.

        :param filename: Name of the eventual file to be created.
        :return: Instance of a ObjWriter.
        """
        self.file = open(filename, 'w')
        self.vertices = []
        self.faces = {}
        self.v_seq_num = 1

    def add_vertex(self, x, y, z):
        """
        Creates a Vertex object instance and adds it to the writer.

        :param x: x-coordinate for the vertex.
        :param y: y-coordinate for the vertex.
        :param z: z-coordinate for the vertex.
        :return: An instance of the Vertex class.
        """
        v = Vertex(x, y, z, self.v_seq_num)
        self.v_seq_num += 1
        self.vertices.append(v)
        return v

    def write_vertices(self):
        """
        Write all created vertices to the actual file.
        """
        for v in self.vertices:
            self.file.write(str(v))

        self.file.write("\n")

    def add_face(self, vertices, group=None):
        """
        Creates a Face object instance and adds it to the writer.

        :param vertices: A list of Vertex objects.
        :param group: An optional group name for the face to belong to.
        """
        vertices_num = []
        for v in vertices:
            vertices_num.append(v.num)

        if group is None:
            if '_none' not in self.faces:
                self.faces['_none'] = []
            self.faces['_none'].append(Face(vertices_num))
        else:
            if group not in self.faces:
                self.faces[group] = []
            self.faces[group].append(Face(vertices_num))

    def write_faces(self):
        """
        Write all instances of a Face object to the file. Splits Faces into groups where provided.
        """
        for face_group in self.faces.keys():
            if face_group is not "_none":
                self.file.write("g " + face_group + "\n")
            for face in self.faces[face_group]:
                self.file.write(str(face))

        self.file.write("\n")

    def write_all(self):
        """
        Write both all vertices and all faces to the file.
        """
        self.write_vertices()
        self.write_faces()

    def close(self):
        """
        Closes the file.
        """
        self.file.close()


class Vertex:
    """Class to represent a Vertex in 3D space for writing to a .obj file."""
    def __init__(self, x, y, z, num):
        """
        Initialise a Vertex object.

        :param x: x-coordinate for the vertex.
        :param y: y-coordinate for the vertex.
        :param z: z-coordinate for the vertex.
        :param num: The sequence number of the Vertex (for linking Vertices to Faces)
        :return: An instance of a Vertex object.
        """
        self.x = x
        self.y = y
        self.z = z
        self.num = num

    def __str__(self):
        """
        Write the Vertex as needed for the .obj file.
        """
        return "v " + str(self.x) + " " + str(self.y) + " " + str(self.z) + "\n"


class Face:
    """Class to represent a Face consisting of multiple Vertices"""
    def __init__(self, vertices_num):
        """
        Initialise a Face object.

        :param vertices_num: A list of the numbers of each Vertex to be added to the face (list larger than 3).
        :return: An instance of a Face object.
        """
        if len(vertices_num) <= 3:
            raise Exception("A face must have at least three vertices")
        self.vertices_num = vertices_num

    def __str__(self):
        """
        Write the Face as needed for the .obj file.
        """
        face = "f"
        for vertex_num in self.vertices_num:
            face += (" " + str(vertex_num))

        face += "\n"

        return face