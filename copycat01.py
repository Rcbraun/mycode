#!/usr/bin/python3

#imports the additional code
import shutil
import os

def main():
  #changes current directory   
  os.chdir("/home/student/mycode/")

  #copies file A to file B
  shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

  #copies directory and contents
  shutil.copytree("5g_research/", "5g_research_backup/")

main()
  
