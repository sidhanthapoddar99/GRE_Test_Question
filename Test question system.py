#!/usr/bin/env python
# coding: utf-8

# In[34]:


import json
import random


# In[46]:


print("to search a specific word go to the website")
print("https://www.merriam-webster.com/dictionary")
print()


# In[14]:


print("enter data file name")
name=input()+".json"


# In[15]:


with open('DATA OUT/'+name) as json_file:
    data = json.load(json_file)


# In[29]:


print("enter the range of question")
print("Starting question:")
st=max(int(input())-1,0)
print("Ending question:")
ed=min(int(input()),len(data))
print("start : ",st,"  end : ",ed)


# In[64]:


all_words=list(data.keys())
MwordsO=[]
if ed==len(data):
    MwordsO=all_words[st:]
else:
    MwordsO=all_words[st:ed]


# In[50]:


print("Do you want the option to be restricted to the range(Y/n)")
stC=0
edC=len(data)
opt=input()
if(opt=="Y" or opt=='y'):
    stC=st
    edC=ed
else:
    print("enter the range of options")
    print("Starting question:")
    stC=max(int(input())-1,0)
    print("Ending question:")
    edC=min(int(input()),len(data))
    print("start : ",st,"  end : ",ed)


# In[45]:


print("Enter number of option to be displayed")
num=max(int(input()),3)


# In[59]:


def question(data,word,st,ed,words,num):
    
    random_word_list = []
    for i in range(num-1):
        n = random.randint(st,ed-1)
        random_word_list.append(words[n])
    random_word_list.append(word)
    random.shuffle(random_word_list)
    x=random.randint(0,len(data[word]["sent"])-1)
    print(data[word]["sent"][x])
    print("\n\nOptions:")
    k=1
    for i in random_word_list:
        print(k,". ",i)
        k+=1
    print("Please enter your answer")
    ans=int(input())-1
    cor=False
    if(random_word_list[ans]==word):
        cor=True
    
    if cor:
        print("Correct answer!!")
    else:
        print("Sorry the correct answer is || "+word+" ||")
        
    print("\n\n\n===================Meanings=======================")
    
    for i in random_word_list:
        print("--------------------",i,"---------------------")
        print(data[i]["meaning"])

    print("=============Synonyms of "+word+"================")
    print(data[word]["synonyms"])
    print("=============Antonyms of "+word+"================")
    print(data[word]["antonyms"])
    
    return(cor)
    


# In[68]:


def question_set(data,stC,edC,all_words,num,MwordsO):
    
    
    Mwords=MwordsO[:]
    
    #########################################################
    
    print("Do you want the question jumbled up(Y/n)")
    temp=input()
    if(temp!="Y" or temp!="y"):
        random.shuffle(Mwords)
    
    ##########################################################
    
    print("Enter the target number of question to solve (< main words)")   
    nosi=min(int(input()),len(Mwords))
    c=0
    m=nosi
    for i in range(len(Mwords)):
        if i==nosi:
            print("You have solved your target question do you want to solve the remaning?(Y/n)")
            temp=input()
            if(temp!="Y" or temp!="y"):
                break
            else:
                nosi=len(Mwords)
        input("Press Enter to continue...")
        print("\n\n\n\n\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n\n")
        print("Question: ",(i+1),"/",nosi,"\t\t\t\t Score: ",c,"/",i)
        if(question(data,Mwords[i],stC,edC,all_words,num)):
            c+=1
    print("Final Score is ",c,"/",nosi)
    input("Press Enter to continue...")
        


# In[70]:


while(True):
    print("Do you want to Practice more?(Y/n)")
    temp=input()
    if(temp!="Y" or temp!="y"):
        question_set(data,stC,edC,all_words,num,MwordsO)
    else:
        break


# In[ ]:




