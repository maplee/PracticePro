import os
import sys
from objLoader import OBJ, MTL
import cv2
import struct
from bitarray import bitarray


def str2bitarray(s):
    ret = bitarray(''.join([bin(int('1' + hex(c)[2:], 16))[3:] for c in s.encode('utf-8')]))
    return ret


def bitarray2str(bit):
    return bit.tobytes().decode('utf-8')

def encode(s):
    return ' '.join([bin(ord(c)).replace('<0b', '') for c in s])


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


if __name__ == '__main__':
    print(sys.argv)

path = "/Users/matt/Desktop/model/jiangshiche3/"
path = "/Users/matt/Downloads/hq/"
path = "/Users/matt/Documents/test_work/tree/"
path = "/Users/matt/Downloads/car_1130/"
path = "/Users/matt/Downloads/daba/"


system_type = os.name
print(system_type)

os.chdir(path)
print(os.getcwd())

files = os.listdir(path)

objNames = []
pngNames = []
mtlName =''
for str in files:
    print(str)
    if str.endswith(".obj"):
        objNames.append(str)

    elif str.endswith(".png"):
        pngNames.append(str)

    elif str.endswith(".mtl"):
        mtlName = str


print("Start to load obj model ...")


vertexScaleFactor = 163840

print('(1 << 9) * 320',vertexScaleFactor)
normalScaleFactor = 65536.0
texcoordScaleFactor = 65536.0
materialScaleFactor = 65536.0

modelID = 666
modelType = 1
lat = 419033370
lon = 143672331
confType = 111
modelName = "123"
if len(objNames)>len(pngNames):
    modelType = 3
elif len(objNames)<len(pngNames):
    modelType = 2

# 输出文件名称
outfileName = path+objNames[0].replace(".obj","")+".nt3d"
f = open(outfileName, 'wb')
# 模型id，
idBt = struct.pack("h", modelID)
print('idBt',len(idBt))
f.write(idBt)
# 模型类型
f.write(struct.pack("i", modelType))
# 经度，纬度，
f.write(struct.pack("i", lon))
f.write(struct.pack("i", lat))
# 配置类型
f.write(struct.pack("h", confType))
# 写入模型名称
nameBitArray = str2bitarray(modelName)
# 模型名称长度
nameSize = 0
f.write(struct.pack("B", nameSize))
# for i in nameBitArray:
#     f.write(struct.pack('<B', i))
# 写入obj数量
f.write(struct.pack("i", len(objNames)))

# 得到mtl使用信息
usemtl =''
# 依次写入每个obj文件信息
for name in objNames:
    # 读取obj文件信息
    obj = OBJ(path, name, True)
    obj.create_bbox()
    meshCount = len(obj.meshs)

    # print(obj.bbox_half_r)
    info = "{}-{}-{}-{}-{}-{}".format(name, meshCount*3,len(obj.vertices),len(obj.normals),len(obj.texcoords),len(obj.faces))
    print(info)
    # 写入顶点数量
    fCount = 0
    if len(obj.vertices)>0:
        fCount = meshCount*3

    f.write(struct.pack("i", fCount))
    # 写入法线数量
    nCount = 0
    if len(obj.normals) > 0:
        nCount = meshCount*3
    f.write(struct.pack("i", nCount))
    # 写入uv数量
    uvCount = 0
    if len(obj.texcoords) > 0:
        uvCount = meshCount*3
    f.write(struct.pack("i", uvCount))

    # 写入顶点数据
    ffnum = 0
    nSortRule = [0,2,1]
    for loop in range(meshCount):
        verts = obj.meshs[loop][0]
        if ffnum < 4 or ffnum > fCount*3-4:
            print(verts)
        for i in range(3):
            fps = obj.vertices[verts[i]]

            if ffnum < 4 or ffnum>fCount*3-4:
                print(fps)

            for j in nSortRule:
                ffnum+=1
                s = struct.pack("i", int(fps[j]*vertexScaleFactor))
                f.write(s)

                if ffnum <4 or ffnum>fCount*3-4:
                    print(int(fps[j] * vertexScaleFactor))
                    print(ffnum,s)
    print('顶点计数',ffnum)
    # 写入法线数据
    nnNum = 0

    print("面数", meshCount)
    for loop in range(meshCount):

        norms = obj.meshs[loop][1]
        for i in range(3):
            if nnNum < 4 or nnNum >= nCount*3-4:
                print("法向量",obj.normals[norms[i]])
            for j in nSortRule:

                s = struct.pack("i", int((obj.normals[norms[i]][j]) * normalScaleFactor))
                f.write(s)

                nnNum += 1
                if nnNum <4 or nnNum>nCount*3-4:
                    print(nnNum,s)
    print('法线计数', nnNum)
    # 写入uv数据
    uvNum = 0
    for loop in range(meshCount):
        uvs = obj.meshs[loop][2]
        for i in range(3):
            if uvNum < 3 or uvNum >= uvCount*2-3:
                print(obj.texcoords[uvs[i]])
            for j in range(2):
                uvNum+=1
                s = struct.pack("i", int((obj.texcoords[uvs[i]][j]) * texcoordScaleFactor))
                f.write(s)
                if uvNum <3 or uvNum>=uvCount*2-3:
                    print(uvNum,s)

    print('uv计数', uvNum)
    #读取usemtl信息
    usemtl = obj.faces[0][3]
    print(usemtl)

# 写入图片数量
f.write(struct.pack("i", len(pngNames)))

mtl = MTL(path,mtlName)

# 依次写入图片数据
for pngName in pngNames:
    # 读取图片的大小
    img_path = path+pngName
    img_cv = cv2.imread(img_path)
    # 写入图片宽
    f.write(struct.pack("i", img_cv.shape[1]))
    # 写入图片高
    f.write(struct.pack("i", img_cv.shape[0]))
    # 写入颜色类型
    f.write(struct.pack("i", 0))

    info = os.stat(img_path)
    # 写入图片大小
    f.write(struct.pack("i", info.st_size))

    # 写入图片数据
    imgFile = open(img_path,'rb')
    datas = imgFile.read()
    f.write(datas)
    imgFile.close()
    # 图片光照信息s
    for i in range(len(mtl.mtlnames)):
        name = mtl.mtlnames[i]
        if name == usemtl:
            if len(mtl.kas) > 0:
                for j in range(3):
                    f.write(struct.pack("i", int(float(mtl.kas[i][j])* materialScaleFactor)))
            else:
                for j in range(3):
                    f.write(struct.pack("i", int(1.0* materialScaleFactor)))


            if len(mtl.kds) > 0:
                for j in range(3):
                    f.write(struct.pack("i", int(float(mtl.kds[i][j])* materialScaleFactor)))
            else:
                for j in range(3):
                    f.write(struct.pack("i", int(1.0* materialScaleFactor)))


            if len(mtl.kes)>0:
                for j in range(3):
                    f.write(struct.pack("i", int(float(mtl.kes[i][j])* materialScaleFactor)))
            else:
                for j in range(3):
                    f.write(struct.pack("i", int(1.0* materialScaleFactor)))


            f.write(struct.pack("i", int(mtl.shininess[i] * materialScaleFactor)))
            f.write(struct.pack("i", int(mtl.dissolves[i] * materialScaleFactor)))
            f.write(struct.pack("i", int(float(mtl.illums[i]) * materialScaleFactor)))
            break


f.close()

# print(len(obj.vertices))
# print(len(obj.faces))
# print(len(obj.normals))
# print(len(obj.texcoords))


print('finsh-----')
