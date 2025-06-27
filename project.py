HISTORY = "history.txt"#importing history file
#for calling show history 
def show_history():
    try:
        with open(HISTORY,'r') as file:
            lines=file.readlines()
            if not lines:
                print("NO HISTORY")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("NO HISTORY")

def clear():
    with open(HISTORY,'w') as file:
        pass
    print("HISTORY CLEARED")
    
def save(eq,res):
    with open(HISTORY,'a') as file:
        file.write(eq + "=" + str(res) + "\n")
    
    
def calc(uinput):
    try:
        res=eval(uinput)
        print("RESULT:",res)
        save(uinput,res)
    except Exception as e:
        print("ERROR:", e)
    
def main():
    print('---SIMPLE CALCULATOR---')
    while True:
        uinput=input("Enter calculation or command---history, clear, exit \n").strip()
        if uinput=="exit":
            break
        elif uinput=="history":
            show_history()
        elif uinput=="clear":
            clear()
        else:
            calc(uinput)
            
main()
                     
        
    
       
