# 1. 打开文件
file_read = open("README")
file_write = open("README[复件]", "w")
# 2.读写
text = file_read.read()
file_write.write(text)

# 3. 关闭文件
file_read.close()
file_write.close()