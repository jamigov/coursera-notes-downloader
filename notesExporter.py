
#code developed by jamigov
#email: jamigovfecrd@gmail.com

import pandas as pd

fileName = 'example.txt'

#inserting manually the strings from de .txt document
videoName = '<div class="video-title" aria-label="Item Name">'
videoDuration = '<div class="video-details" aria-label="Duration">'
videoTranscript = '<div class="video-section-text" aria-label="Transcript">'
videoUserNote = '<div class="video-note-text-box video-note-text" aria-label="User Note">'

file = open('./notes container/' + fileName)
fileStr = file.read()

#removing the '\n' from the file
fileStr = fileStr.replace('\n', '')

posSt = 0           #initial position of the found string
posEnd = 0          #final position of the found string
lastPosition = 0    #last position where a string was found
entries = []        #list that carries the notes
number = -1         #number of the video

while(True):

    #first we get the position of the video, then check for the stop condition, which is that the you didn't found another videoName string
    posSt = fileStr.find(videoName,lastPosition)
    if(posSt == -1): break
    posSt +=len(videoName)  #fix the length to the start of the string that we want to extract (the actual name of the video, not the string that we matched)

    posEnd = fileStr.find('<',posSt)
    name = fileStr[posSt:posEnd]        #get the name on the relevant interval
    lastPosition = posEnd

    posSt = fileStr.find(videoDuration,lastPosition)+len(videoDuration) #repeat process for Duration, note that we don't check for the stop condition
    posEnd = fileStr.find('<',posSt)
    duration = fileStr[posSt:posEnd]
    if(duration.find(':')==1): duration = '0'+duration  #add a cero at the  beggining for the duration that doesn't have it (excel purposes)
    
    lastPosition = posEnd

    posSt = fileStr.find(videoTranscript,lastPosition)+len(videoTranscript)
    posEnd = fileStr.find('<',posSt)
    transcript = fileStr[posSt:posEnd]
    lastPosition = posEnd

    if(number<0):           #get the number of the video (is assumed that they come ordered)
        number+=1
    elif(entries[-1]["name"] != name):
        number+=1

    posUserNote = fileStr.find(videoUserNote,lastPosition)      #this is to check if the User Note exists, if it exists then you add it and update as usual
    posNextNote = fileStr.find(videoName,lastPosition)          #if it doesn't exist then you just put '-1'
                                                                #there is a special case because with the current logic if the last element has a User Note
                                                                #I wasn't adding it, so I added this particular case
    if((posUserNote < posNextNote) and (posUserNote!=-1)):
        posSt = posUserNote+len(videoUserNote)
        posEnd = fileStr.find('<',posSt)
        userNote = fileStr[posSt:posEnd]
        lastPosition = posEnd

    elif((posNextNote==-1)and(posUserNote>0)):                  #Special Case. After you add, you break the cycle
        posSt = posUserNote+len(videoUserNote)
        posEnd = fileStr.find('<',posSt)
        userNote = fileStr[posSt:posEnd]
        note = {
            "videoNumber": number,
            "duration": duration,
            "name": name,
            "transcript": transcript,
            "userNote": userNote
        }   
        entries.append(note)
        break
    else:
        userNote = '-1'

    note = {
        "videoNumber": number,
        "duration": duration,
        "name": name,
        "transcript": transcript,
        "userNote": userNote
    }   

    entries.append(note)


df = pd.DataFrame.from_dict(entries)            #export the data to a excel file to better read it
df.to_excel('output.xlsx')
print("Exported sucessfully, check the output.xlsx file")