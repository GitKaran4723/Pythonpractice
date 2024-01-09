import statistics

def swim_data(filename):
    fn = filename
    swimmer,age,distance,stroke = fn.split(".")[0].split("-")
    with open("swimdata/"+fn,"r") as data:
        data1 = data.readlines()
    times = data1[0].removesuffix('\n').split(",")
    alltimes = []
    for t in times:
        if ":" in t:
            minute,rest = t.split(":")
        else:
            rest = t
            minute = 0
        seconds, hundreds = rest.split(".")
        convertedTime = (int(minute)*60*100) + (int(seconds)*100) + (int(hundreds))
        alltimes.append(convertedTime)
    avg = statistics.mean(alltimes)
    min_sec, hundredth = str(round(avg/100,2)).split(".")
    min_sec = int(min_sec)
    minute = min_sec//60
    seconds = min_sec - minute*60
    average = str(minute)+":"+str(seconds)+"."+hundredth
    return swimmer, age, distance, stroke, times, average, alltimes
    

