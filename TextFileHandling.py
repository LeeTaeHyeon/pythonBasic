import csv
import pandas as pd


fields = ["title", "singer", "released date"]
rows = [ ["Tho Box","Roddy Ricch","2019-12-19"],
               ["Don't Start Now", "Dua Lipa", "2019-11-01"],
               ["Life Is Good", "Future Featuring Drake", "2020-02-10"],
               ["Blinding", "The Weeknd", "2019-11-29"],
               ["Circles", "Post Malone","2019-08-30"]]

# 데이터 프레임 만들고
df = pd.DataFrame(rows, columns=fields)
df
# 이걸 csv로 파일을 만든다.
df.to_csv('pandas.csv', index=False)

filename = 'test.csv'

with open(filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow((fields))
    csv_writer.writerows(rows)



# billboardchart = {1: ["Tho Box","Roddy Ricch","2019-12-19"],
#                   2: ["Don't Start Now", "Dua Lipa", "2019-11-01"],
#                   3: ["Life Is Good", "Future Featuring Drake", "2020-02-10"],
#                   4: ["Blinding", "The Weeknd", "2019-11-29"],
#                   5: ["Circles", "Post Malone","2019-08-30"]}

# with open("billboardchart.csv","w") as f:
#     for i in billboardchart.values():
#         data = ",".join(i)
#         f.write(data+"\n")
#
# header = ["title", "singer", "released date"]
#
# with open("billboardchart.csv","r") as inputfile:
#     with open("billboardchart_out.csv", "w", newline="\n") as outputfile:
#         fi = csv.reader(inputfile)
#         fo = csv.writer(outputfile)
#         fo.writerow(header)
#         for row in fi:
#             fo.writerow(row)

# f = open("hello.txt", "w")
#
# for i in range(1, 10):
#     f.write("안녕")
#
# f.close()
#
# with open("hello.txt", "r") as f:
#     print(f.read())
#
# for i in range(1, 10):
#     print(i)

'''
n = 1 / output[0].append(number) -> [[1],[],[]]
n = 2 / output[1].append(number) -> [[1],[2],[]]
n = 3 / output[2].append(number) -> [[1],[2],[3]]
n = 4 / output[0].append(number) -> [[1,4],[2],[3]]
.
.
.

'''
# numbers = list(range(0,10))
# output = [[], [], []]
#
# for number in numbers:
#     output[(number + 2) % 3].append(number)
#
# print(output)
