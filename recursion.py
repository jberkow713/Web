

d = {
  "items": [
    {
      "id": "12345",
      "links": {
        "self": "https://www.google.com"
      },
      "name": "beast",
      "type": "Device"
    }
  ],
  "links": {
    "self": "https://www.google.com"
  },
  "paging": {
    "count": 1,
    "limit": 1,
    "offset": 0,
    "pages": [{'k':1,'g':{}, 'v':[1,2,3,[4,5,[6,[8]]]], 'f':{'f':[1,2,3,4,5,[3,4]]}}]
  }
}

d2 = {
    "id": 1,
    "class": "c1",
    "owner": "myself",
    "metadata": {
        "m1": {
            "value": "m1_1",
            "timestamp": "d1"
        },
        "m2": {
            "value": "m1_2",
            "timestamp": "d2"
        },
        "m3": {
            "value": "m1_3",
            "timestamp": "d3"
        },
        "m4": {
            "value": "m1_4",
            "timestamp": "d4"
        }
    },
    "a1": {
        "a11": [

        ]
    },
    "m1": {},
    "comm1": "COMM1",
    "comm2": "COMM21529089656387",
    "share": "xxx",
    "share1": "yyy",
    "hub1": "h1",
    "hub2": "h2",
    "context": [{'f':[1,2,3,[4,5]]}

    ]
}

def flatten_list(List):
    L = []
    for val in List:
        if isinstance(val, list):
            output = flatten_list(val)
            for x in output:
                L.append(x)              
        else:
            L.append(val)
    return L

def flatten_dict(Dict, sep=''):
    Final = {}

    for k,v in Dict.items():
        key = sep+k 
        if isinstance(v,dict):
            output = flatten_dict(v, key + '.')
            if output == {}:
                Final[key]={}
            else:
                Final.update(output)

        elif isinstance(v,list):
            v = flatten_list(v)
            l = len(v)
            count = 0
            for x in v:
                if type(x)==dict:
                    count +=1
            if count == 0:                
                Final[key]=v
                
            for i in v:                               
                if isinstance(i, dict):                   
                    Final.update(flatten_dict(i,key+'.'))
        else:
            Final[key]=v
    return Final             

d3 = {
    "count": 1,
    "limit": 1,
    "offset": 0,
    "pages": [{'k':1, 'v':[1,2,3,[4,5,{},[6,{'f':2},[8]]]]}]
  }

d4 = {'f':[2], 'G':{'k':{'f':{'j':{'i':[1,2,3]}}}}}  

def flatten_dict_2(Dict, sep=''):
    Final = {}

    for k,v in Dict.items():
        key = sep+k 
        if isinstance(v,dict):
            output = flatten_dict(v, key + '.')
            if output == {}:
                Final[key]={}
            else:
                Final.update(output)
        elif isinstance(v,list):
            val = flatten_list(v)
            
            for x in val:
                if x == {}:
                    Final[key+'E']=x
                    val.remove(x)
                else:
                    if type(x)==dict:
                        
                        output = flatten_dict_2(x, key + '.')
                        
                        Final.update(output)
                        val.remove(x)
            Final[key]=val        
        else:
            Final[key]=v
    keys = []
    for k,v in Final.items():
        if v == []:
            keys.append(k)
    for x in keys:
        del Final[x]

    return Final

print(flatten_dict_2(d3))                         


