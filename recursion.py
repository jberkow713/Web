

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

d5 = {'k': {}, 'j':2, 'f':{1:{}}, 'L':[4,5,[4,3,4,5,{}],(3,4)]}

def flatten(D, sep='', div='.'):
    Final = {}
    
    if D == {}:        
        return {sep:D}         
    
    for k,v in D.items():
        key = sep + str(k) 
        if isinstance(v,dict):            
            Final.update(flatten(v,key + div))
                                         
        if isinstance(v,list):
            if v == []:
                Final[key]=v

            full = list(enumerate(flatten_list(v)))
            for idx,val in full:
                k = key + div + str(idx) 
                if not isinstance(val,dict):                    
                    Final[k]=val                  
                if isinstance(val,dict):                   
                    Final.update(flatten(val, k+div))                     

        elif type(v)!=list and type(v)!=dict:
            Final[key]=v        
    return Final                               

print(flatten({'k':[1,2,[3,4,[5,{'j':{'h':[1,2,3,{'f':[]}]}},6]]], 3:{}}))



