class FST:
    trans = []
    sts = []

    def add_state(self, state_name: str, is_final: bool) -> None:
        self.sts.append(state(state_name, is_final))

    def add_transition(
        self, in_state_name: str, input: chr, output: chr, out_stat_name: str
    ) -> None:
        if in_state_name in self.sts and out_stat_name in self.sts:
            self.trans.append(transition(in_state_name, input, output, out_stat_name))

    def __is_final(self, state_name: str) -> bool:
        for s in self.sts:
            if s.name == state_name:
                return s.is_final
        return False

    def run(self, inp: str) -> list[str]:
        to_p = [("", "q0")]  # list to pars
        p_out = []  # list for output
        for c in inp:
            for tp in to_p:
                for t in self.trans:
                    if tp[1] == t.in_state_name and c == t.input:
                        p_out.append((tp[0] + t.output, t.out_stat_name))
            to_p = p_out
            p_out = []
        return [i[0] for i in to_p if self.__is_final(i[1])]


class state:
    name = ""
    is_final = False

    def __init__(self, name: str, is_final: bool) -> None:
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
    in_state_name = ""
    input = ""
    output = ""
    out_stat_name = ""

    def __init__(
        self, in_state_name: str, input: chr, output: chr, out_stat_name: str
    ) -> None:
        self.in_state_name = in_state_name
        self.input = input
        self.output = output
        self.out_stat_name = out_stat_name
