import os
from os import path
import shutil
if path.exists("../config/test.txt"):
  src = path.realpath("../config/test.txt")

  dst = path.realpath("../src/assets/test.txt")

  shutil.copy(src,dst)

