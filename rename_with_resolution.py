with open("filenames.txt","r") as f:
	lines=f.readlines()
import os
import sys
for i in lines:
	split=i.split(".")
	name=split[0]
	extension="mp4"
	os.system("ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "+name+".mp4"+" > tmp.txt")
	with open('tmp.txt',"r") as k:
		res=k.readlines()
	res=res[0].strip()
	print(res)
	os.rename(name+"."+extension,name+res+"."+extension)
