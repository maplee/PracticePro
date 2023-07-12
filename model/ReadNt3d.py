import os
import sys
from objLoader import OBJ, MTL
import cv2
import struct
from bitarray import bitarray

vertexScaleFactor = (1 << 9) * 320
normalScaleFactor = 65536.0
texcoordScaleFactor = 65536.0
materialScaleFactor = 65536.0
nt3dName = "/Users/matt/Desktop/model/jiangshiche3/001.nt3d"
nt3dName = "/Users/matt/Downloads/hq/h9.nt3d"
nt3dName = "/Users/matt/StudioProjects/map_jni/app/src/main/res/raw/car.nt3d"
nt3dName = "/Users/matt/Desktop/model/others/pengyouhao.nt3d"
nt3dName = "/Users/matt/Desktop/model/others/aiqinghao.nt3d"
nt3dName = "/Users/matt/Desktop/model/m1.nt3d"

path = "/Users/matt/Desktop/model/m1/"

saveFlag = False


print('read-----')
info = os.stat(nt3dName)
fc = open(nt3dName, 'rb')
datas = fc.read(info.st_size)
fc.close()
# print(datas)
seekIndex=0
# 模型id，
idRb = struct.unpack("h",datas[seekIndex:seekIndex+2])
print('id:',idRb[0])
seekIndex+=2
# 模型类型，
typeRb = struct.unpack("i",datas[seekIndex:seekIndex+4])
print('type:',typeRb[0])
seekIndex+=4
# 经度，
lonRb = struct.unpack("i",datas[seekIndex:seekIndex+4])
print('lon:',lonRb[0])
seekIndex+=4
# 纬度，
latRb = struct.unpack("i",datas[seekIndex:seekIndex+4])
print('lat:',latRb[0])
seekIndex+=4
# 配置类型，
confTypeRb = struct.unpack("h",datas[seekIndex:seekIndex+2])
print('conf:',confTypeRb[0])
seekIndex+=2
# 模型名称长度，
nameSizeRb = struct.unpack("B",datas[seekIndex:seekIndex+1])
print('nameSize:',nameSizeRb[0])
seekIndex+=1
seekIndex+=nameSizeRb[0]*2

# obj数量，
obiSizeRb = struct.unpack("i",datas[seekIndex:seekIndex+4])
print('obj:',obiSizeRb[0])
seekIndex+=4

for i in range(obiSizeRb[0]):
    print('index',i)
    # 顶点数量，
    fCountRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    fCount = fCountRb[0]
    print('fCount:', fCount)
    seekIndex += 4
    # 法线数量，
    nCountRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('nCount:', nCountRb[0])
    seekIndex += 4
    # 纹理数量，
    uvCountRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('uvCount:', uvCountRb[0])
    seekIndex += 4

    # 顶点数据
    for loop in range(fCount):
        fRb = struct.unpack("iii", datas[seekIndex:seekIndex + 12])
        if loop == 0 or loop == fCount-1:
            print(datas[seekIndex:seekIndex + 12])
            print(loop,'f:', fRb[0]/vertexScaleFactor, fRb[1]/vertexScaleFactor, fRb[2]/vertexScaleFactor)
        seekIndex += 12
    # 法线数据
    for loop in range(nCountRb[0]):
        nRb = struct.unpack("iii", datas[seekIndex:seekIndex + 12])
        if loop == 0 or loop == fCount-1:
            print(datas[seekIndex:seekIndex + 12])
            print(loop,'n:', nRb[0]/normalScaleFactor, nRb[1]/normalScaleFactor, nRb[2]/normalScaleFactor)
        seekIndex += 12
    # 纹理数据
    for loop in range(uvCountRb[0]):
        uvRb = struct.unpack("ii", datas[seekIndex:seekIndex + 8])
        if loop == 0 or loop == fCount-1:
            print(datas[seekIndex:seekIndex + 8])
            print(loop,'uv:', uvRb[0]/texcoordScaleFactor, uvRb[1]/texcoordScaleFactor)
        seekIndex += 8


# png数量
pngSizeRb = struct.unpack("i",datas[seekIndex:seekIndex+4])
print('png:',pngSizeRb[0])
seekIndex+=4

for i in range(pngSizeRb[0]):
    # 图片长
    pngWidthRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('width:', pngWidthRb[0])
    seekIndex += 4
    # 图片高
    pngHeightRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('height:', pngHeightRb[0])
    seekIndex += 4
    # 图片颜色类型
    colorTypeRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('colorType:', colorTypeRb[0])
    seekIndex += 4
    # 图片大小
    pngSizeRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('pngSize:', pngSizeRb[0])
    seekIndex += 4
    # 图片数据
    pngDatas = datas[seekIndex:seekIndex + pngSizeRb[0]]
    if saveFlag:
        outFileName = path + str(i) +".png"
        pngSaveFile = open(outFileName, 'wb')
        pngSaveFile.write(pngDatas)
        pngSaveFile.close()
    print('pngDatas', len(pngDatas))
    seekIndex += pngSizeRb[0]

    # 纹理ka
    for ki in range(3):
        kaRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
        print('ka:', kaRb[0]/materialScaleFactor)
        seekIndex += 4
    # 纹理kd
    for ki in range(3):
        kdRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
        print('kd:', kdRb[0]/materialScaleFactor)
        seekIndex += 4
    # 纹理ks
    for ki in range(3):
        ksRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
        print('ks:', ksRb[0]/materialScaleFactor)
        seekIndex += 4
    # 纹理Ns
    nsRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('ns:', nsRb[0] / materialScaleFactor)
    seekIndex += 4
    # 纹理d
    dRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('d:', dRb[0] / materialScaleFactor)
    seekIndex += 4
    # 纹理illum
    illumRb = struct.unpack("i", datas[seekIndex:seekIndex + 4])
    print('illum:', illumRb[0] / materialScaleFactor)
    seekIndex += 4


# fr = open("/Users/matt/Desktop/model/one/one.nt3d", 'rb')
# print(fr.readline())
# fr.close()