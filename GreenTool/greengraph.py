#!/usr/bin/env python
from argparse import ArgumentParser
from green import Green

def process():
		parser = ArgumentParser()

		parser.add_argument('start')
		parser.add_argument('end')
		parser.add_argument('steps',type=int)
   
		arguments= parser.parse_args()
		graph=Green(arguments.start, arguments.end, arguments.steps)
		
if __name__ == "__main__":
     process()