import time

def time_maker():
    last_time = None 
    
    def elsped():
        nonlocal last_time
        now = time.time
        
        if last_time is None:
            last_time = now
            return None 
        
        result = now - last_time
        last_time = now 
        return result
    return elsped


