events = {}

def register_event(event, func):
    handlers = events.get(event)

    if handlers==None:
        events[event]=[func]
    else:
        handlers.append(func)       

def dispatch(event,data):
    handlers = events.get(event)
    
    if event is None:
        print(f'event {event} was not found')
    else:
        for func in handlers:
            func(*data)    
    


