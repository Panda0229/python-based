# - 定义函数时，可以给 某个参数指定一个默认值，具有默认值的参数就叫做缺省参数
# - 调用函数时，如果没有传入缺省参数的值，则在函数内部使用定义函数时指定的参数默认值
# - 函数的缺省参数，将常见的值设置为参数的缺省值，从而简化函数的调用


gl_list = [6,5,4]

# sort默认按照升序排序 - 这种情况多
# gl_list.sort()

# 如果需要降序排序，需要执行reverse参数，其中reverse就相当于缺省参数
gl_list.sort(reverse=True)

print(gl_list)

