import json
target = open("step1_result.txt", 'w',encoding='utf-8') # file to store the step1 result
tmp = []
i = 0
for line in open(r"C:\Users\Desktop\arxiv-metadata-oai-snapshot.json",'r'): #arXiv dataset download from https://www.kaggle.com/Cornell-University/arxiv
    tmp.append(json.loads(line))
    
for i in tmp:
    if 'math'in i["categories"]:  # "math" can change to other domain that included in the "categories"
        data= i["abstract"]    # focus on the abtract part
        target.writelines(data+'\n')
        target.writelines(".\n")
target.close()

