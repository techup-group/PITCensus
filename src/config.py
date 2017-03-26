#!/usr/bin/env python
# Small module to read from a configuration .ini file
import os
import ConfigParser
from collections import namedtuple

#What is the filename of the config file?
config_file_location = os.path.join(os.path.dirname(__file__), '..', 'pitconfig.ini')

def readConfigFileToDict(filename):
    parser = ConfigParser.ConfigParser(allow_no_value=True)
    successFilenames = parser.read(filename)
    if len(successFilenames) is 0:
        raise Exception("Cannot read main config file " + config_file_location)
    dict = { }
    for section in parser.sections():
        dict[section] = { }
        for option in parser.options(section):
            dict[section][option] = parser.get(section, option)
    return dict    
 
PitConfig = readConfigFileToDict(config_file_location)
