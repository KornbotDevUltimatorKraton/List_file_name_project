import requests 
res = requests.get("http://192.168.50.201:5890/project_files")
datas = res.json()
print(datas)
list_proj_files = {} 
current_list = [] 
#check_email = [] # Checking current email
datas['teslacoil358@gmail.com'] = {'devians':'serevices_robotics','pubpet':'humanoid_services'}

for rtj in list(datas):
          for ir in list(datas.get(rtj)):
                  print(ir,datas.get(rtj).get(ir))
                  if datas.get(rtj).get(ir) not in current_list:  
                      if rtj not in list(list_proj_files):    
                              list_proj_files[rtj] = [datas.get(rtj).get(ir)]
                              if list_proj_files[rtj] != []:
                                    if datas.get(rtj).get(ir) not in list_proj_files[rtj]:
                                        list_proj_files[rtj].append(datas.get(rtj).get(ir))
                      if rtj in list(list_proj_files):
                              if list_proj_files[rtj] != []:             
                                   if datas.get(rtj).get(ir) not in list_proj_files[rtj]:
                                        list_proj_files[rtj].append(datas.get(rtj).get(ir))                                                              
          
                     
          '''  
                  list_proj_files[rtj] = [] 
                  if list_proj_files[rtj] == []:
                         list_proj_files[rtj].append(datas.get(rtj).get(ir)) 
                  if list_proj_files[rtj] !=[]:
                         list_proj_files[rtj].append(datas.get(rtj).get(ir))       
          '''
print(list_proj_files)
          
