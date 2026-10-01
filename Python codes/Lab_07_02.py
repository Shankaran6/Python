# import os 
# os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
# import matplotlib.pyplot as plt


# MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()
# ################################################################################
# # Please do not edit anything above this line.


# # Function to read a file and return speed list.
# def get_speed(file_name):
#     speed = []
    

# ################## YOUR CODE STARTS HERE. ######################################
# # Read the file and get the values into the list.
#     with open (file_name) as file:
#         for line in file:
#             time,speed_val=map(float,line.split())
#             speed.append(speed_val)
    
    
    
# ################## YOUR CODE ENDS HERE. ########################################     
#     return speed


# # Function gets the filename and returns the speeds in metres per second format.
# def convert_kmph_to_ms(filename):
# ################## YOUR CODE STARTS HERE. ######################################
# # Read the values using get_speed function and return the converted values as a list.
#     M_S=[]
#     speed=get_speed(filename)
#     for speed_val in speed:
#        m_s=round(speed_val*(5/18),2)
#        M_S.append(m_s)
#     return M_S
   
# ################## YOUR CODE ENDS HERE. ########################################


# # Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
# def get_acceleration(speeds):
#     #Acceleration list is initialized to zero.
#     #i.e. acceleration at time=0 is zero.
#     acceleration = [0]
# ################## YOUR CODE STARTS HERE. ######################################
#     #Write the code to calculate the acceleration. 
#     for i in range(len(speeds)-1):
#         ins_acceleration=(speeds[i+1]-speeds[i])/0.1
#         acceleration.append(ins_acceleration)
    
    
    
# ################## YOUR CODE ENDS HERE. ########################################
#     return acceleration


# ######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

#         # Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable 
#         # names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
        
# # Plotting the lines with different styles
# # plt.plot(time, model_acceleration[0] , label='model_1')      
        
# # Adding labels and title

# Time=[0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
# Acceleration_01=get_acceleration(convert_kmph_to_ms(MODEL_1_INPUT_FILE))
# Acceleration_02=get_acceleration(convert_kmph_to_ms(MODEL_2_INPUT_FILE))
# Acceleration_03=get_acceleration(convert_kmph_to_ms(MODEL_3_INPUT_FILE))


# Accelerations=[Acceleration_01,Acceleration_02,Acceleration_03]

# plt.plot(Time,Accelerations[0])
# plt.plot(Time,Accelerations[1])
# plt.plot(Time,Accelerations[2])
# plt.xlabel('Time(s)')
# plt.ylabel('Acceleration(ms-2)')
# plt.title('Acceleration Vs Time')
# plt.show()

# ################################################################################
# # Please do not edit anything below this line.


# ##################### End of the programme #####################################


# # Lab_07_model_1.txt Lab_07_model_2.txt Lab_07_model_3.txt








import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt


MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()
################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################
# Read the file and get the values into the list.
    with open(file_name) as file:
        for line in file:
            time,speed_val=line.strip().split()
            speed.append(float(speed_val))
    
    
################## YOUR CODE ENDS HERE. ########################################     
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
    M_S=[]
    speed=get_speed(filename)
    for speed_val in speed:
        m_s=round(speed_val*(5/18),2)
        M_S.append(m_s)
    return M_S
   
   
   
################## YOUR CODE ENDS HERE. ########################################


# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    #Acceleration list is initialized to zero.
    #i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    #Write the code to calculate the acceleration.    
    for i in range(len(speeds)-1):
        ins_acceleration=(speeds[i+1]-speeds[i])
        acceleration.append(ins_acceleration)
    
    
################## YOUR CODE ENDS HERE. ########################################
    return acceleration


######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

        # Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable 
        # names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
        
# Plotting the lines with different styles
# plt.plot(time, model_acceleration[0] , label='model_1')      

Time=[0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

acceleration_1=get_acceleration(convert_kmph_to_ms(MODEL_1_INPUT_FILE))
acceleration_2=get_acceleration(convert_kmph_to_ms(MODEL_2_INPUT_FILE))
acceleration_3=get_acceleration(convert_kmph_to_ms(MODEL_3_INPUT_FILE))

Accelerations=[acceleration_1,acceleration_2,acceleration_3]

plt.plot(Time,Accelerations[0])
plt.plot(Time,Accelerations[1])
plt.plot(Time,Accelerations[2])


# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.show()

################################################################################
# Please do not edit anything below this line.


##################### End of the programme #####################################