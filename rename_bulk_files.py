import os
i=0
path = 'C:/Users/a459367/Desktop/python projects/File_rename/'
s = ['text_1','text_2','text_3']
for filename in os.listdir(path):
    my_dest = s[i]+".txt"
    my_source = path+filename
    my_dest = path+my_dest
    os.rename(my_source,my_dest)
    i=i+1
    