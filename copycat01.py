#!/usr/bin/env python3
import shutil
import os

#Linux will CD to argument/source
os.chdir("/home/student/mycode/")

#Linux will copy file from source/$1 to destination/$2
##if destination exists, it will be overwriteen
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#recursively copy source/$1 to destination/$2
## destination must not exist
shutil.copytree("5g_research/", "5g_research_backup/")

