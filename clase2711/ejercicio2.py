import os

ruta=os.getcwd()
file_path=os.path.join(ruta,'marketing_campaign.txt')
list_heardes=[]
list_id=[]
print(file_path)
try:
    with open(file_path,'r') as file:
        index=1
        for linea in file:
            listTemp=linea.split('\t')
            list_id.append(listTemp[0])
            index+=1
except:
    print("not found file")

print(list_id)
