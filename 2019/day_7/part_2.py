import itertools

with open('2019/day_7/input.txt', 'r') as input_file:
    program = input_file.read().split(',')
    program = list(map(int, program))
    # print(program)

class Amplifier:
    def __init__(self):
        self.phase_setting = -1
        self.input_signal = -1
        self.phase_setting_provided = False
        self.memory = program[:]
        self.pointer = 0
    
    def run(self):
        while True:
            operation = str(self.memory[self.pointer])
            # print(operation)

            while len(operation) < 5:
                operation = '0' + operation
            opcode = int(operation[3:])
            parameter_1_mode = int(operation[2])
            parameter_2_mode = int(operation[1])
            parameter_3_mode = int(operation[0])
            # print(self.memory)
            
            if opcode == 1: # Addition
                parameter_1 = self.memory[self.pointer + 1]
                parameter_2 = self.memory[self.pointer + 2]
                parameter_3 = self.memory[self.pointer + 3]
                
                argument_1 = parameter_1 if parameter_1_mode else self.memory[parameter_1]
                argument_2 = parameter_2 if parameter_2_mode else self.memory[parameter_2]
                
                self.memory[parameter_3] = argument_1 + argument_2
                
                self.pointer += 4
                
            elif opcode == 2: # Multiplication
                parameter_1 = self.memory[self.pointer + 1]
                parameter_2 = self.memory[self.pointer + 2]
                parameter_3 = self.memory[self.pointer + 3]
                
                argument_1 = parameter_1 if parameter_1_mode else self.memory[parameter_1]
                argument_2 = parameter_2 if parameter_2_mode else self.memory[parameter_2]
                
                self.memory[parameter_3] = argument_1 * argument_2
                
                self.pointer += 4
                
            elif opcode == 3: # Input
                parameter_1 = self.memory[self.pointer + 1]
                
                self.memory[parameter_1] = self.input_signal if self.phase_setting_provided else self.phase_setting
                self.phase_setting_provided = True
                
                self.pointer += 2

            elif opcode == 4: # Output
                parameter_1 = self.memory[self.pointer + 1]
                
                argument_1 = parameter_1 if parameter_1_mode else self.memory[parameter_1]
                
                self.pointer += 2
                
                return argument_1

            elif opcode == 5: # Jump if true
                parameter_1 = self.memory[self.pointer + 1]
                parameter_2 = self.memory[self.pointer + 2]
                
                argument_1 = parameter_1 if parameter_1_mode else self.memory[parameter_1]
                argument_2 = parameter_2 if parameter_2_mode else self.memory[parameter_2]
                
                if argument_1 != 0:
                    self.pointer = argument_2
                else:
                    self.pointer += 3

            elif opcode == 6: # Jump if false
                parameter_1 = self.memory[self.pointer + 1]
                parameter_2 = self.memory[self.pointer + 2]
                
                argument_1 = parameter_1 if parameter_1_mode else self.memory[parameter_1]
                argument_2 = parameter_2 if parameter_2_mode else self.memory[parameter_2]
                
                if argument_1 == 0:
                    self.pointer = argument_2
                else:
                    self.pointer += 3

            elif opcode == 7: # Less than
                parameter_1 = self.memory[self.pointer + 1]
                parameter_2 = self.memory[self.pointer + 2]
                parameter_3 = self.memory[self.pointer + 3]
                
                argument_1 = parameter_1 if parameter_1_mode else self.memory[parameter_1]
                argument_2 = parameter_2 if parameter_2_mode else self.memory[parameter_2]
                
                if argument_1 < argument_2:
                    self.memory[parameter_3] = 1
                else:
                    self.memory[parameter_3] = 0
                
                self.pointer += 4

            elif opcode == 8: # Equals
                parameter_1 = self.memory[self.pointer + 1]
                parameter_2 = self.memory[self.pointer + 2]
                parameter_3 = self.memory[self.pointer + 3]
                
                argument_1 = parameter_1 if parameter_1_mode else self.memory[parameter_1]
                argument_2 = parameter_2 if parameter_2_mode else self.memory[parameter_2]
                
                if argument_1 == argument_2:
                    self.memory[parameter_3] = 1
                else:
                    self.memory[parameter_3] = 0
                
                self.pointer += 4
                
            elif opcode == 99: # Exit
                return -1
                
            else: # Invalid opcode
                raise Exception(f'Encountered invalid opcode {opcode} at {self.pointer}!')

signals = []
for phase_setting in itertools.permutations(range(5, 10)):
    
    amplifiers = [Amplifier() for _ in range(5)]
    for j, amplifier in enumerate(amplifiers):
        amplifier.phase_setting = phase_setting[j]
        
    outputs = [0]
    i = 0
    while outputs[-1] != -1:
        amplifiers[i % 5].input_signal = outputs[-1]
        outputs.append(amplifiers[i % 5].run())
        i += 1
    
    signals.append(outputs[-2])

print(max(signals))
