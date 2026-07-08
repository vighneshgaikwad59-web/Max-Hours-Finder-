mera = [("Sonu", 300), ("abhi", 500), ("Ravi", 500)]  

def max_hours_worker(workers):
    max_hours = 0
    top_worker = ""
    for name, hrs in workers:
        if hrs > max_hours:
            max_hours = hrs
            top_worker = name
    return max_hours, top_worker

hours, name = max_hours_worker(mera)
print(f"{name} worked the most: {hours} hours")
