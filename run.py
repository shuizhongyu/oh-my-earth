#!/usr/bin/env python

#-*- coding: utf-8 -*-
'''
Created on Jun 03, 2017

@author ujnzxw <ujnzxw@gmail.com>
'''

import random
from   manage_earth    import EarthManager
from   manage_momentum import MomentumdashManager
from   manage_infinity import InfinityManager
from   config          import display_model


def main():

    obj_list = [ EarthManager, MomentumdashManager ,InfinityManager]

    if display_model == "random":
        index = random.randint(0, len(obj_list)-1)
        obj_list[index]().run()

    elif display_model == "earth":
        EarthManager().run()

    elif display_model == "momentumdash":
        MomentumdashManager().run()

    elif display_model == "infinity":
        InfinityManager().run()

    else:
        EarthManager().run()

if __name__ == "__main__":
    main()
