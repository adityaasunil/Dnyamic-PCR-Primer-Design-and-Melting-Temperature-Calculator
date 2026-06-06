import random
import textwrap
from rich.table import Table
from rich.console import Console
import argparse

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

        self.primer_length = desired_primer_length
    
    def primer_list(self) -> tuple[list[str], int, list[str], int]:
        self.forward_primer_list = []
        self.reverse_primer_list = []
        l = len(self.seq)
        n = self.primer_length
        i,j = 0
        while (i+n) <= l:
            self.forward_primer_list.append(self.seq[i:i+n])
            i+=1

        while (j+n) <= l:
            complimentary_nucleotides = str.maketrans('cgat', 'gcta')
            if i == 0:
                window = self.seq[-n: ]
            else:
                window = self.seq[-(i+n):-i]
            rev_complement = window.translate(complimentary_nucleotides)[::-1]
            self.reverse_primer_list.append(rev_complement)
            j+=1
        
        return self.forward_primer_list, len(self.forward_primer_list), self.reverse_primer_list, len(self.reverse_primer_list)
    
    def info(self):
        table = Table(title=':bulb: INFO BOX')

        _, f_len, _, r_len = self.primer_list()

        table.add_column("SI No.", justify='left', style='cyan', no_wrap=True)
        table.add_column("Data", justify='center', style='magenta')
        table.add_column("Sequence Generated?", justify='center')
        table.add_column("Sizes", justify='center', style='green')

        seq_len = lambda x: f'{round(x/1000, 1)}kb' if x > 1000 else f'{x}bp'

        table.add_row("1. ", ":dna: DNA sequence", "✅", str(seq_len(len(self.seq))))
        table.add_row("2. ", "Desired primer", "❌", str(self.primer_length)+'bp')
        table.add_row("3. ", "Forward Primer candidates", "✅", str(f_len)+' nos' )
        table.add_row("4. ", "Reverse Primer candidates", "✅", str(r_len)+' nos')

        console = Console()
        return console.print(table)

 
if __name__ == '__main__':
    ob = Agent(True, 30, 20000)
    
    parser = argparse.ArgumentParser(description='Have fun doing cool stuff!!')
    parser.add_argument('-i', '--info', action='store_true')
    args = parser.parse_args()

    if args.info:
        ob.info()

