import json
import matplotlib.pyplot as plt

NUMBER = 50

sum_8_257 = 0
sum_8_449 = 0
sum_8_801 = 0
sum_16_257 = 0
sum_16_449 = 0
sum_16_801 = 0

with open('posenet_8_257.json') as json_file:
    data = json.load(json_file)
    for x in data:
        sum_8_257 += x.get('time')

with open('posenet_8_449.json') as json_file:
    data = json.load(json_file)
    for x in data:
        sum_8_449 += x.get('time')

with open('posenet_8_801.json') as json_file:
    data = json.load(json_file)
    for x in data:
        sum_8_801 += x.get('time')

with open('posenet_16_257.json') as json_file:
    data = json.load(json_file)
    for x in data:
        sum_16_257 += x.get('time')

with open('posenet_16_449.json') as json_file:
    data = json.load(json_file)
    for x in data:
        sum_16_449 += x.get('time')

with open('posenet_16_801.json') as json_file:
    data = json.load(json_file)
    for x in data:
        sum_16_801 += x.get('time')

avg_8_257 = sum_8_257/NUMBER
avg_8_449 = sum_8_449/NUMBER
avg_8_801 = sum_8_801/NUMBER
avg_16_257 = sum_16_257/NUMBER
avg_16_449 = sum_16_449/NUMBER
avg_16_801 = sum_16_801/NUMBER

# make graph
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(20,10))
plt.ylim([1100, 1360])
plt.xticks([257, 449, 801])
# ouput stride 8 points
x8 = [257, 449, 801]
y8 = [avg_8_257, avg_8_449, avg_8_801]
# output stride 16 points
x16 = [257, 449, 801]
y16 = [avg_16_257, avg_16_449, avg_16_801]
# plotting the points  
plt.plot(x8, y8, 'o', color='red', label='8', markersize=3)
plt.plot(x16, y16, 'o', color='blue', label='16', markersize=3)

for i_x, i_y in zip(x8, y8):
    plt.text(i_x - 10, i_y - 6, '{}'.format(i_y))
for i_x, i_y in zip(x16, y16):
    plt.text(i_x + 5, i_y - 2, '{}'.format(i_y))

plt.xlabel('Input Resolution')
plt.ylabel('time (ms)')
plt.title('Time')
plt.legend(frameon=True)
plt.show()