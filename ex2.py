# coding=utf-8
def print_args(*args):
	var1,var2 = args
	print "参数1：%s----参数2:%s" % (var1,var2)

print_args(1,2)

def print_two(var1,var2):
	print "aaa%sbbbb%s" % (var1,var2)

print_two("fff","bbbb")