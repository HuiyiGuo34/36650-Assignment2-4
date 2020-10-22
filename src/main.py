from src.Reader import CountiesDataSetReader
from src.Reader import StateDataSetReader
from src.Reader import UsDataSetReader

from src.Function import UsDataFunction
from src.Function import StateDataFunction
from src.Function import CountiesDataFunction

def run():
    while(True):
        cmd = input("please select one dataset：country, all states, all counties: ")

        if (cmd == 'country'):
            print(CountiesDataSetReader())
            while (True):
                cmd1 = input("please input state name; input quit to skip：\n")
                print(CountiesDataFunction(cmd1))
                if (cmd1 == "quit"):
                    break

        elif( cmd == 'all states'):
            print(StateDataSetReader())
            cmd2 = input("input y to display the death percentage; otherwise skip：\n")
            if(cmd2 == "y"):
                print(StateDataFunction())
            else:
                continue

        elif(cmd =="all counties"):
            cmd1 = input("To only display deaths and cases column? Please input y/n:\n")
            if (cmd1 == "y"):
                print(UsDataFunction())
            elif(cmd1 == "n"):
                print(UsDataSetReader())
            else:
                print("input error!")
                continue

        elif(cmd =="quit"):
            print("Bye ~")
            break
        else:
            print("invalid input")

if __name__ == '__main__':
    run()