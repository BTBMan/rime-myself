#!/usr/bin/env python
# coding=utf-8

# dotnet ./imewlconverter/ImeWlConverterCmd.dll -ct:pinyin -i:scel ./ext-dict/搜狗标准词库.scel -o:rime ./ext-dict/output/sougou.txt

from glob import glob
import os
import shutil

if not os.path.exists('./output/'):
    os.mkdir('output')

original_files = glob("*.scel")
print("---------------")
for of in original_files:
    if ' ' in of:
        new_fn = of.replace(' ', '_')
        print('rename "%s" to "%s"' % (of, new_fn))
        shutil.move(of, new_fn)
        of = new_fn
    print('>> ', of)
print("---------------")

original_files = glob("*.scel")
# print(original_files)

yaml_file = 'luna_pinyin.sogou.dict.yaml'

command='''imewlconverter -i:scel %s -o:rime "%s"''' % (str(original_files).strip('[]').replace(',', ''), yaml_file)
print(command)
os.system(command)

data = '''---
name: luna_pinyin.sogou
version: "1.0"
sort: by_weight
use_preset_vocabulary: true
# 此处为扩充词库（基本）默认链接载入的词库
import_tables:
    - luna_pinyin
    - luna_pinyin.sogou
...

# 自定义词语

'''
with open(yaml_file, "r+") as f:
     old = f.read()
     f.seek(0)
     f.write(data)
     f.write(old)

print("Now don't forget to copy the file to rime config folder (like ~/.config/fcitx/rime)")