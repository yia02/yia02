import sys
from simhash import Simhash as hs
import re

# 清除Html
def remove(file):
    result = re.compile(r'<[^>]+>', re.S).sub('', file).strip()
    return result


# 读取文件
def readfile(file):
    with open(file, 'r', encoding='UTF-8') as co:
        result = remove(co.read())
    return result


# 相似度比较
def analyse(ori, ori_add):
    ori_hs = hs(ori)
    ori_add_hs = hs(ori_add)
    max_hs = max(len(bin(ori_hs.value)), len(bin(ori_add_hs.value)))
    dst = ori_hs.distance(ori_add_hs)  # 汉明距离
    result = 1 - dst / max_hs
    return result


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('传入参数个数错误！')
        exit()

    ori_file = sys.argv[1]
    ori_add_file = sys.argv[2]
    ans_file = sys.argv[3]

    analyse_result = analyse(readfile(ori_file), readfile(ori_add_file))

    f = open(ans_file, 'w', encoding="utf-8")
    f.write("文章相似度： %.2f" % analyse_result)
    f.close()
