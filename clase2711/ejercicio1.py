import os

ruta=os.getcwd()
file_path=os.path.join(ruta,'marketing_campaign.csv')
list_heardes=[]
list_id=[]
print(file_path)
try:
    with open(file_path,'r') as file:
        index=1
        for linea in file:
            listTemp=linea.split(',')
            if type(listTemp[2])!='str':
                list_id.append(listTemp[0])
            index+=1
except:
    print("not found file")

print(list_id)
###
class User():
    def __init__(self,p1,p2,p3):
            self.p1=p1
            self.p2=p2
import User


input("ingrse nombre")

u1=User("nombre")






