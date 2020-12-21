#!/usr/bin/env python
# coding: utf-8

# In[38]:


def log_parser(filename,TYPE):
    parsed_results=[]
    tca_results=[]
    myDict = {} 
    with open(filename, 'r') as logfile:
       
        for line in logfile:
            
            
            if TYPE in line:
                if TYPE=="DAIW":
                    Date=line[0:8]
                    Time=line[8:18]
                    IdNo=line[18:22]
                    Status=line[22:31]
                    Action=line[31:36]
                    Time2=line[36:45]
                    CharCode1=line[45:53]
                    ACode=line[53:59]
                    PCode=line[59:66]
                    charCode2=line[66:74]
                    DynamicValues=line[74:-1].split(" ")
                    templist=DynamicValues
                    templist[:] = [item for item in templist if item != '']
                        
                    DynamicValues=templist
                    result=[]
                    result1=[]
                    result.extend((Date,Time,IdNo,Status[4:],Action,Time2,CharCode1,ACode,PCode,charCode2,DynamicValues))
                    for i in result[:-1]:
                        try:
                            k=i.strip()
                            #print(i)
                            #print(k)
                            result1.append(k)
                            
                        except:
                            pass
                    result1.append(DynamicValues)
                    print(result1)
                    DAIW_logs = open('DAIW_logs.txt', 'a')
                    data=str(result1)
                    DAIW_logs.write(data+"\n")
                    DAIW_logs.close()
                elif TYPE=="STCA":
                    Date=line[0:8]
                    Time=line[8:18]
                    IdNo=line[18:22]
                    Status=line[22:31]
                    Action=line[31:36]
                    Time2=line[36:45]
                    CharCode1=line[45:53]
                    ACode=line[53:59]
                    PCode=line[59:66]
                    charCode2=line[66:74]
                    ACode2=line[74:80]
                    PCode2=line[80:86]
                    DynamicValues=line[86:-1].split(" ")
                    templist=DynamicValues
                    templist[:] = [item for item in templist if item != '']
                        
                    DynamicValues=templist
                    result=[]
                    result1=[]
                    result.extend((Date,Time,IdNo,Status[4:],Action,Time2,CharCode1,ACode,PCode,charCode2,ACode2,PCode2,DynamicValues))
                    for i in result[:-1]:
                        try:
                            k=i.strip()
                            #print(i)
                            #print(k)
                            result1.append(k)
                            
                        except:
                            pass
                    result1.append(DynamicValues)
                    STCA_logs = open('STCA_logs.txt', 'a')
                    data=str(result1)
                    STCA_logs.write(data+"\n")
                    STCA_logs.close()
                elif TYPE=="MSAW":
                    Date=line[0:8]
                    Time=line[8:18]
                    IdNo=line[18:22]
                    Status=line[22:31]
                    Action=line[31:36]
                    Time2=line[36:45]
                    CharCode1=line[45:53]
                    ACode=line[53:59]
                    PCode=line[59:66]
                    DynamicValues=line[66:-1].split(" ")
                    templist=DynamicValues
                    templist[:] = [item for item in templist if item != '']
                        
                    DynamicValues=templist
                    result=[]
                    result1=[]
                    result.extend((Date,Time,IdNo,Status[4:],Action,Time2,CharCode1,ACode,PCode,DynamicValues))
                    for i in result[:-1]:
                        try:
                            k=i.strip()
                            #print(i)
                            #print(k)
                            result1.append(k)
                            
                        except:
                            pass
                    result1.append(DynamicValues)
                    MSAW_logs = open('MSAW_logs.txt', 'a')
                    data=str(result1)
                    MSAW_logs.write(data+"\n")
                    MSAW_logs.close()
                    
                
                    
                    
                    
                    
                    
                    #print(date,time,idNo,status,action,time2,charCode1,ACode,PCode,charCode2,dynamicNumericValues)
                
                #parsed_results.append(line.split(" "))
                
                #for li in parsed_results:
                    #try:
                        #li.remove(TYPE)
                   # except:
                      #  pass
                    #print(li)
                   #tca_results.append(li)
                    
                   # myDict.setdefault(TYPE, []).append(li)

                #print(type(parsed_results)) 
                
                #last log type does not exist
                
                
        
        
    
           
            


# In[39]:


log_parser("Tca.log","DAIW")
log_parser("Tca.log","STCA")
log_parser("Tca.log","MSAW")
log_parser("Tca.log","APAN")#NO LOGS
#last log type=log_parser("Tca.log","xyz ")





# In[ ]:





# In[ ]:




