# A network transmitter is transmitting a signal from tower A to tower B. The signal which was received by  transmitter B contains some distortions. The received signal N is in the form of a binary sequence consisting of 0s and 15 in a random order. The distortion in a signal is a subsequence of 01 of length two where the first character is 0 and the second character is always 1. Before using the signal, the transmitter must clean the signal by removing the distortions. To clean the signal the transmitter uses an iterative process comprising two filters. Each filter removes a single distortion from N. In each iteration, first filter 1 removes the distortion and then filter 2 removes the distortion. To limit the iterations, once both the filters complete their tasks. then that iteration is marked completed and the next iteration begins. If either of the filters are unable to complete their task, then that iteration will be marked as incomplete and the cleaning process ends. The process is designed so that the first filter tries to maximise the number of iterations and the second filter tries to minimise the number of iterations. The process stores the number of completed iterations if both the filters operate optimally.

# Write an algorithm for the transmitter to identify the total number of completed iterations.

# Removal of the substring twice from the given string

X = "01010"
N = list(X)
flag = True
count = 0

def filter1(N):
    for i in range(len(N) - 1):
        if N[i] == '0' and N[i + 1] == '1':
            del N[i:i + 2]  
            return True
    return False

def filter2(N):
    for i in range(len(N) - 1, 0, -1):
        if N[i - 1] == '0' and N[i] == '1':
            del N[i - 1:i + 1]  
            return True
    return False

def iteration(N): 
    global flag,count 
    while flag:
        if filter1(N) and filter2(N):
            count += 1
        else:
            flag = False
    return count

print("Number of iterations:", iteration(N))


