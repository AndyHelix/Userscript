#!/bin/bash

target=`pwd`

echo $target

echo 'export PATH=$PATH:'$target >> $HOME/.zshrc
