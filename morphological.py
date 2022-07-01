from FST import FST

fst = FST()
AZ = "abcdefghijklmnopqrstuvwxyz"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
NONSPECIAL = "abcdgijklmnpqrtuvw"

fst.add_state("q0", False)
fst.add_set_transition("q0", AZ, "q0")
fst.add_state("qs", False)
fst.add_state("qf", True)
fst.add_transition("qs", "", "s", "qf")

# ##[xzso] -> ##[xzso]es
fst.add_state("qes", False)
fst.add_transition("q0", "x", "x", "qes")
fst.add_transition("q0", "z", "z", "qes")
fst.add_transition("q0", "s", "s", "qes")
fst.add_transition("q0", "o", "o", "qes")
fst.add_transition("qes", "", "e", "qs")

# ##[sc]h -> ##[sc]hes
fst.add_state("qsc", False)
fst.add_transition("q0", "c", "c", "qsc")
fst.add_transition("q0", "s", "s", "qsc")
fst.add_transition("qsc", "h", "h", "qes")

# y
# #[CONSONANTS]y -> #[CONSONANTS]ies
fst.add_state("qcons", False)
fst.add_set_transition("q0", CONSONANTS, "qcons")
fst.add_transition("qcons", "y", "i", "qes")
# #[VOWELS]y -> #[VOWELS]ies
fst.add_state("qvow", False)
fst.add_set_transition("q0", VOWELS, "qvow")
fst.add_transition("qvow", "y", "y", "qs")

# #fe -> #ves || #f -> #ves
fst.add_state("qv", False)
fst.add_transition("q0", "f", "v", "qv")
fst.add_transition("qv", "", "", "qes")
fst.add_transition("qv", "e", "e", "qs")

# normal nonens
fst.add_state("qn", False)
fst.add_set_transition("q0", NONSPECIAL, "qn")
fst.add_transition("qn", "", "", "qs")

# h but not [cs]h
AZ_SC = AZ.replace("c", "").replace("s", "")
fst.add_state("qh", False)
fst.add_set_transition("q0", AZ_SC, "qh")
fst.add_transition("qh", "h", "h", "qs")

# e but not fe
AZ_E = AZ.replace("f", "")
fst.add_state("qe", False)
fst.add_set_transition("q0", AZ_E, "qe")
fst.add_transition("qe", "e", "e", "qs")

with open("test.txt") as f:
    for t in f:
        print(t.strip() + " --> ", end="")
        fst.run(t.strip())
