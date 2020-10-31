from .models import Branch
def create_branch(branch_name):
    if not Branch.query.filter_by(name=branch_name).first():
        branch=Branch(name=branch_name)
        return branch
    return None

def create_branch_array():
    branch_names=['CSE','ME','CE','MEMS','EE']
    branch_array = [Branch(name=branch_name)
                    for branch_name in branch_names if not Branch.query.filter_by(name=branch_name).first()]
    return branch_array