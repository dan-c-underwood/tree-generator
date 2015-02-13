class ObjWriter:

    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.vertices = []
        self.faces = []
        self.v_seq_num = 1

    def add_vertex(self, x, y, z):
        v = Vertex(x, y, z, self.v_seq_num)
        self.v_seq_num += 1
        self.vertices.append(v)
        return v

    def write_vertices(self):
        for v in self.vertices:
            self.file.write(str(v))

        self.file.write("\n")

    def add_face(self, vertices, group=None):
        vertices_num = []
        for v in vertices:
            vertices_num.append(v.num)

        self.faces.append(Face(vertices_num))

    def write_faces(self):
        for face in self.faces:
            self.file.write(str(face))

        self.file.write("\n")

    def write_all(self):
        self.write_vertices()
        self.file.write("g all\n")
        self.write_faces()

    def close(self):
        self.file.close()


class Vertex:

    def __init__(self, x, y, z, num):
        self.x = x
        self.y = y
        self.z = z
        self.num = num

    def __str__(self):
        return "v " + str(self.x) + " " + str(self.y) + " " + str(self.z) + "\n"


class Face:

    def __init__(self, vertices_num):
        if len(vertices_num) < 3:
            raise Exception("A face must have at least three vertices")
        self.vertices_num = vertices_num

    def __str__(self):
        face = "f"
        for vertex_num in self.vertices_num:
            face += (" " + str(vertex_num))

        face += "\n"

        return face