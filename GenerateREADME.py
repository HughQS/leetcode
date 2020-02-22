# -*- coding: utf-8 -*-
"""
Created on 2019-09-12
@author: hugh
"""
import os
from urllib import parse


def rewrite_readme(readme_name, head, content):
    with open(readme_name, 'w', encoding='utf-8') as f:
        f.writelines(head)
        f.writelines(content)


def generate_readme_head_lines():
    """
    生成Readme头部
    """
    head_lines = ""
    head_lines += "# Leetcode \n"
    head_lines += "Leetcode solution <br/> \n\n\n"
    return head_lines


def generate_readme_content_lines(src_dir):
    """
    生成Readme内容
    """
    dict = {}
    content_lines = ""
    key_set_haved = read_old_readme_content_key(os.path.join(src_dir, 'README.md'))
    size_key_set_haved = len(key_set_haved)
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for file_name in files:
            if file_name.endswith('.md') and root != "./":
                key = int(file_name.split('.')[0])  # 提取文件名前的数字作为键
                value = [file_name, root, '']  # 文件名与根目录组合成list作为字典的值
                if size_key_set_haved and (key not in key_set_haved):
                    value = [file_name, root, '   [<span style="color:red">new !!!</span>]']
                dict.setdefault(key, value)
    # 对字典按键进行升序排序
    tup = sorted(dict.items(), key = lambda d : d[0])
    for i in range(len(tup)):
        content_lines += "[" + tup[i][1][0] + "](" + tup[i][1][1] + "/" + parse.quote(tup[i][1][0]) + \
                         ")   [" + tup[i][1][1][2:] + "]" + tup[i][1][2] + "<br/> \n"
    return content_lines


def read_old_readme_content_key(file_name):
    """
    读取旧的Readme,返回键集合
    :param file_name: 旧的Readme路径
    :return  返回内容的键的集合set，即题目名称前的数字集合
    """
    res = set()
    if os.path.exists(file_name):
        with open(file_name, 'r') as fr:
            while 1:
                line = fr.readline()
                if line:
                    line = line.strip().split()
                    if len(line) and len(line[0]) > 1 and line[0][1:-1].isdigit():
                        res.add(int(line[0][1:-1]))
                else:
                    break
    return res


if __name__ == '__main__':
    head_lines = generate_readme_head_lines()
    content_lines = generate_readme_content_lines("./")
    rewrite_readme("README.md", head_lines, content_lines)

