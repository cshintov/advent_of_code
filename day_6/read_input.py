from pdb import set_trace

def make_para(lines):
    para = []
    for line in lines:
        if not line:
            yield para
            para = []
        else:
            para.append(line)


def get_answers(input_file):
    return make_para(line.strip() for line in open(input_file))
