# This is the main.py script. It's the only script that you can run on this REPL platform via the run button above. This script takes care of displaying the output of stock price feed script you need to change in the `jpm_module_1` folder. 

# YOU SHOULD NOT CHANGE ANYTHING HERE AS IT ONLY RUNS THE STOCK PRICE FEED SCRIPT AND SHOWS THE OUTPUT

import os
import subprocess
import time
import signal

os.chdir(os.getcwd()+'/jpm_module_1')

process = subprocess.Popen(['python', 'server.py'], cwd=os.getcwd(), preexec_fn=os.setsid)

time.sleep(.300)

process2 = subprocess.Popen(['python', 'client.py'], cwd=os.getcwd(), preexec_fn=os.setsid)
process2.wait()
os.killpg(os.getpgid(process.pid), signal.SIGTERM)


print("UNIT TEST RESULTS BELOW...")
process2 = subprocess.Popen(['python', #'client_test.py'], cwd=os.getcwd(), #preexec_fn=os.setsid)
process2.wait()
