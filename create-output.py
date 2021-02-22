import os
import json
import time

print("running simluation 1 out of 10")
time.sleep(.4)
print("running simluation 2 out of 10")
time.sleep(1.4)
print("running simluation 3 out of 10")
time.sleep(1.4)
print("running simluation 4 out of 10")
time.sleep(1.4)
print("running simluation 5 out of 10")
time.sleep(1.4)
print("running simluation 6 out of 10")
time.sleep(1.4)
print("running simluation 7 out of 10")
time.sleep(1.4)
print("running simluation 8 out of 10")
time.sleep(1.4)
print("running simluation 9 out of 10")
time.sleep(1.4)
print("running simluation 10 out of 10")
time.sleep(1.4)

os.makedirs("/root/results", exist_ok=True)

print("creating bitstream.bin in results")
time.sleep(3)
with open('/root/results/bitstream.bin', 'wb') as fout:
    fout.write(os.urandom(1024))
print("creating debug.bin in results")
with open('/root/results/debug.bin', 'wb') as fout:
    fout.write(os.urandom(1024))


print("creating results data in /root")

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})



with open('/root/data.txt', 'w') as fout:
    fout.write(json.dumps(data,indent=4))
    
print("done")