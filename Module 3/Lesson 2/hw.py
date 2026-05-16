def shut(running, backup, save):
    if (running and backup and save)=="yes":
        print("Shutting down")
    elif (running and backup and save)=="no":
        print("Abort shut down")
    else:
        print("Sorry")

running=input("Is the program running (yes/no)):").lower()
backup=input("Has a backup of the program been made (yes/no):").lower()
save=input("Have unsaved changes been saved (yes/no):").lower()
shut(running,backup,save)
