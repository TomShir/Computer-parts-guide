#Creating ascii animation in Python 
import os 
import time 
import sys 
from colorama import Fore 
import random
import tqdm
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.CYAN,Fore.RESET,]
count=0
computer_parts_names=['PC','Monitor','GPU','CPU','RAM']
def fg(r,g,b):
   return f'\033[38;2;{r};{g};{b}m'
   
fg_orange = fg(255,168,5)
fg_purple = fg(151,71,255)
fg_silver = fg(0,0,10)
#Appending the colors of orange,purple and sliver to the end of the colors list 
colors.extend([fg_orange,fg_purple,fg_silver])
computer_parts=[f'''
           __________
          |\\         \\
          | \\         \\
          |  \\         \\
          |   \\         \\
          |    \\_________\\
          |    |__________|
          |    |__________|
          |    |__________|
          |    |    ___   |
          |    |   |   |  |
          \    |   |___|  |
           \   |   -----  |
            \  |   -----  |
             \ |   -----  |
              \|__________|
       {computer_parts_names[0]}''',f'''
              
             
      ________ ________________________                
     /        \ _____________________  |
     |        | |                    | |
     |  ----- | |                    | |
     |  ----- | |                    | |
     |  ----- | |                    | |
     |        | |____________________| |
     |        |        DELL            |
     |________|________________________|
                   |  |   |
                   |  |   |
                   |  |   |
                   |  |   |
             ______|__|___|_____   
            |_ _________________|
            |_|_________________|
        {computer_parts_names[1]}
        ''',f'''
        _________
       |______   |  ___________________________
              |  | |                           |
          ____|  | |    ......       ......    |
         |____|  | | ..       ..   ..      ..  |
           ___|  | | ..       ..   ..      ..  |
          |   |  | |    ......       ......    |
          |   |  | |                           |
          |___|  | |                           |
          ____|  | |                           |
         |____|  | |___________________________|
              |  |        ___________________
              |__|        |_|_|_|_|_|_|_|_|_|
                          | | | | | | | | | |
        
        {computer_parts_names[2]}
                    ''',
                        f'''
                              _________________________
                            /\\      _____________     \\
                           /\ \\     \            \     \\
                            /\ \\     \ {"intel core".upper()} \     \\ 
                             /\ \\     \            \     \\
                              /\ \\     \ ___________\     \\
                               /\ \\________________________\\
                                /\/_________________________/
                                 / / / / / / / / / / / / / / 
                                 
                                {computer_parts_names[-2]}''',
                            
                        f''' 
                           
                             ____   ________  
                           /\\    \\__\\      \\
                          /   \\ \ \ \ \ \ \ \  \\
                          \    \\ \ \ \ \ \ \ \  \\ 
                           \    \\  ____________  \\ 
                            \    \\ \            \ \\ 
                             \    \\ \____________\ \\
                              \    \\  _____________ \\ 
                               \    \\ \            \ \\
                                \    \\ \____________\ \\ 
                                 \    \\  ____________  \\ 
                                  \    \\ \           \  \\ 
                                   \    \\ \___________\  \\
                                    \    \\  ___________   \\
                                     \    \\ \           \  \\
                                      \    \\ \___________\  \\ 
                                       \    \\                \\  
                                        \    \\     _______    \\
                                         \    \\   \\       \\    \\
                                          \___ \\___\\       \\____\\
                                              
                                       {computer_parts_names[-1]}     ''']
computer_part_information=['''A personal computer, often referred to as a PC, is a computer designed for individual use.\n It is typically used for tasks such as word processing, internet browsing, email, multimedia playback, and gaming.\n Personal computers are intended to be operated directly by an end user\n, rather than by a computer expert or technician.\n Unlike large, costly minicomputers and mainframes, time-sharing by many people at the same time is not used with personal computers.\n Primarily in the late 1970s and 1980s, the term home computer was also used. The advent of personal computers and the concurrent Digital Revolution have significantly affected the lives of people in all countries.''','''A computer monitor is an output device that displays information in pictorial or textual form. A discrete monitor comprises a visual display, support electronics, power supply, housing, electrical connectors, and external user controls.The display in modern monitors is typically an LCD with LED backlight, having by the 2010s replaced CCFL backlit LCDs. Before the mid-2000s, most monitors used a cathode-ray tube (CRT) as the image output technology. A monitor is typically connected to its host computer via DisplayPort, HDMI, USB-C, DVI, or VGA. Less commonly, monitors sometimes use other proprietary connectors and signals to connect to a computer.''','''The GPU is a processing unit in the computer that is designed for parallel processing. It is utilised in graphics and video rendering.However it noticed for its use in gaming.The original purpose of the GPU is was to speed 
up the process of 3d rendering graphics.As time progressed,it became more flexible,meaning it could be 
Programmed and modified based on the user\'s wish.This proved to be a boon as it allowed graphics programmers to create realistic graphics and visual effects.
''','''CPU is an acronym or an abbreviation for 
Central Processing Unit.It acts as the brains of the computer.The cpu is made up of three 
Components,control unit,arithmetic and logic unit and immediate access store.
The control unit component of the CPU is used 
to control the flow of data within the system.''','''The purpose of RAM(Random Access Memory) in a computer system is 
To:
 Read files 
Load software applications 
Ensure system stability 
Allow applications to access and temporarily store information 
Store data that helps your computer perform vital tasks,such as loading apps,browsing websites and editing documents 
Allow the CPU to retrieve data quickly no matter where its physical 
''']
def generate_options(number_of_options,option1,option2,option3,option4,option5,option6,option7,option8,option9):
     for num in range(1,number_of_options+1,1):
        if num==1:
           print(colors[0])
           print(f'{num}:{option1}')
           time.sleep(1)
           loop_over(f'\n\t{computer_part_information[0]}',delay_time=0.01,color=colors[-3])
        elif num==2:
           print(f'{colors[1]}')
           print(f'{num}:{option2}')
           time.sleep(1)
           loop_over(f'\n\t{computer_part_information[1]}',delay_time=0.01,color=colors[-2])
        elif num==3:
           print(f'{colors[2]}')
           print(f'{num}:{option3}')
           time.sleep(1)
           loop_over(f'\n\t{computer_part_information[2]}',delay_time=0.01,color=colors[-1])
        elif num==4:
           print(f'{colors[3]}')
           print(f'{num}:{option4}')
           time.sleep(1)
           loop_over(f'\n\t{computer_part_information[3]}',delay_time=0.01,color=colors[4])
        elif num==5:
           print(f'{Fore.BLACK}')
           print(f'{num}:{option5}')
           time.sleep(1)
           loop_over(f'\n\t{computer_part_information[-1]}',delay_time=0.01,color=Fore.YELLOW)
        elif num==6:
           print(f'{colors[5]}')
           print(f'{num}:{option6}')
           time.sleep(1)
        elif num==7:
           print(f'{colors[6]}')
           print(f'{num}:{option7}')
           time.sleep(1)
        elif num==8:
           print(f'{colors[7]}')
           print(f'{num}:{option8}')
           time.sleep(1)
        elif num==9:
           print(f'{colors[8]}')
           print(f'{num}:{option9}')
     else:
        print(f'{colors[4]}')
#Creating a function that takes a subscriptable sequence  and prints it out horizontially
def loop_over(sequence,delay_time,color):
    for text in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{color}{text}')
    else:
        print(f'{colors[4]}')       
for num in tqdm.tqdm(list(range(1,101,1)),ncols=200,desc='Loading computer parts...',colour='GREEN'):
    time.sleep(0.02)
else:
#Clears the all the text the output stream is showing  once the for loop terminates naturally(on its own)
 time.sleep(1)
 os.system('cls') 
 time.sleep(1)
 loop_over(sequence='Computer parts:',delay_time=0.1,color=colors[1])
 time.sleep(1)
 generate_options(number_of_options=5,option1=computer_parts[0],option2=computer_parts[1],option3=computer_parts[2],option4=computer_parts[3],option5=computer_parts[4],option6=None,option7=None,option8=None,option9=None)