class frame:

    def __init__(self, buying, maint, doors, persons, lug_boot, safety, val):
        self.val = val
        self.buying = buying
        self.maint = maint
        self.doors = doors
        self.persons = persons
        self.lug_boot = lug_boot
        self.safety = safety

    def print_frame(self):
      print(self.val, self.buying, self.maint, self.doors, self.persons, self.lug_boot,
        self.safety)

    def get_val(self):
      if(self.val == "unacc"): return 0
      else: return 1

    def get_buy(self):
      if(self.buying == "low"): return 0
      else: return 1

    def get_maint(self):
      if(self.maint == "low"): return 0
      else: return 1

    def get_door(self):
      if(self.doors == "2"): return 0
      else: return 1

    def get_person(self):
      if(self.persons == "2"): return 0
      else: return 1

    def get_boot(self):
      if(self.lug_boot == "small"): return 0
      else: return 1

    def get_safety(self):
      if(self.safety == "low"): return 0
      else: return 1

def get_probs(func1, func2, data_frames):
  probs = [0,0,0,0]
  for x in data_frames:
    if(func1(x) == 0 and func2(x) == 0): probs[0] += 1
    elif(func1(x) == 1 and func2(x) == 0): probs[1] += 1
    elif(func1(x) == 0 and func2(x) == 1): probs[2] += 1
    elif(func1(x) == 1 and func2(x) == 1): probs[3] += 1
  for x in range(len(probs)):
    probs[x] = probs[x]/len(data_frames)
  return probs

def get_val(frame):
  return frame.get_val()

def get_buy(frame):
  return frame.get_buy()

def get_maint(frame):
  return frame.get_maint()
    
def get_door(frame):
  return frame.get_door()

def get_person(frame):
  return frame.get_person()

def get_boot(frame):
  return frame.get_boot()
    
def get_safety(frame):
  return frame.get_safety()








