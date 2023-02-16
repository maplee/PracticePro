import numpy as np


class MTL:
    def __init__(self, fdir, filename):
        self.mtlnames = []
        self.kas = []
        self.kds = []
        self.kes = []
        self.shininess = []
        self.dissolves = []
        self.illums = []

        mtl = None
        for line in open(fdir + filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'newmtl':
                self.mtlnames.append(values[1])
            elif values[0] == 'Kd':
                self.kds.append((values[1],values[2],values[3]))
            elif values[0] == 'Ka':
                self.kas.append((values[1],values[2],values[3]))
            elif values[0] == 'Ke':
                self.kes.append((values[1],values[2],values[3]))
            elif values[0] == 'illum':
                self.illums.append(values[1])
                self.shininess.append(50)
                self.dissolves.append(1)
            else:
                pass





class OBJ:
    def __init__(self, fdir, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.meshs = []

        self.mtl = None

        material = None
        for line in open(fdir + filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                # v = map(float, values[1:4])
                v = [float(x) for x in values[1:4]]
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                # v = map(float, values[1:4])
                v = [float(x) for x in values[1:4]]
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == 'vt':
                v = [float(x) for x in values[1:3]]

                self.texcoords.append(v)
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'mtllib':
                # print(values[1])
                # self.mtl = MTL(fdir,values[1])
                self.mtl = [fdir, values[1]]
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0])-1)
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1])-1)
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2])-1)
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))


        for loop in range(len(self.faces)):
            fss = self.faces[loop]
            vss = fss[0]
            nss = fss[1]
            vnss = fss[2]
            index = 1
            while (index < len(vss) and (index + 1) < len(vss)):
                self.meshs.append(([vss[0], vss[index], vss[index + 1]],
                                   [nss[0], nss[index], nss[index + 1]],
                                    [vnss[0], vnss[index], vnss[index + 1]]))
                index += 1

    def create_bbox(self):
        # self.vertices is not None
        ps = np.array(self.vertices)
        vmin = ps.min(axis=0)
        vmax = ps.max(axis=0)

        self.bbox_center = (vmax + vmin) / 2
        self.bbox_half_r = np.max(vmax - vmin) / 2
