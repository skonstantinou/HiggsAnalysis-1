import FWCore.ParameterSet.Config as cms
Taus = cms.VPSet(
    cms.PSet(
            branchname = cms.untracked.string("Taus"),
            src = cms.InputTag("NewTauIDsEmbedded"),
            discriminators = cms.vstring(
                'againstElectronLooseMVA6',
                'againstElectronMVA6Raw',
                'againstElectronMVA6category',
                'againstElectronMediumMVA6',
                'againstElectronTightMVA6',
                'againstElectronVLooseMVA6',
                'againstElectronVTightMVA6',
                'againstMuonLoose3',
                'againstMuonTight3',
                'byCombinedIsolationDeltaBetaCorrRaw3Hits',
                'byIsolationMVArun2v1DBdR03oldDMwLTraw',
                'byIsolationMVArun2v1DBnewDMwLTraw',
                'byIsolationMVArun2v1DBoldDMwLTraw',
                'byIsolationMVArun2v1PWdR03oldDMwLTraw',
                'byIsolationMVArun2v1PWnewDMwLTraw',
                'byIsolationMVArun2v1PWoldDMwLTraw',
                'byLooseCombinedIsolationDeltaBetaCorr3Hits',
                'byLooseIsolationMVArun2v1DBdR03oldDMwLT',
                'byLooseIsolationMVArun2v1DBnewDMwLT',
                'byLooseIsolationMVArun2v1DBoldDMwLT',
                'byLooseIsolationMVArun2v1PWdR03oldDMwLT',
                'byLooseIsolationMVArun2v1PWnewDMwLT',
                'byLooseIsolationMVArun2v1PWoldDMwLT',
                'byMediumCombinedIsolationDeltaBetaCorr3Hits',
                'byMediumIsolationMVArun2v1DBdR03oldDMwLT',
                'byMediumIsolationMVArun2v1DBnewDMwLT',
                'byMediumIsolationMVArun2v1DBoldDMwLT',
                'byMediumIsolationMVArun2v1PWdR03oldDMwLT',
                'byMediumIsolationMVArun2v1PWnewDMwLT',
                'byMediumIsolationMVArun2v1PWoldDMwLT',
                'byPhotonPtSumOutsideSignalCone',
                'byTightCombinedIsolationDeltaBetaCorr3Hits',
                'byTightIsolationMVArun2v1DBdR03oldDMwLT',
                'byTightIsolationMVArun2v1DBnewDMwLT',
                'byTightIsolationMVArun2v1DBoldDMwLT',
                'byTightIsolationMVArun2v1PWdR03oldDMwLT',
                'byTightIsolationMVArun2v1PWnewDMwLT',
                'byTightIsolationMVArun2v1PWoldDMwLT',
                'byVLooseIsolationMVArun2v1DBdR03oldDMwLT',
                'byVLooseIsolationMVArun2v1DBnewDMwLT',
                'byVLooseIsolationMVArun2v1DBoldDMwLT',
                'byVLooseIsolationMVArun2v1PWdR03oldDMwLT',
                'byVLooseIsolationMVArun2v1PWnewDMwLT',
                'byVLooseIsolationMVArun2v1PWoldDMwLT',
                'byVTightIsolationMVArun2v1DBdR03oldDMwLT',
                'byVTightIsolationMVArun2v1DBnewDMwLT',
                'byVTightIsolationMVArun2v1DBoldDMwLT',
                'byVTightIsolationMVArun2v1PWdR03oldDMwLT',
                'byVTightIsolationMVArun2v1PWnewDMwLT',
                'byVTightIsolationMVArun2v1PWoldDMwLT',
                'byVVLooseIsolationMVArun2v1DBoldDMwLT',
                'byVVTightIsolationMVArun2v1DBdR03oldDMwLT',
                'byVVTightIsolationMVArun2v1DBnewDMwLT',
                'byVVTightIsolationMVArun2v1DBoldDMwLT',
                'byVVTightIsolationMVArun2v1PWdR03oldDMwLT',
                'byVVTightIsolationMVArun2v1PWnewDMwLT',
                'byVVTightIsolationMVArun2v1PWoldDMwLT',
                'chargedIsoPtSum',
                'chargedIsoPtSumdR03',
                'decayModeFinding',
                'decayModeFindingNewDMs',
                'footprintCorrection',
                'footprintCorrectiondR03',
                'neutralIsoPtSum',
                'neutralIsoPtSumWeight',
                'neutralIsoPtSumWeightdR03',
                'neutralIsoPtSumdR03',
                'photonPtSumOutsideSignalCone',
                'photonPtSumOutsideSignalConedR03',
                'puCorrPtSum',
                'byIsolationMVArun2017v2DBnewDMwLTraw2017',
                'byIsolationMVArun2017v2DBoldDMdR0p3wLTraw2017',
                'byIsolationMVArun2017v2DBoldDMwLTraw2017',
                'byLooseIsolationMVArun2017v2DBnewDMwLT2017',
                'byLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byLooseIsolationMVArun2017v2DBoldDMwLT2017',
                'byMediumIsolationMVArun2017v2DBnewDMwLT2017',
                'byMediumIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byMediumIsolationMVArun2017v2DBoldDMwLT2017',
                'byTightIsolationMVArun2017v2DBnewDMwLT2017',
                'byTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byTightIsolationMVArun2017v2DBoldDMwLT2017',
                'byVLooseIsolationMVArun2017v2DBnewDMwLT2017',
                'byVLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byVLooseIsolationMVArun2017v2DBoldDMwLT2017',
                'byVTightIsolationMVArun2017v2DBnewDMwLT2017',
                'byVTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byVTightIsolationMVArun2017v2DBoldDMwLT2017',
                'byVVLooseIsolationMVArun2017v2DBnewDMwLT2017',
                'byVVLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byVVLooseIsolationMVArun2017v2DBoldDMwLT2017',
                'byVVTightIsolationMVArun2017v2DBnewDMwLT2017',
                'byVVTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byVVTightIsolationMVArun2017v2DBoldDMwLT2017',
                ),
            filter = cms.untracked.bool(False), 
            jetSrc = cms.InputTag("slimmedJets"), # made from ak4PFJetsCHS
            systVariations = cms.bool(True),
            TEScorrection = cms.bool(True),
            TESvariationExtreme = cms.untracked.double(0.03)
    )
)

# https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauIDRecommendation13TeV
Taus_TauPOGRecommendation = cms.VPSet()
Taus_TauPOGRecommendation.append(Taus[0].clone())
Taus_TauPOGRecommendation[0].discriminators = cms.vstring(
                'decayModeFinding',
                #'decayModeFindingOldDMs',
                'decayModeFindingNewDMs',
                # Against-Leptons
                'againstElectronLooseMVA6',
                'againstElectronMediumMVA6',
                'againstElectronTightMVA6',
                'againstElectronVLooseMVA6',
                'againstElectronVTightMVA6',
                'againstMuonLoose3',
                'againstMuonTight3',
                # Cut-based Isolation (DR<0.5) 
                'byLooseCombinedIsolationDeltaBetaCorr3Hits',
                'byMediumCombinedIsolationDeltaBetaCorr3Hits',
                'byTightCombinedIsolationDeltaBetaCorr3Hits',
                'byCombinedIsolationDeltaBetaCorrRaw3Hits',
                # MVA Isolation 2017v2 (Old Decay Mode DR<0.5)
                'byIsolationMVArun2017v2DBoldDMwLTraw2017',       
                'byVVLooseIsolationMVArun2017v2DBoldDMwLT2017',
                'byVLooseIsolationMVArun2017v2DBoldDMwLT2017',
                'byLooseIsolationMVArun2017v2DBoldDMwLT2017',
                'byMediumIsolationMVArun2017v2DBoldDMwLT2017',
                'byTightIsolationMVArun2017v2DBoldDMwLT2017',
                'byVTightIsolationMVArun2017v2DBoldDMwLT2017',
                'byVVTightIsolationMVArun2017v2DBoldDMwLT2017',
                # MVA Isolation 2017v2 (New Decay Mode DR<0.5)
                'byIsolationMVArun2017v2DBnewDMwLTraw2017',
                'byVVLooseIsolationMVArun2017v2DBnewDMwLT2017',
                'byVLooseIsolationMVArun2017v2DBnewDMwLT2017',
                'byLooseIsolationMVArun2017v2DBnewDMwLT2017',
                'byMediumIsolationMVArun2017v2DBnewDMwLT2017',
                'byTightIsolationMVArun2017v2DBnewDMwLT2017',
                'byVTightIsolationMVArun2017v2DBnewDMwLT2017',
                'byVVTightIsolationMVArun2017v2DBnewDMwLT2017',
                # MVA Isolation 2017v2 (Old Decay Mode DR<0.3)
                'byIsolationMVArun2017v2DBoldDMdR0p3wLTraw2017',
                'byVVLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byVLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byMediumIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byVTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
                'byVVTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017',
)

TausNoSysVariations = cms.VPSet()
TausNoSysVariations.append(Taus_TauPOGRecommendation[0].clone())
for i in range(len(TausNoSysVariations)):
    TausNoSysVariations[i].systVariations = cms.bool(False)
