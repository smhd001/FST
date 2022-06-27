class FST():
    trans = []
    sts = []
    def add_state(self,state_name : str, is_final : bool ):
        self.sts.append(state(state_name,is_final))
    def add_transition(self,in_state_name : str ,input : chr,output : chr,out_stat_name : str):
        if in_state_name in self.sts and out_stat_name in self.sts:
            self.trans.append(transition(in_state_name,input,output,out_stat_name))
    def print_tarn():
        for t in trans:
            print(t)

        

class state():
    name = ""
    is_final = False
    def __init__(self,name : str,is_final : bool) -> None:
        self.name = name 
        self.is_final = is_final
    def __eq__(self, __o: object) -> bool:
        if __o == self.name:
            return True
        if isinstance(__o,state):
            if __o.name == self.name:
                return True
        return False 
class transition():
    in_state_name = ""
    input = ""
    output = ""
    out_stat_name = ""
    def __init__(self,in_state_name:str,input:chr, output : chr,out_stat_name:str) -> None:
         self.in_state_name = in_state_name
         self.input = input 
         self.output = output
         self.out_stat_name = out_stat_name
