#!/usr/bin/python

import sys, os

if len(sys.argv) != 2:
    print("Usage: swap_cf.py CONFIGNAME")
    exit(0)

current_dir = os.path.dirname(os.path.realpath(__file__))
template_file_names = ["Configuration%s.h", "Configuration_adv%s.h"]
marlin_config_paths = [os.path.join(current_dir, "Marlin/" + f % '') for f in template_file_names]
config_paths = [os.path.join(current_dir, f % ("_" + sys.argv[1])) for f in template_file_names]

if not os.path.isfile(config_paths[1]):
    print("%s not found, using base." % config_paths[1])
    config_paths[1] = os.path.join(current_dir,"Configuration_adv_base.h")

for i in range(0, 2):
    if os.path.exists(config_paths[i]):
        print("Switching to config file: %s." % config_paths[i])
        try:
            os.remove(marlin_config_paths[i])
        except OSError:
            pass
        os.symlink(config_paths[i], marlin_config_paths[i])
    else:
        print("Could not find configuration file: [%s]." % config_paths[i])
