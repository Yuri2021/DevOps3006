for i in range(1, 101):
    if i % 7 != 0 and "7" not in str(i):    # print num / 7
        continue
    print(i)


else:
    print("lopp finished")