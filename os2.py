import keyboard

  
# It records all the keys until escape is pressed
rk = keyboard.record(until ='Esc')
  
# It replay back the all keys
f1=open("keylog.txt","w+")
for i in rk:
    f1.write((str(i).strip("KeyboardEvent(")))
f1.close()