import os
libs = {"numpy","matplotlib","pillow","sklearn"}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Succesful")
except:
    print("Errors")