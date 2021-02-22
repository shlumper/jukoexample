import os
import json

os.makedirs("/root/results", exist_ok=True)

with open('/root/results/installer.bin', 'wb') as fout:
    fout.write(os.urandom(1024))
with open('/root/results/bolier.bin', 'wb') as fout:
    fout.write(os.urandom(1024))



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
    