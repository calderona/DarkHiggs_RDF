# cuts

cuts = {}

#_tmp = [
#	    'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 && Lepton_pt[0] > 25',
#    'Lepton_pt[1] > 20',
#    '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13)',
#    '(nLepton >= 2 && Alt(Lepton_pt,2, 0) < 10)',
#    'ptll>30',
#     'mll>12'
#    'PuppiMET_pt > 20',
#    'mpmet > 20'
#     ]

#_tmp = ['Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 && Lepton_pt[0] > 25']


preselections = 'mll < 80'

#' && '.join(_tmp)

#preselections = 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 && Lepton_pt[0] > 25'


#cuts['DHWW2l2v_13TeV_sr'] = {
#    'expr': 'mth > 50 && mll < 80 && drll < 2.5 && bVeto',
#    'categories': {
#        '0j':'bVeto',
#    }
#}
