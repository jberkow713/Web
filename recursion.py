

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
        key = sep+str(k) 
        if isinstance(v,dict):
            if len(v)>0:                
                Final.update(flatten_dict(v, key + '.'))
            else:                
                Final[key]={}                
        if isinstance(v,list):
            new = list(enumerate(flatten_list(v)))
            for idx, val in new:
                k = key + '.' + str(idx)
                if type(val)!=dict:
                    Final[k]=val
                if type(val)==dict:
                    if len(val)>0:
                        output = flatten_dict(val, k + '.')
                        Final.update(output)                        
                    else:
                        Final[k]={}
        elif type(v)==int or type(v)==str or type(v)==tuple:
            Final[key]=v 

    return Final
# 'L':[4,5,{}]
d5 = {'k': {}, 'j':2, 'f':{1:{}}, 'L':[4,5,{'f':3, 'h':{'h':[4,3,4,5]}},(3,4)]}
print(flatten_dict(d5))
