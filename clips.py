"""
This Program collects the amount of little clips by a videographer
save each individual running total for each clip, save them in an array and prints 
and save the total running total of all clips in a file
"""
#creat the mail function
def main():
    #get the number of video clips from the user
    total_clips = int(input("Enter the total number of clips: "))
    #create a file and save it to a varible
    clips = open("video_clips.doc",'w')
    #create variables and dict
    run_time = {}
    running_total = 0
    #loop to sum up the total running time
    for i in range(total_clips):
        print("Enter the running total for #",i+1, " video clip")
        runing_time = float(input())
        run_time['#'+str(i+1) + ' Video'] = str(runing_time) + " second(s)"
        running_total += runing_time
    clips.write("The total runing time for " + str(total_clips) + " Video(s) is " + str(running_total) + " second(s)")
    print(run_time)
    clips.close()
    

    print("The total clips running time have been saved in the file video_clips.doc")



main()