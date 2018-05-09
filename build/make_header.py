# generates a single header from all header files

header_files = [
    # Core
    "Node.h",
	"Composite.h",
    "Decorator.h",
    "Blackboard.h",
    "Leaf.h",
    "BehaviorTree.h",
	"Builder.h",
    # Composites
    "Composites/Selector.h",
    "Composites/Sequence.h",
	"Composites/StatefulSelector.h",
    "Composites/StatefulSequence.h",
	"Composites/ParallelSequence.h",
    # Decorators
	"Decorators/Succeeder.h",
    "Decorators/Failer.h",
    "Decorators/Inverter.h",
    "Decorators/Repeater.h",
	"Decorators/UntilSuccess.h",
    "Decorators/UntilFailure.h"
]

def process_file(path):
    lines = []
    start = 0
    end = 1
    with open(path, "r") as infile:
        for line in infile:
            if start:
                lines.append(line)
            elif '{' in line.rstrip():
                start = 1
		for line in reversed(lines):
			if end:
				lines.pop()
            elif '}' in line.rstrip():
				lines.pop()
				end = 0
	lines.pop()
    return lines

def process_files(files):
    data = []
    for file in files:
        data.extend(process_file("src/" + file))
    data = data[:-1]
    return "".join(data)

def generate_single_header(header_source):
    with open("build/template_header.h", "r") as infile, open("BrainTree.h", "w") as outfile:
        data = infile.read().replace("/*INTERFACE*/\n", header_source)
        outfile.write(data)

def generate():
    generate_single_header(process_files(header_files))
    
if __name__ == '__main__':
    generate()