class Agent:
    def __init__(self, sequence: str):
        self.seq = sequence.upper()
    
    def __str__(self):
        return f'The DNA sequence is: {self.seq}'
    
if __name__ == '__main__':
    ob = Agent('cgagcgct')
    print(ob)