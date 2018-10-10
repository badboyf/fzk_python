# -*- coding: utf-8 -*-
'''
Created on 2018年10月10日

@author: Administrator
'''

config = {
    "dev" : {
            "mongo" :{
                    "host" : "local.vm.sss.com",
                    "port" : 27017,
                    "db"   : "fwgame"
                }
        }
    }


def get_config():
    return config["dev"]