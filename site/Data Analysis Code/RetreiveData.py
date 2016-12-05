__author__ = 'Rakesh'
import json
import numpy as np
fileLoc='C:/Users/Rakesh/Desktop/webmd-dataset/'
coorMApper={}
coorMApper["diabetes"]=[102,51,204]#yellow
coorMApper["pain"]=[101,16,103]#orange
coorMApper["muscle"]=[230,115,0]#blue
coorMApper["women_related"]=[255,20,147]#pink
coorMApper["lung_liver"]=[139,7,7]#purple
coorMApper["heart"]=[0,153,198]
coorMApper["blood"]=[184,46,46]
coorMApper["infection"]=[49,99,149]
def UserBasedModelling(data,users,year):
    listData=[]
    for f in data:
        locaData=[]
        locaData.append(f['topicName'])
        if(f['answerMemberId'] in users.keys() ):
            locaData.append(users[f['answerMemberId']].split(',')[0])
        else:
            locaData.append(f['answerMemberId'])
        locaData.append(f['topicVal'])
        listData.append(locaData)
    with open(fileLoc+"userModelData"+year+".json", "w") as jsonFile:
        jsonFile.write(json.dumps(listData))
    pass

def treeDataCreator(data,year):
    mainData='id,value,color\nRoot\n'
    dataFormat="Root.{}.{},{},{}"
    mainDataMap={}
    maxDataValMap={}
    #print(len(data))
    for f in data:
        if f['topicName'] in maxDataValMap.keys():
            if maxDataValMap[f['topicName']]>f['topicVal']:
                maxDataValMap[f['topicName']]=f['topicVal']
        else:
            maxDataValMap[f['topicName']]=f['topicVal']

    for f in data:
        print (maxDataValMap[f['topicName']]-f['topicVal'])
        col=lighter(coorMApper[f['topicName']],(maxDataValMap[f['topicName']]-max(f['topicVal'],0.25)))
        print col

        cdata='#%02x%02x%02x' %(clamp(col[0]),clamp(col[1]),clamp(col[2]))
        if f['topicName'] in mainDataMap.keys():
            mainDataMap[f['topicName']]=mainDataMap[f['topicName']]+"\n"+dataFormat.format(f['topicName'],f['questionId'],f['topicVal'],cdata)
        else:
            mainDataMap[f['topicName']]=dataFormat.format(f['topicName'],f['questionId'],f['topicVal'],cdata)

    for k,v in mainDataMap.iteritems():
        mainData+="\nRoot."+k+"\n"+v
    with open(fileLoc+"topicModelData"+year+".txt", "w") as jsonFile:
        jsonFile.write(mainData)
    print(mainData)

def treeDataCreator2(data,year):
    mainData='id,value,color\nRoot\n'
    dataFormat="Root.{}.{},{},{}"
    mainDataMap={}
    maxDataValMap={}
    #print(len(data))
    for f in data:
        if f['topicName'] in maxDataValMap.keys():
            if maxDataValMap[f['topicName']]>f['topicVal']:
                maxDataValMap[f['topicName']]=f['topicVal']
        else:
            maxDataValMap[f['topicName']]=f['topicVal']

    for f in data:
        print (maxDataValMap[f['topicName']]-f['topicVal'])
        col=lighter(coorMApper[f['topicName']],(sentimentMap[f['questionId']]))
        print col

        cdata='#%02x%02x%02x' %(clamp(col[0]),clamp(col[1]),clamp(col[2]))
        if f['topicName'] in mainDataMap.keys():
            mainDataMap[f['topicName']]=mainDataMap[f['topicName']]+"\n"+dataFormat.format(f['topicName'],f['questionId'],(sentimentMap[f['questionId']]),cdata)
        else:
            mainDataMap[f['topicName']]=dataFormat.format(f['topicName'],f['questionId'],(sentimentMap[f['questionId']]),cdata)

    for k,v in mainDataMap.iteritems():
        mainData+="\nRoot."+k+"\n"+v
    with open(fileLoc+"sentimentModelData"+year+".txt", "w") as jsonFile:
        jsonFile.write(mainData)
    print(mainData)

def clamp(x):
  return max(0, min(x, 255))



def getUserList(data):
    dataMap={}
    for d in data:
        dataMap[str(d["memberId"])]=d["memberName"]
    return dataMap

def readfile(param):
    with open(fileLoc+param,'r') as f:
        yield f
    pass

def lighter(color, percent):
    '''assumes color is rgb between (0, 0, 0) and (255, 255, 255)'''
    color = np.array(color)
    white = np.array([255, 255, 255])
    vector = white-color
    return color + vector * percent

def shadeColor1(color, percent):
    num = int(color[1:],16)
    amt = int(round(2.55 * percent))
    R = (num >> 16) + amt
    G = (num >> 8 & 0x00FF) + amt
    B = (num & 0x0000FF) + amt
    if R<1:
        R=0
    elif G>255:
        R=255
    if G<1:
        G=0
    elif G>255:
        G=255
    if B<1:
        B=0
    elif B>255:
        B=255


    return "#" + str(hex(0x1000000 + (R)*0x10000 + (G)*0x100 + (B)))[2:]


def color_variant(hex_color, brightness_offset=1):
    """ takes a color like #87c95f and produces a lighter or darker variant """
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    return "#" + "".join([hex(i)[2:] for i in new_rgb_int])


def polylinear_gradient(colors, n):
      n_out = int(float(n) / (len(colors) - 1))
      # returns dictionary defined by color_dict()
      gradient_dict = linear_gradient(colors[0], colors[1], n_out)

      if len(colors) > 1:
        for col in range(1, len(colors) - 1):
          next = linear_gradient(colors[col], colors[col+1], n_out)
          for k in ("hex", "r", "g", "b"):
            # Exclude first point to avoid duplicates
            gradient_dict[k] += next[k][1:]

      return gradient_dict
def color_dict(gradient):
      ''' Takes in a list of RGB sub-lists and returns dictionary of
        colors in RGB and hex form for use in a graphing function
        defined later on '''
      return {"hex":[RGB_to_hex(RGB) for RGB in gradient],
          "r":[RGB[0] for RGB in gradient],
          "g":[RGB[1] for RGB in gradient],
          "b":[RGB[2] for RGB in gradient]}


def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
  ''' returns a gradient list of (n) colors between
    two hex colors. start_hex and finish_hex
    should be the full six-digit color string,
    inlcuding the number sign ("#FFFFFF") '''
  # Starting and ending colors in RGB form
  s = hex_to_RGB(start_hex)
  f = hex_to_RGB(finish_hex)
  # Initilize a list of the output colors with the starting color
  RGB_list = [s]
  # Calcuate a color at each evenly spaced value of t from 1 to n
  for t in range(1, n):
    # Interpolate RGB vector for color at the current value of t
    curr_vector = [
      int(s[j] + (float(t)/(n-1))*(f[j]-s[j]))
      for j in range(3)
    ]
    # Add it to our list of output colors
    RGB_list.append(curr_vector)

  return color_dict(RGB_list)

def hex_to_RGB(hex):
  ''' "#FFFFFF" -> [255,255,255] '''
  # Pass 16 to the integer function for change of base
  return [int(hex[i:i+2], 16) for i in range(1,6,2)]


def RGB_to_hex(RGB):
  ''' [255,255,255] -> "#FFFFFF" '''
  # Components need to be integers for hex to make sense
  RGB = [int(x) for x in RGB]
  return "#"+"".join(["0{0:x}".format(v) if v < 16 else
            "{0:x}".format(v) for v in RGB])
'''
print(str(hex(0x5+0x5)))
print(shadeColor1("#ff0000",40))
print(polylinear_gradient("#ff0000",10))

print(color_variant("#ff0000",2))
print(color_variant("#ff0000",3))
print(color_variant("#ff0000",4))
print(color_variant("#ff0000",5))
print(color_variant("#2f2f2f",6))
'''


for f in readfile("new-webmd-member.json"):
    member = json.load(f, strict=False)


sentimentMap={}
lines = [line.rstrip('\n') for line in open('subjectivity.txt')]

for some in lines:
    somearray=some.split(",")
    sentimentMap[somearray[0].strip()]=max(float(somearray[2].strip()),0.1)


year=["2010","2012","2013","2014"]
getUser=getUserList(member)
for y in year:
    for f in readfile("mainDataF"+y+".json"):
        topics_data = json.load(f, strict=False)
    treeDataCreator2(topics_data,y)
    UserBasedModelling(topics_data,getUser,y)
    treeDataCreator(topics_data,y)
'''
'''
