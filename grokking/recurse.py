empty = []

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box():
            if item.is_a_box():
                pile.append(item)
                
            elif item.is_a_key():
                print("found the key! ")
        


def look_for_box(box):
    for item in box:
        if item.as_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key ")



def countdown(i):
  print(i)
  if i <= 1:        
    return
  else:             
    countdown(i-1)
        
countdown(3)

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye! ")

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()














