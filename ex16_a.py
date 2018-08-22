# coding=utf-8
ts = '>'
print "请输入要显示的文本",
filename = raw_input(ts )
fileread = open(filename).read()
print "以下内容为当前文本内容:"
print "%s" % fileread
#追加内容
# 查了资料，关于open()的mode参数：
# 'r'：读
# 'w'：写
# 'a'：追加
# 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
# 'w+' == w+r（可读可写，文件若不存在就创建）
# 'a+' ==a+r（可追加可写，文件若不存在就创建）
# 对应的，如果是二进制文件，就都加一个b就好啦：

print "输入要追加的内容:"
file_w = raw_input(ts )
file_a_open = open(filename,"a")
file_a_open.write(file_w)
file_a_open.close()

fileread = open(filename).read()
print "追加后最新内容:"
print "%s" % fileread
