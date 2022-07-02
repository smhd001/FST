class FST:
    sts = {}

    def add_state(self, state_name: str, is_final: bool) -> None:
        self.sts[state_name] = state(state_name, is_final)

    def add_transition(
        self, in_state_name: str, input: chr, output: chr, out_stat_name: str
    ) -> None:
        if in_state_name in self.sts and out_stat_name in self.sts:
            self.sts[in_state_name].trans.append(transition(input,output,out_stat_name))
        else:
            print("no such state name", in_state_name, out_stat_name)

    def add_set_transition(
        self, in_state_name: str, input_set: str, out_stat_name: str
    ) -> None:
        for inp in input_set:
            self.add_transition(in_state_name, inp, inp, out_stat_name)

    def __is_final(self, state_name: str) -> bool:
        for s in self.sts:
            if s == state_name:
                return self.sts[s].is_final
        return False

    def __landa_transition(self, to_p: list) -> list[str]:
        for tp in to_p:
            for t in self.sts[tp[1]].trans:
                if t.input == "" :
                    to_p.append((tp[0] + t.output, t.out_stat_name))
        return to_p

    def run(self, inp: str) -> None:
        to_p = [("", "q0")]  # list to pars
        p_out = []  # list for output
        for c in inp:
            for tp in to_p:
                for t in self.sts[tp[1]].trans:
                    if c == t.input:
                        p_out.append((tp[0] + t.output, t.out_stat_name))
            p_out = self.__landa_transition(p_out)
            to_p = p_out
            p_out = []
        res = [i[0] for i in to_p if self.__is_final(i[1])]
        if res:
            print(res)
        else:
            print("\033[91m" + "FAIL" + "\033[0m")


class state:
    def __init__(self, name: str, is_final: bool) -> None:
        self.trans = []
        self.is_final = False
        self.name = name
        self.is_final = is_final

    def __eq__(self, __o: object) -> bool:
        if __o == self.name:
            return True
        if isinstance(__o, state):
            if __o.name == self.name:
                return True
        return False


class transition:
    def __init__(self, input: chr, output: chr, out_stat_name: str) -> None:
        self.input = input
        self.output = output
        self.out_stat_name = out_stat_name

    def __str__(self) -> str:
        return (
            "->"
            + self.out_stat_name
            + "("
            + self.input
            + ","
            + self.output
            + ")"
        )
