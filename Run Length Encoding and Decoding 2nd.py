class Codec:
    def compress(self,data):
        cdata = ""
        i = 0
        while (i <= len(data)-1):
            count = 1
            ch = data[i]
            j = i
            while (j < len(data)-1):
                if (data[j] == data[j+1]):
                    count = count+1
                    j = j+1
                else:
                    break
            i = j+1
            if(count==1):
                cdata=cdata+ch
            else:
                cdata=cdata+str(count)+ch
        return cdata
        
        
    def decompress(self,data):
        org_data=""
        num=""
        for i in data:
            if(i==" "):
                org_data+=i
            elif(i.isalpha()):
                if(num!=''):
                    if(num.isdigit()):
                        org_data+=i*int(num)
                else:
                    org_data+=i
                
                num=""
            else:
                num+=i
        return org_data

data=input("Enter String : ")       
ob1=Codec()
cdata=ob1.compress(data)
print("Compressed data : ",cdata)
print("Decompressed data : ",ob1.decompress(cdata))
