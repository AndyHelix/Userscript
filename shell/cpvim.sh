#!/bin/bash

#read 接受键盘输入

# read filepath

#判断命令行参数的个数，如果不够，则提示共有几个参数，每个参数大概是做什么的
#if [ $# -lt 5 ]; then
#    echo $0 '<database name> <username> <password> <host name(or IP)> <table name>'
#    echo Host name can be 'localhost' when connects to local maxdb.
#    exit
#fi

filepath=$1

# 将第一个参数给 filepath

#filepath='/disk/emacs.txt'

FILE_NAME=$filepath
#
#echo ${FILE_NAME##*/}
#echo ${FILE_NAME}
#echo ${FILE_NAME%/*}                 # 相当与dirname， 即删除按从右至左方向开始，匹配到第一个/之间的子串
#echo ${FILE_NAME#*/}                 # 从左至右， 删除第一个/及左边的子串
#echo ${FILE_NAME%%/*}                # 从右至左， 删除至最后一个/及右边的子串

vim $1
cd ${FILE_NAME%/*}


#echo ${FILE_NAME##*/}
