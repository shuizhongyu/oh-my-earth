#!/usr/bin/env python

#-*- coding: utf-8 -*-
'''
Created on Jun 04, 2017

@author ljx <jiaxinustc#gmail.com>
'''

import urllib,re,sys,os,random,json
from   config    import infinity_output_file
from   utils     import set_background, get_desktop_environment

class InfinityManager():
    '''
    Lifeofpix.com background image manager
    '''

    def __init__(self):
        pass

    def get_bg_picture(self,index):
        '''
        get background picture from https://Lifeofpix.com
        '''

        #ljx
        filename = "/home/ljx/Pictures/infinity/"+str(index)+".jpg"
        #imgurl = "https://infinitypro-img.infinitynewtab.com/findaphoto/bigLink/"+str(index)+".jpg?imageView2/2/w/1920/format/jpg/interlace/1"
        imgurl = "https://infinitypro-img.infinitynewtab.com/findaphoto/bigLink/"+str(index)+".jpg"
        #xjl


        urllib.urlretrieve(imgurl,filename)

    def run(self):
        ''' main function '''

        ''' get background picture from momentumdash.com '''

        print("Updating  infinity new tab image...")

        success = 0
        #ljx
        while success == 0:
            print("test!!!")
            index = random.randint(1000,20000)
            filename = "/home/ljx/Pictures/infinity/"+str(index)+".jpg"
            self.get_bg_picture(index)
            r = os.system("cat "+filename+" |grep error")
            if r!=0:
                success=1
                break
            os.system("rm "+filename)

        #xjl


        print("\nSaving to '%s'..." % (filename))

        ''' set background picture as wallpaper '''
        ''' scaled, wallpaper, stretched, spanned '''
        if not set_background(filename, "stretched"):
            exit("Your desktop environment '{}' is not supported.".format(get_desktop_environment()))

        print("Done!")

if __name__ == "__main__":
    b = LifeofpixashManager()
    b.run()
