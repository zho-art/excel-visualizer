fw = open("score.csv", "w")
ls = [["姓名", "语文", "数学", "英语"], ["小明", "80", "90", "86"],
      ["小萌", "85", " ", "82"], ["小辉", " ", "82", "90"]]
for line in ls:
    fw.write(",".join(line)+"\n")
fw.close()
fo = open("score.csv", "r")
for line in fo:
    line = line.replace("\n", "")
    line = line.replace(" ", "缺")
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns += "{}\t".format(s)
    print(lns)
fo.close()