def fun(user):
    import requests
    import json 
    from pprint import pprint
    f=requests.get("http://join.navgurukul.org/api/partners")
    s=json.loads(f.text)
    with open("partener.json","w") as l:
        json.dump(s,l,indent=2)
        l=[]
        for i in s:
            for j in s[i]:
                l.append(j["id"])         
        list1=[]
        if user=="1":
            l.sort()
            for i in l:
                for j in s:
                    for k in s[j]:
                        for p in k:
                            if p=="id":
                                 if i==k[p]:
                                    list1.append(k)
        elif user=="2":
            l.sort(reverse = True) 
            for i in l:
                for j in s:
                    for k in s[j]:
                        for p in k:
                            if p=="id":
                                if i==k[p]:
                                    list1.append(k)
    with open("newfile.json","w") as f:
        json.dump(list1,f,indent=4)
print("asending [1] ar desending [2]")
user=input("enter the choice:-")
fun(user)


# import requests
# import json
# f=requests.get("http://join.navgurukul.org/api/partners")
# print(f.text)