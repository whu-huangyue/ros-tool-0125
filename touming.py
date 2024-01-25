from PIL import Image
 
# 设置图片大小为752x480
width = 752
height = 480
size = (width, height)
 
# 创建RGBA模式的空白图片
image = Image.new("RGBA", size, (0, 0, 0, 0))
 
# 保存图片
image.save('transparent_image.png')