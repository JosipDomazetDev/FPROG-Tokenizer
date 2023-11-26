with open('./res/output.txt', 'r') as file:
    output = file.read()

with open('./res/myoutput.txt', 'r') as file:
    myoutput = file.read()

output_lines = output.splitlines()
myoutput_lines = myoutput.splitlines()
matches = 0

for i in range(len(output_lines)):
    if output_lines[i] == myoutput_lines[i]:
        matches += 1

print(f"Matches: {matches}/{len(output_lines)} ({matches/len(output_lines)*100}%)")