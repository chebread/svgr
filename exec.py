import os
import sys

argv_1 = sys.argv[1]
argv_2 = sys.argv[2]
now_dir = os.getcwd()


os.system(f'npx @svgr/cli -- {now_dir}/{argv_1}.svg > {now_dir}/{argv_2}.jsx')
