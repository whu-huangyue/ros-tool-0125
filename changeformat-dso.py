#coding=utf-8
import sys
import os

if __name__ == '__main__':
    path = sys.argv[1]  # 数据文件路径
    # out_path = sys.argv[2]
    out_path = os.path.dirname(path) + "/times.txt"
    fin = open(path, 'r')
    l0s = []
    l1s = []
    # l1s = []
    # l2s = []
    # l3s = []
    # l4s = []
    # l5s = []
    # l6s = []
    # l7s = []

    # fin.readline()
    line = fin.readline()
    while line:
        # parts = line.split(",")
        # l0 = float(parts[0]) / 1000000000
        # l1 = float(parts[1])
        # l2 = float(parts[2])
        # l3 = float(parts[3])
        # l4 = float(parts[4])
        # l5 = float(parts[5])
        # l6 = float(parts[6])
        # l7 = float(parts[7])

        l0 = line
        l0s.append(str(l0))
        l1 = float(l0) / 1e9
        l1s.append(float(l1))
        # l1s.append(l1)
        # l2s.append(l2)
        # l3s.append(l3)
        # l4s.append(l4)
        # l5s.append(l5)
        # l6s.append(l6)
        # l7s.append(l7)

        line = fin.readline().strip()
    
    with open(out_path, 'w+') as f_out:
        for i in range(len(l0s)):
            print('working : ', i+1 , '/' , len(l0s))
            # out_name = f"{names[i].split(img_type)[0]:0>{6}}"
            # f_out.write(f"{l0s[i]:0>{6}}" + ' ')
            # f_out.write("{:.6f}".format(l1s[i]) + '\n')
            # f_out.write("{:.0f}".format(l0s[i]) + ' ')
            f_out.write(l0s[i] + ' ')
            f_out.write("{:.6f}".format(l1s[i]) + '\n')
            # f_out.write("{:.9f}".format(l2s[i]) + ' ')
            # f_out.write("{:.9f}".format(l3s[i]) + ' ')
            # f_out.write("{:.9f}".format(l4s[i]) + ' ')
            # f_out.write("{:.9f}".format(l5s[i]) + ' ')
            # f_out.write("{:.9f}".format(l6s[i]) + ' ')
            # f_out.write("{:.9f}".format(l7s[i]) + '\n')
            # f_out.write(' ' + str(l1s[i]) + ' ' + str(l2s[i]) + ' ' + str(l3s[i]) + ' ' + str(l4s[i]) + ' ' + str(l5s[i]) + ' ' + str(l6s[i]) + ' ' + str(l7s[i]) + '\n')
