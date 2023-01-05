#!/usr/bin/python3
# simple script to move and rename files

#imports more functions
import shutil
import os
def main():
  #changes to the mycode directory
  os.chdir ('/home/student/mycode/')

  #moves file raynor.obj to ceph_storage
  shutil.move ('raynor.obj', 'ceph_storage/')

  #allows you to input a new name for kerrigan.obj
  xname = input('What is the new name for kerrigan.obj? ')

  #changes the file name of kerrigan.obj
  shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


main()
