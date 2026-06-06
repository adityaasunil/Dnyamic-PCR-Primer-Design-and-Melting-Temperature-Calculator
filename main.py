import random

def sequence_generator(desired_length: int) -> str:

    if desired_length == 0:
        raise ValueError("The length of the sequence can't be 0bp.")

    nucleotides = ['c', 'g', 'a', 't']
    seq = ''
    for i in range(desired_length):
        seq += nucleotides[random.randint(0, len(nucleotides)-1)]
    return seq.upper()

class Agent:
    def __init__(self,use_sequence_generator:bool, desired_primer_length:int, seq_length=0, sequence = ''):

        self.use_generator = use_sequence_generator

        if self.use_generator == True:
            self.seq = sequence_generator(seq_length)
        else:
            self.seq = sequence

        self.length = desired_primer_length
    
    def __str__(self):
        return f'The DNA sequence is: 5\'-{self.seq}-\'3\nThe desired primer length: {round(self.length/1000, 1)}kb'
    
if __name__ == '__main__':
    ob = Agent(True, 1500, 3000)
    print(ob)