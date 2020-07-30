import json
import matplotlib.pyplot as plt

NUMBER = 25

sum_8_257 = 0
sum_8_257_nose_x = 0
sum_8_257_nose_y = 0
sum_8_257_nose = 0
sum_8_257_l_eye_x = 0
sum_8_257_l_eye_y = 0
sum_8_257_l_eye = 0
sum_8_257_r_eye_x = 0
sum_8_257_r_eye_y = 0
sum_8_257_r_eye = 0
sum_8_257_l_ear_x = 0
sum_8_257_l_ear_y = 0
sum_8_257_l_ear = 0
sum_8_257_r_ear_x = 0
sum_8_257_r_ear_y = 0
sum_8_257_r_ear = 0
sum_8_257_l_shoulder_x = 0
sum_8_257_l_shoulder_y = 0
sum_8_257_l_shoulder = 0
sum_8_257_r_shoulder_x = 0
sum_8_257_r_shoulder_y = 0
sum_8_257_r_shoulder = 0

# sum_8_449 = 0
# sum_8_449_nose_x = 0
# sum_8_449_nose_y = 0
# sum_8_449_nose = 0
# sum_8_449_l_eye_x = 0
# sum_8_449_l_eye_y = 0
# sum_8_449_l_eye = 0
# sum_8_449_r_eye_x = 0
# sum_8_449_r_eye_y = 0
# sum_8_449_r_eye = 0
# sum_8_449_l_ear_x = 0
# sum_8_449_l_ear_y = 0
# sum_8_449_l_ear = 0
# sum_8_449_r_ear_x = 0
# sum_8_449_r_ear_y = 0
# sum_8_449_r_ear = 0
# sum_8_449_l_shoulder_x = 0
# sum_8_449_l_shoulder_y = 0
# sum_8_449_l_shoulder = 0
# sum_8_449_r_shoulder_x = 0
# sum_8_449_r_shoulder_y = 0
# sum_8_449_r_shoulder = 0

sum_8_801 = 0
sum_8_801_nose_x = 0
sum_8_801_nose_y = 0
sum_8_801_nose = 0
sum_8_801_l_eye_x = 0
sum_8_801_l_eye_y = 0
sum_8_801_l_eye = 0
sum_8_801_r_eye_x = 0
sum_8_801_r_eye_y = 0
sum_8_801_r_eye = 0
sum_8_801_l_ear_x = 0
sum_8_801_l_ear_y = 0
sum_8_801_l_ear = 0
sum_8_801_r_ear_x = 0
sum_8_801_r_ear_y = 0
sum_8_801_r_ear = 0
sum_8_801_l_shoulder_x = 0
sum_8_801_l_shoulder_y = 0
sum_8_801_l_shoulder = 0
sum_8_801_r_shoulder_x = 0
sum_8_801_r_shoulder_y = 0
sum_8_801_r_shoulder = 0

sum_16_257 = 0
sum_16_257_nose_x = 0
sum_16_257_nose_y = 0
sum_16_257_nose = 0
sum_16_257_l_eye_x = 0
sum_16_257_l_eye_y = 0
sum_16_257_l_eye = 0
sum_16_257_r_eye_x = 0
sum_16_257_r_eye_y = 0
sum_16_257_r_eye = 0
sum_16_257_l_ear_x = 0
sum_16_257_l_ear_y = 0
sum_16_257_l_ear = 0
sum_16_257_r_ear_x = 0
sum_16_257_r_ear_y = 0
sum_16_257_r_ear = 0
sum_16_257_l_shoulder_x = 0
sum_16_257_l_shoulder_y = 0
sum_16_257_l_shoulder = 0
sum_16_257_r_shoulder_x = 0
sum_16_257_r_shoulder_y = 0
sum_16_257_r_shoulder = 0

# sum_16_449 = 0
# sum_16_449_nose_x = 0
# sum_16_449_nose_y = 0
# sum_16_449_nose = 0
# sum_16_449_l_eye_x = 0
# sum_16_449_l_eye_y = 0
# sum_16_449_l_eye = 0
# sum_16_449_r_eye_x = 0
# sum_16_449_r_eye_y = 0
# sum_16_449_r_eye = 0
# sum_16_449_l_ear_x = 0
# sum_16_449_l_ear_y = 0
# sum_16_449_l_ear = 0
# sum_16_449_r_ear_x = 0
# sum_16_449_r_ear_y = 0
# sum_16_449_r_ear = 0
# sum_16_449_l_shoulder_x = 0
# sum_16_449_l_shoulder_y = 0
# sum_16_449_l_shoulder = 0
# sum_16_449_r_shoulder_x = 0
# sum_16_449_r_shoulder_y = 0
# sum_16_449_r_shoulder = 0


sum_16_801 = 0
sum_16_801_nose_x = 0
sum_16_801_nose_y = 0
sum_16_801_nose = 0
sum_16_801_l_eye_x = 0
sum_16_801_l_eye_y = 0
sum_16_801_l_eye = 0
sum_16_801_r_eye_x = 0
sum_16_801_r_eye_y = 0
sum_16_801_r_eye = 0
sum_16_801_l_ear_x = 0
sum_16_801_l_ear_y = 0
sum_16_801_l_ear = 0
sum_16_801_r_ear_x = 0
sum_16_801_r_ear_y = 0
sum_16_801_r_ear = 0
sum_16_801_l_shoulder_x = 0
sum_16_801_l_shoulder_y = 0
sum_16_801_l_shoulder = 0
sum_16_801_r_shoulder_x = 0
sum_16_801_r_shoulder_y = 0
sum_16_801_r_shoulder = 0

gt_data = []
files = ['posenet_8_257.json', 'posenet_8_801.json', 'posenet_16_257.json', 'posenet_16_801.json']

with open('data_gt.json') as json_file:
    data1 = json.load(json_file)
    data = data1[:NUMBER]
    for x in data:
        gt_data.append(x)

for x in range(len(gt_data)):
    nose_x_gt = gt_data[x].get('nose_x')
    nose_y_gt = gt_data[x].get('nose_y')
    l_eye_x_gt = gt_data[x].get('l_eye_x')
    l_eye_y_gt = gt_data[x].get('l_eye_y')
    r_eye_x_gt = gt_data[x].get('r_eye_x')
    r_eye_y_gt = gt_data[x].get('r_eye_y')
    l_ear_x_gt = gt_data[x].get('l_ear_x')
    l_ear_y_gt = gt_data[x].get('l_ear_y')
    r_ear_x_gt = gt_data[x].get('r_ear_x')
    r_ear_y_gt = gt_data[x].get('r_ear_y')
    l_shoulder_x_gt = gt_data[x].get('l_shoulder_x')
    l_shoulder_y_gt = gt_data[x].get('l_shoulder_y')
    r_shoulder_x_gt = gt_data[x].get('r_shoulder_x')
    r_shoulder_y_gt = gt_data[x].get('r_shoulder_y')

    for a in files:
        with open(a) as json_file1:
            data1 = json.load(json_file1)

            nose_x = data1[x].get('nose_x')
            nose_y = data1[x].get('nose_y')
            l_eye_x = data1[x].get('l_eye_x')
            l_eye_y = data1[x].get('l_eye_y')
            r_eye_x = data1[x].get('r_eye_x')
            r_eye_y = data1[x].get('r_eye_y')
            l_ear_x = data1[x].get('l_ear_x')
            l_ear_y = data1[x].get('l_ear_y')
            r_ear_x = data1[x].get('r_ear_x')
            r_ear_y = data1[x].get('r_ear_y')
            l_shoulder_x = data1[x].get('l_shoulder_x')
            l_shoulder_y = data1[x].get('l_shoulder_y')
            r_shoulder_x = data1[x].get('r_shoulder_x')
            r_shoulder_y = data1[x].get('r_shoulder_y')

            nose_x_acc = abs(nose_x_gt - nose_x)
            nose_y_acc = abs(nose_y_gt - nose_y)
            l_eye_x_acc = abs(l_eye_x_gt - l_eye_x)
            l_eye_y_acc = abs(l_eye_y_gt - l_eye_y)
            r_eye_x_acc = abs(r_eye_x_gt - r_eye_x)
            r_eye_y_acc = abs(r_eye_y_gt - r_eye_x)
            l_ear_x_acc = abs(l_ear_x_gt - l_ear_x)
            l_ear_y_acc = abs(l_ear_y_gt - l_ear_y)
            r_ear_x_acc = abs(r_ear_x_gt - r_ear_x)
            r_ear_y_acc = abs(r_ear_y_gt - r_ear_y)
            l_shoulder_x_acc = abs(l_shoulder_x_gt - l_shoulder_x)
            l_shoulder_y_acc = abs(l_shoulder_y_gt - l_shoulder_y)
            r_shoulder_x_acc = abs(r_shoulder_x_gt - r_shoulder_x)
            r_shoulder_y_acc = abs(r_shoulder_y_gt - r_shoulder_y)

            if a == 'posenet_8_257.json':
                sum_8_257_nose_x += nose_x_acc
                sum_8_257_nose_y += nose_y_acc
                sum_8_257_l_eye_x += l_eye_x_acc
                sum_8_257_l_eye_y += l_eye_y_acc
                sum_8_257_r_eye_x += r_eye_x_acc
                sum_8_257_r_eye_y += r_eye_y_acc
                sum_8_257_l_ear_x += l_ear_x_acc
                sum_8_257_l_ear_y += l_ear_y_acc
                sum_8_257_r_ear_x += r_ear_x_acc
                sum_8_257_r_ear_y += r_ear_y_acc
                sum_8_257_l_shoulder_x += l_shoulder_x_acc
                sum_8_257_l_shoulder_y += l_shoulder_y_acc
                sum_8_257_r_shoulder_x += r_shoulder_x_acc
                sum_8_257_r_shoulder_y += r_shoulder_y_acc
            # if a == 'posenet_8_449.json':
            #     sum_8_449_nose_x += nose_x_acc
            #     sum_8_449_nose_y += nose_y_acc
            #     sum_8_449_l_eye_x += l_eye_x_acc
            #     sum_8_449_l_eye_y += l_eye_y_acc
            #     sum_8_449_r_eye_x += r_eye_x_acc
            #     sum_8_449_r_eye_y += r_eye_y_acc
            #     sum_8_449_l_ear_x += l_ear_x_acc
            #     sum_8_449_l_ear_y += l_ear_y_acc
            #     sum_8_449_r_ear_x += r_ear_x_acc
            #     sum_8_449_r_ear_y += r_ear_y_acc
            #     sum_8_449_l_shoulder_x += l_shoulder_x_acc
            #     sum_8_449_l_shoulder_y += l_shoulder_y_acc
            #     sum_8_449_r_shoulder_x += r_shoulder_x_acc
            #     sum_8_449_r_shoulder_y += r_shoulder_y_acc
            if a == 'posenet_8_801.json':
                sum_8_801_nose_x += nose_x_acc
                sum_8_801_nose_y += nose_y_acc
                sum_8_801_l_eye_x += l_eye_x_acc
                sum_8_801_l_eye_y += l_eye_y_acc
                sum_8_801_r_eye_x += r_eye_x_acc
                sum_8_801_r_eye_y += r_eye_y_acc
                sum_8_801_l_ear_x += l_ear_x_acc
                sum_8_801_l_ear_y += l_ear_y_acc
                sum_8_801_r_ear_x += r_ear_x_acc
                sum_8_801_r_ear_y += r_ear_y_acc
                sum_8_801_l_shoulder_x += l_shoulder_x_acc
                sum_8_801_l_shoulder_y += l_shoulder_y_acc
                sum_8_801_r_shoulder_x += r_shoulder_x_acc
                sum_8_801_r_shoulder_y += r_shoulder_y_acc
            if a == 'posenet_16_257.json':
                sum_16_257_nose_x += nose_x_acc
                sum_16_257_nose_y += nose_y_acc
                sum_16_257_l_eye_x += l_eye_x_acc
                sum_16_257_l_eye_y += l_eye_y_acc
                sum_16_257_r_eye_x += r_eye_x_acc
                sum_16_257_r_eye_y += r_eye_y_acc
                sum_16_257_l_ear_x += l_ear_x_acc
                sum_16_257_l_ear_y += l_ear_y_acc
                sum_16_257_r_ear_x += r_ear_x_acc
                sum_16_257_r_ear_y += r_ear_y_acc
                sum_16_257_l_shoulder_x += l_shoulder_x_acc
                sum_16_257_l_shoulder_y += l_shoulder_y_acc
                sum_16_257_r_shoulder_x += r_shoulder_x_acc
                sum_16_257_r_shoulder_y += r_shoulder_y_acc
            # if a == 'posenet_16_449.json':
            #     sum_16_449_nose_x += nose_x_acc
            #     sum_16_449_nose_y += nose_y_acc
            #     sum_16_449_l_eye_x += l_eye_x_acc
            #     sum_16_449_l_eye_y += l_eye_y_acc
            #     sum_16_449_r_eye_x += r_eye_x_acc
            #     sum_16_449_r_eye_y += r_eye_y_acc
            #     sum_16_449_l_ear_x += l_ear_x_acc
            #     sum_16_449_l_ear_y += l_ear_y_acc
            #     sum_16_449_r_ear_x += r_ear_x_acc
            #     sum_16_449_r_ear_y += r_ear_y_acc
            #     sum_16_449_l_shoulder_x += l_shoulder_x_acc
            #     sum_16_449_l_shoulder_y += l_shoulder_y_acc
            #     sum_16_449_r_shoulder_x += r_shoulder_x_acc
            #     sum_16_449_r_shoulder_y += r_shoulder_y_acc
            if a == 'posenet_16_801.json':
                sum_16_801_nose_x += nose_x_acc
                sum_16_801_nose_y += nose_y_acc
                sum_16_801_l_eye_x += l_eye_x_acc
                sum_16_801_l_eye_y += l_eye_y_acc
                sum_16_801_r_eye_x += r_eye_x_acc
                sum_16_801_r_eye_y += r_eye_y_acc
                sum_16_801_l_ear_x += l_ear_x_acc
                sum_16_801_l_ear_y += l_ear_y_acc
                sum_16_801_r_ear_x += r_ear_x_acc
                sum_16_801_r_ear_y += r_ear_y_acc
                sum_16_801_l_shoulder_x += l_shoulder_x_acc
                sum_16_801_l_shoulder_y += l_shoulder_y_acc
                sum_16_801_r_shoulder_x += r_shoulder_x_acc
                sum_16_801_r_shoulder_y += r_shoulder_y_acc

sum_8_257_nose = sum_8_257_nose_x + sum_8_257_nose_y
sum_8_257_l_eye = sum_8_257_l_eye_x + sum_8_257_l_eye_y
sum_8_257_r_eye = sum_8_257_r_eye_x + sum_8_257_r_eye_y
sum_8_257_l_ear = sum_8_257_l_ear_x + sum_8_257_l_ear_y
sum_8_257_r_ear = sum_8_257_r_ear_x + sum_8_257_r_ear_y
sum_8_257_l_shoulder = sum_8_257_l_shoulder_x + sum_8_257_l_shoulder_y
sum_8_257_r_shoulder = sum_8_257_l_shoulder_x + sum_8_257_l_shoulder_y
sum_8_257 = sum_8_257_nose + sum_8_257_l_eye + sum_8_257_r_eye + sum_8_257_l_ear + sum_8_257_r_ear + sum_8_257_l_shoulder + sum_8_257_r_shoulder

# sum_8_449_nose = sum_8_449_nose_x + sum_8_449_nose_y
# sum_8_449_l_eye = sum_8_449_l_eye_x + sum_8_449_l_eye_y
# sum_8_449_r_eye = sum_8_449_r_eye_x + sum_8_449_r_eye_y
# sum_8_449_l_ear = sum_8_449_l_ear_x + sum_8_449_l_ear_y
# sum_8_449_r_ear = sum_8_449_r_ear_x + sum_8_449_r_ear_y
# sum_8_449_l_shoulder = sum_8_449_l_shoulder_x + sum_8_449_l_shoulder_y
# sum_8_449_r_shoulder = sum_8_449_r_shoulder_x + sum_8_449_r_shoulder_y
# sum_8_449 = sum_8_449_nose + sum_8_449_l_eye + sum_8_449_r_eye + sum_8_449_l_ear + sum_8_449_r_ear + sum_8_449_l_shoulder + sum_8_449_r_shoulder

sum_8_801_nose = sum_8_801_nose_x + sum_8_801_nose_y
sum_8_801_l_eye = sum_8_801_l_eye_x + sum_8_801_l_eye_y
sum_8_801_r_eye = sum_8_801_r_eye_x + sum_8_801_r_eye_y
sum_8_801_l_ear = sum_8_801_l_ear_x + sum_8_801_l_ear_y
sum_8_801_r_ear = sum_8_801_r_ear_x + sum_8_801_r_ear_y
sum_8_801_l_shoulder = sum_8_801_l_shoulder_x + sum_8_801_l_shoulder_y
sum_8_801_r_shoulder = sum_8_801_r_shoulder_x + sum_8_801_r_shoulder_y
sum_8_801 = sum_8_801_nose + sum_8_801_l_eye + sum_8_801_r_eye + sum_8_801_l_ear + sum_8_801_r_ear + sum_8_801_l_shoulder + sum_8_801_r_shoulder

sum_16_257_nose = sum_16_257_nose_x + sum_16_257_nose_y
sum_16_257_l_eye = sum_16_257_l_eye_x + sum_16_257_l_eye_y
sum_16_257_r_eye = sum_16_257_r_eye_x + sum_16_257_r_eye_y
sum_16_257_l_ear = sum_16_257_l_ear_x + sum_16_257_l_ear_y
sum_16_257_r_ear = sum_16_257_r_ear_x + sum_16_257_r_ear_y
sum_16_257_l_shoulder = sum_16_257_l_shoulder_x + sum_16_257_l_shoulder_y
sum_16_257_r_shoulder = sum_16_257_r_shoulder_x + sum_16_257_r_shoulder_y
sum_16_257 = sum_16_257_nose + sum_16_257_l_eye + sum_16_257_r_eye + sum_16_257_l_ear + sum_16_257_r_ear + sum_16_257_l_shoulder + sum_16_257_r_shoulder

# sum_16_449_nose = sum_16_449_nose_x + sum_16_449_nose_y
# sum_16_449_l_eye = sum_16_449_l_eye_x + sum_16_449_l_eye_y
# sum_16_449_r_eye = sum_16_449_r_eye_x + sum_16_449_r_eye_y
# sum_16_449_l_ear = sum_16_449_l_ear_x + sum_16_449_l_ear_y
# sum_16_449_r_ear = sum_16_449_r_ear_x + sum_16_449_r_ear_y
# sum_16_449_l_shoulder = sum_16_449_l_shoulder_x + sum_16_449_l_shoulder_y
# sum_16_449_r_shoulder = sum_16_449_r_shoulder_x + sum_16_449_r_shoulder_y
# sum_16_449 = sum_16_449_nose + sum_16_449_l_eye + sum_16_449_r_eye + sum_16_449_l_ear + sum_16_449_r_ear + sum_16_449_l_shoulder + sum_16_449_r_shoulder

sum_16_801_nose = sum_16_801_nose_x + sum_16_801_nose_y 
sum_16_801_l_eye = sum_16_801_l_eye_x + sum_16_801_l_eye_y
sum_16_801_r_eye = sum_16_801_r_eye_x + sum_16_801_r_eye_y
sum_16_801_l_ear = sum_16_801_l_ear_x + sum_16_801_l_ear_y
sum_16_801_r_ear = sum_16_801_r_ear_x + sum_16_801_r_ear_y
sum_16_801_l_shoulder = sum_16_801_l_shoulder_x + sum_16_801_l_shoulder_y
sum_16_801_r_shoulder = sum_16_801_r_shoulder_x + sum_16_801_r_shoulder_y
sum_16_801 = sum_16_801_nose + sum_16_801_l_eye + sum_16_801_r_eye + sum_16_801_l_ear + sum_16_801_r_ear + sum_16_801_l_shoulder + sum_16_801_r_shoulder

avg_8_257 = sum_8_257/(14*NUMBER)
# avg_8_449 = sum_8_449/(14*NUMBER)
avg_8_801 = sum_8_801/(14*NUMBER)
avg_16_257 = sum_16_257/(14*NUMBER)
# avg_16_449 = sum_16_449/(14*NUMBER)
avg_16_801 = sum_16_801/(14*NUMBER)

avg_8_257_nose_x = sum_8_257_nose_x/NUMBER
avg_8_257_nose_y = sum_8_257_nose_y/NUMBER
avg_8_257_nose = sum_8_257_nose/NUMBER
avg_8_257_l_eye_x = sum_8_257_l_eye_x/NUMBER
avg_8_257_l_eye_y = sum_8_257_l_eye_y/NUMBER
avg_8_257_l_eye = sum_8_257_l_eye/NUMBER
avg_8_257_r_eye_x = sum_8_257_r_eye_x/NUMBER
avg_8_257_r_eye_y = sum_8_257_r_eye_y/NUMBER
avg_8_257_r_eye = sum_8_257_r_eye/NUMBER
avg_8_257_l_ear_x = sum_8_257_l_ear_x/NUMBER
avg_8_257_l_ear_y = sum_8_257_l_ear_y/NUMBER
avg_8_257_l_ear = sum_8_257_l_ear/NUMBER
avg_8_257_r_ear_x = sum_8_257_r_ear_x/NUMBER
avg_8_257_r_ear_y = sum_8_257_r_ear_y/NUMBER
avg_8_257_r_ear = sum_8_257_r_ear/NUMBER
avg_8_257_l_shoulder_x = sum_8_257_l_shoulder_x/NUMBER
avg_8_257_l_shoulder_y = sum_8_257_l_shoulder_y/NUMBER
avg_8_257_l_shoulder = sum_8_257_l_shoulder/NUMBER
avg_8_257_r_shoulder_x = sum_8_257_r_shoulder_x/NUMBER
avg_8_257_r_shoulder_y = sum_8_257_r_shoulder_y/NUMBER
avg_8_257_r_shoulder = sum_8_257_r_shoulder/NUMBER

# avg_8_449_nose_x = sum_8_449_nose_x/NUMBER
# avg_8_449_nose_y = sum_8_449_nose_y/NUMBER
# avg_8_449_nose = sum_8_449_nose/NUMBER
# avg_8_449_l_eye_x = sum_8_449_l_eye_x/NUMBER
# avg_8_449_l_eye_y = sum_8_449_l_eye_y/NUMBER
# avg_8_449_l_eye = sum_8_449_l_eye/NUMBER
# avg_8_449_r_eye_x = sum_8_449_r_eye_x/NUMBER
# avg_8_449_r_eye_y = sum_8_449_r_eye_y/NUMBER
# avg_8_449_r_eye = sum_8_449_r_eye/NUMBER
# avg_8_449_l_ear_x = sum_8_449_l_ear_x/NUMBER
# avg_8_449_l_ear_y = sum_8_449_l_ear_y/NUMBER
# avg_8_449_l_ear = sum_8_449_l_ear/NUMBER
# avg_8_449_r_ear_x = sum_8_449_r_ear_x/NUMBER
# avg_8_449_r_ear_y = sum_8_449_r_ear_y/NUMBER
# avg_8_449_r_ear = sum_8_449_r_ear/NUMBER
# avg_8_449_l_shoulder_x = sum_8_449_l_shoulder_x/NUMBER
# avg_8_449_l_shoulder_y = sum_8_449_l_shoulder_y/NUMBER
# avg_8_449_l_shoulder = sum_8_449_l_shoulder/NUMBER
# avg_8_449_r_shoulder_x = sum_8_449_r_shoulder_x/NUMBER
# avg_8_449_r_shoulder_y = sum_8_449_r_shoulder_y/NUMBER
# avg_8_449_r_shoulder = sum_8_449_r_shoulder/NUMBER

avg_8_257_nose_x = sum_8_257_nose_x/NUMBER
avg_8_257_nose_y = sum_8_257_nose_y/NUMBER
avg_8_257_nose = sum_8_257_nose/NUMBER
avg_8_257_l_eye_x = sum_8_257_l_eye_x/NUMBER
avg_8_257_l_eye_y = sum_8_257_l_eye_y/NUMBER
avg_8_257_l_eye = sum_8_257_l_eye/NUMBER
avg_8_257_r_eye_x = sum_8_257_r_eye_x/NUMBER
avg_8_257_r_eye_y = sum_8_257_r_eye_y/NUMBER
avg_8_257_r_eye = sum_8_257_r_eye/NUMBER
avg_8_257_l_ear_x = sum_8_257_l_ear_x/NUMBER
avg_8_257_l_ear_y = sum_8_257_l_ear_y/NUMBER
avg_8_257_l_ear = sum_8_257_l_ear/NUMBER
avg_8_257_r_ear_x = sum_8_257_r_ear_x/NUMBER
avg_8_257_r_ear_y = sum_8_257_r_ear_y/NUMBER
avg_8_257_r_ear = sum_8_257_r_ear/NUMBER
avg_8_257_l_shoulder_x = sum_8_257_l_shoulder_x/NUMBER
avg_8_257_l_shoulder_y = sum_8_257_l_shoulder_y/NUMBER
avg_8_257_l_shoulder = sum_8_257_l_shoulder/NUMBER
avg_8_257_r_shoulder_x = sum_8_257_r_shoulder_x/NUMBER
avg_8_257_r_shoulder_y = sum_8_257_r_shoulder_y/NUMBER
avg_8_257_r_shoulder = sum_8_257_r_shoulder/NUMBER

avg_8_801_nose_x = sum_8_801_nose_x/NUMBER
avg_8_801_nose_y = sum_8_801_nose_y/NUMBER
avg_8_801_nose = sum_8_801_nose/NUMBER
avg_8_801_l_eye_x = sum_8_801_l_eye_x/NUMBER
avg_8_801_l_eye_y = sum_8_801_l_eye_y/NUMBER
avg_8_801_l_eye = sum_8_801_l_eye/NUMBER
avg_8_801_r_eye_x = sum_8_801_r_eye_x/NUMBER
avg_8_801_r_eye_y = sum_8_801_r_eye_y/NUMBER
avg_8_801_r_eye = sum_8_801_r_eye/NUMBER
avg_8_801_l_ear_x = sum_8_801_l_ear_x/NUMBER
avg_8_801_l_ear_y = sum_8_801_l_ear_y/NUMBER
avg_8_801_l_ear = sum_8_801_l_ear/NUMBER
avg_8_801_r_ear_x = sum_8_801_r_ear_x/NUMBER
avg_8_801_r_ear_y = sum_8_801_r_ear_y/NUMBER
avg_8_801_r_ear = sum_8_801_r_ear/NUMBER
avg_8_801_l_shoulder_x = sum_8_801_l_shoulder_x/NUMBER
avg_8_801_l_shoulder_y = sum_8_801_l_shoulder_y/NUMBER
avg_8_801_l_shoulder = sum_8_801_l_shoulder/NUMBER
avg_8_801_r_shoulder_x = sum_8_801_r_shoulder_x/NUMBER
avg_8_801_r_shoulder_y = sum_8_801_r_shoulder_y/NUMBER
avg_8_801_r_shoulder = sum_8_801_r_shoulder/NUMBER

avg_16_257_nose_x = sum_16_257_nose_x/NUMBER
avg_16_257_nose_y = sum_16_257_nose_y/NUMBER
avg_16_257_nose = sum_16_257_nose/NUMBER
avg_16_257_l_eye_x = sum_16_257_l_eye_x/NUMBER
avg_16_257_l_eye_y = sum_16_257_l_eye_y/NUMBER
avg_16_257_l_eye = sum_16_257_l_eye/NUMBER
avg_16_257_r_eye_x = sum_16_257_r_eye_x/NUMBER
avg_16_257_r_eye_y = sum_16_257_r_eye_y/NUMBER
avg_16_257_r_eye = sum_16_257_r_eye/NUMBER
avg_16_257_l_ear_x = sum_16_257_l_ear_x/NUMBER
avg_16_257_l_ear_y = sum_16_257_l_ear_y/NUMBER
avg_16_257_l_ear = sum_16_257_l_ear/NUMBER
avg_16_257_r_ear_x = sum_16_257_r_ear_x/NUMBER
avg_16_257_r_ear_y = sum_16_257_r_ear_y/NUMBER
avg_16_257_r_ear = sum_16_257_r_ear/NUMBER
avg_16_257_l_shoulder_x = sum_16_257_l_shoulder_x/NUMBER
avg_16_257_l_shoulder_y = sum_16_257_l_shoulder_y/NUMBER
avg_16_257_l_shoulder = sum_16_257_l_shoulder/NUMBER
avg_16_257_r_shoulder_x = sum_16_257_r_shoulder_x/NUMBER
avg_16_257_r_shoulder_y = sum_16_257_r_shoulder_y/NUMBER
avg_16_257_r_shoulder = sum_16_257_r_shoulder/NUMBER

# avg_16_449_nose_x = sum_16_449_nose_x/NUMBER
# avg_16_449_nose_y = sum_16_449_nose_y/NUMBER
# avg_16_449_nose = sum_16_449_nose/NUMBER
# avg_16_449_l_eye_x = sum_16_449_l_eye_x/NUMBER
# avg_16_449_l_eye_y = sum_16_449_l_eye_y/NUMBER
# avg_16_449_l_eye = sum_16_449_l_eye/NUMBER
# avg_16_449_r_eye_x = sum_16_449_r_eye_x/NUMBER
# avg_16_449_r_eye_y = sum_16_449_r_eye_y/NUMBER
# avg_16_449_r_eye = sum_16_449_r_eye/NUMBER
# avg_16_449_l_ear_x = sum_16_449_l_ear_x/NUMBER
# avg_16_449_l_ear_y = sum_16_449_l_ear_y/NUMBER
# avg_16_449_l_ear = sum_16_449_l_ear/NUMBER
# avg_16_449_r_ear_x = sum_16_449_r_ear_x/NUMBER
# avg_16_449_r_ear_y = sum_16_449_r_ear_y/NUMBER
# avg_16_449_r_ear = sum_16_449_r_ear/NUMBER
# avg_16_449_l_shoulder_x = sum_16_449_l_shoulder_x/NUMBER
# avg_16_449_l_shoulder_y = sum_16_449_l_shoulder_y/NUMBER
# avg_16_449_l_shoulder = sum_16_449_l_shoulder/NUMBER
# avg_16_449_r_shoulder_x = sum_16_449_r_shoulder_x/NUMBER
# avg_16_449_r_shoulder_y = sum_16_449_r_shoulder_y/NUMBER
# avg_16_449_r_shoulder = sum_16_449_r_shoulder/NUMBER

avg_16_801_nose_x = sum_16_801_nose_x/NUMBER
avg_16_801_nose_y = sum_16_801_nose_y/NUMBER
avg_16_801_nose = sum_16_801_nose/(2*NUMBER)
avg_16_801_l_eye_x = sum_16_801_l_eye_x/NUMBER
avg_16_801_l_eye_y = sum_16_801_l_eye_y/NUMBER
avg_16_801_l_eye = sum_16_801_l_eye/(2*NUMBER)
avg_16_801_r_eye_x = sum_16_801_r_eye_x/NUMBER
avg_16_801_r_eye_y = sum_16_801_r_eye_y/NUMBER
avg_16_801_r_eye = sum_16_801_r_eye/(2*NUMBER)
avg_16_801_l_ear_x = sum_16_801_l_ear_x/NUMBER
avg_16_801_l_ear_y = sum_16_801_l_ear_y/NUMBER
avg_16_801_l_ear = sum_16_801_l_ear/(2*NUMBER)
avg_16_801_r_ear_x = sum_16_801_r_ear_x/NUMBER
avg_16_801_r_ear_y = sum_16_801_r_ear_y/NUMBER
avg_16_801_r_ear = sum_16_801_r_ear/(2*NUMBER)
avg_16_801_l_shoulder_x = sum_16_801_l_shoulder_x/NUMBER
avg_16_801_l_shoulder_y = sum_16_801_l_shoulder_y/NUMBER
avg_16_801_l_shoulder = sum_16_801_l_shoulder/(2*NUMBER)
avg_16_801_r_shoulder_x = sum_16_801_r_shoulder_x/NUMBER
avg_16_801_r_shoulder_y = sum_16_801_r_shoulder_y/NUMBER
avg_16_801_r_shoulder = sum_16_801_r_shoulder/(2*NUMBER)

# make graph
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(20,10))
plt.xticks([257, 801])
# ouput stride 8 points
x8 = [257, 801]
y8 = [avg_8_257, avg_8_801]
# output stride 16 points
x16 = [257, 801]
y16 = [avg_16_257, avg_16_801]
# plotting the points  
plt.plot(x8, y8, 'o', color='red', label='8', markersize=3)
plt.plot(x16, y16, 'o', color='blue', label='16', markersize=3)

for i_x, i_y in zip(x8, y8):
    plt.text(i_x, i_y, '{}'.format(i_y))
for i_x, i_y in zip(x16, y16):
    plt.text(i_x, i_y, '{}'.format(i_y))

plt.xlabel('Input Resolution')
plt.ylabel('Accuracy (ground truth - posenet)')
plt.title('Accuracy')
plt.legend(frameon=True)
plt.show()

print(avg_8_257, avg_8_801, avg_16_257, avg_16_801)
