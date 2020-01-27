# 一个完整的切片表达式包含两个“:”，用于分隔三个参数(start_index、end_index、step)。当只有一个“:”时，默认第三个参数step=1；当一个“:”也没有时，start_index=end_index，表示切取start_index指定的那个元素。
'''
step：正负数均可，其绝对值大小决定了切取数据时的‘‘步长”，而正负号决定了“切取方向”，正表示“从左往右”取值，负表示“从右往左”取值。当step省略时，默认为1，即从左往右以步长1取值。“切取方向非常重要！”“切取方向非常重要！”“切取方向非常重要！”，重要的事情说三遍！

start_index：表示起始索引（包含该索引对应值）；该参数省略时，表示从对象“端点”开始取值，至于是从“起点”还是从“终点”开始，则由step参数的正负决定，step为正从“起点”开始，为负从“终点”开始。

end_index：表示终止索引（不包含该索引对应值）；该参数省略时，表示一直取到数据“端点”，至于是到“起点”还是到“终点”，同样由step参数的正负决定，step为正时直到“终点”，为负时直到“起点”
'''

# str = 'abcdefgc'
#
# print(str.replace('c', 'tt'))
#
# print(str)

# arr = [1, 1, 4, 2, 1, 3]
# for i in range(len(arr)):
#     for j in range(len(arr) - i -1):
#         print(j)
#         if arr[j] > arr[j + 1]:
#             temp = arr[j]
#             arr[j] = arr[j + 1]
#             arr[j + 1] = temp
#
# print(arr)

arr = 'abcd'
print(arr[3:4])