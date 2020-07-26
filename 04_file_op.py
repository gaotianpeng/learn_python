'''
01 文件操作
'''
print('文件操作------------------------')
print('文件写操作')
file_1 = open('name.txt', 'w')
file_1.write('诸葛亮')
file_1.close()

print('文件读操作')
file_2 = open('name.txt', 'r')
print(file_2.read())
file_2.close()

print('文件尾写入')
file_3 = open('name.txt', 'a')
file_3.write('刘备')
file_3.close()

print('文件读取行')
file_4 = open('name1.txt')
print(file_4.readline())
file_4.close()

print('文件读取所有行')
file_5 = open('name1.txt')
for line in file_5.readlines():
    print(line)
    print('----------------')
file_5.close()

print('文件seek操作')
file_6 = open('name1.txt')
print('文件指针当前位置%s' %file_6.tell())
file_6.read(1)
print('文件指针当前位置%s' %file_6.tell())

file_6.seek(0)
print('文件指针当前位置%s' %file_6.tell())

### 第一个参数:偏移位置
### 第二个参数:
###     0: 从文件开头偏移
###     1: 从当前位置偏移
###     2: 从文件结尾
file_6.seek(5, 0)
print('文件指针当前位置%s' %file_6.tell())
file_6.close()