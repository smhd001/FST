from FST import FST
f = FST() # q0 -> initial state
f.add_state("q0",False)
f.add_state('qf', True);
    
f.add_transition('q0', 'a', '', 'q0');
f.add_transition('q0', 'b', 'b', 'q0');
f.add_transition('q0', 'a', '', 'qf');
f.add_transition('q0', '', '', 'qf');

f.run('baab')
f.run('bb')
f.run('aaba')
