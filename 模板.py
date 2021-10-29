from PIL import Image
import os

#获取文件路径
file_root=os.path.dirname(os.path.realpath('模板.py'))
file_root=file_root.replace('\\','/')
print('文件夹路径是'+file_root)

#母图空白处的左上右下坐标位置（单位：像素）
position=[643,640,782,779]#按顺序为左上右下

#得到子图需要调整到的尺寸
icon_w=int(position[2])-int(position[0])
icon_h=int(position[3])-int(position[1])
#得到子图需要贴到母图的位置：左上坐标
w=int(position[0])
h=int(position[1])

#读取母图
for r, d, f in os.walk(f"{file_root}/mutu"):
    for s in f:
        mutu = Image.open(f'{r}/{s}')
        # 读取子图
        for r1, d1, f1 in os.walk(f"{file_root}/zitu"):
            #子图有多张，按照子图的名称p到母图上
            for s1 in f1:
                zitu = Image.open(f'{r1}/{s1}')
                if len(f1)>1:
                    if s[:s.rfind('.')]==s1[:s1.rfind('.')]:
                        mutu_w, mutu_h = mutu.size#获取母图尺寸
                        zitu_w,zitu_h=zitu.size
                        #重置子图大小
                        zitu = zitu.resize((icon_w, icon_h), Image.ANTIALIAS)
                        # 子图贴到母图的指定位置
                        mutu.paste(zitu, (w, h), mask=None)
                        mutu.save(f"{file_root}/result/{s}")
                    else :
                        continue
                #子图有1张，不管名称，直接p到全部母图上
                elif len(f1)==1:
                    mutu_w, mutu_h = mutu.size  # 获取母图尺寸
                    zitu_w, zitu_h = zitu.size
                    # 重置子图大小
                    zitu = zitu.resize((icon_w, icon_h), Image.ANTIALIAS)
                    # 子图贴到母图的指定位置
                    mutu.paste(zitu, (w, h), mask=None)
                    mutu.save(f"{file_root}/result/{s}")

