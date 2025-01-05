import time 
from xml.etree import ElementTree as ET
import mido

def getdiff(start:float)->str:
    now=time.time()
    diff=now-start
    mins=int(diff/60)
    sec=int(diff%60)
    ms=int((diff%1)*1000)
    event=f"{mins:02d}:{sec:02d}.{ms:03d}"
    return event

lyrics=open('lyrics.txt','r')
lines=lyrics.readlines()
lyrics.close()
total_lines=len(lines)

if lines[0].strip()=="":
    raise ValueError('First line in the file cannot be blank')

print(f"total lines: {total_lines}")
input('Press Enter to begin recording lyric times.')
print('Timer started')
index=0
time_array=[]
inport = mido.open_input()
start=time.time()
while index!=total_lines:
    if lines[index].strip()=='':
        time_array.append(['00:00.000','00:00.000'])
        index+=1
        continue

    msg = inport.receive()
    if msg.type=='note_on':
        print(f"\t\t\t\t\t\t {lines[index].strip()}\n")
        event=getdiff(start)
        time_array.append([event])
        print(f"start: {event} ",end="")

    msg = inport.receive()
    if msg.type=='note_off':
        event=getdiff(start)
        time_array[index].append(event)
        print(f"end:{event} \t {total_lines-index}")
    index+=1
    pass


root = ET.Element('tt',attrib={
    'xmlns':"http://www.w3.org/ns/ttml",
    'xmlns:ttp':"http://www.w3.org/ns/ttml#parameter",
    'ttp:timeBase':"media",
    'xmlns:tts':"http://www.w3.org/ns/ttml#styling",
    'xml:lang':"en",
    'xmlns:ttm':"http://www.w3.org/ns/ttml#metadata",
})
head=ET.SubElement(root,'head')
metadata=ET.SubElement(head,'metadata')
title=ET.SubElement(metadata,'ttm:title').text="Song Name"

body=ET.SubElement(root,'body',attrib={
    'dur':time_array[-1][1]
})

div=ET.SubElement(body,'div',attrib={'begin':time_array[0][0]})

for index in range(len(time_array)):
    if lines[index].strip()=='':
        div.set('end',time_array[index-1][1])    
        div=ET.SubElement(body,'div',attrib={'begin':time_array[index+1][0]})
    else:
        p=ET.SubElement(div,'p',attrib={
            'begin':f"{time_array[index][0]}",
            'end':f"{time_array[index][1]}",
        }).text=lines[index].strip()

    if index==len(time_array)-1:
        div.set('end',time_array[index][1])    

et = ET.ElementTree(root)

op_file=open('output.ttml','wb')
et.write(op_file,encoding='utf-8')
