from collections import OrderedDict
samples = [('WW', ['/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7/nanoLatino_WWTo2L2Nu__part3.root', '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7/nanoLatino_WWTo2L2Nu__part4.root', '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7/nanoLatino_WWTo2L2Nu__part5.root'], '( XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*nllW ) * ( 1.0 )', 1, False)]
aliases = OrderedDict([('LepWPCut', {'expr': 'LepCut2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW', 'samples': ['WW', 'DATA']}), ('LepWPSF', {'expr': 'LepSF2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW', 'samples': ['WW']}), ('gstarLow', {'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4', 'samples': 'VgS'}), ('gstarHigh', {'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4', 'samples': 'VgS'}), ('zeroJet', {'expr': 'Alt(CleanJet_pt,0, 0) < 30.'}), ('oneJet', {'expr': 'Alt(CleanJet_pt, 0, 0) > 30.'}), ('multiJet', {'expr': 'Alt(CleanJet_pt, 1, 0) > 30.'}), ('bVeto', {'expr': 'Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0'}), ('bReq', {'expr': 'Sum(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 1'}), ('topcr', {'expr': 'mth>50 && mll<80 && drll<2.5 && ((zeroJet && !bVeto) || bReq)'}), ('bVetoSF', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSF', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSF', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF', 'samples': ['WW']}), ('JetPUID_SF', {'expr': '( 1 * !(topcr) + (topcr)*Jet_PUIDSF_loose)', 'samples': ['WW']}), ('bVetoSFjesup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_jes, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFjesdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_jes, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFjesup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_jes, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFjesdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_jes, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFjesup', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFjesup + (topcr && !zeroJet)*bReqSFjesup', 'samples': ['WW']}), ('btagSFjesdown', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFjesdown + (topcr && !zeroJet)*bReqSFjesdown', 'samples': ['WW']}), ('bVetoSFlfup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lf, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFlfdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lf, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFlfup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lf, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFlfdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lf, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFlfup', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfup + (topcr && !zeroJet)*bReqSFlfup', 'samples': ['WW']}), ('btagSFlfdown', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfdown + (topcr && !zeroJet)*bReqSFlfdown', 'samples': ['WW']}), ('bVetoSFhfup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hf, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFhfdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hf, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFhfup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hf, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFhfdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hf, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFhfup', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfup + (topcr && !zeroJet)*bReqSFhfup', 'samples': ['WW']}), ('btagSFhfdown', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfdown + (topcr && !zeroJet)*bReqSFhfdown', 'samples': ['WW']}), ('bVetoSFlfstats1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFlfstats1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFlfstats1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFlfstats1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFlfstats1up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfstats1up + (topcr && !zeroJet)*bReqSFlfstats1up', 'samples': ['WW']}), ('btagSFlfstats1down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfstats1down + (topcr && !zeroJet)*bReqSFlfstats1down', 'samples': ['WW']}), ('bVetoSFlfstats2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFlfstats2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFlfstats2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFlfstats2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFlfstats2up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfstats2up + (topcr && !zeroJet)*bReqSFlfstats2up', 'samples': ['WW']}), ('btagSFlfstats2down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfstats2down + (topcr && !zeroJet)*bReqSFlfstats2down', 'samples': ['WW']}), ('bVetoSFhfstats1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFhfstats1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFhfstats1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFhfstats1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFhfstats1up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfstats1up + (topcr && !zeroJet)*bReqSFhfstats1up', 'samples': ['WW']}), ('btagSFhfstats1down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfstats1down + (topcr && !zeroJet)*bReqSFhfstats1down', 'samples': ['WW']}), ('bVetoSFhfstats2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFhfstats2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFhfstats2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFhfstats2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFhfstats2up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfstats2up + (topcr && !zeroJet)*bReqSFhfstats2up', 'samples': ['WW']}), ('btagSFhfstats2down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfstats2down + (topcr && !zeroJet)*bReqSFhfstats2down', 'samples': ['WW']}), ('bVetoSFcferr1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_cferr1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFcferr1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_cferr1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFcferr1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_cferr1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFcferr1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_cferr1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFcferr1up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFcferr1up + (topcr && !zeroJet)*bReqSFcferr1up', 'samples': ['WW']}), ('btagSFcferr1down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFcferr1down + (topcr && !zeroJet)*bReqSFcferr1down', 'samples': ['WW']}), ('bVetoSFcferr2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_cferr2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bVetoSFcferr2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_cferr2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFcferr2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_cferr2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('bReqSFcferr2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_cferr2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['WW']}), ('btagSFcferr2up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFcferr2up + (topcr && !zeroJet)*bReqSFcferr2up', 'samples': ['WW']}), ('btagSFcferr2down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFcferr2down + (topcr && !zeroJet)*bReqSFcferr2down', 'samples': ['WW']}), ('fakeW', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW', 'samples': ['Fake']}), ('fakeWEleUp', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_EleUp', 'samples': ['Fake']}), ('fakeWEleDown', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_EleDown', 'samples': ['Fake']}), ('fakeWMuUp', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_MuUp', 'samples': ['Fake']}), ('fakeWMuDown', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_MuDown', 'samples': ['Fake']}), ('fakeWStatEleUp', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_statEleUp', 'samples': ['Fake']}), ('fakeWStatEleDown', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_statEleDown', 'samples': ['Fake']}), ('fakeWStatMuUp', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_statMuUp', 'samples': ['Fake']}), ('fakeWStatMuDown', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_statMuDown', 'samples': ['Fake']}), ('PromptGenLepMatch2l', {'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)', 'samples': ['WW']}), ('Top_pTrw', {'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)', 'samples': ['top']}), ('SFweight', {'expr': 'SFweight2l * LepWPCut * LepWPSF * btagSF * JetPUID_SF', 'samples': ['WW']}), ('SFweightEleUp', {'expr': 'LepSF2l__ele_mvaFall17V1Iso_WP90__Up', 'samples': ['WW']}), ('SFweightEleDown', {'expr': 'LepSF2l__ele_mvaFall17V1Iso_WP90__Do', 'samples': ['WW']}), ('SFweightMuUp', {'expr': 'LepSF2l__mu_cut_Tight_HWWW__Up', 'samples': ['WW']}), ('SFweightMuDown', {'expr': 'LepSF2l__mu_cut_Tight_HWWW__Do', 'samples': ['WW']})])
variables = {'mll': {'name': 'mll', 'range': (40, 20.0, 100.0), 'xaxis': 'm_{ll} [GeV]', 'fold': 3}}
cuts = {'cuts': {'DHWW2l2v_13TeV_sr': {'expr': 'mth > 50 && mll < 80 && drll < 2.5 && bVeto', 'categories': {}}}, 'preselections': 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 && Lepton_pt[0] > 25'}
plot = {'plot': {'DY': {'color': 418, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'Fake': {'color': 921, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'top': {'nameHR': 'tW and t#bar{t}', 'color': 400, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'WW': {'color': 851, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'ggWW': {'color': 850, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'WWewk': {'color': 851, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'Vg': {'color': 859, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'VgS': {'color': 617, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'VZ': {'color': 858, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'VVV': {'color': 857, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'Higgs': {'color': 632, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'DATA': {'nameHR': 'Data', 'color': 1, 'isSignal': 0, 'isData': 1, 'isBlind': 1}}, 'groupPlot': {'VZ': {'nameHR': 'VZ', 'isSignal': 0, 'color': 617, 'samples': ['VZ', 'WZ', 'ZZ']}, 'VVV': {'nameHR': 'VVV', 'isSignal': 0, 'color': 857, 'samples': ['VVV']}, 'Vg': {'nameHR': 'V#gamma', 'isSignal': 0, 'color': 800, 'samples': ['Vg', 'Wg']}, 'VgS': {'nameHR': 'V#gamma*', 'isSignal': 0, 'color': 409, 'samples': ['VgS']}, 'DY': {'nameHR': 'DY', 'isSignal': 0, 'color': 418, 'samples': ['DY']}, 'Higgs': {'nameHR': 'Higgs', 'isSignal': 0, 'color': 632, 'samples': ['Higgs']}, 'Fake': {'nameHR': 'nonprompt', 'isSignal': 0, 'color': 921, 'samples': ['Fake']}, 'WW': {'nameHR': 'WW', 'isSignal': 0, 'color': 851, 'samples': ['WW', 'ggWW', 'WWewk']}, 'top': {'nameHR': 'tW and t#bar{t}', 'isSignal': 0, 'color': 400, 'samples': ['top']}}, 'legend': {'lumi': 'L = 59.7/fb', 'sqrt': '#sqrt{s} = 13 TeV'}}
nuisances = {'lumi': {'name': 'lumi_13TeV_2018', 'type': 'lnN', 'samples': {}}, 'stat': {'type': 'auto', 'maxPoiss': '10', 'includeSignal': '0', 'samples': {}}}
structure = {'DY': {'isSignal': 0, 'isData': 0}, 'Fake': {'isSignal': 0, 'isData': 0}, 'top': {'isSignal': 0, 'isData': 0}, 'WW': {'isSignal': 0, 'isData': 0}, 'WWewk': {'isSignal': 0, 'isData': 0}, 'ggWW': {'isSignal': 0, 'isData': 0}, 'Vg': {'isSignal': 0, 'isData': 0}, 'VgS': {'isSignal': 0, 'isData': 0}, 'VZ': {'isSignal': 0, 'isData': 0}, 'VVV': {'isSignal': 0, 'isData': 0}, 'Higgs': {'isSignal': 0, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_100_mZp_1500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_150_mZp_1500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_160_mx_200_mZp_1500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_100_mZp_1500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_150_mZp_1500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_180_mx_200_mZp_1500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_100_mZp_1500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_150_mZp_1500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_195': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_295': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_300': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_400': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_500': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_800': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_1000': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_1200': {'isSignal': 2, 'isData': 0}, 'DH_mhs_200_mx_200_mZp_1500': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_1p0_mXd_10_MA_200_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_1p0_mXd_10_MA_400_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_1p0_mXd_10_MA_500_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_1p0_mXd_10_MA_600_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_0p5_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_1p0_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_1p5_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_2p0_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_4p0_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p35_tanb_8p0_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p7_tanb_0p5_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p7_tanb_1p0_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p7_tanb_1p5_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p7_tanb_2p0_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p7_tanb_4p0_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, '2HMDa__gg_sinp_0p7_tanb_8p0_mXd_10_MA_300_ma_150': {'isSignal': 2, 'isData': 0}, 'DATA': {'isSignal': 0, 'isData': 1}}
lumi = 35.867
