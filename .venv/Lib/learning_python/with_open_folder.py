import statistics
FN ="Darius-13-100m-Fly.txt"
FOLDER ="swimdata/"
swimmer, age, distance, stroke = FN.removesuffix('.txt').split('-')
with open(FOLDER+FN) as file:
    lines = file.readlines()
times = lines[0].strip('\n').split(',')
# print(times[0])
# print(type(times[0]))
# first = times[0]
# minutes, rest = first.split(':')
# print(minutes,rest)
# seconds, hundredths = rest.split('.')
# print(seconds, hundredths)
# converted_time = (int(minutes)*60*100)+(int(seconds)*100)+(int(hundredths))
# print(converted_time)
converts = []
for t in times:
    minutes, rest = t.split(':')
    seconds, hundredths = rest.split('.')
    converts.append((int(minutes)*60*100)+(int(seconds)*100)+int(hundredths))
average = statistics.mean(converts)
mintus_seconds, hundreds = str(round(average/100,2)).split('.')
minutes = int(mintus_seconds)//60
seconds = int(mintus_seconds) - minutes*60
average = str(minutes)+":"+str(seconds)+"."+str(hundreds)
print("Swimmer_Name: "+swimmer+"\n", "Age_Group: "+age+"\n", "Distance: "+distance+"\n", "Stroke_Type: "+stroke+"\n")
print("Times listed by stopwatch : "+str(times))
print("Average of the times is : "+average)

