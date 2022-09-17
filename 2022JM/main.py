import subprocess
try:
    subprocess.check_output(['wolframscript','-file','D:/study/USTC/2022JM/1_p_gamma.wls'])
except subprocess.CalledProcessError:
    pass