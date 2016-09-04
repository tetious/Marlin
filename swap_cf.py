#!/usr/bin/python

import sys, os

if len(sys.argv) != 2:
    print("Usage: swap_cf.py CONFIGNAME")
    exit(0)

config_file_name = "Configuration_%s.h" % sys.argv[1]
current_dir = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.join(current_dir, config_file_name)
marlin_config_path = os.path.join(current_dir, "Marlin/Configuration.h")

if os.path.exists(config_file_path):
    print("Switching to config file: %s." % config_file_name)
    os.remove(marlin_config_path)
    os.link(config_file_path, marlin_config_path)
else:
    print("Could not find configuration file: [%s]." % config_file_path)
