## Causality, Conditionality for Stage I
### e.g.
    {"annotator_labels": ["contradiction"], "genre": "slate", "gold_label": "contradiction", "pairID": "91402c", "promptID": "91402", "sentence1": "That is why icons have the power they have.", "sentence1_binary_parse": "( That ( ( is ( why ( icons ( have ( ( the power ) ( they have ) ) ) ) ) ) . ) )", "sentence1_parse": "(ROOT (S (NP (DT That)) (VP (VBZ is) (SBAR (WHADVP (WRB why)) (S (NP (NNS icons)) (VP (VBP have) (NP (NP (DT the) (NN power)) (SBAR (S (NP (PRP they)) (VP (VBP have))))))))) (. .)))", "sentence2": "That is why God moves me.", "sentence2_binary_parse": "( That ( ( is ( why ( God ( moves me ) ) ) ) . ) )", "sentence2_parse": "(ROOT (S (NP (DT That)) (VP (VBZ is) (SBAR (WHADVP (WRB why)) (S (NP (NNP God)) (VP (VBZ moves) (NP (PRP me)))))) (. .)))"}

- Extracted from GLUE's MultiNLI dataset
- with average of a C-Unit = 6.9502400698384985
- in total of 2426 examples