# Program to determine f(n) for fibonacci given an n
# I know why/how this is working.  I'm sure there is a better way, but I want to get this committed in time.

def fibonacci(n):

    fseq = [0, 1]
    for nums in range(n+1):
        if (n == 0):
            return 0
        elif (n == 1):
            return fseq
        elif (nums > 1):
            next_to_add = fseq[nums-1] + fseq[nums-2]
            fseq.append(next_to_add)
    return fseq
    

print("0 and 1 are the first 2 values of the Fibonacci Sequence")
num_to_pass = input("Enter a sequence number 2 or greter to see its value: ")

build_sequence = fibonacci(int(num_to_pass))
print(build_sequence)
fofn = build_sequence.pop(-1)
print(fofn)

    
