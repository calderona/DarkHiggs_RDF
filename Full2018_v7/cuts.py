# cuts

cuts = {}


_tmp = [
    'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'Lepton_pt[0] > 25.',
    'Lepton_pt[1] > 20.',
    '(nLepton >= 2 && Alt(Lepton_pt,2, 0) < 10.)',
    'mll > 12',
    'mpmet > 20.',
    'PuppiMET_pt > 20.',
     ]

preselections = ' && '.join(_tmp)

cuts['dhww2l2v_13TeV_sr'] = {
    'expr': 'ptll>30 && mth > 50 && mll < 80 && drll < 2.5 && bVeto',
    'categories' : {
        '0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0',
    }
}





