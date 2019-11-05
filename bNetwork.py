import frames as fr

f = open("car.data", "r")
data = f.readlines()
data_frames = []
for x in data:
  temp = fr.frame(x.split(",")[0],x.split(",")[1],x.split(",")[2],x.split(",")[3],
    x.split(",")[4],x.split(",")[5],x.split(",")[6].rstrip("\n"))
  data_frames.append(temp)

print(fr.get_probs(fr.get_safety, fr.get_val, data_frames))

