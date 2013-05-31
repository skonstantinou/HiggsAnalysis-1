# Generated on Mon May 27 19:54:42 2013
# by HiggsAnalysis/TriggerEfficiency/test/PythonWriter.py

import FWCore.ParameterSet.Config as cms

def triggerBin(pt, efficiency, uncertainty):
    return cms.PSet(
        pt = cms.double(pt),
        efficiency = cms.double(efficiency),
        uncertainty = cms.double(uncertainty)
    )


tauLegEfficiency_byLooseCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronMediumMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronMediumMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0220731298222, 0.00120342535728),
                triggerBin(25.0, 0.0320803629294, 0.00158602975364),
                triggerBin(29.0, 0.0811659975563, 0.00255123923692),
                triggerBin(33.0, 0.452121705505, 0.00502064192266),
                triggerBin(37.0, 0.737529077281, 0.0050016789304),
                triggerBin(41.0, 0.779506871463, 0.00589376286804),
                triggerBin(45.0, 0.80050906777, 0.00712807921279),
                triggerBin(50.0, 0.805259862242, 0.00990930748174),
                triggerBin(55.0, 0.756218905473, 0.0151424361887),
                triggerBin(60.0, 0.772673733804, 0.0143836477504),
                triggerBin(70.0, 0.838797814208, 0.019220893195),
                triggerBin(80.0, 0.772532188841, 0.0274625149161),
                triggerBin(100.0, 0.736486486486, 0.0362120389968),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0225253522391, 0.00140568328706),
                triggerBin(25.0, 0.0328826392645, 0.00185468203807),
                triggerBin(29.0, 0.0793779737728, 0.00291214260777),
                triggerBin(33.0, 0.47219578518, 0.00582111449656),
                triggerBin(37.0, 0.774799860773, 0.00551056695437),
                triggerBin(41.0, 0.824845055241, 0.00623953049465),
                triggerBin(45.0, 0.828322440087, 0.00787163837951),
                triggerBin(50.0, 0.851046025105, 0.0102995587612),
                triggerBin(55.0, 0.837398373984, 0.0148795891866),
                triggerBin(60.0, 0.813186813187, 0.0154429125476),
                triggerBin(70.0, 0.85447761194, 0.0215401068673),
                triggerBin(80.0, 0.854838709677, 0.0258292043299),
                triggerBin(100.0, 0.819047619048, 0.0375700763374),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0128881077914, 0.00272998971793),
                triggerBin(25.0, 0.0416047548291, 0.00544278624816),
                triggerBin(29.0, 0.0523672883788, 0.00596648671864),
                triggerBin(33.0, 0.478538812785, 0.0150960219576),
                triggerBin(37.0, 0.748414376321, 0.0141080958884),
                triggerBin(41.0, 0.825515947467, 0.0164390606968),
                triggerBin(45.0, 0.793785310734, 0.0215035269211),
                triggerBin(50.0, 0.840425531915, 0.0267086782873),
                triggerBin(55.0, 0.928571428571, 0.0260154056816),
                triggerBin(60.0, 0.739130434783, 0.0457802685758),
                triggerBin(70.0, 0.761904761905, 0.0657205294612),
                triggerBin(80.0, 0.827586206897, 0.0701445003746),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0242687579483, 0.00158414493981),
                triggerBin(25.0, 0.0313963792885, 0.00196212544897),
                triggerBin(29.0, 0.0845908902118, 0.00327424071992),
                triggerBin(33.0, 0.471086261981, 0.00630892663075),
                triggerBin(37.0, 0.78, 0.00597913037155),
                triggerBin(41.0, 0.824732536186, 0.00674419732735),
                triggerBin(45.0, 0.834621329212, 0.00843279844792),
                triggerBin(50.0, 0.853028798411, 0.0111579197559),
                triggerBin(55.0, 0.820116054159, 0.0168922923074),
                triggerBin(60.0, 0.825688073394, 0.0162507461423),
                triggerBin(70.0, 0.871681415929, 0.0222468974722),
                triggerBin(80.0, 0.859872611465, 0.0277031240067),
                triggerBin(100.0, 0.865979381443, 0.0345902513467),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223285486443, 0.00240889194085),
                triggerBin(25.0, 0.0406582768635, 0.00354772838555),
                triggerBin(29.0, 0.101724744808, 0.00567129718779),
                triggerBin(33.0, 0.477346278317, 0.0100461477445),
                triggerBin(37.0, 0.785642570281, 0.00919469033426),
                triggerBin(41.0, 0.823767178658, 0.0108333004838),
                triggerBin(45.0, 0.849056603774, 0.0122935540405),
                triggerBin(50.0, 0.805970149254, 0.0197233520562),
                triggerBin(55.0, 0.777777777778, 0.0302406141084),
                triggerBin(60.0, 0.801886792453, 0.0273744444712),
                triggerBin(70.0, 0.897959183673, 0.0305775174394),
                triggerBin(80.0, 0.851063829787, 0.0519316628328),
                triggerBin(100.0, 0.53488372093, 0.0760634872547),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0196975726224, 0.00113165624575),
                triggerBin(25.0, 0.0407193756362, 0.0018203434181),
                triggerBin(29.0, 0.087974966473, 0.00267833526961),
                triggerBin(33.0, 0.471248386136, 0.00497459375698),
                triggerBin(37.0, 0.77292860865, 0.00478171203732),
                triggerBin(41.0, 0.834296326868, 0.00534114697221),
                triggerBin(45.0, 0.834063869756, 0.00658267899729),
                triggerBin(50.0, 0.825129533679, 0.00966708755623),
                triggerBin(55.0, 0.842751842752, 0.0127594053709),
                triggerBin(60.0, 0.866910866911, 0.0118690667071),
                triggerBin(70.0, 0.812307692308, 0.0216591714683),
                triggerBin(80.0, 0.877394636015, 0.0203016795926),
                triggerBin(100.0, 0.786666666667, 0.033448689284),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240146301554, 0.00106205567409),
                triggerBin(25.0, 0.0332921334875, 0.0011327811561),
                triggerBin(29.0, 0.0765011168046, 0.00152335533647),
                triggerBin(33.0, 0.533925847317, 0.00287273467731),
                triggerBin(37.0, 0.856587105402, 0.00223117526402),
                triggerBin(41.0, 0.875388617474, 0.00263079749899),
                triggerBin(45.0, 0.884551667012, 0.00325171021473),
                triggerBin(50.0, 0.88736068295, 0.00486847893093),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.90664189503, 0.00627006279942),
                triggerBin(70.0, 0.850215517241, 0.011714504874),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240146301554, 0.00106205567409),
                triggerBin(25.0, 0.0332921334875, 0.0011327811561),
                triggerBin(29.0, 0.0765011168046, 0.00152335533647),
                triggerBin(33.0, 0.533925847317, 0.00287273467731),
                triggerBin(37.0, 0.856587105402, 0.00223117526402),
                triggerBin(41.0, 0.875388617474, 0.00263079749899),
                triggerBin(45.0, 0.884551667012, 0.00325171021473),
                triggerBin(50.0, 0.88736068295, 0.00486847893093),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.90664189503, 0.00627006279942),
                triggerBin(70.0, 0.850215517241, 0.011714504874),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240146301554, 0.00106205567409),
                triggerBin(25.0, 0.0332921334875, 0.0011327811561),
                triggerBin(29.0, 0.0765011168046, 0.00152335533647),
                triggerBin(33.0, 0.533925847317, 0.00287273467731),
                triggerBin(37.0, 0.856587105402, 0.00223117526402),
                triggerBin(41.0, 0.875388617474, 0.00263079749899),
                triggerBin(45.0, 0.884551667012, 0.00325171021473),
                triggerBin(50.0, 0.88736068295, 0.00486847893093),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.90664189503, 0.00627006279942),
                triggerBin(70.0, 0.850215517241, 0.011714504874),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240146301554, 0.00106205567409),
                triggerBin(25.0, 0.0332921334875, 0.0011327811561),
                triggerBin(29.0, 0.0765011168046, 0.00152335533647),
                triggerBin(33.0, 0.533925847317, 0.00287273467731),
                triggerBin(37.0, 0.856587105402, 0.00223117526402),
                triggerBin(41.0, 0.875388617474, 0.00263079749899),
                triggerBin(45.0, 0.884551667012, 0.00325171021473),
                triggerBin(50.0, 0.88736068295, 0.00486847893093),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.90664189503, 0.00627006279942),
                triggerBin(70.0, 0.850215517241, 0.011714504874),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240146301554, 0.00106205567409),
                triggerBin(25.0, 0.0332921334875, 0.0011327811561),
                triggerBin(29.0, 0.0765011168046, 0.00152335533647),
                triggerBin(33.0, 0.533925847317, 0.00287273467731),
                triggerBin(37.0, 0.856587105402, 0.00223117526402),
                triggerBin(41.0, 0.875388617474, 0.00263079749899),
                triggerBin(45.0, 0.884551667012, 0.00325171021473),
                triggerBin(50.0, 0.88736068295, 0.00486847893093),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.90664189503, 0.00627006279942),
                triggerBin(70.0, 0.850215517241, 0.011714504874),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240146301554, 0.00106205567409),
                triggerBin(25.0, 0.0332921334875, 0.0011327811561),
                triggerBin(29.0, 0.0765011168046, 0.00152335533647),
                triggerBin(33.0, 0.533925847317, 0.00287273467731),
                triggerBin(37.0, 0.856587105402, 0.00223117526402),
                triggerBin(41.0, 0.875388617474, 0.00263079749899),
                triggerBin(45.0, 0.884551667012, 0.00325171021473),
                triggerBin(50.0, 0.88736068295, 0.00486847893093),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.90664189503, 0.00627006279942),
                triggerBin(70.0, 0.850215517241, 0.011714504874),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240146301554, 0.00106205567409),
                triggerBin(25.0, 0.0332921334875, 0.0011327811561),
                triggerBin(29.0, 0.0765011168046, 0.00152335533647),
                triggerBin(33.0, 0.533925847317, 0.00287273467731),
                triggerBin(37.0, 0.856587105402, 0.00223117526402),
                triggerBin(41.0, 0.875388617474, 0.00263079749899),
                triggerBin(45.0, 0.884551667012, 0.00325171021473),
                triggerBin(50.0, 0.88736068295, 0.00486847893093),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.90664189503, 0.00627006279942),
                triggerBin(70.0, 0.850215517241, 0.011714504874),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byMediumCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronMediumMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronMediumMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0257693536365, 0.00163503380372),
                triggerBin(25.0, 0.0348766557297, 0.0020224849392),
                triggerBin(29.0, 0.0765973346619, 0.00296805306878),
                triggerBin(33.0, 0.453227380454, 0.0058777489579),
                triggerBin(37.0, 0.770968846286, 0.00549774913238),
                triggerBin(41.0, 0.805174234424, 0.00643521624264),
                triggerBin(45.0, 0.830530401035, 0.00779064282094),
                triggerBin(50.0, 0.836718115353, 0.0105348792389),
                triggerBin(55.0, 0.780327868852, 0.0167633619786),
                triggerBin(60.0, 0.795216741405, 0.0156018796343),
                triggerBin(70.0, 0.85559566787, 0.0211195429362),
                triggerBin(80.0, 0.792929292929, 0.0287967826963),
                triggerBin(100.0, 0.728070175439, 0.0416737532649),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.027004100099, 0.00192738524811),
                triggerBin(25.0, 0.0341811112911, 0.00231255887433),
                triggerBin(29.0, 0.0753843610514, 0.00339452846039),
                triggerBin(33.0, 0.469615313139, 0.00680354273844),
                triggerBin(37.0, 0.807594350544, 0.00599810334137),
                triggerBin(41.0, 0.856687898089, 0.00659123308869),
                triggerBin(45.0, 0.864234449761, 0.00837707574817),
                triggerBin(50.0, 0.872043010753, 0.0109536657658),
                triggerBin(55.0, 0.85864978903, 0.01600173572),
                triggerBin(60.0, 0.836653386454, 0.0164996980166),
                triggerBin(70.0, 0.862745098039, 0.0240929566073),
                triggerBin(80.0, 0.903225806452, 0.0237471830603),
                triggerBin(100.0, 0.7875, 0.0457361659412),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0172727272727, 0.00392826357259),
                triggerBin(25.0, 0.0395348837209, 0.00664479834069),
                triggerBin(29.0, 0.0581162324649, 0.00740597278247),
                triggerBin(33.0, 0.482716049383, 0.0175577096094),
                triggerBin(37.0, 0.78591954023, 0.0155479429339),
                triggerBin(41.0, 0.887218045113, 0.0158361112618),
                triggerBin(45.0, 0.832684824903, 0.0232831335623),
                triggerBin(50.0, 0.887323943662, 0.0265346123503),
                triggerBin(55.0, 0.971428571429, 0.0199123443553),
                triggerBin(60.0, 0.761904761905, 0.0464714320452),
                triggerBin(70.0, 0.684210526316, 0.10663920529),
                triggerBin(80.0, 0.888888888889, 0.0604812282169),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0287962497907, 0.00216384866604),
                triggerBin(25.0, 0.0333145115754, 0.00246200775658),
                triggerBin(29.0, 0.0787962779648, 0.00379089721719),
                triggerBin(33.0, 0.467293808795, 0.00737960769457),
                triggerBin(37.0, 0.811758211427, 0.00649437255301),
                triggerBin(41.0, 0.851668726823, 0.00721467586426),
                triggerBin(45.0, 0.869964664311, 0.00894135376669),
                triggerBin(50.0, 0.869289340102, 0.0120081076295),
                triggerBin(55.0, 0.839108910891, 0.0182803488708),
                triggerBin(60.0, 0.851674641148, 0.0173842685012),
                triggerBin(70.0, 0.881081081081, 0.0237983885035),
                triggerBin(80.0, 0.90625, 0.0257634881997),
                triggerBin(100.0, 0.847222222222, 0.0423996738056),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.02329594478, 0.00313303281555),
                triggerBin(25.0, 0.0437743190661, 0.00451209615374),
                triggerBin(29.0, 0.0979797979798, 0.0066810359222),
                triggerBin(33.0, 0.490513392857, 0.0118092636412),
                triggerBin(37.0, 0.81812212738, 0.00988437129232),
                triggerBin(41.0, 0.838877338877, 0.0118533199818),
                triggerBin(45.0, 0.86398763524, 0.0134769252333),
                triggerBin(50.0, 0.880398671096, 0.0187035671823),
                triggerBin(55.0, 0.816176470588, 0.0332141491207),
                triggerBin(60.0, 0.838323353293, 0.0284886056239),
                triggerBin(70.0, 0.917808219178, 0.0321461329375),
                triggerBin(80.0, 0.837209302326, 0.0562985989385),
                triggerBin(100.0, 0.588235294118, 0.0844035357623),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0214263207646, 0.00148398422287),
                triggerBin(25.0, 0.0401350337584, 0.00219470517055),
                triggerBin(29.0, 0.083572051314, 0.00308850966662),
                triggerBin(33.0, 0.467883795309, 0.00576004440897),
                triggerBin(37.0, 0.79758828596, 0.00527358672805),
                triggerBin(41.0, 0.857258718573, 0.00575159881163),
                triggerBin(45.0, 0.852272727273, 0.00714824260994),
                triggerBin(50.0, 0.847807394669, 0.0105330832946),
                triggerBin(55.0, 0.858766233766, 0.0140318971922),
                triggerBin(60.0, 0.89243697479, 0.0127016984782),
                triggerBin(70.0, 0.877118644068, 0.0213705730173),
                triggerBin(80.0, 0.913043478261, 0.0195844615853),
                triggerBin(100.0, 0.78813559322, 0.0376173733663),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0239330346616, 0.00117347694146),
                triggerBin(25.0, 0.0314591373162, 0.00122000848049),
                triggerBin(29.0, 0.0730149916713, 0.00163840589178),
                triggerBin(33.0, 0.531764520077, 0.00313545060086),
                triggerBin(37.0, 0.86043255769, 0.00240778936299),
                triggerBin(41.0, 0.888720551473, 0.00273707487751),
                triggerBin(45.0, 0.894620486367, 0.00340276506511),
                triggerBin(50.0, 0.902923644621, 0.00498799400472),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.923931149361, 0.00624692620032),
                triggerBin(70.0, 0.862023653088, 0.0125017147105),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0239330346616, 0.00117347694146),
                triggerBin(25.0, 0.0314591373162, 0.00122000848049),
                triggerBin(29.0, 0.0730149916713, 0.00163840589178),
                triggerBin(33.0, 0.531764520077, 0.00313545060086),
                triggerBin(37.0, 0.86043255769, 0.00240778936299),
                triggerBin(41.0, 0.888720551473, 0.00273707487751),
                triggerBin(45.0, 0.894620486367, 0.00340276506511),
                triggerBin(50.0, 0.902923644621, 0.00498799400472),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.923931149361, 0.00624692620032),
                triggerBin(70.0, 0.862023653088, 0.0125017147105),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0239330346616, 0.00117347694146),
                triggerBin(25.0, 0.0314591373162, 0.00122000848049),
                triggerBin(29.0, 0.0730149916713, 0.00163840589178),
                triggerBin(33.0, 0.531764520077, 0.00313545060086),
                triggerBin(37.0, 0.86043255769, 0.00240778936299),
                triggerBin(41.0, 0.888720551473, 0.00273707487751),
                triggerBin(45.0, 0.894620486367, 0.00340276506511),
                triggerBin(50.0, 0.902923644621, 0.00498799400472),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.923931149361, 0.00624692620032),
                triggerBin(70.0, 0.862023653088, 0.0125017147105),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0239330346616, 0.00117347694146),
                triggerBin(25.0, 0.0314591373162, 0.00122000848049),
                triggerBin(29.0, 0.0730149916713, 0.00163840589178),
                triggerBin(33.0, 0.531764520077, 0.00313545060086),
                triggerBin(37.0, 0.86043255769, 0.00240778936299),
                triggerBin(41.0, 0.888720551473, 0.00273707487751),
                triggerBin(45.0, 0.894620486367, 0.00340276506511),
                triggerBin(50.0, 0.902923644621, 0.00498799400472),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.923931149361, 0.00624692620032),
                triggerBin(70.0, 0.862023653088, 0.0125017147105),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0239330346616, 0.00117347694146),
                triggerBin(25.0, 0.0314591373162, 0.00122000848049),
                triggerBin(29.0, 0.0730149916713, 0.00163840589178),
                triggerBin(33.0, 0.531764520077, 0.00313545060086),
                triggerBin(37.0, 0.86043255769, 0.00240778936299),
                triggerBin(41.0, 0.888720551473, 0.00273707487751),
                triggerBin(45.0, 0.894620486367, 0.00340276506511),
                triggerBin(50.0, 0.902923644621, 0.00498799400472),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.923931149361, 0.00624692620032),
                triggerBin(70.0, 0.862023653088, 0.0125017147105),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0239330346616, 0.00117347694146),
                triggerBin(25.0, 0.0314591373162, 0.00122000848049),
                triggerBin(29.0, 0.0730149916713, 0.00163840589178),
                triggerBin(33.0, 0.531764520077, 0.00313545060086),
                triggerBin(37.0, 0.86043255769, 0.00240778936299),
                triggerBin(41.0, 0.888720551473, 0.00273707487751),
                triggerBin(45.0, 0.894620486367, 0.00340276506511),
                triggerBin(50.0, 0.902923644621, 0.00498799400472),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.923931149361, 0.00624692620032),
                triggerBin(70.0, 0.862023653088, 0.0125017147105),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0239330346616, 0.00117347694146),
                triggerBin(25.0, 0.0314591373162, 0.00122000848049),
                triggerBin(29.0, 0.0730149916713, 0.00163840589178),
                triggerBin(33.0, 0.531764520077, 0.00313545060086),
                triggerBin(37.0, 0.86043255769, 0.00240778936299),
                triggerBin(41.0, 0.888720551473, 0.00273707487751),
                triggerBin(45.0, 0.894620486367, 0.00340276506511),
                triggerBin(50.0, 0.902923644621, 0.00498799400472),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.923931149361, 0.00624692620032),
                triggerBin(70.0, 0.862023653088, 0.0125017147105),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byTightCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronMediumMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronMediumMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0267857142857, 0.00177349914101),
                triggerBin(25.0, 0.0338683351469, 0.00210965934305),
                triggerBin(29.0, 0.0736289542755, 0.00306956980507),
                triggerBin(33.0, 0.453569267998, 0.00612241756522),
                triggerBin(37.0, 0.775316455696, 0.00569452012232),
                triggerBin(41.0, 0.802272727273, 0.00671309774609),
                triggerBin(45.0, 0.828249648053, 0.00817029472456),
                triggerBin(50.0, 0.855251544572, 0.0104529517987),
                triggerBin(55.0, 0.794545454545, 0.0172280413706),
                triggerBin(60.0, 0.808219178082, 0.016291487517),
                triggerBin(70.0, 0.856060606061, 0.0216042964312),
                triggerBin(80.0, 0.809248554913, 0.0298711424611),
                triggerBin(100.0, 0.728971962617, 0.0429705224256),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0277288026927, 0.00207874767318),
                triggerBin(25.0, 0.034127843987, 0.00243970757102),
                triggerBin(29.0, 0.0724664336951, 0.00351603828638),
                triggerBin(33.0, 0.469959677419, 0.0070866978271),
                triggerBin(37.0, 0.812168644282, 0.00620589944847),
                triggerBin(41.0, 0.854214123007, 0.00687595800083),
                triggerBin(45.0, 0.860661049903, 0.0088159552775),
                triggerBin(50.0, 0.890058479532, 0.0106981105915),
                triggerBin(55.0, 0.87323943662, 0.0161195885087),
                triggerBin(60.0, 0.858823529412, 0.0168903505164),
                triggerBin(70.0, 0.865979381443, 0.0244590012902),
                triggerBin(80.0, 0.895833333333, 0.0254563859351),
                triggerBin(100.0, 0.773333333333, 0.0483444431676),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0178384050367, 0.00428768660153),
                triggerBin(25.0, 0.0445609436435, 0.00746992799868),
                triggerBin(29.0, 0.0568927789934, 0.00766189173781),
                triggerBin(33.0, 0.486166007905, 0.0181419022562),
                triggerBin(37.0, 0.792511700468, 0.0160166111651),
                triggerBin(41.0, 0.885941644562, 0.0163717625015),
                triggerBin(45.0, 0.831932773109, 0.024238020877),
                triggerBin(50.0, 0.893129770992, 0.0269929285565),
                triggerBin(55.0, 0.967741935484, 0.0224389788271),
                triggerBin(60.0, 0.788732394366, 0.048445352463),
                triggerBin(70.0, 0.684210526316, 0.10663920529),
                triggerBin(80.0, 0.875, 0.0675077156084),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0295119182747, 0.00232771734924),
                triggerBin(25.0, 0.0324607329843, 0.00256464213432),
                triggerBin(29.0, 0.0756135308424, 0.00393109242886),
                triggerBin(33.0, 0.467031659129, 0.00769746151085),
                triggerBin(37.0, 0.815963855422, 0.00672539787122),
                triggerBin(41.0, 0.848914488259, 0.00753837266394),
                triggerBin(45.0, 0.865900383142, 0.00943284022986),
                triggerBin(50.0, 0.889502762431, 0.0116514527382),
                triggerBin(55.0, 0.857142857143, 0.0183411639648),
                triggerBin(60.0, 0.872881355932, 0.0177043751494),
                triggerBin(70.0, 0.885714285714, 0.0240504814084),
                triggerBin(80.0, 0.9, 0.0273861278753),
                triggerBin(100.0, 0.835820895522, 0.0452562069843),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0253782332845, 0.0034743836022),
                triggerBin(25.0, 0.0407938257993, 0.00464445286706),
                triggerBin(29.0, 0.0932297447281, 0.0068493362457),
                triggerBin(33.0, 0.494552058111, 0.0123009655305),
                triggerBin(37.0, 0.824238128987, 0.0101326998252),
                triggerBin(41.0, 0.84085778781, 0.0122895819489),
                triggerBin(45.0, 0.865646258503, 0.0140639219549),
                triggerBin(50.0, 0.902877697842, 0.0177603511799),
                triggerBin(55.0, 0.838709677419, 0.0330292825143),
                triggerBin(60.0, 0.830188679245, 0.029776466595),
                triggerBin(70.0, 0.914285714286, 0.0334594310725),
                triggerBin(80.0, 0.931034482759, 0.0470543613256),
                triggerBin(100.0, 0.625, 0.0855816496102),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0231756596149, 0.00164029905384),
                triggerBin(25.0, 0.0416318574213, 0.00235698260716),
                triggerBin(29.0, 0.0813410277549, 0.00320424682468),
                triggerBin(33.0, 0.464109985528, 0.00599941997753),
                triggerBin(37.0, 0.799772468714, 0.00551029764777),
                triggerBin(41.0, 0.860246623605, 0.00594114731424),
                triggerBin(45.0, 0.856455142232, 0.00733504914675),
                triggerBin(50.0, 0.847805788982, 0.010976212849),
                triggerBin(55.0, 0.861111111111, 0.0144096060162),
                triggerBin(60.0, 0.903811252269, 0.0125610286999),
                triggerBin(70.0, 0.883177570093, 0.0219573662705),
                triggerBin(80.0, 0.903743315508, 0.0215683635399),
                triggerBin(100.0, 0.798165137615, 0.0384442346892),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0237582361885, 0.00121220829938),
                triggerBin(25.0, 0.0313207348529, 0.00126375667345),
                triggerBin(29.0, 0.0734725115864, 0.00170130497215),
                triggerBin(33.0, 0.531410742896, 0.00324020357154),
                triggerBin(37.0, 0.860643106637, 0.00248207617917),
                triggerBin(41.0, 0.889085783327, 0.0028183315289),
                triggerBin(45.0, 0.894990868771, 0.0035013733951),
                triggerBin(50.0, 0.901659125189, 0.00517185640642),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.92054958184, 0.00660988584837),
                triggerBin(70.0, 0.855337078652, 0.0131827880066),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0237582361885, 0.00121220829938),
                triggerBin(25.0, 0.0313207348529, 0.00126375667345),
                triggerBin(29.0, 0.0734725115864, 0.00170130497215),
                triggerBin(33.0, 0.531410742896, 0.00324020357154),
                triggerBin(37.0, 0.860643106637, 0.00248207617917),
                triggerBin(41.0, 0.889085783327, 0.0028183315289),
                triggerBin(45.0, 0.894990868771, 0.0035013733951),
                triggerBin(50.0, 0.901659125189, 0.00517185640642),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.92054958184, 0.00660988584837),
                triggerBin(70.0, 0.855337078652, 0.0131827880066),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0237582361885, 0.00121220829938),
                triggerBin(25.0, 0.0313207348529, 0.00126375667345),
                triggerBin(29.0, 0.0734725115864, 0.00170130497215),
                triggerBin(33.0, 0.531410742896, 0.00324020357154),
                triggerBin(37.0, 0.860643106637, 0.00248207617917),
                triggerBin(41.0, 0.889085783327, 0.0028183315289),
                triggerBin(45.0, 0.894990868771, 0.0035013733951),
                triggerBin(50.0, 0.901659125189, 0.00517185640642),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.92054958184, 0.00660988584837),
                triggerBin(70.0, 0.855337078652, 0.0131827880066),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0237582361885, 0.00121220829938),
                triggerBin(25.0, 0.0313207348529, 0.00126375667345),
                triggerBin(29.0, 0.0734725115864, 0.00170130497215),
                triggerBin(33.0, 0.531410742896, 0.00324020357154),
                triggerBin(37.0, 0.860643106637, 0.00248207617917),
                triggerBin(41.0, 0.889085783327, 0.0028183315289),
                triggerBin(45.0, 0.894990868771, 0.0035013733951),
                triggerBin(50.0, 0.901659125189, 0.00517185640642),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.92054958184, 0.00660988584837),
                triggerBin(70.0, 0.855337078652, 0.0131827880066),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0237582361885, 0.00121220829938),
                triggerBin(25.0, 0.0313207348529, 0.00126375667345),
                triggerBin(29.0, 0.0734725115864, 0.00170130497215),
                triggerBin(33.0, 0.531410742896, 0.00324020357154),
                triggerBin(37.0, 0.860643106637, 0.00248207617917),
                triggerBin(41.0, 0.889085783327, 0.0028183315289),
                triggerBin(45.0, 0.894990868771, 0.0035013733951),
                triggerBin(50.0, 0.901659125189, 0.00517185640642),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.92054958184, 0.00660988584837),
                triggerBin(70.0, 0.855337078652, 0.0131827880066),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0237582361885, 0.00121220829938),
                triggerBin(25.0, 0.0313207348529, 0.00126375667345),
                triggerBin(29.0, 0.0734725115864, 0.00170130497215),
                triggerBin(33.0, 0.531410742896, 0.00324020357154),
                triggerBin(37.0, 0.860643106637, 0.00248207617917),
                triggerBin(41.0, 0.889085783327, 0.0028183315289),
                triggerBin(45.0, 0.894990868771, 0.0035013733951),
                triggerBin(50.0, 0.901659125189, 0.00517185640642),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.92054958184, 0.00660988584837),
                triggerBin(70.0, 0.855337078652, 0.0131827880066),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0237582361885, 0.00121220829938),
                triggerBin(25.0, 0.0313207348529, 0.00126375667345),
                triggerBin(29.0, 0.0734725115864, 0.00170130497215),
                triggerBin(33.0, 0.531410742896, 0.00324020357154),
                triggerBin(37.0, 0.860643106637, 0.00248207617917),
                triggerBin(41.0, 0.889085783327, 0.0028183315289),
                triggerBin(45.0, 0.894990868771, 0.0035013733951),
                triggerBin(50.0, 0.901659125189, 0.00517185640642),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.92054958184, 0.00660988584837),
                triggerBin(70.0, 0.855337078652, 0.0131827880066),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byLooseCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronMediumMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronMediumMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0216274668829, 0.0011958667542),
                triggerBin(25.0, 0.0321872713972, 0.0015912273461),
                triggerBin(29.0, 0.0810527236163, 0.00255195518484),
                triggerBin(33.0, 0.452230596863, 0.00502304816284),
                triggerBin(37.0, 0.738573093358, 0.00500010202053),
                triggerBin(41.0, 0.779712492407, 0.0058971566958),
                triggerBin(45.0, 0.801404853129, 0.00712852083048),
                triggerBin(50.0, 0.804648241206, 0.00993665392182),
                triggerBin(55.0, 0.75719649562, 0.0151690500164),
                triggerBin(60.0, 0.771597633136, 0.0144416690702),
                triggerBin(70.0, 0.836565096953, 0.0194611578142),
                triggerBin(80.0, 0.772532188841, 0.0274625149161),
                triggerBin(100.0, 0.736486486486, 0.0362120389968),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224190923884, 0.00140756526753),
                triggerBin(25.0, 0.033018355599, 0.00186220618078),
                triggerBin(29.0, 0.0791400348635, 0.00291017749159),
                triggerBin(33.0, 0.472388465724, 0.00582242675483),
                triggerBin(37.0, 0.776421346355, 0.00550218333934),
                triggerBin(41.0, 0.825229605619, 0.00624170337776),
                triggerBin(45.0, 0.829684763573, 0.00786566160705),
                triggerBin(50.0, 0.850420168067, 0.0103390304721),
                triggerBin(55.0, 0.839344262295, 0.014868024423),
                triggerBin(60.0, 0.812006319115, 0.0155292140138),
                triggerBin(70.0, 0.851711026616, 0.0219140521055),
                triggerBin(80.0, 0.854838709677, 0.0258292043299),
                triggerBin(100.0, 0.819047619048, 0.0375700763374),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0129183793306, 0.00273635994888),
                triggerBin(25.0, 0.0416666666667, 0.00545070956742),
                triggerBin(29.0, 0.0523672883788, 0.00596648671864),
                triggerBin(33.0, 0.479853479853, 0.015118400771),
                triggerBin(37.0, 0.748414376321, 0.0141080958884),
                triggerBin(41.0, 0.825515947467, 0.0164390606968),
                triggerBin(45.0, 0.793785310734, 0.0215035269211),
                triggerBin(50.0, 0.837837837838, 0.0270999746011),
                triggerBin(55.0, 0.928571428571, 0.0260154056816),
                triggerBin(60.0, 0.733333333333, 0.0466137265853),
                triggerBin(70.0, 0.761904761905, 0.0657205294612),
                triggerBin(80.0, 0.827586206897, 0.0701445003746),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0241478790469, 0.0015867802176),
                triggerBin(25.0, 0.0315401246344, 0.00197096258796),
                triggerBin(29.0, 0.0843156289003, 0.00327211979321),
                triggerBin(33.0, 0.471086261981, 0.00630892663075),
                triggerBin(37.0, 0.781954887218, 0.00596742482641),
                triggerBin(41.0, 0.825181445251, 0.00674694811188),
                triggerBin(45.0, 0.836269430052, 0.00842285536156),
                triggerBin(50.0, 0.852736318408, 0.0111782077291),
                triggerBin(55.0, 0.822265625, 0.01689494579),
                triggerBin(60.0, 0.825046040516, 0.0163042589847),
                triggerBin(70.0, 0.868778280543, 0.0227123045368),
                triggerBin(80.0, 0.859872611465, 0.0277031240067),
                triggerBin(100.0, 0.865979381443, 0.0345902513467),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0208891269416, 0.00234039372195),
                triggerBin(25.0, 0.0406976744186, 0.00355109318774),
                triggerBin(29.0, 0.102048022599, 0.00568829652902),
                triggerBin(33.0, 0.477291159773, 0.0100583115086),
                triggerBin(37.0, 0.785319255907, 0.00920666365795),
                triggerBin(41.0, 0.823767178658, 0.0108333004838),
                triggerBin(45.0, 0.849056603774, 0.0122935540405),
                triggerBin(50.0, 0.805970149254, 0.0197233520562),
                triggerBin(55.0, 0.777777777778, 0.0302406141084),
                triggerBin(60.0, 0.801886792453, 0.0273744444712),
                triggerBin(70.0, 0.897959183673, 0.0305775174394),
                triggerBin(80.0, 0.851063829787, 0.0519316628328),
                triggerBin(100.0, 0.53488372093, 0.0760634872547),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0196130753836, 0.00113258495323),
                triggerBin(25.0, 0.0403954320777, 0.0018175620251),
                triggerBin(29.0, 0.0882352941176, 0.00268587735021),
                triggerBin(33.0, 0.470471266653, 0.00497686089352),
                triggerBin(37.0, 0.773385518591, 0.00478173790383),
                triggerBin(41.0, 0.834090909091, 0.00534710983305),
                triggerBin(45.0, 0.835058011916, 0.00657198670859),
                triggerBin(50.0, 0.826199740597, 0.00964996082849),
                triggerBin(55.0, 0.842170160296, 0.0128021837207),
                triggerBin(60.0, 0.868711656442, 0.0118296556953),
                triggerBin(70.0, 0.812307692308, 0.0216591714683),
                triggerBin(80.0, 0.877394636015, 0.0203016795926),
                triggerBin(100.0, 0.786666666667, 0.033448689284),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240853364224, 0.00106514409941),
                triggerBin(25.0, 0.0333399880216, 0.00113438135163),
                triggerBin(29.0, 0.0764071541294, 0.00152319758491),
                triggerBin(33.0, 0.53407658106, 0.0028734379497),
                triggerBin(37.0, 0.857166037889, 0.00222859395679),
                triggerBin(41.0, 0.875476009139, 0.00263042336864),
                triggerBin(45.0, 0.884826514759, 0.00324884640385),
                triggerBin(50.0, 0.887280493593, 0.00487172472289),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.907484890748, 0.00624749373502),
                triggerBin(70.0, 0.852972972973, 0.0116438166099),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240853364224, 0.00106514409941),
                triggerBin(25.0, 0.0333399880216, 0.00113438135163),
                triggerBin(29.0, 0.0764071541294, 0.00152319758491),
                triggerBin(33.0, 0.53407658106, 0.0028734379497),
                triggerBin(37.0, 0.857166037889, 0.00222859395679),
                triggerBin(41.0, 0.875476009139, 0.00263042336864),
                triggerBin(45.0, 0.884826514759, 0.00324884640385),
                triggerBin(50.0, 0.887280493593, 0.00487172472289),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.907484890748, 0.00624749373502),
                triggerBin(70.0, 0.852972972973, 0.0116438166099),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240853364224, 0.00106514409941),
                triggerBin(25.0, 0.0333399880216, 0.00113438135163),
                triggerBin(29.0, 0.0764071541294, 0.00152319758491),
                triggerBin(33.0, 0.53407658106, 0.0028734379497),
                triggerBin(37.0, 0.857166037889, 0.00222859395679),
                triggerBin(41.0, 0.875476009139, 0.00263042336864),
                triggerBin(45.0, 0.884826514759, 0.00324884640385),
                triggerBin(50.0, 0.887280493593, 0.00487172472289),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.907484890748, 0.00624749373502),
                triggerBin(70.0, 0.852972972973, 0.0116438166099),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240853364224, 0.00106514409941),
                triggerBin(25.0, 0.0333399880216, 0.00113438135163),
                triggerBin(29.0, 0.0764071541294, 0.00152319758491),
                triggerBin(33.0, 0.53407658106, 0.0028734379497),
                triggerBin(37.0, 0.857166037889, 0.00222859395679),
                triggerBin(41.0, 0.875476009139, 0.00263042336864),
                triggerBin(45.0, 0.884826514759, 0.00324884640385),
                triggerBin(50.0, 0.887280493593, 0.00487172472289),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.907484890748, 0.00624749373502),
                triggerBin(70.0, 0.852972972973, 0.0116438166099),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240853364224, 0.00106514409941),
                triggerBin(25.0, 0.0333399880216, 0.00113438135163),
                triggerBin(29.0, 0.0764071541294, 0.00152319758491),
                triggerBin(33.0, 0.53407658106, 0.0028734379497),
                triggerBin(37.0, 0.857166037889, 0.00222859395679),
                triggerBin(41.0, 0.875476009139, 0.00263042336864),
                triggerBin(45.0, 0.884826514759, 0.00324884640385),
                triggerBin(50.0, 0.887280493593, 0.00487172472289),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.907484890748, 0.00624749373502),
                triggerBin(70.0, 0.852972972973, 0.0116438166099),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240853364224, 0.00106514409941),
                triggerBin(25.0, 0.0333399880216, 0.00113438135163),
                triggerBin(29.0, 0.0764071541294, 0.00152319758491),
                triggerBin(33.0, 0.53407658106, 0.0028734379497),
                triggerBin(37.0, 0.857166037889, 0.00222859395679),
                triggerBin(41.0, 0.875476009139, 0.00263042336864),
                triggerBin(45.0, 0.884826514759, 0.00324884640385),
                triggerBin(50.0, 0.887280493593, 0.00487172472289),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.907484890748, 0.00624749373502),
                triggerBin(70.0, 0.852972972973, 0.0116438166099),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240853364224, 0.00106514409941),
                triggerBin(25.0, 0.0333399880216, 0.00113438135163),
                triggerBin(29.0, 0.0764071541294, 0.00152319758491),
                triggerBin(33.0, 0.53407658106, 0.0028734379497),
                triggerBin(37.0, 0.857166037889, 0.00222859395679),
                triggerBin(41.0, 0.875476009139, 0.00263042336864),
                triggerBin(45.0, 0.884826514759, 0.00324884640385),
                triggerBin(50.0, 0.887280493593, 0.00487172472289),
                triggerBin(55.0, 0.87757909216, 0.00701848052294),
                triggerBin(60.0, 0.907484890748, 0.00624749373502),
                triggerBin(70.0, 0.852972972973, 0.0116438166099),
                triggerBin(80.0, 0.87399463807, 0.0121500896793),
                triggerBin(100.0, 0.854700854701, 0.0162897970056),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byMediumCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronMediumMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronMediumMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.025641025641, 0.00163717814033),
                triggerBin(25.0, 0.0350042688133, 0.00202975097196),
                triggerBin(29.0, 0.0764235764236, 0.00296884870129),
                triggerBin(33.0, 0.453378001117, 0.00588160678112),
                triggerBin(37.0, 0.772555746141, 0.00548994660851),
                triggerBin(41.0, 0.805504101614, 0.00643873655048),
                triggerBin(45.0, 0.831168831169, 0.00779408159476),
                triggerBin(50.0, 0.836718115353, 0.0105348792389),
                triggerBin(55.0, 0.781818181818, 0.0167913059163),
                triggerBin(60.0, 0.793984962406, 0.0156835645921),
                triggerBin(70.0, 0.852941176471, 0.0214743799088),
                triggerBin(80.0, 0.792929292929, 0.0287967826963),
                triggerBin(100.0, 0.728070175439, 0.0416737532649),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0267920763859, 0.00192765924804),
                triggerBin(25.0, 0.0343312723723, 0.00232253760971),
                triggerBin(29.0, 0.0750372701673, 0.00339070527593),
                triggerBin(33.0, 0.469877277798, 0.00680565661745),
                triggerBin(37.0, 0.809844439285, 0.0059795414585),
                triggerBin(41.0, 0.857294994675, 0.00659008966419),
                triggerBin(45.0, 0.86530366807, 0.00837174578791),
                triggerBin(50.0, 0.872043010753, 0.0109536657658),
                triggerBin(55.0, 0.861407249467, 0.0159546799541),
                triggerBin(60.0, 0.835341365462, 0.016619179454),
                triggerBin(70.0, 0.859296482412, 0.0246488950822),
                triggerBin(80.0, 0.903225806452, 0.0237471830603),
                triggerBin(100.0, 0.7875, 0.0457361659412),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0173357664234, 0.00394247384565),
                triggerBin(25.0, 0.039627039627, 0.00665996784866),
                triggerBin(29.0, 0.0581162324649, 0.00740597278247),
                triggerBin(33.0, 0.484510532838, 0.0175923858574),
                triggerBin(37.0, 0.78591954023, 0.0155479429339),
                triggerBin(41.0, 0.887218045113, 0.0158361112618),
                triggerBin(45.0, 0.832684824903, 0.0232831335623),
                triggerBin(50.0, 0.887323943662, 0.0265346123503),
                triggerBin(55.0, 0.971428571429, 0.0199123443553),
                triggerBin(60.0, 0.756097560976, 0.0474231135452),
                triggerBin(70.0, 0.684210526316, 0.10663920529),
                triggerBin(80.0, 0.888888888889, 0.0604812282169),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0285424759331, 0.0021640146641),
                triggerBin(25.0, 0.0334720121029, 0.0024734458326),
                triggerBin(29.0, 0.0783885691605, 0.00378641416196),
                triggerBin(33.0, 0.467293808795, 0.00737960769457),
                triggerBin(37.0, 0.81445582941, 0.00646909726521),
                triggerBin(41.0, 0.852357320099, 0.00721420799036),
                triggerBin(45.0, 0.871266002845, 0.00893160176289),
                triggerBin(50.0, 0.869289340102, 0.0120081076295),
                triggerBin(55.0, 0.842105263158, 0.0182549467268),
                triggerBin(60.0, 0.850961538462, 0.0174605323158),
                triggerBin(70.0, 0.877777777778, 0.0244135607373),
                triggerBin(80.0, 0.90625, 0.0257634881997),
                triggerBin(100.0, 0.847222222222, 0.0423996738056),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0234375, 0.00315184191586),
                triggerBin(25.0, 0.0438382854359, 0.0045185384318),
                triggerBin(29.0, 0.0984271943176, 0.0067098782876),
                triggerBin(33.0, 0.490481522956, 0.0118290690637),
                triggerBin(37.0, 0.81812212738, 0.00988437129232),
                triggerBin(41.0, 0.838877338877, 0.0118533199818),
                triggerBin(45.0, 0.86398763524, 0.0134769252333),
                triggerBin(50.0, 0.880398671096, 0.0187035671823),
                triggerBin(55.0, 0.816176470588, 0.0332141491207),
                triggerBin(60.0, 0.838323353293, 0.0284886056239),
                triggerBin(70.0, 0.917808219178, 0.0321461329375),
                triggerBin(80.0, 0.837209302326, 0.0562985989385),
                triggerBin(100.0, 0.588235294118, 0.0844035357623),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0212720922849, 0.00148437340883),
                triggerBin(25.0, 0.0395778364116, 0.00218538450275),
                triggerBin(29.0, 0.083875, 0.00309919312836),
                triggerBin(33.0, 0.467582710779, 0.00576289236493),
                triggerBin(37.0, 0.797964113182, 0.00527401973884),
                triggerBin(41.0, 0.857142857143, 0.00575587831447),
                triggerBin(45.0, 0.852905323039, 0.00713991569757),
                triggerBin(50.0, 0.849267872524, 0.0105004800031),
                triggerBin(55.0, 0.858075040783, 0.0140948931069),
                triggerBin(60.0, 0.895093062606, 0.0126049886641),
                triggerBin(70.0, 0.877118644068, 0.0213705730173),
                triggerBin(80.0, 0.913043478261, 0.0195844615853),
                triggerBin(100.0, 0.78813559322, 0.0376173733663),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240037838477, 0.00117690323743),
                triggerBin(25.0, 0.0315099324787, 0.00122194631048),
                triggerBin(29.0, 0.0728889594664, 0.00163791472957),
                triggerBin(33.0, 0.53187959232, 0.00313620947826),
                triggerBin(37.0, 0.861147358755, 0.00240394800034),
                triggerBin(41.0, 0.888829948469, 0.00273641580245),
                triggerBin(45.0, 0.894950239587, 0.00339868921362),
                triggerBin(50.0, 0.902840909091, 0.00499201640926),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.924958310172, 0.00621150444305),
                triggerBin(70.0, 0.865435356201, 0.0123950475491),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240037838477, 0.00117690323743),
                triggerBin(25.0, 0.0315099324787, 0.00122194631048),
                triggerBin(29.0, 0.0728889594664, 0.00163791472957),
                triggerBin(33.0, 0.53187959232, 0.00313620947826),
                triggerBin(37.0, 0.861147358755, 0.00240394800034),
                triggerBin(41.0, 0.888829948469, 0.00273641580245),
                triggerBin(45.0, 0.894950239587, 0.00339868921362),
                triggerBin(50.0, 0.902840909091, 0.00499201640926),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.924958310172, 0.00621150444305),
                triggerBin(70.0, 0.865435356201, 0.0123950475491),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240037838477, 0.00117690323743),
                triggerBin(25.0, 0.0315099324787, 0.00122194631048),
                triggerBin(29.0, 0.0728889594664, 0.00163791472957),
                triggerBin(33.0, 0.53187959232, 0.00313620947826),
                triggerBin(37.0, 0.861147358755, 0.00240394800034),
                triggerBin(41.0, 0.888829948469, 0.00273641580245),
                triggerBin(45.0, 0.894950239587, 0.00339868921362),
                triggerBin(50.0, 0.902840909091, 0.00499201640926),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.924958310172, 0.00621150444305),
                triggerBin(70.0, 0.865435356201, 0.0123950475491),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240037838477, 0.00117690323743),
                triggerBin(25.0, 0.0315099324787, 0.00122194631048),
                triggerBin(29.0, 0.0728889594664, 0.00163791472957),
                triggerBin(33.0, 0.53187959232, 0.00313620947826),
                triggerBin(37.0, 0.861147358755, 0.00240394800034),
                triggerBin(41.0, 0.888829948469, 0.00273641580245),
                triggerBin(45.0, 0.894950239587, 0.00339868921362),
                triggerBin(50.0, 0.902840909091, 0.00499201640926),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.924958310172, 0.00621150444305),
                triggerBin(70.0, 0.865435356201, 0.0123950475491),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240037838477, 0.00117690323743),
                triggerBin(25.0, 0.0315099324787, 0.00122194631048),
                triggerBin(29.0, 0.0728889594664, 0.00163791472957),
                triggerBin(33.0, 0.53187959232, 0.00313620947826),
                triggerBin(37.0, 0.861147358755, 0.00240394800034),
                triggerBin(41.0, 0.888829948469, 0.00273641580245),
                triggerBin(45.0, 0.894950239587, 0.00339868921362),
                triggerBin(50.0, 0.902840909091, 0.00499201640926),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.924958310172, 0.00621150444305),
                triggerBin(70.0, 0.865435356201, 0.0123950475491),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240037838477, 0.00117690323743),
                triggerBin(25.0, 0.0315099324787, 0.00122194631048),
                triggerBin(29.0, 0.0728889594664, 0.00163791472957),
                triggerBin(33.0, 0.53187959232, 0.00313620947826),
                triggerBin(37.0, 0.861147358755, 0.00240394800034),
                triggerBin(41.0, 0.888829948469, 0.00273641580245),
                triggerBin(45.0, 0.894950239587, 0.00339868921362),
                triggerBin(50.0, 0.902840909091, 0.00499201640926),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.924958310172, 0.00621150444305),
                triggerBin(70.0, 0.865435356201, 0.0123950475491),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0240037838477, 0.00117690323743),
                triggerBin(25.0, 0.0315099324787, 0.00122194631048),
                triggerBin(29.0, 0.0728889594664, 0.00163791472957),
                triggerBin(33.0, 0.53187959232, 0.00313620947826),
                triggerBin(37.0, 0.861147358755, 0.00240394800034),
                triggerBin(41.0, 0.888829948469, 0.00273641580245),
                triggerBin(45.0, 0.894950239587, 0.00339868921362),
                triggerBin(50.0, 0.902840909091, 0.00499201640926),
                triggerBin(55.0, 0.881149806523, 0.00760861375744),
                triggerBin(60.0, 0.924958310172, 0.00621150444305),
                triggerBin(70.0, 0.865435356201, 0.0123950475491),
                triggerBin(80.0, 0.885167464115, 0.0127324338502),
                triggerBin(100.0, 0.858942065491, 0.0174696998298),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byTightCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronMediumMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronMediumMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0266261398176, 0.00177511294203),
                triggerBin(25.0, 0.0339931740614, 0.00211729875491),
                triggerBin(29.0, 0.0738124913447, 0.00307691656037),
                triggerBin(33.0, 0.453567641266, 0.00612751481613),
                triggerBin(37.0, 0.776617564796, 0.00568753675768),
                triggerBin(41.0, 0.802620336087, 0.00671724003137),
                triggerBin(45.0, 0.828934967012, 0.0081746310946),
                triggerBin(50.0, 0.855251544572, 0.0104529517987),
                triggerBin(55.0, 0.793418647166, 0.0173102403089),
                triggerBin(60.0, 0.807560137457, 0.0163408055974),
                triggerBin(70.0, 0.853281853282, 0.0219855983172),
                triggerBin(80.0, 0.809248554913, 0.0298711424611),
                triggerBin(100.0, 0.728971962617, 0.0429705224256),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0274858528698, 0.00207889579398),
                triggerBin(25.0, 0.0342950462711, 0.00245144819875),
                triggerBin(29.0, 0.0725865880619, 0.00352163999946),
                triggerBin(33.0, 0.470030272452, 0.00709033274623),
                triggerBin(37.0, 0.814018218623, 0.00618933224155),
                triggerBin(41.0, 0.854857142857, 0.00687511477066),
                triggerBin(45.0, 0.861799217731, 0.00881141423906),
                triggerBin(50.0, 0.890058479532, 0.0106981105915),
                triggerBin(55.0, 0.872340425532, 0.0162255531704),
                triggerBin(60.0, 0.858156028369, 0.0169636141929),
                triggerBin(70.0, 0.862433862434, 0.0250546170973),
                triggerBin(80.0, 0.895833333333, 0.0254563859351),
                triggerBin(100.0, 0.773333333333, 0.0483444431676),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0179135932561, 0.00430559422812),
                triggerBin(25.0, 0.0446780551905, 0.00748910084753),
                triggerBin(29.0, 0.0568927789934, 0.00766189173781),
                triggerBin(33.0, 0.488095238095, 0.018179669027),
                triggerBin(37.0, 0.792511700468, 0.0160166111651),
                triggerBin(41.0, 0.885941644562, 0.0163717625015),
                triggerBin(45.0, 0.831932773109, 0.024238020877),
                triggerBin(50.0, 0.893129770992, 0.0269929285565),
                triggerBin(55.0, 0.967741935484, 0.0224389788271),
                triggerBin(60.0, 0.788732394366, 0.048445352463),
                triggerBin(70.0, 0.684210526316, 0.10663920529),
                triggerBin(80.0, 0.875, 0.0675077156084),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0292207792208, 0.00232758909302),
                triggerBin(25.0, 0.0326315789474, 0.00257791261959),
                triggerBin(29.0, 0.075764288879, 0.00393860901661),
                triggerBin(33.0, 0.466777804239, 0.00769903458454),
                triggerBin(37.0, 0.818181818182, 0.00670291908846),
                triggerBin(41.0, 0.849644128114, 0.00753842421951),
                triggerBin(45.0, 0.867283950617, 0.00942409980387),
                triggerBin(50.0, 0.889502762431, 0.0116514527382),
                triggerBin(55.0, 0.85595567867, 0.0184807719813),
                triggerBin(60.0, 0.872159090909, 0.0177976003118),
                triggerBin(70.0, 0.882352941176, 0.0247108250123),
                triggerBin(80.0, 0.9, 0.0273861278753),
                triggerBin(100.0, 0.835820895522, 0.0452562069843),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0254901960784, 0.0034895113135),
                triggerBin(25.0, 0.0407938257993, 0.00464445286706),
                triggerBin(29.0, 0.0936977133296, 0.00688194011504),
                triggerBin(33.0, 0.494532199271, 0.0123233595359),
                triggerBin(37.0, 0.824238128987, 0.0101326998252),
                triggerBin(41.0, 0.84085778781, 0.0122895819489),
                triggerBin(45.0, 0.865646258503, 0.0140639219549),
                triggerBin(50.0, 0.902877697842, 0.0177603511799),
                triggerBin(55.0, 0.838709677419, 0.0330292825143),
                triggerBin(60.0, 0.830188679245, 0.029776466595),
                triggerBin(70.0, 0.914285714286, 0.0334594310725),
                triggerBin(80.0, 0.931034482759, 0.0470543613256),
                triggerBin(100.0, 0.625, 0.0855816496102),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229995208433, 0.00164064856241),
                triggerBin(25.0, 0.0410076976907, 0.00234606012273),
                triggerBin(29.0, 0.0816326530612, 0.00321522429487),
                triggerBin(33.0, 0.463778614894, 0.0060026075091),
                triggerBin(37.0, 0.800189933523, 0.00551069070307),
                triggerBin(41.0, 0.860123420511, 0.00594595905073),
                triggerBin(45.0, 0.857142857143, 0.00732520469578),
                triggerBin(50.0, 0.849391955098, 0.0109392942532),
                triggerBin(55.0, 0.860383944154, 0.014478931724),
                triggerBin(60.0, 0.90676416819, 0.0124321126524),
                triggerBin(70.0, 0.883177570093, 0.0219573662705),
                triggerBin(80.0, 0.903743315508, 0.0215683635399),
                triggerBin(100.0, 0.798165137615, 0.0384442346892),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0238337358587, 0.00121601346885),
                triggerBin(25.0, 0.0313603541875, 0.00126532939234),
                triggerBin(29.0, 0.0733316309159, 0.00170063406758),
                triggerBin(33.0, 0.531398928767, 0.00324068665383),
                triggerBin(37.0, 0.861403959887, 0.00247784918406),
                triggerBin(41.0, 0.889202256245, 0.00281760328904),
                triggerBin(45.0, 0.895341250163, 0.00349689551024),
                triggerBin(50.0, 0.901570048309, 0.00517628535173),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.921650717703, 0.00657177305699),
                triggerBin(70.0, 0.858956276446, 0.013071917358),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0238337358587, 0.00121601346885),
                triggerBin(25.0, 0.0313603541875, 0.00126532939234),
                triggerBin(29.0, 0.0733316309159, 0.00170063406758),
                triggerBin(33.0, 0.531398928767, 0.00324068665383),
                triggerBin(37.0, 0.861403959887, 0.00247784918406),
                triggerBin(41.0, 0.889202256245, 0.00281760328904),
                triggerBin(45.0, 0.895341250163, 0.00349689551024),
                triggerBin(50.0, 0.901570048309, 0.00517628535173),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.921650717703, 0.00657177305699),
                triggerBin(70.0, 0.858956276446, 0.013071917358),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0238337358587, 0.00121601346885),
                triggerBin(25.0, 0.0313603541875, 0.00126532939234),
                triggerBin(29.0, 0.0733316309159, 0.00170063406758),
                triggerBin(33.0, 0.531398928767, 0.00324068665383),
                triggerBin(37.0, 0.861403959887, 0.00247784918406),
                triggerBin(41.0, 0.889202256245, 0.00281760328904),
                triggerBin(45.0, 0.895341250163, 0.00349689551024),
                triggerBin(50.0, 0.901570048309, 0.00517628535173),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.921650717703, 0.00657177305699),
                triggerBin(70.0, 0.858956276446, 0.013071917358),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0238337358587, 0.00121601346885),
                triggerBin(25.0, 0.0313603541875, 0.00126532939234),
                triggerBin(29.0, 0.0733316309159, 0.00170063406758),
                triggerBin(33.0, 0.531398928767, 0.00324068665383),
                triggerBin(37.0, 0.861403959887, 0.00247784918406),
                triggerBin(41.0, 0.889202256245, 0.00281760328904),
                triggerBin(45.0, 0.895341250163, 0.00349689551024),
                triggerBin(50.0, 0.901570048309, 0.00517628535173),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.921650717703, 0.00657177305699),
                triggerBin(70.0, 0.858956276446, 0.013071917358),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0238337358587, 0.00121601346885),
                triggerBin(25.0, 0.0313603541875, 0.00126532939234),
                triggerBin(29.0, 0.0733316309159, 0.00170063406758),
                triggerBin(33.0, 0.531398928767, 0.00324068665383),
                triggerBin(37.0, 0.861403959887, 0.00247784918406),
                triggerBin(41.0, 0.889202256245, 0.00281760328904),
                triggerBin(45.0, 0.895341250163, 0.00349689551024),
                triggerBin(50.0, 0.901570048309, 0.00517628535173),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.921650717703, 0.00657177305699),
                triggerBin(70.0, 0.858956276446, 0.013071917358),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0238337358587, 0.00121601346885),
                triggerBin(25.0, 0.0313603541875, 0.00126532939234),
                triggerBin(29.0, 0.0733316309159, 0.00170063406758),
                triggerBin(33.0, 0.531398928767, 0.00324068665383),
                triggerBin(37.0, 0.861403959887, 0.00247784918406),
                triggerBin(41.0, 0.889202256245, 0.00281760328904),
                triggerBin(45.0, 0.895341250163, 0.00349689551024),
                triggerBin(50.0, 0.901570048309, 0.00517628535173),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.921650717703, 0.00657177305699),
                triggerBin(70.0, 0.858956276446, 0.013071917358),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0238337358587, 0.00121601346885),
                triggerBin(25.0, 0.0313603541875, 0.00126532939234),
                triggerBin(29.0, 0.0733316309159, 0.00170063406758),
                triggerBin(33.0, 0.531398928767, 0.00324068665383),
                triggerBin(37.0, 0.861403959887, 0.00247784918406),
                triggerBin(41.0, 0.889202256245, 0.00281760328904),
                triggerBin(45.0, 0.895341250163, 0.00349689551024),
                triggerBin(50.0, 0.901570048309, 0.00517628535173),
                triggerBin(55.0, 0.880994671403, 0.0078787082715),
                triggerBin(60.0, 0.921650717703, 0.00657177305699),
                triggerBin(70.0, 0.858956276446, 0.013071917358),
                triggerBin(80.0, 0.88, 0.0135518328618),
                triggerBin(100.0, 0.851458885942, 0.0183161631953),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byLooseCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronTightMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0216894186127, 0.00121259037735),
                triggerBin(25.0, 0.0296852341551, 0.0015674986561),
                triggerBin(29.0, 0.0795918367347, 0.00260684442803),
                triggerBin(33.0, 0.45884013901, 0.00519291046075),
                triggerBin(37.0, 0.74809054298, 0.00511567461008),
                triggerBin(41.0, 0.785355191257, 0.00607012598464),
                triggerBin(45.0, 0.808406304729, 0.00736550275911),
                triggerBin(50.0, 0.812718378756, 0.0103133036277),
                triggerBin(55.0, 0.763983628922, 0.0156841541876),
                triggerBin(60.0, 0.788387096774, 0.0146720221978),
                triggerBin(70.0, 0.859375, 0.019433348381),
                triggerBin(80.0, 0.788461538462, 0.0283173924562),
                triggerBin(100.0, 0.755905511811, 0.038116312773),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224927967283, 0.00142953817909),
                triggerBin(25.0, 0.0299578539697, 0.00181939973488),
                triggerBin(29.0, 0.0777681767683, 0.00297544340895),
                triggerBin(33.0, 0.477995642702, 0.00602000789259),
                triggerBin(37.0, 0.786169415292, 0.00561287116074),
                triggerBin(41.0, 0.829339567504, 0.00643120882069),
                triggerBin(45.0, 0.836852207294, 0.00809405454774),
                triggerBin(50.0, 0.862453531599, 0.0104999308473),
                triggerBin(55.0, 0.839350180505, 0.0156011579103),
                triggerBin(60.0, 0.810763888889, 0.01632066927),
                triggerBin(70.0, 0.878787878788, 0.0214738079545),
                triggerBin(80.0, 0.879518072289, 0.0252655812365),
                triggerBin(100.0, 0.842696629213, 0.0385930977594),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0132930513595, 0.00281518821392),
                triggerBin(25.0, 0.0337784760408, 0.0050634226272),
                triggerBin(29.0, 0.0496941896024, 0.00600870145811),
                triggerBin(33.0, 0.491723466407, 0.0156000243113),
                triggerBin(37.0, 0.77027027027, 0.0141163912221),
                triggerBin(41.0, 0.814, 0.0174013792557),
                triggerBin(45.0, 0.805642633229, 0.0221552360655),
                triggerBin(50.0, 0.843023255814, 0.0277378766699),
                triggerBin(55.0, 0.917647058824, 0.029817273765),
                triggerBin(60.0, 0.714285714286, 0.0492903970959),
                triggerBin(70.0, 0.820512820513, 0.0614507373862),
                triggerBin(80.0, 0.827586206897, 0.0701445003746),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.024165202109, 0.00160941202449),
                triggerBin(25.0, 0.029309885425, 0.00194689748343),
                triggerBin(29.0, 0.0831738554394, 0.00335047285709),
                triggerBin(33.0, 0.475588938204, 0.00652494883765),
                triggerBin(37.0, 0.78934352518, 0.00611417749702),
                triggerBin(41.0, 0.83196440794, 0.00691692247437),
                triggerBin(45.0, 0.842492917847, 0.00867083291674),
                triggerBin(50.0, 0.866150442478, 0.011324549136),
                triggerBin(55.0, 0.825159914712, 0.0175389320134),
                triggerBin(60.0, 0.827235772358, 0.0170435089621),
                triggerBin(70.0, 0.890625, 0.0225245363177),
                triggerBin(80.0, 0.890510948905, 0.0266774733131),
                triggerBin(100.0, 0.901234567901, 0.0331496460181),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0209694989107, 0.00236450807306),
                triggerBin(25.0, 0.0370244565217, 0.00348003067501),
                triggerBin(29.0, 0.0992907801418, 0.00577777211916),
                triggerBin(33.0, 0.486870426173, 0.0103704025656),
                triggerBin(37.0, 0.800536193029, 0.00925301187627),
                triggerBin(41.0, 0.835212489159, 0.0109256172753),
                triggerBin(45.0, 0.857328145266, 0.0125955026973),
                triggerBin(50.0, 0.802816901408, 0.021116839567),
                triggerBin(55.0, 0.793296089385, 0.0302667289678),
                triggerBin(60.0, 0.854271356784, 0.0250117365177),
                triggerBin(70.0, 0.921348314607, 0.0285345439731),
                triggerBin(80.0, 0.880952380952, 0.0499702967597),
                triggerBin(100.0, 0.552631578947, 0.08066009202),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.019390202124, 0.00114139832939),
                triggerBin(25.0, 0.0391424250512, 0.00182915664692),
                triggerBin(29.0, 0.0863078375826, 0.00272883381157),
                triggerBin(33.0, 0.475151001378, 0.0051406262951),
                triggerBin(37.0, 0.784734982332, 0.0048863549804),
                triggerBin(41.0, 0.841825431989, 0.00543123472143),
                triggerBin(45.0, 0.847544338336, 0.00663851604322),
                triggerBin(50.0, 0.841989758595, 0.00986533336987),
                triggerBin(55.0, 0.868918918919, 0.0124063427143),
                triggerBin(60.0, 0.879240162822, 0.0120027642057),
                triggerBin(70.0, 0.839869281046, 0.0209644011839),
                triggerBin(80.0, 0.927272727273, 0.0175081820521),
                triggerBin(100.0, 0.837209302326, 0.0325040112522),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0228789323165, 0.00105907696154),
                triggerBin(25.0, 0.0288509994961, 0.00108473943369),
                triggerBin(29.0, 0.0733016939758, 0.00153400001563),
                triggerBin(33.0, 0.534952040491, 0.00296738577912),
                triggerBin(37.0, 0.862856646545, 0.00226692956371),
                triggerBin(41.0, 0.880746534925, 0.0026845505893),
                triggerBin(45.0, 0.890311614731, 0.00332654945313),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.910597689603, 0.00639443258645),
                triggerBin(70.0, 0.877171215881, 0.0115617810707),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0228789323165, 0.00105907696154),
                triggerBin(25.0, 0.0288509994961, 0.00108473943369),
                triggerBin(29.0, 0.0733016939758, 0.00153400001563),
                triggerBin(33.0, 0.534952040491, 0.00296738577912),
                triggerBin(37.0, 0.862856646545, 0.00226692956371),
                triggerBin(41.0, 0.880746534925, 0.0026845505893),
                triggerBin(45.0, 0.890311614731, 0.00332654945313),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.910597689603, 0.00639443258645),
                triggerBin(70.0, 0.877171215881, 0.0115617810707),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0228789323165, 0.00105907696154),
                triggerBin(25.0, 0.0288509994961, 0.00108473943369),
                triggerBin(29.0, 0.0733016939758, 0.00153400001563),
                triggerBin(33.0, 0.534952040491, 0.00296738577912),
                triggerBin(37.0, 0.862856646545, 0.00226692956371),
                triggerBin(41.0, 0.880746534925, 0.0026845505893),
                triggerBin(45.0, 0.890311614731, 0.00332654945313),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.910597689603, 0.00639443258645),
                triggerBin(70.0, 0.877171215881, 0.0115617810707),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0228789323165, 0.00105907696154),
                triggerBin(25.0, 0.0288509994961, 0.00108473943369),
                triggerBin(29.0, 0.0733016939758, 0.00153400001563),
                triggerBin(33.0, 0.534952040491, 0.00296738577912),
                triggerBin(37.0, 0.862856646545, 0.00226692956371),
                triggerBin(41.0, 0.880746534925, 0.0026845505893),
                triggerBin(45.0, 0.890311614731, 0.00332654945313),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.910597689603, 0.00639443258645),
                triggerBin(70.0, 0.877171215881, 0.0115617810707),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0228789323165, 0.00105907696154),
                triggerBin(25.0, 0.0288509994961, 0.00108473943369),
                triggerBin(29.0, 0.0733016939758, 0.00153400001563),
                triggerBin(33.0, 0.534952040491, 0.00296738577912),
                triggerBin(37.0, 0.862856646545, 0.00226692956371),
                triggerBin(41.0, 0.880746534925, 0.0026845505893),
                triggerBin(45.0, 0.890311614731, 0.00332654945313),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.910597689603, 0.00639443258645),
                triggerBin(70.0, 0.877171215881, 0.0115617810707),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0228789323165, 0.00105907696154),
                triggerBin(25.0, 0.0288509994961, 0.00108473943369),
                triggerBin(29.0, 0.0733016939758, 0.00153400001563),
                triggerBin(33.0, 0.534952040491, 0.00296738577912),
                triggerBin(37.0, 0.862856646545, 0.00226692956371),
                triggerBin(41.0, 0.880746534925, 0.0026845505893),
                triggerBin(45.0, 0.890311614731, 0.00332654945313),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.910597689603, 0.00639443258645),
                triggerBin(70.0, 0.877171215881, 0.0115617810707),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0228789323165, 0.00105907696154),
                triggerBin(25.0, 0.0288509994961, 0.00108473943369),
                triggerBin(29.0, 0.0733016939758, 0.00153400001563),
                triggerBin(33.0, 0.534952040491, 0.00296738577912),
                triggerBin(37.0, 0.862856646545, 0.00226692956371),
                triggerBin(41.0, 0.880746534925, 0.0026845505893),
                triggerBin(45.0, 0.890311614731, 0.00332654945313),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.910597689603, 0.00639443258645),
                triggerBin(70.0, 0.877171215881, 0.0115617810707),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byMediumCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronTightMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0254995032564, 0.00165621518711),
                triggerBin(25.0, 0.0322168243416, 0.00199651001339),
                triggerBin(29.0, 0.0751919512841, 0.00303405177623),
                triggerBin(33.0, 0.458562713882, 0.00607794130673),
                triggerBin(37.0, 0.782232848998, 0.00559737679546),
                triggerBin(41.0, 0.812019367702, 0.0065936263421),
                triggerBin(45.0, 0.839716312057, 0.00797729719903),
                triggerBin(50.0, 0.848594741614, 0.0107927692342),
                triggerBin(55.0, 0.786618444846, 0.0174219970222),
                triggerBin(60.0, 0.807504078303, 0.0159240264889),
                triggerBin(70.0, 0.885245901639, 0.0204042742298),
                triggerBin(80.0, 0.82320441989, 0.0283563456182),
                triggerBin(100.0, 0.772277227723, 0.0417281526716),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0267765190525, 0.00195805421908),
                triggerBin(25.0, 0.031228668942, 0.00227215821003),
                triggerBin(29.0, 0.073930646013, 0.00347153551168),
                triggerBin(33.0, 0.473235527359, 0.00703006547478),
                triggerBin(37.0, 0.820039880359, 0.00606492118153),
                triggerBin(41.0, 0.864523536165, 0.00669500077902),
                triggerBin(45.0, 0.874752801582, 0.00849833586045),
                triggerBin(50.0, 0.88622754491, 0.0109887413015),
                triggerBin(55.0, 0.861176470588, 0.0167719343367),
                triggerBin(60.0, 0.828571428571, 0.0176685488453),
                triggerBin(70.0, 0.892655367232, 0.0232672707962),
                triggerBin(80.0, 0.944055944056, 0.0192179837377),
                triggerBin(100.0, 0.833333333333, 0.0439205230579),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0178907721281, 0.00406754325098),
                triggerBin(25.0, 0.034398034398, 0.00638783487826),
                triggerBin(29.0, 0.0586353944563, 0.00767109637455),
                triggerBin(33.0, 0.5, 0.0180893651323),
                triggerBin(37.0, 0.805810397554, 0.0154682273125),
                triggerBin(41.0, 0.88, 0.0167809415707),
                triggerBin(45.0, 0.84388185654, 0.0235772604406),
                triggerBin(50.0, 0.878787878788, 0.0284071777746),
                triggerBin(55.0, 0.966101694915, 0.0235599523744),
                triggerBin(60.0, 0.736842105263, 0.0505113089441),
                triggerBin(70.0, 0.8125, 0.097578093725),
                triggerBin(80.0, 0.888888888889, 0.0604812282169),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0284219703575, 0.00219431626735),
                triggerBin(25.0, 0.0307173999207, 0.00242909114724),
                triggerBin(29.0, 0.0769555133882, 0.00386994349437),
                triggerBin(33.0, 0.468457943925, 0.00762750033616),
                triggerBin(37.0, 0.822811197141, 0.00658912714144),
                triggerBin(41.0, 0.861930294906, 0.00729214389999),
                triggerBin(45.0, 0.88046875, 0.00906760762418),
                triggerBin(50.0, 0.887624466572, 0.0119116754775),
                triggerBin(55.0, 0.844262295082, 0.0189537452637),
                triggerBin(60.0, 0.846965699208, 0.0184930139824),
                triggerBin(70.0, 0.900621118012, 0.0235779030938),
                triggerBin(80.0, 0.956896551724, 0.0188564314974),
                triggerBin(100.0, 0.90625, 0.0364350744261),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229885057471, 0.00315107621649),
                triggerBin(25.0, 0.0407747196738, 0.00446484409329),
                triggerBin(29.0, 0.0961025093433, 0.00681017176171),
                triggerBin(33.0, 0.502683363148, 0.0122094814316),
                triggerBin(37.0, 0.830877192982, 0.00993029330017),
                triggerBin(41.0, 0.847438752784, 0.0119988080822),
                triggerBin(45.0, 0.871237458194, 0.0136965897688),
                triggerBin(50.0, 0.884328358209, 0.0195367729309),
                triggerBin(55.0, 0.828125, 0.0333464278886),
                triggerBin(60.0, 0.886075949367, 0.0252763662717),
                triggerBin(70.0, 0.955223880597, 0.0252661116128),
                triggerBin(80.0, 0.868421052632, 0.0548361022017),
                triggerBin(100.0, 0.620689655172, 0.0901022421425),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0210993291495, 0.00149492930206),
                triggerBin(25.0, 0.0385222193006, 0.00220671941129),
                triggerBin(29.0, 0.0818528753783, 0.0031448134415),
                triggerBin(33.0, 0.471660495585, 0.00595718217259),
                triggerBin(37.0, 0.811127651656, 0.0053392463875),
                triggerBin(41.0, 0.863965267728, 0.00583242307001),
                triggerBin(45.0, 0.863395225464, 0.0072209021589),
                triggerBin(50.0, 0.864734299517, 0.0106307770657),
                triggerBin(55.0, 0.876543209877, 0.0138150552475),
                triggerBin(60.0, 0.909259259259, 0.0123608445947),
                triggerBin(70.0, 0.908256880734, 0.0195507243505),
                triggerBin(80.0, 0.943181818182, 0.017449582574),
                triggerBin(100.0, 0.843137254902, 0.0360088257561),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0226895406752, 0.00116769331641),
                triggerBin(25.0, 0.026651574398, 0.00115529303437),
                triggerBin(29.0, 0.0693462712786, 0.00164295213825),
                triggerBin(33.0, 0.53159866953, 0.00323787480822),
                triggerBin(37.0, 0.866828713281, 0.00244336654772),
                triggerBin(41.0, 0.894465367611, 0.00278003528414),
                triggerBin(45.0, 0.900295619457, 0.00347300057698),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.929129129129, 0.00628875685509),
                triggerBin(70.0, 0.890243902439, 0.0122044134741),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0226895406752, 0.00116769331641),
                triggerBin(25.0, 0.026651574398, 0.00115529303437),
                triggerBin(29.0, 0.0693462712786, 0.00164295213825),
                triggerBin(33.0, 0.53159866953, 0.00323787480822),
                triggerBin(37.0, 0.866828713281, 0.00244336654772),
                triggerBin(41.0, 0.894465367611, 0.00278003528414),
                triggerBin(45.0, 0.900295619457, 0.00347300057698),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.929129129129, 0.00628875685509),
                triggerBin(70.0, 0.890243902439, 0.0122044134741),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0226895406752, 0.00116769331641),
                triggerBin(25.0, 0.026651574398, 0.00115529303437),
                triggerBin(29.0, 0.0693462712786, 0.00164295213825),
                triggerBin(33.0, 0.53159866953, 0.00323787480822),
                triggerBin(37.0, 0.866828713281, 0.00244336654772),
                triggerBin(41.0, 0.894465367611, 0.00278003528414),
                triggerBin(45.0, 0.900295619457, 0.00347300057698),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.929129129129, 0.00628875685509),
                triggerBin(70.0, 0.890243902439, 0.0122044134741),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0226895406752, 0.00116769331641),
                triggerBin(25.0, 0.026651574398, 0.00115529303437),
                triggerBin(29.0, 0.0693462712786, 0.00164295213825),
                triggerBin(33.0, 0.53159866953, 0.00323787480822),
                triggerBin(37.0, 0.866828713281, 0.00244336654772),
                triggerBin(41.0, 0.894465367611, 0.00278003528414),
                triggerBin(45.0, 0.900295619457, 0.00347300057698),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.929129129129, 0.00628875685509),
                triggerBin(70.0, 0.890243902439, 0.0122044134741),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0226895406752, 0.00116769331641),
                triggerBin(25.0, 0.026651574398, 0.00115529303437),
                triggerBin(29.0, 0.0693462712786, 0.00164295213825),
                triggerBin(33.0, 0.53159866953, 0.00323787480822),
                triggerBin(37.0, 0.866828713281, 0.00244336654772),
                triggerBin(41.0, 0.894465367611, 0.00278003528414),
                triggerBin(45.0, 0.900295619457, 0.00347300057698),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.929129129129, 0.00628875685509),
                triggerBin(70.0, 0.890243902439, 0.0122044134741),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0226895406752, 0.00116769331641),
                triggerBin(25.0, 0.026651574398, 0.00115529303437),
                triggerBin(29.0, 0.0693462712786, 0.00164295213825),
                triggerBin(33.0, 0.53159866953, 0.00323787480822),
                triggerBin(37.0, 0.866828713281, 0.00244336654772),
                triggerBin(41.0, 0.894465367611, 0.00278003528414),
                triggerBin(45.0, 0.900295619457, 0.00347300057698),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.929129129129, 0.00628875685509),
                triggerBin(70.0, 0.890243902439, 0.0122044134741),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0226895406752, 0.00116769331641),
                triggerBin(25.0, 0.026651574398, 0.00115529303437),
                triggerBin(29.0, 0.0693462712786, 0.00164295213825),
                triggerBin(33.0, 0.53159866953, 0.00323787480822),
                triggerBin(37.0, 0.866828713281, 0.00244336654772),
                triggerBin(41.0, 0.894465367611, 0.00278003528414),
                triggerBin(45.0, 0.900295619457, 0.00347300057698),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.929129129129, 0.00628875685509),
                triggerBin(70.0, 0.890243902439, 0.0122044134741),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byTightCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronTightMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0264014014014, 0.00179339404144),
                triggerBin(25.0, 0.031317031317, 0.00208280859514),
                triggerBin(29.0, 0.0721725099017, 0.00313417235295),
                triggerBin(33.0, 0.459045469203, 0.00632764859926),
                triggerBin(37.0, 0.788035892323, 0.00577123414151),
                triggerBin(41.0, 0.809071406681, 0.00688050597113),
                triggerBin(45.0, 0.838129496403, 0.00834964485469),
                triggerBin(50.0, 0.866273352999, 0.0106727412129),
                triggerBin(55.0, 0.80404040404, 0.0178410169067),
                triggerBin(60.0, 0.825842696629, 0.0164115229144),
                triggerBin(70.0, 0.887445887446, 0.0207943636533),
                triggerBin(80.0, 0.835443037975, 0.0294976901342),
                triggerBin(100.0, 0.776595744681, 0.0429614862188),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.027397260274, 0.00210985668299),
                triggerBin(25.0, 0.0309768148993, 0.00238841638883),
                triggerBin(29.0, 0.0705905357841, 0.00358175950916),
                triggerBin(33.0, 0.473819742489, 0.00731443681099),
                triggerBin(37.0, 0.826464208243, 0.0062360716979),
                triggerBin(41.0, 0.861361771944, 0.00699870109176),
                triggerBin(45.0, 0.872675250358, 0.00891516035988),
                triggerBin(50.0, 0.905071521456, 0.010570037794),
                triggerBin(55.0, 0.878627968338, 0.0167742154807),
                triggerBin(60.0, 0.854166666667, 0.0180108454177),
                triggerBin(70.0, 0.898203592814, 0.0233988968814),
                triggerBin(80.0, 0.939393939394, 0.0207680126316),
                triggerBin(100.0, 0.820895522388, 0.0468446246795),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0185792349727, 0.00446406991647),
                triggerBin(25.0, 0.0387811634349, 0.00718543317122),
                triggerBin(29.0, 0.0570430733411, 0.00791317560936),
                triggerBin(33.0, 0.502793296089, 0.0186855857233),
                triggerBin(37.0, 0.81561461794, 0.0158054730492),
                triggerBin(41.0, 0.879213483146, 0.0172715533969),
                triggerBin(45.0, 0.844036697248, 0.0245733083122),
                triggerBin(50.0, 0.884297520661, 0.0290788917812),
                triggerBin(55.0, 0.960784313725, 0.0271805207876),
                triggerBin(60.0, 0.761904761905, 0.0536605876018),
                triggerBin(70.0, 0.8125, 0.097578093725),
                triggerBin(80.0, 0.875, 0.0675077156084),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.028988365214, 0.00235601078236),
                triggerBin(25.0, 0.0297356828194, 0.00252090257186),
                triggerBin(29.0, 0.0733254994125, 0.00399614592671),
                triggerBin(33.0, 0.468559837728, 0.00794586648311),
                triggerBin(37.0, 0.828580686973, 0.00678421054255),
                triggerBin(41.0, 0.858309317963, 0.00764279474776),
                triggerBin(45.0, 0.877966101695, 0.0095287978313),
                triggerBin(50.0, 0.908950617284, 0.011301111099),
                triggerBin(55.0, 0.865853658537, 0.0188180553977),
                triggerBin(60.0, 0.872274143302, 0.0186300231871),
                triggerBin(70.0, 0.907284768212, 0.0236025475085),
                triggerBin(80.0, 0.953703703704, 0.0202193868385),
                triggerBin(100.0, 0.898305084746, 0.0393491669555),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.024925224327, 0.00348075162343),
                triggerBin(25.0, 0.0387059503177, 0.00463626723196),
                triggerBin(29.0, 0.0921902524956, 0.00701023535902),
                triggerBin(33.0, 0.506485084306, 0.0127318432984),
                triggerBin(37.0, 0.836473247928, 0.0101527799167),
                triggerBin(41.0, 0.850909090909, 0.0124005283327),
                triggerBin(45.0, 0.870437956204, 0.0143455606579),
                triggerBin(50.0, 0.899193548387, 0.0191181081749),
                triggerBin(55.0, 0.853448275862, 0.0328363649719),
                triggerBin(60.0, 0.88, 0.0265329983228),
                triggerBin(70.0, 0.953125, 0.0264213852704),
                triggerBin(80.0, 0.923076923077, 0.0522589400374),
                triggerBin(100.0, 0.666666666667, 0.0907218423253),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0227690047741, 0.0016503885147),
                triggerBin(25.0, 0.0397127784291, 0.00236399308682),
                triggerBin(29.0, 0.0795817600929, 0.003261488632),
                triggerBin(33.0, 0.468282142306, 0.00619926828157),
                triggerBin(37.0, 0.812436080998, 0.00558289206768),
                triggerBin(41.0, 0.866394215655, 0.00603237828571),
                triggerBin(45.0, 0.868421052632, 0.00739409851249),
                triggerBin(50.0, 0.860612460401, 0.0112548782526),
                triggerBin(55.0, 0.877589453861, 0.0142235451288),
                triggerBin(60.0, 0.918163672655, 0.0122465639706),
                triggerBin(70.0, 0.918367346939, 0.0195574458673),
                triggerBin(80.0, 0.936708860759, 0.0193706960812),
                triggerBin(100.0, 0.860215053763, 0.0359577283245),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223559759243, 0.0012023354664),
                triggerBin(25.0, 0.0269222246842, 0.00120466581527),
                triggerBin(29.0, 0.0695816124978, 0.00170477780355),
                triggerBin(33.0, 0.53166037057, 0.00334633384661),
                triggerBin(37.0, 0.86640655053, 0.00252204916167),
                triggerBin(41.0, 0.894401813743, 0.00286979399775),
                triggerBin(45.0, 0.901201029454, 0.00356799498507),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.926022063595, 0.00666746054094),
                triggerBin(70.0, 0.882736156352, 0.012984144341),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223559759243, 0.0012023354664),
                triggerBin(25.0, 0.0269222246842, 0.00120466581527),
                triggerBin(29.0, 0.0695816124978, 0.00170477780355),
                triggerBin(33.0, 0.53166037057, 0.00334633384661),
                triggerBin(37.0, 0.86640655053, 0.00252204916167),
                triggerBin(41.0, 0.894401813743, 0.00286979399775),
                triggerBin(45.0, 0.901201029454, 0.00356799498507),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.926022063595, 0.00666746054094),
                triggerBin(70.0, 0.882736156352, 0.012984144341),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223559759243, 0.0012023354664),
                triggerBin(25.0, 0.0269222246842, 0.00120466581527),
                triggerBin(29.0, 0.0695816124978, 0.00170477780355),
                triggerBin(33.0, 0.53166037057, 0.00334633384661),
                triggerBin(37.0, 0.86640655053, 0.00252204916167),
                triggerBin(41.0, 0.894401813743, 0.00286979399775),
                triggerBin(45.0, 0.901201029454, 0.00356799498507),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.926022063595, 0.00666746054094),
                triggerBin(70.0, 0.882736156352, 0.012984144341),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223559759243, 0.0012023354664),
                triggerBin(25.0, 0.0269222246842, 0.00120466581527),
                triggerBin(29.0, 0.0695816124978, 0.00170477780355),
                triggerBin(33.0, 0.53166037057, 0.00334633384661),
                triggerBin(37.0, 0.86640655053, 0.00252204916167),
                triggerBin(41.0, 0.894401813743, 0.00286979399775),
                triggerBin(45.0, 0.901201029454, 0.00356799498507),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.926022063595, 0.00666746054094),
                triggerBin(70.0, 0.882736156352, 0.012984144341),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223559759243, 0.0012023354664),
                triggerBin(25.0, 0.0269222246842, 0.00120466581527),
                triggerBin(29.0, 0.0695816124978, 0.00170477780355),
                triggerBin(33.0, 0.53166037057, 0.00334633384661),
                triggerBin(37.0, 0.86640655053, 0.00252204916167),
                triggerBin(41.0, 0.894401813743, 0.00286979399775),
                triggerBin(45.0, 0.901201029454, 0.00356799498507),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.926022063595, 0.00666746054094),
                triggerBin(70.0, 0.882736156352, 0.012984144341),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223559759243, 0.0012023354664),
                triggerBin(25.0, 0.0269222246842, 0.00120466581527),
                triggerBin(29.0, 0.0695816124978, 0.00170477780355),
                triggerBin(33.0, 0.53166037057, 0.00334633384661),
                triggerBin(37.0, 0.86640655053, 0.00252204916167),
                triggerBin(41.0, 0.894401813743, 0.00286979399775),
                triggerBin(45.0, 0.901201029454, 0.00356799498507),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.926022063595, 0.00666746054094),
                triggerBin(70.0, 0.882736156352, 0.012984144341),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223559759243, 0.0012023354664),
                triggerBin(25.0, 0.0269222246842, 0.00120466581527),
                triggerBin(29.0, 0.0695816124978, 0.00170477780355),
                triggerBin(33.0, 0.53166037057, 0.00334633384661),
                triggerBin(37.0, 0.86640655053, 0.00252204916167),
                triggerBin(41.0, 0.894401813743, 0.00286979399775),
                triggerBin(45.0, 0.901201029454, 0.00356799498507),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.926022063595, 0.00666746054094),
                triggerBin(70.0, 0.882736156352, 0.012984144341),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byLooseCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronTightMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.021372876636, 0.00120670862109),
                triggerBin(25.0, 0.0297410477737, 0.00157040067),
                triggerBin(29.0, 0.0797027403623, 0.00261031953884),
                triggerBin(33.0, 0.459080534724, 0.0051950918348),
                triggerBin(37.0, 0.749234622878, 0.00511327440224),
                triggerBin(41.0, 0.785870516185, 0.00606681318461),
                triggerBin(45.0, 0.809055809056, 0.00736370261092),
                triggerBin(50.0, 0.812324929972, 0.0103324682745),
                triggerBin(55.0, 0.76510989011, 0.0157118955672),
                triggerBin(60.0, 0.787839586028, 0.0147048747413),
                triggerBin(70.0, 0.858044164038, 0.019602064576),
                triggerBin(80.0, 0.788461538462, 0.0283173924562),
                triggerBin(100.0, 0.755905511811, 0.038116312773),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.022597814922, 0.00143613549839),
                triggerBin(25.0, 0.0300228310502, 0.00182328485321),
                triggerBin(29.0, 0.0778258184064, 0.00297755574601),
                triggerBin(33.0, 0.478355607205, 0.00602063467368),
                triggerBin(37.0, 0.787941397446, 0.0056021648379),
                triggerBin(41.0, 0.830067271132, 0.0064231137108),
                triggerBin(45.0, 0.837824831569, 0.00808622871845),
                triggerBin(50.0, 0.862068965517, 0.0105269398426),
                triggerBin(55.0, 0.841530054645, 0.0155855487321),
                triggerBin(60.0, 0.810104529617, 0.0163708747875),
                triggerBin(70.0, 0.877192982456, 0.0217366064817),
                triggerBin(80.0, 0.879518072289, 0.0252655812365),
                triggerBin(100.0, 0.842696629213, 0.0385930977594),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0133010882709, 0.00281687879035),
                triggerBin(25.0, 0.0337784760408, 0.0050634226272),
                triggerBin(29.0, 0.0496941896024, 0.00600870145811),
                triggerBin(33.0, 0.4931640625, 0.015623539618),
                triggerBin(37.0, 0.77027027027, 0.0141163912221),
                triggerBin(41.0, 0.814, 0.0174013792557),
                triggerBin(45.0, 0.805642633229, 0.0221552360655),
                triggerBin(50.0, 0.840236686391, 0.0281835695592),
                triggerBin(55.0, 0.917647058824, 0.029817273765),
                triggerBin(60.0, 0.707317073171, 0.0502456928347),
                triggerBin(70.0, 0.820512820513, 0.0614507373862),
                triggerBin(80.0, 0.827586206897, 0.0701445003746),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0242959690779, 0.00161801273439),
                triggerBin(25.0, 0.0293842660612, 0.00195176340486),
                triggerBin(29.0, 0.0832473847061, 0.00335330034416),
                triggerBin(33.0, 0.475767918089, 0.00652394913544),
                triggerBin(37.0, 0.791478809739, 0.00609956656122),
                triggerBin(41.0, 0.832819458719, 0.00690639236737),
                triggerBin(45.0, 0.84366117112, 0.00865933493752),
                triggerBin(50.0, 0.866150442478, 0.011324549136),
                triggerBin(55.0, 0.827586206897, 0.0175361250936),
                triggerBin(60.0, 0.827235772358, 0.0170435089621),
                triggerBin(70.0, 0.888888888889, 0.0228597555499),
                triggerBin(80.0, 0.890510948905, 0.0266774733131),
                triggerBin(100.0, 0.901234567901, 0.0331496460181),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0194254445964, 0.00228287484646),
                triggerBin(25.0, 0.0370622237334, 0.00348351220685),
                triggerBin(29.0, 0.0996254681648, 0.00579617057676),
                triggerBin(33.0, 0.486836426413, 0.0103838026721),
                triggerBin(37.0, 0.800214822771, 0.00926605959761),
                triggerBin(41.0, 0.835212489159, 0.0109256172753),
                triggerBin(45.0, 0.857328145266, 0.0125955026973),
                triggerBin(50.0, 0.802816901408, 0.021116839567),
                triggerBin(55.0, 0.793296089385, 0.0302667289678),
                triggerBin(60.0, 0.854271356784, 0.0250117365177),
                triggerBin(70.0, 0.921348314607, 0.0285345439731),
                triggerBin(80.0, 0.880952380952, 0.0499702967597),
                triggerBin(100.0, 0.552631578947, 0.08066009202),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0192718012251, 0.00114055865185),
                triggerBin(25.0, 0.0387569208787, 0.00182398395879),
                triggerBin(29.0, 0.0864793263317, 0.00273399924357),
                triggerBin(33.0, 0.474605025978, 0.00514197843666),
                triggerBin(37.0, 0.7853099349, 0.00488472032439),
                triggerBin(41.0, 0.841614906832, 0.00543778344384),
                triggerBin(45.0, 0.847492323439, 0.00664057719554),
                triggerBin(50.0, 0.841989758595, 0.00986533336987),
                triggerBin(55.0, 0.868385345997, 0.0124530181862),
                triggerBin(60.0, 0.881309686221, 0.0119459288386),
                triggerBin(70.0, 0.839869281046, 0.0209644011839),
                triggerBin(80.0, 0.927272727273, 0.0175081820521),
                triggerBin(100.0, 0.837209302326, 0.0325040112522),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229157244083, 0.00106076011419),
                triggerBin(25.0, 0.0288837502628, 0.00108595248487),
                triggerBin(29.0, 0.0732958879412, 0.00153460872848),
                triggerBin(33.0, 0.535146428698, 0.00296803996838),
                triggerBin(37.0, 0.863276836158, 0.00226484134436),
                triggerBin(41.0, 0.880867416964, 0.00268355790486),
                triggerBin(45.0, 0.890614373158, 0.00332308502293),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.911513323278, 0.00636800009587),
                triggerBin(70.0, 0.880448318804, 0.0114491173162),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229157244083, 0.00106076011419),
                triggerBin(25.0, 0.0288837502628, 0.00108595248487),
                triggerBin(29.0, 0.0732958879412, 0.00153460872848),
                triggerBin(33.0, 0.535146428698, 0.00296803996838),
                triggerBin(37.0, 0.863276836158, 0.00226484134436),
                triggerBin(41.0, 0.880867416964, 0.00268355790486),
                triggerBin(45.0, 0.890614373158, 0.00332308502293),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.911513323278, 0.00636800009587),
                triggerBin(70.0, 0.880448318804, 0.0114491173162),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229157244083, 0.00106076011419),
                triggerBin(25.0, 0.0288837502628, 0.00108595248487),
                triggerBin(29.0, 0.0732958879412, 0.00153460872848),
                triggerBin(33.0, 0.535146428698, 0.00296803996838),
                triggerBin(37.0, 0.863276836158, 0.00226484134436),
                triggerBin(41.0, 0.880867416964, 0.00268355790486),
                triggerBin(45.0, 0.890614373158, 0.00332308502293),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.911513323278, 0.00636800009587),
                triggerBin(70.0, 0.880448318804, 0.0114491173162),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229157244083, 0.00106076011419),
                triggerBin(25.0, 0.0288837502628, 0.00108595248487),
                triggerBin(29.0, 0.0732958879412, 0.00153460872848),
                triggerBin(33.0, 0.535146428698, 0.00296803996838),
                triggerBin(37.0, 0.863276836158, 0.00226484134436),
                triggerBin(41.0, 0.880867416964, 0.00268355790486),
                triggerBin(45.0, 0.890614373158, 0.00332308502293),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.911513323278, 0.00636800009587),
                triggerBin(70.0, 0.880448318804, 0.0114491173162),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229157244083, 0.00106076011419),
                triggerBin(25.0, 0.0288837502628, 0.00108595248487),
                triggerBin(29.0, 0.0732958879412, 0.00153460872848),
                triggerBin(33.0, 0.535146428698, 0.00296803996838),
                triggerBin(37.0, 0.863276836158, 0.00226484134436),
                triggerBin(41.0, 0.880867416964, 0.00268355790486),
                triggerBin(45.0, 0.890614373158, 0.00332308502293),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.911513323278, 0.00636800009587),
                triggerBin(70.0, 0.880448318804, 0.0114491173162),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229157244083, 0.00106076011419),
                triggerBin(25.0, 0.0288837502628, 0.00108595248487),
                triggerBin(29.0, 0.0732958879412, 0.00153460872848),
                triggerBin(33.0, 0.535146428698, 0.00296803996838),
                triggerBin(37.0, 0.863276836158, 0.00226484134436),
                triggerBin(41.0, 0.880867416964, 0.00268355790486),
                triggerBin(45.0, 0.890614373158, 0.00332308502293),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.911513323278, 0.00636800009587),
                triggerBin(70.0, 0.880448318804, 0.0114491173162),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0229157244083, 0.00106076011419),
                triggerBin(25.0, 0.0288837502628, 0.00108595248487),
                triggerBin(29.0, 0.0732958879412, 0.00153460872848),
                triggerBin(33.0, 0.535146428698, 0.00296803996838),
                triggerBin(37.0, 0.863276836158, 0.00226484134436),
                triggerBin(41.0, 0.880867416964, 0.00268355790486),
                triggerBin(45.0, 0.890614373158, 0.00332308502293),
                triggerBin(50.0, 0.895909805978, 0.00494477699081),
                triggerBin(55.0, 0.889003613836, 0.00713742195505),
                triggerBin(60.0, 0.911513323278, 0.00636800009587),
                triggerBin(70.0, 0.880448318804, 0.0114491173162),
                triggerBin(80.0, 0.879284649776, 0.0125772222406),
                triggerBin(100.0, 0.903465346535, 0.0146928717601),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byMediumCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronTightMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0256069171932, 0.00166310015201),
                triggerBin(25.0, 0.0322869955157, 0.00200078605425),
                triggerBin(29.0, 0.0753415572357, 0.00303984258178),
                triggerBin(33.0, 0.458891867739, 0.00608144163007),
                triggerBin(37.0, 0.783963133641, 0.00558742727427),
                triggerBin(41.0, 0.812713797035, 0.00658706450538),
                triggerBin(45.0, 0.840682788051, 0.0079690974365),
                triggerBin(50.0, 0.848594741614, 0.0107927692342),
                triggerBin(55.0, 0.788321167883, 0.0174501847893),
                triggerBin(60.0, 0.806873977087, 0.0159699165929),
                triggerBin(70.0, 0.883817427386, 0.0206415950398),
                triggerBin(80.0, 0.82320441989, 0.0283563456182),
                triggerBin(100.0, 0.772277227723, 0.0417281526716),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0268992018918, 0.00196690151533),
                triggerBin(25.0, 0.0313034553541, 0.00227751166038),
                triggerBin(29.0, 0.0740088105727, 0.00347505919273),
                triggerBin(33.0, 0.473725956772, 0.0070311292574),
                triggerBin(37.0, 0.8225, 0.00604139367199),
                triggerBin(41.0, 0.865517241379, 0.00667806916409),
                triggerBin(45.0, 0.876240900066, 0.00847165184141),
                triggerBin(50.0, 0.88622754491, 0.0109887413015),
                triggerBin(55.0, 0.864285714286, 0.0167115527738),
                triggerBin(60.0, 0.827814569536, 0.0177384485311),
                triggerBin(70.0, 0.890804597701, 0.0236438816678),
                triggerBin(80.0, 0.944055944056, 0.0192179837377),
                triggerBin(100.0, 0.833333333333, 0.0439205230579),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0179076343073, 0.00407134198765),
                triggerBin(25.0, 0.034398034398, 0.00638783487826),
                triggerBin(29.0, 0.0586353944563, 0.00767109637455),
                triggerBin(33.0, 0.50197109067, 0.018124845001),
                triggerBin(37.0, 0.805810397554, 0.0154682273125),
                triggerBin(41.0, 0.88, 0.0167809415707),
                triggerBin(45.0, 0.84388185654, 0.0235772604406),
                triggerBin(50.0, 0.878787878788, 0.0284071777746),
                triggerBin(55.0, 0.966101694915, 0.0235599523744),
                triggerBin(60.0, 0.72972972973, 0.0516255032406),
                triggerBin(70.0, 0.8125, 0.097578093725),
                triggerBin(80.0, 0.888888888889, 0.0604812282169),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0285714285714, 0.00220568550819),
                triggerBin(25.0, 0.0308028616852, 0.00243574196302),
                triggerBin(29.0, 0.0770529871227, 0.00387464066168),
                triggerBin(33.0, 0.46870621205, 0.00762595770566),
                triggerBin(37.0, 0.825762104005, 0.00655746248819),
                triggerBin(41.0, 0.863087248322, 0.00727127442851),
                triggerBin(45.0, 0.882260596546, 0.00902972747537),
                triggerBin(50.0, 0.887624466572, 0.0119116754775),
                triggerBin(55.0, 0.847645429363, 0.0189139072551),
                triggerBin(60.0, 0.846965699208, 0.0184930139824),
                triggerBin(70.0, 0.898734177215, 0.0240004029397),
                triggerBin(80.0, 0.956896551724, 0.0188564314974),
                triggerBin(100.0, 0.90625, 0.0364350744261),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0230598669623, 0.00316074239069),
                triggerBin(25.0, 0.0408371618173, 0.0044715359792),
                triggerBin(29.0, 0.0965665236052, 0.00684129683183),
                triggerBin(33.0, 0.502692998205, 0.0122313805971),
                triggerBin(37.0, 0.830877192982, 0.00993029330017),
                triggerBin(41.0, 0.847438752784, 0.0119988080822),
                triggerBin(45.0, 0.871237458194, 0.0136965897688),
                triggerBin(50.0, 0.884328358209, 0.0195367729309),
                triggerBin(55.0, 0.828125, 0.0333464278886),
                triggerBin(60.0, 0.886075949367, 0.0252763662717),
                triggerBin(70.0, 0.955223880597, 0.0252661116128),
                triggerBin(80.0, 0.868421052632, 0.0548361022017),
                triggerBin(100.0, 0.620689655172, 0.0901022421425),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0209059233449, 0.00149290080041),
                triggerBin(25.0, 0.0378827877508, 0.00219338553218),
                triggerBin(29.0, 0.0820580474934, 0.00315234394375),
                triggerBin(33.0, 0.471569046601, 0.00595924212888),
                triggerBin(37.0, 0.811626607043, 0.00533730621863),
                triggerBin(41.0, 0.863847045191, 0.00583709239735),
                triggerBin(45.0, 0.863334807607, 0.00722384307031),
                triggerBin(50.0, 0.864734299517, 0.0106307770657),
                triggerBin(55.0, 0.875886524823, 0.0138833361296),
                triggerBin(60.0, 0.912313432836, 0.0122167637077),
                triggerBin(70.0, 0.908256880734, 0.0195507243505),
                triggerBin(80.0, 0.943181818182, 0.017449582574),
                triggerBin(100.0, 0.843137254902, 0.0360088257561),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.022730072687, 0.00116975499632),
                triggerBin(25.0, 0.0266845250361, 0.00115670180002),
                triggerBin(29.0, 0.0693264118558, 0.00164349070129),
                triggerBin(33.0, 0.531760741365, 0.00323855808001),
                triggerBin(37.0, 0.867353276058, 0.00244017086194),
                triggerBin(41.0, 0.89461185719, 0.00277856015029),
                triggerBin(45.0, 0.900658690684, 0.00346806942291),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.930246542393, 0.0062464860962),
                triggerBin(70.0, 0.894333843798, 0.0120298772801),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.022730072687, 0.00116975499632),
                triggerBin(25.0, 0.0266845250361, 0.00115670180002),
                triggerBin(29.0, 0.0693264118558, 0.00164349070129),
                triggerBin(33.0, 0.531760741365, 0.00323855808001),
                triggerBin(37.0, 0.867353276058, 0.00244017086194),
                triggerBin(41.0, 0.89461185719, 0.00277856015029),
                triggerBin(45.0, 0.900658690684, 0.00346806942291),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.930246542393, 0.0062464860962),
                triggerBin(70.0, 0.894333843798, 0.0120298772801),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.022730072687, 0.00116975499632),
                triggerBin(25.0, 0.0266845250361, 0.00115670180002),
                triggerBin(29.0, 0.0693264118558, 0.00164349070129),
                triggerBin(33.0, 0.531760741365, 0.00323855808001),
                triggerBin(37.0, 0.867353276058, 0.00244017086194),
                triggerBin(41.0, 0.89461185719, 0.00277856015029),
                triggerBin(45.0, 0.900658690684, 0.00346806942291),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.930246542393, 0.0062464860962),
                triggerBin(70.0, 0.894333843798, 0.0120298772801),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.022730072687, 0.00116975499632),
                triggerBin(25.0, 0.0266845250361, 0.00115670180002),
                triggerBin(29.0, 0.0693264118558, 0.00164349070129),
                triggerBin(33.0, 0.531760741365, 0.00323855808001),
                triggerBin(37.0, 0.867353276058, 0.00244017086194),
                triggerBin(41.0, 0.89461185719, 0.00277856015029),
                triggerBin(45.0, 0.900658690684, 0.00346806942291),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.930246542393, 0.0062464860962),
                triggerBin(70.0, 0.894333843798, 0.0120298772801),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.022730072687, 0.00116975499632),
                triggerBin(25.0, 0.0266845250361, 0.00115670180002),
                triggerBin(29.0, 0.0693264118558, 0.00164349070129),
                triggerBin(33.0, 0.531760741365, 0.00323855808001),
                triggerBin(37.0, 0.867353276058, 0.00244017086194),
                triggerBin(41.0, 0.89461185719, 0.00277856015029),
                triggerBin(45.0, 0.900658690684, 0.00346806942291),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.930246542393, 0.0062464860962),
                triggerBin(70.0, 0.894333843798, 0.0120298772801),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.022730072687, 0.00116975499632),
                triggerBin(25.0, 0.0266845250361, 0.00115670180002),
                triggerBin(29.0, 0.0693264118558, 0.00164349070129),
                triggerBin(33.0, 0.531760741365, 0.00323855808001),
                triggerBin(37.0, 0.867353276058, 0.00244017086194),
                triggerBin(41.0, 0.89461185719, 0.00277856015029),
                triggerBin(45.0, 0.900658690684, 0.00346806942291),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.930246542393, 0.0062464860962),
                triggerBin(70.0, 0.894333843798, 0.0120298772801),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.022730072687, 0.00116975499632),
                triggerBin(25.0, 0.0266845250361, 0.00115670180002),
                triggerBin(29.0, 0.0693264118558, 0.00164349070129),
                triggerBin(33.0, 0.531760741365, 0.00323855808001),
                triggerBin(37.0, 0.867353276058, 0.00244017086194),
                triggerBin(41.0, 0.89461185719, 0.00277856015029),
                triggerBin(45.0, 0.900658690684, 0.00346806942291),
                triggerBin(50.0, 0.911313068004, 0.00503269037895),
                triggerBin(55.0, 0.894900497512, 0.00764794370733),
                triggerBin(60.0, 0.930246542393, 0.0062464860962),
                triggerBin(70.0, 0.894333843798, 0.0120298772801),
                triggerBin(80.0, 0.881415929204, 0.0136012680922),
                triggerBin(100.0, 0.903225806452, 0.0160103475531),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byTightCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronTightMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0265175317331, 0.00180117510983),
                triggerBin(25.0, 0.0313798538473, 0.00208691907144),
                triggerBin(29.0, 0.0723316671567, 0.00314081451714),
                triggerBin(33.0, 0.459053464707, 0.00633327585182),
                triggerBin(37.0, 0.789452656812, 0.00576225542542),
                triggerBin(41.0, 0.80981595092, 0.00687339666871),
                triggerBin(45.0, 0.839175257732, 0.00834068850969),
                triggerBin(50.0, 0.866273352999, 0.0106727412129),
                triggerBin(55.0, 0.802845528455, 0.0179364611336),
                triggerBin(60.0, 0.825842696629, 0.0164115229144),
                triggerBin(70.0, 0.885964912281, 0.021050387179),
                triggerBin(80.0, 0.835443037975, 0.0294976901342),
                triggerBin(100.0, 0.776595744681, 0.0429614862188),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0275398824517, 0.00212068447857),
                triggerBin(25.0, 0.0310594512195, 0.00239468581296),
                triggerBin(29.0, 0.0706734534064, 0.00358580677902),
                triggerBin(33.0, 0.473899033298, 0.00731842486761),
                triggerBin(37.0, 0.828486001631, 0.00621480460991),
                triggerBin(41.0, 0.862422997947, 0.00698045292387),
                triggerBin(45.0, 0.874281609195, 0.00888598264195),
                triggerBin(50.0, 0.905071521456, 0.010570037794),
                triggerBin(55.0, 0.877659574468, 0.0168987319974),
                triggerBin(60.0, 0.854166666667, 0.0180108454177),
                triggerBin(70.0, 0.896341463415, 0.0238022140262),
                triggerBin(80.0, 0.939393939394, 0.0207680126316),
                triggerBin(100.0, 0.820895522388, 0.0468446246795),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0185995623632, 0.00446890773803),
                triggerBin(25.0, 0.0387811634349, 0.00718543317122),
                triggerBin(29.0, 0.0570430733411, 0.00791317560936),
                triggerBin(33.0, 0.504908835905, 0.0187242447077),
                triggerBin(37.0, 0.81561461794, 0.0158054730492),
                triggerBin(41.0, 0.879213483146, 0.0172715533969),
                triggerBin(45.0, 0.844036697248, 0.0245733083122),
                triggerBin(50.0, 0.884297520661, 0.0290788917812),
                triggerBin(55.0, 0.960784313725, 0.0271805207876),
                triggerBin(60.0, 0.761904761905, 0.0536605876018),
                triggerBin(70.0, 0.8125, 0.097578093725),
                triggerBin(80.0, 0.875, 0.0675077156084),
                triggerBin(100.0, 0.25, 0.153093108924),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0291608807776, 0.00236982132794),
                triggerBin(25.0, 0.0298276623951, 0.00252858046486),
                triggerBin(29.0, 0.0734290421276, 0.00400156529445),
                triggerBin(33.0, 0.468290208016, 0.00794761018381),
                triggerBin(37.0, 0.831004224894, 0.00675578455788),
                triggerBin(41.0, 0.859547859548, 0.00762029822376),
                triggerBin(45.0, 0.879897785349, 0.00948762633096),
                triggerBin(50.0, 0.908950617284, 0.011301111099),
                triggerBin(55.0, 0.864615384615, 0.0189781754251),
                triggerBin(60.0, 0.872274143302, 0.0186300231871),
                triggerBin(70.0, 0.905405405405, 0.0240560237537),
                triggerBin(80.0, 0.953703703704, 0.0202193868385),
                triggerBin(100.0, 0.898305084746, 0.0393491669555),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.024975024975, 0.00348761710602),
                triggerBin(25.0, 0.0387059503177, 0.00463626723196),
                triggerBin(29.0, 0.0926800472255, 0.00704557838482),
                triggerBin(33.0, 0.506510416667, 0.0127566775425),
                triggerBin(37.0, 0.836473247928, 0.0101527799167),
                triggerBin(41.0, 0.850909090909, 0.0124005283327),
                triggerBin(45.0, 0.870437956204, 0.0143455606579),
                triggerBin(50.0, 0.899193548387, 0.0191181081749),
                triggerBin(55.0, 0.853448275862, 0.0328363649719),
                triggerBin(60.0, 0.88, 0.0265329983228),
                triggerBin(70.0, 0.953125, 0.0264213852704),
                triggerBin(80.0, 0.923076923077, 0.0522589400374),
                triggerBin(100.0, 0.666666666667, 0.0907218423253),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.022545275348, 0.00164770069157),
                triggerBin(25.0, 0.0390050044157, 0.00234886446382),
                triggerBin(29.0, 0.0797671033479, 0.00326875536791),
                triggerBin(33.0, 0.468180413964, 0.00620158123508),
                triggerBin(37.0, 0.81298648095, 0.00558057919415),
                triggerBin(41.0, 0.86626809314, 0.00603763328769),
                triggerBin(45.0, 0.86835806606, 0.00739736977205),
                triggerBin(50.0, 0.860612460401, 0.0112548782526),
                triggerBin(55.0, 0.876893939394, 0.0142986912974),
                triggerBin(60.0, 0.92152917505, 0.0120623092728),
                triggerBin(70.0, 0.918367346939, 0.0195574458673),
                triggerBin(80.0, 0.936708860759, 0.0193706960812),
                triggerBin(100.0, 0.860215053763, 0.0359577283245),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223989396952, 0.00120461964761),
                triggerBin(25.0, 0.0269490961517, 0.0012058515598),
                triggerBin(29.0, 0.0695542774982, 0.00170523362332),
                triggerBin(33.0, 0.531689982457, 0.00334669753245),
                triggerBin(37.0, 0.866963647363, 0.0025185631177),
                triggerBin(41.0, 0.894557823129, 0.00286817352069),
                triggerBin(45.0, 0.901587755686, 0.00356253319319),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.927225471085, 0.0066216019204),
                triggerBin(70.0, 0.887070376432, 0.0128044925939),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223989396952, 0.00120461964761),
                triggerBin(25.0, 0.0269490961517, 0.0012058515598),
                triggerBin(29.0, 0.0695542774982, 0.00170523362332),
                triggerBin(33.0, 0.531689982457, 0.00334669753245),
                triggerBin(37.0, 0.866963647363, 0.0025185631177),
                triggerBin(41.0, 0.894557823129, 0.00286817352069),
                triggerBin(45.0, 0.901587755686, 0.00356253319319),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.927225471085, 0.0066216019204),
                triggerBin(70.0, 0.887070376432, 0.0128044925939),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223989396952, 0.00120461964761),
                triggerBin(25.0, 0.0269490961517, 0.0012058515598),
                triggerBin(29.0, 0.0695542774982, 0.00170523362332),
                triggerBin(33.0, 0.531689982457, 0.00334669753245),
                triggerBin(37.0, 0.866963647363, 0.0025185631177),
                triggerBin(41.0, 0.894557823129, 0.00286817352069),
                triggerBin(45.0, 0.901587755686, 0.00356253319319),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.927225471085, 0.0066216019204),
                triggerBin(70.0, 0.887070376432, 0.0128044925939),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223989396952, 0.00120461964761),
                triggerBin(25.0, 0.0269490961517, 0.0012058515598),
                triggerBin(29.0, 0.0695542774982, 0.00170523362332),
                triggerBin(33.0, 0.531689982457, 0.00334669753245),
                triggerBin(37.0, 0.866963647363, 0.0025185631177),
                triggerBin(41.0, 0.894557823129, 0.00286817352069),
                triggerBin(45.0, 0.901587755686, 0.00356253319319),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.927225471085, 0.0066216019204),
                triggerBin(70.0, 0.887070376432, 0.0128044925939),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223989396952, 0.00120461964761),
                triggerBin(25.0, 0.0269490961517, 0.0012058515598),
                triggerBin(29.0, 0.0695542774982, 0.00170523362332),
                triggerBin(33.0, 0.531689982457, 0.00334669753245),
                triggerBin(37.0, 0.866963647363, 0.0025185631177),
                triggerBin(41.0, 0.894557823129, 0.00286817352069),
                triggerBin(45.0, 0.901587755686, 0.00356253319319),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.927225471085, 0.0066216019204),
                triggerBin(70.0, 0.887070376432, 0.0128044925939),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223989396952, 0.00120461964761),
                triggerBin(25.0, 0.0269490961517, 0.0012058515598),
                triggerBin(29.0, 0.0695542774982, 0.00170523362332),
                triggerBin(33.0, 0.531689982457, 0.00334669753245),
                triggerBin(37.0, 0.866963647363, 0.0025185631177),
                triggerBin(41.0, 0.894557823129, 0.00286817352069),
                triggerBin(45.0, 0.901587755686, 0.00356253319319),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.927225471085, 0.0066216019204),
                triggerBin(70.0, 0.887070376432, 0.0128044925939),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223989396952, 0.00120461964761),
                triggerBin(25.0, 0.0269490961517, 0.0012058515598),
                triggerBin(29.0, 0.0695542774982, 0.00170523362332),
                triggerBin(33.0, 0.531689982457, 0.00334669753245),
                triggerBin(37.0, 0.866963647363, 0.0025185631177),
                triggerBin(41.0, 0.894557823129, 0.00286817352069),
                triggerBin(45.0, 0.901587755686, 0.00356253319319),
                triggerBin(50.0, 0.911044973545, 0.00517683426466),
                triggerBin(55.0, 0.894736842105, 0.00792128267246),
                triggerBin(60.0, 0.927225471085, 0.0066216019204),
                triggerBin(70.0, 0.887070376432, 0.0128044925939),
                triggerBin(80.0, 0.878095238095, 0.0142791216837),
                triggerBin(100.0, 0.897196261682, 0.0169510133227),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byLooseCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronVTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronVTightMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0210012728044, 0.00120575328926),
                triggerBin(25.0, 0.0292920353982, 0.00158628000465),
                triggerBin(29.0, 0.0796740172579, 0.00265147199899),
                triggerBin(33.0, 0.462491552151, 0.00529159964908),
                triggerBin(37.0, 0.750620891161, 0.00522942130403),
                triggerBin(41.0, 0.788117892783, 0.00622521690905),
                triggerBin(45.0, 0.811940298507, 0.00754818477158),
                triggerBin(50.0, 0.817767653759, 0.0106373833362),
                triggerBin(55.0, 0.771851851852, 0.0161518979802),
                triggerBin(60.0, 0.798319327731, 0.0150165911374),
                triggerBin(70.0, 0.861016949153, 0.0201407557484),
                triggerBin(80.0, 0.804347826087, 0.0292452523791),
                triggerBin(100.0, 0.838095238095, 0.0359485889487),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.021454338333, 0.00141172938136),
                triggerBin(25.0, 0.0296935999054, 0.00184620719753),
                triggerBin(29.0, 0.0766773162939, 0.00300793212188),
                triggerBin(33.0, 0.481314044605, 0.0061335699548),
                triggerBin(37.0, 0.791650256006, 0.00569923829013),
                triggerBin(41.0, 0.830235439901, 0.00660780757061),
                triggerBin(45.0, 0.840040753948, 0.00827360346781),
                triggerBin(50.0, 0.867602808425, 0.0107337699196),
                triggerBin(55.0, 0.842105263158, 0.0160993497453),
                triggerBin(60.0, 0.832391713748, 0.0162093035892),
                triggerBin(70.0, 0.889908256881, 0.0211993109651),
                triggerBin(80.0, 0.918367346939, 0.0225829932723),
                triggerBin(100.0, 0.8625, 0.0385022320781),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0134392180819, 0.0028459324304),
                triggerBin(25.0, 0.0345937248592, 0.00518344097929),
                triggerBin(29.0, 0.0451306413302, 0.00584125352218),
                triggerBin(33.0, 0.492385786802, 0.0159294773131),
                triggerBin(37.0, 0.773851590106, 0.0143572665635),
                triggerBin(41.0, 0.824742268041, 0.0172634205584),
                triggerBin(45.0, 0.807073954984, 0.0223754563927),
                triggerBin(50.0, 0.846625766871, 0.0282246224296),
                triggerBin(55.0, 0.914634146341, 0.0308573675212),
                triggerBin(60.0, 0.74358974359, 0.0494409822762),
                triggerBin(70.0, 0.810810810811, 0.064388315182),
                triggerBin(80.0, 0.913043478261, 0.0587533847558),
                triggerBin(100.0, 0.4, 0.219089023002),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.022929077217, 0.00158684510927),
                triggerBin(25.0, 0.0288488210818, 0.00197124145441),
                triggerBin(29.0, 0.0827491618409, 0.00340100873519),
                triggerBin(33.0, 0.479384179791, 0.00664565628593),
                triggerBin(37.0, 0.795223457082, 0.00620534385506),
                triggerBin(41.0, 0.831206707984, 0.00715186334605),
                triggerBin(45.0, 0.846246973366, 0.00887473470719),
                triggerBin(50.0, 0.87170263789, 0.0115800389007),
                triggerBin(55.0, 0.828306264501, 0.0181649439728),
                triggerBin(60.0, 0.847682119205, 0.0168827369793),
                triggerBin(70.0, 0.906077348066, 0.0216834569663),
                triggerBin(80.0, 0.91935483871, 0.0244523102759),
                triggerBin(100.0, 0.893333333333, 0.0356443336102),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0213414634146, 0.00240599338001),
                triggerBin(25.0, 0.0365296803653, 0.0035159960033),
                triggerBin(29.0, 0.101343570058, 0.005912771267),
                triggerBin(33.0, 0.489295272079, 0.0105572946992),
                triggerBin(37.0, 0.797962648557, 0.00955187961144),
                triggerBin(41.0, 0.851063829787, 0.0108285002466),
                triggerBin(45.0, 0.866108786611, 0.0127175274325),
                triggerBin(50.0, 0.81875, 0.0215347420971),
                triggerBin(55.0, 0.820987654321, 0.030119814832),
                triggerBin(60.0, 0.841530054645, 0.0269949622678),
                triggerBin(70.0, 0.909090909091, 0.0327613622798),
                triggerBin(80.0, 0.864864864865, 0.0562027291795),
                triggerBin(100.0, 0.76, 0.0854166260162),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0190015425607, 0.00114324253843),
                triggerBin(25.0, 0.0384154767388, 0.00184472626847),
                triggerBin(29.0, 0.0865460267506, 0.00278836185627),
                triggerBin(33.0, 0.476931567329, 0.00524738815946),
                triggerBin(37.0, 0.789442201286, 0.00498574627675),
                triggerBin(41.0, 0.843081982617, 0.00557467412421),
                triggerBin(45.0, 0.851488743646, 0.006776214946),
                triggerBin(50.0, 0.849348534202, 0.0102077604145),
                triggerBin(55.0, 0.867435158501, 0.0128722051776),
                triggerBin(60.0, 0.899259259259, 0.011584922762),
                triggerBin(70.0, 0.830935251799, 0.0224795557892),
                triggerBin(80.0, 0.935643564356, 0.0172653554606),
                triggerBin(100.0, 0.876033057851, 0.0299585304844),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223750384892, 0.00105951396984),
                triggerBin(25.0, 0.0284536976795, 0.00109501115835),
                triggerBin(29.0, 0.0723504947655, 0.00155121816965),
                triggerBin(33.0, 0.536734393404, 0.00302528230938),
                triggerBin(37.0, 0.866198467713, 0.00229900405769),
                triggerBin(41.0, 0.883746276248, 0.00273218863124),
                triggerBin(45.0, 0.889758093633, 0.00343585598129),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915008068854, 0.0064678749644),
                triggerBin(70.0, 0.89701897019, 0.0111879688398),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223750384892, 0.00105951396984),
                triggerBin(25.0, 0.0284536976795, 0.00109501115835),
                triggerBin(29.0, 0.0723504947655, 0.00155121816965),
                triggerBin(33.0, 0.536734393404, 0.00302528230938),
                triggerBin(37.0, 0.866198467713, 0.00229900405769),
                triggerBin(41.0, 0.883746276248, 0.00273218863124),
                triggerBin(45.0, 0.889758093633, 0.00343585598129),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915008068854, 0.0064678749644),
                triggerBin(70.0, 0.89701897019, 0.0111879688398),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223750384892, 0.00105951396984),
                triggerBin(25.0, 0.0284536976795, 0.00109501115835),
                triggerBin(29.0, 0.0723504947655, 0.00155121816965),
                triggerBin(33.0, 0.536734393404, 0.00302528230938),
                triggerBin(37.0, 0.866198467713, 0.00229900405769),
                triggerBin(41.0, 0.883746276248, 0.00273218863124),
                triggerBin(45.0, 0.889758093633, 0.00343585598129),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915008068854, 0.0064678749644),
                triggerBin(70.0, 0.89701897019, 0.0111879688398),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223750384892, 0.00105951396984),
                triggerBin(25.0, 0.0284536976795, 0.00109501115835),
                triggerBin(29.0, 0.0723504947655, 0.00155121816965),
                triggerBin(33.0, 0.536734393404, 0.00302528230938),
                triggerBin(37.0, 0.866198467713, 0.00229900405769),
                triggerBin(41.0, 0.883746276248, 0.00273218863124),
                triggerBin(45.0, 0.889758093633, 0.00343585598129),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915008068854, 0.0064678749644),
                triggerBin(70.0, 0.89701897019, 0.0111879688398),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223750384892, 0.00105951396984),
                triggerBin(25.0, 0.0284536976795, 0.00109501115835),
                triggerBin(29.0, 0.0723504947655, 0.00155121816965),
                triggerBin(33.0, 0.536734393404, 0.00302528230938),
                triggerBin(37.0, 0.866198467713, 0.00229900405769),
                triggerBin(41.0, 0.883746276248, 0.00273218863124),
                triggerBin(45.0, 0.889758093633, 0.00343585598129),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915008068854, 0.0064678749644),
                triggerBin(70.0, 0.89701897019, 0.0111879688398),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223750384892, 0.00105951396984),
                triggerBin(25.0, 0.0284536976795, 0.00109501115835),
                triggerBin(29.0, 0.0723504947655, 0.00155121816965),
                triggerBin(33.0, 0.536734393404, 0.00302528230938),
                triggerBin(37.0, 0.866198467713, 0.00229900405769),
                triggerBin(41.0, 0.883746276248, 0.00273218863124),
                triggerBin(45.0, 0.889758093633, 0.00343585598129),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915008068854, 0.0064678749644),
                triggerBin(70.0, 0.89701897019, 0.0111879688398),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223750384892, 0.00105951396984),
                triggerBin(25.0, 0.0284536976795, 0.00109501115835),
                triggerBin(29.0, 0.0723504947655, 0.00155121816965),
                triggerBin(33.0, 0.536734393404, 0.00302528230938),
                triggerBin(37.0, 0.866198467713, 0.00229900405769),
                triggerBin(41.0, 0.883746276248, 0.00273218863124),
                triggerBin(45.0, 0.889758093633, 0.00343585598129),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915008068854, 0.0064678749644),
                triggerBin(70.0, 0.89701897019, 0.0111879688398),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byMediumCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronVTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronVTightMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0247971145176, 0.0016509628318),
                triggerBin(25.0, 0.0320063483666, 0.00202425257068),
                triggerBin(29.0, 0.0753424657534, 0.00308922073358),
                triggerBin(33.0, 0.462264150943, 0.00620028642584),
                triggerBin(37.0, 0.786281728347, 0.00570614743802),
                triggerBin(41.0, 0.815273166315, 0.0067422654841),
                triggerBin(45.0, 0.840725806452, 0.00821540660309),
                triggerBin(50.0, 0.853346456693, 0.011098444664),
                triggerBin(55.0, 0.791748526523, 0.0179981879284),
                triggerBin(60.0, 0.81914893617, 0.0162069919977),
                triggerBin(70.0, 0.893805309735, 0.0204936184784),
                triggerBin(80.0, 0.823170731707, 0.0297920309945),
                triggerBin(100.0, 0.829545454545, 0.0400851073837),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0257181531057, 0.00194126143791),
                triggerBin(25.0, 0.0311284046693, 0.00230958335862),
                triggerBin(29.0, 0.0724849370093, 0.00350358774138),
                triggerBin(33.0, 0.476662536142, 0.00717767896585),
                triggerBin(37.0, 0.827059752566, 0.00613595032183),
                triggerBin(41.0, 0.865883306321, 0.00685959578678),
                triggerBin(45.0, 0.874297752809, 0.0087850898425),
                triggerBin(50.0, 0.890322580645, 0.0112248734766),
                triggerBin(55.0, 0.863753213368, 0.0173933474093),
                triggerBin(60.0, 0.852028639618, 0.0173463824878),
                triggerBin(70.0, 0.910179640719, 0.0221254807911),
                triggerBin(80.0, 0.961240310078, 0.0169946129996),
                triggerBin(100.0, 0.863636363636, 0.0422418353311),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0181297709924, 0.00412137909506),
                triggerBin(25.0, 0.0351317440402, 0.00652160819134),
                triggerBin(29.0, 0.0519337016575, 0.00737597955211),
                triggerBin(33.0, 0.498633879781, 0.0184804627939),
                triggerBin(37.0, 0.807383627608, 0.0157994709808),
                triggerBin(41.0, 0.889807162534, 0.0164350609598),
                triggerBin(45.0, 0.839826839827, 0.0241314688237),
                triggerBin(50.0, 0.872, 0.0298819008766),
                triggerBin(55.0, 0.964285714286, 0.0247987526725),
                triggerBin(60.0, 0.72972972973, 0.0516255032406),
                triggerBin(70.0, 0.785714285714, 0.109664210511),
                triggerBin(80.0, 1.0, 0.0),
                triggerBin(100.0, 0.4, 0.219089023002),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0271380110695, 0.00217111005618),
                triggerBin(25.0, 0.0304714844554, 0.00246628378567),
                triggerBin(29.0, 0.0765529308836, 0.00393218374968),
                triggerBin(33.0, 0.472749391727, 0.00778759079569),
                triggerBin(37.0, 0.830919395466, 0.00665098697493),
                triggerBin(41.0, 0.861757719715, 0.0075229293906),
                triggerBin(45.0, 0.880972338642, 0.00937529333163),
                triggerBin(50.0, 0.893846153846, 0.0120821041915),
                triggerBin(55.0, 0.846846846847, 0.0197352799771),
                triggerBin(60.0, 0.878260869565, 0.0176042414649),
                triggerBin(70.0, 0.921568627451, 0.0217351695888),
                triggerBin(80.0, 0.953703703704, 0.0202193868385),
                triggerBin(100.0, 0.901639344262, 0.0381295972),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0233918128655, 0.00320569640001),
                triggerBin(25.0, 0.0403775563713, 0.0045075947862),
                triggerBin(29.0, 0.09873834339, 0.00698674722789),
                triggerBin(33.0, 0.504926108374, 0.0124066894958),
                triggerBin(37.0, 0.828193832599, 0.010221080698),
                triggerBin(41.0, 0.862721893491, 0.0118388003141),
                triggerBin(45.0, 0.878571428571, 0.0138024113751),
                triggerBin(50.0, 0.904564315353, 0.0189263384003),
                triggerBin(55.0, 0.841666666667, 0.0333246516472),
                triggerBin(60.0, 0.875862068966, 0.0273833205101),
                triggerBin(70.0, 0.949152542373, 0.0286006974195),
                triggerBin(80.0, 0.857142857143, 0.059148476515),
                triggerBin(100.0, 0.727272727273, 0.0949514487031),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0209511140672, 0.0015079203702),
                triggerBin(25.0, 0.0375785733807, 0.00222308763647),
                triggerBin(29.0, 0.0824544582934, 0.00321906474597),
                triggerBin(33.0, 0.473777777778, 0.00607743117104),
                triggerBin(37.0, 0.81733807267, 0.00542972749648),
                triggerBin(41.0, 0.86555658341, 0.00599023731202),
                triggerBin(45.0, 0.869971936389, 0.00727389987581),
                triggerBin(50.0, 0.869752421959, 0.0110426878161),
                triggerBin(55.0, 0.87358490566, 0.0144349103991),
                triggerBin(60.0, 0.93482688391, 0.0111393306088),
                triggerBin(70.0, 0.906735751295, 0.020932413893),
                triggerBin(80.0, 0.95625, 0.0161701765412),
                triggerBin(100.0, 0.895833333333, 0.0311775781182),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221522970422, 0.00116757031443),
                triggerBin(25.0, 0.026529421128, 0.00117058832096),
                triggerBin(29.0, 0.0681229494042, 0.00165546213394),
                triggerBin(33.0, 0.533981858814, 0.00330215403267),
                triggerBin(37.0, 0.870185526744, 0.00247547015084),
                triggerBin(41.0, 0.897609147609, 0.00282160395315),
                triggerBin(45.0, 0.900540694365, 0.00356992018545),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.933204881182, 0.00632727277817),
                triggerBin(70.0, 0.910447761194, 0.0116280551777),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221522970422, 0.00116757031443),
                triggerBin(25.0, 0.026529421128, 0.00117058832096),
                triggerBin(29.0, 0.0681229494042, 0.00165546213394),
                triggerBin(33.0, 0.533981858814, 0.00330215403267),
                triggerBin(37.0, 0.870185526744, 0.00247547015084),
                triggerBin(41.0, 0.897609147609, 0.00282160395315),
                triggerBin(45.0, 0.900540694365, 0.00356992018545),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.933204881182, 0.00632727277817),
                triggerBin(70.0, 0.910447761194, 0.0116280551777),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221522970422, 0.00116757031443),
                triggerBin(25.0, 0.026529421128, 0.00117058832096),
                triggerBin(29.0, 0.0681229494042, 0.00165546213394),
                triggerBin(33.0, 0.533981858814, 0.00330215403267),
                triggerBin(37.0, 0.870185526744, 0.00247547015084),
                triggerBin(41.0, 0.897609147609, 0.00282160395315),
                triggerBin(45.0, 0.900540694365, 0.00356992018545),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.933204881182, 0.00632727277817),
                triggerBin(70.0, 0.910447761194, 0.0116280551777),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221522970422, 0.00116757031443),
                triggerBin(25.0, 0.026529421128, 0.00117058832096),
                triggerBin(29.0, 0.0681229494042, 0.00165546213394),
                triggerBin(33.0, 0.533981858814, 0.00330215403267),
                triggerBin(37.0, 0.870185526744, 0.00247547015084),
                triggerBin(41.0, 0.897609147609, 0.00282160395315),
                triggerBin(45.0, 0.900540694365, 0.00356992018545),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.933204881182, 0.00632727277817),
                triggerBin(70.0, 0.910447761194, 0.0116280551777),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221522970422, 0.00116757031443),
                triggerBin(25.0, 0.026529421128, 0.00117058832096),
                triggerBin(29.0, 0.0681229494042, 0.00165546213394),
                triggerBin(33.0, 0.533981858814, 0.00330215403267),
                triggerBin(37.0, 0.870185526744, 0.00247547015084),
                triggerBin(41.0, 0.897609147609, 0.00282160395315),
                triggerBin(45.0, 0.900540694365, 0.00356992018545),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.933204881182, 0.00632727277817),
                triggerBin(70.0, 0.910447761194, 0.0116280551777),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221522970422, 0.00116757031443),
                triggerBin(25.0, 0.026529421128, 0.00117058832096),
                triggerBin(29.0, 0.0681229494042, 0.00165546213394),
                triggerBin(33.0, 0.533981858814, 0.00330215403267),
                triggerBin(37.0, 0.870185526744, 0.00247547015084),
                triggerBin(41.0, 0.897609147609, 0.00282160395315),
                triggerBin(45.0, 0.900540694365, 0.00356992018545),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.933204881182, 0.00632727277817),
                triggerBin(70.0, 0.910447761194, 0.0116280551777),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221522970422, 0.00116757031443),
                triggerBin(25.0, 0.026529421128, 0.00117058832096),
                triggerBin(29.0, 0.0681229494042, 0.00165546213394),
                triggerBin(33.0, 0.533981858814, 0.00330215403267),
                triggerBin(37.0, 0.870185526744, 0.00247547015084),
                triggerBin(41.0, 0.897609147609, 0.00282160395315),
                triggerBin(45.0, 0.900540694365, 0.00356992018545),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.933204881182, 0.00632727277817),
                triggerBin(70.0, 0.910447761194, 0.0116280551777),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byTightCombinedIsolationDeltaBetaCorr3Hits_againstMuonMedium2_againstElectronVTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronVTightMVA3 > 0.5&& PFTau_againstMuonMedium2 > 0.5&& PFTau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0255395224109, 0.00178270666695),
                triggerBin(25.0, 0.0313563082384, 0.00211952733427),
                triggerBin(29.0, 0.0718290650098, 0.00317852055882),
                triggerBin(33.0, 0.462481114655, 0.00645996351607),
                triggerBin(37.0, 0.792297979798, 0.00588472833431),
                triggerBin(41.0, 0.813190383366, 0.00702524418115),
                triggerBin(45.0, 0.838427947598, 0.00859910514679),
                triggerBin(50.0, 0.871244635193, 0.0109709634731),
                triggerBin(55.0, 0.81045751634, 0.0182941429338),
                triggerBin(60.0, 0.829365079365, 0.0167568183525),
                triggerBin(70.0, 0.896713615023, 0.0208525234797),
                triggerBin(80.0, 0.839160839161, 0.0307220707412),
                triggerBin(100.0, 0.819277108434, 0.0422360161545),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.026113671275, 0.00208341771247),
                triggerBin(25.0, 0.0313115399764, 0.00244398158156),
                triggerBin(29.0, 0.0690562980964, 0.00360817682689),
                triggerBin(33.0, 0.476723366159, 0.00747209368557),
                triggerBin(37.0, 0.833572453372, 0.00630932489167),
                triggerBin(41.0, 0.862983906046, 0.00717162634444),
                triggerBin(45.0, 0.871385083714, 0.00923534338418),
                triggerBin(50.0, 0.908579465541, 0.0108085773837),
                triggerBin(55.0, 0.880341880342, 0.0173238019535),
                triggerBin(60.0, 0.866485013624, 0.0177546658709),
                triggerBin(70.0, 0.917197452229, 0.0219939606437),
                triggerBin(80.0, 0.958333333333, 0.0182415632452),
                triggerBin(100.0, 0.852459016393, 0.0454075608933),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0188261351052, 0.00452282408446),
                triggerBin(25.0, 0.0397163120567, 0.00735511850658),
                triggerBin(29.0, 0.0530759951749, 0.00778626841095),
                triggerBin(33.0, 0.501461988304, 0.0191178960965),
                triggerBin(37.0, 0.815008726003, 0.0162210678158),
                triggerBin(41.0, 0.889534883721, 0.0169010951864),
                triggerBin(45.0, 0.839622641509, 0.0252026186658),
                triggerBin(50.0, 0.877192982456, 0.0307402036864),
                triggerBin(55.0, 0.958333333333, 0.0288424439685),
                triggerBin(60.0, 0.761904761905, 0.0536605876018),
                triggerBin(70.0, 0.785714285714, 0.109664210511),
                triggerBin(80.0, 1.0, 0.0),
                triggerBin(100.0, 0.4, 0.219089023002),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0274414850686, 0.00232057723112),
                triggerBin(25.0, 0.0299565515664, 0.00257781510347),
                triggerBin(29.0, 0.072280360185, 0.00403971250554),
                triggerBin(33.0, 0.472251585624, 0.0081156744417),
                triggerBin(37.0, 0.837225274725, 0.00684099015647),
                triggerBin(41.0, 0.85831202046, 0.00788707045129),
                triggerBin(45.0, 0.877495462795, 0.00987660600872),
                triggerBin(50.0, 0.914572864322, 0.011439839008),
                triggerBin(55.0, 0.86798679868, 0.0194466110122),
                triggerBin(60.0, 0.888157894737, 0.0180763593026),
                triggerBin(70.0, 0.93006993007, 0.0213266069168),
                triggerBin(80.0, 0.950980392157, 0.021378174203),
                triggerBin(100.0, 0.892857142857, 0.0413312544541),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.025354969574, 0.0035399842349),
                triggerBin(25.0, 0.038027332145, 0.0046621606814),
                triggerBin(29.0, 0.0945213726671, 0.007178261835),
                triggerBin(33.0, 0.509066487576, 0.0129554124761),
                triggerBin(37.0, 0.834254143646, 0.0104467744615),
                triggerBin(41.0, 0.869062901155, 0.0120861570626),
                triggerBin(45.0, 0.876447876448, 0.0144585011478),
                triggerBin(50.0, 0.923076923077, 0.0179246685549),
                triggerBin(55.0, 0.87037037037, 0.0323215598198),
                triggerBin(60.0, 0.868613138686, 0.0288621634959),
                triggerBin(70.0, 0.946428571429, 0.0300896074288),
                triggerBin(80.0, 0.913043478261, 0.0587533847558),
                triggerBin(100.0, 0.727272727273, 0.0949514487031),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0225960331408, 0.00166507192867),
                triggerBin(25.0, 0.0392574558734, 0.00239560830282),
                triggerBin(29.0, 0.0802357207616, 0.00333932560232),
                triggerBin(33.0, 0.470512820513, 0.00631860432503),
                triggerBin(37.0, 0.819504778454, 0.0056681448748),
                triggerBin(41.0, 0.86776029461, 0.00619816613019),
                triggerBin(45.0, 0.873296314992, 0.00747365763274),
                triggerBin(50.0, 0.867058823529, 0.0116451363273),
                triggerBin(55.0, 0.875, 0.0148497176035),
                triggerBin(60.0, 0.94298245614, 0.0108585950627),
                triggerBin(70.0, 0.919075144509, 0.0207344932315),
                triggerBin(80.0, 0.950704225352, 0.0181670071736),
                triggerBin(100.0, 0.888888888889, 0.033126933),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217376582921, 0.00120001841096),
                triggerBin(25.0, 0.0269065981148, 0.0012229975932),
                triggerBin(29.0, 0.06840617324, 0.00171856284493),
                triggerBin(33.0, 0.533782204143, 0.00341115562995),
                triggerBin(37.0, 0.869640387275, 0.00255603391304),
                triggerBin(41.0, 0.896981445583, 0.00292062019552),
                triggerBin(45.0, 0.901758641601, 0.00366481462932),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.928818244644, 0.00675951366008),
                triggerBin(70.0, 0.904255319149, 0.0123897719299),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217376582921, 0.00120001841096),
                triggerBin(25.0, 0.0269065981148, 0.0012229975932),
                triggerBin(29.0, 0.06840617324, 0.00171856284493),
                triggerBin(33.0, 0.533782204143, 0.00341115562995),
                triggerBin(37.0, 0.869640387275, 0.00255603391304),
                triggerBin(41.0, 0.896981445583, 0.00292062019552),
                triggerBin(45.0, 0.901758641601, 0.00366481462932),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.928818244644, 0.00675951366008),
                triggerBin(70.0, 0.904255319149, 0.0123897719299),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217376582921, 0.00120001841096),
                triggerBin(25.0, 0.0269065981148, 0.0012229975932),
                triggerBin(29.0, 0.06840617324, 0.00171856284493),
                triggerBin(33.0, 0.533782204143, 0.00341115562995),
                triggerBin(37.0, 0.869640387275, 0.00255603391304),
                triggerBin(41.0, 0.896981445583, 0.00292062019552),
                triggerBin(45.0, 0.901758641601, 0.00366481462932),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.928818244644, 0.00675951366008),
                triggerBin(70.0, 0.904255319149, 0.0123897719299),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217376582921, 0.00120001841096),
                triggerBin(25.0, 0.0269065981148, 0.0012229975932),
                triggerBin(29.0, 0.06840617324, 0.00171856284493),
                triggerBin(33.0, 0.533782204143, 0.00341115562995),
                triggerBin(37.0, 0.869640387275, 0.00255603391304),
                triggerBin(41.0, 0.896981445583, 0.00292062019552),
                triggerBin(45.0, 0.901758641601, 0.00366481462932),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.928818244644, 0.00675951366008),
                triggerBin(70.0, 0.904255319149, 0.0123897719299),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217376582921, 0.00120001841096),
                triggerBin(25.0, 0.0269065981148, 0.0012229975932),
                triggerBin(29.0, 0.06840617324, 0.00171856284493),
                triggerBin(33.0, 0.533782204143, 0.00341115562995),
                triggerBin(37.0, 0.869640387275, 0.00255603391304),
                triggerBin(41.0, 0.896981445583, 0.00292062019552),
                triggerBin(45.0, 0.901758641601, 0.00366481462932),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.928818244644, 0.00675951366008),
                triggerBin(70.0, 0.904255319149, 0.0123897719299),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217376582921, 0.00120001841096),
                triggerBin(25.0, 0.0269065981148, 0.0012229975932),
                triggerBin(29.0, 0.06840617324, 0.00171856284493),
                triggerBin(33.0, 0.533782204143, 0.00341115562995),
                triggerBin(37.0, 0.869640387275, 0.00255603391304),
                triggerBin(41.0, 0.896981445583, 0.00292062019552),
                triggerBin(45.0, 0.901758641601, 0.00366481462932),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.928818244644, 0.00675951366008),
                triggerBin(70.0, 0.904255319149, 0.0123897719299),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217376582921, 0.00120001841096),
                triggerBin(25.0, 0.0269065981148, 0.0012229975932),
                triggerBin(29.0, 0.06840617324, 0.00171856284493),
                triggerBin(33.0, 0.533782204143, 0.00341115562995),
                triggerBin(37.0, 0.869640387275, 0.00255603391304),
                triggerBin(41.0, 0.896981445583, 0.00292062019552),
                triggerBin(45.0, 0.901758641601, 0.00366481462932),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.928818244644, 0.00675951366008),
                triggerBin(70.0, 0.904255319149, 0.0123897719299),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byLooseCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronVTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronVTightMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.020642689934, 0.00119754096746),
                triggerBin(25.0, 0.0293179805137, 0.00158766381766),
                triggerBin(29.0, 0.0797351755901, 0.00265341911933),
                triggerBin(33.0, 0.462622618108, 0.00529438836177),
                triggerBin(37.0, 0.751389295116, 0.00522670352152),
                triggerBin(41.0, 0.788666976312, 0.00622147698256),
                triggerBin(45.0, 0.812850205454, 0.00753834052468),
                triggerBin(50.0, 0.817351598174, 0.010658957086),
                triggerBin(55.0, 0.770833333333, 0.0162132967163),
                triggerBin(60.0, 0.798319327731, 0.0150165911374),
                triggerBin(70.0, 0.859589041096, 0.0203308020518),
                triggerBin(80.0, 0.804347826087, 0.0292452523791),
                triggerBin(100.0, 0.838095238095, 0.0359485889487),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0215299609412, 0.00141665072554),
                triggerBin(25.0, 0.0297287693948, 0.00184836037104),
                triggerBin(29.0, 0.0766969193404, 0.00300866917996),
                triggerBin(33.0, 0.481531735263, 0.00613505623449),
                triggerBin(37.0, 0.792743048708, 0.00569211897148),
                triggerBin(41.0, 0.831007751938, 0.00659889274614),
                triggerBin(45.0, 0.841326530612, 0.00825289681672),
                triggerBin(50.0, 0.867203219316, 0.0107636860484),
                triggerBin(55.0, 0.841176470588, 0.0161851187955),
                triggerBin(60.0, 0.832391713748, 0.0162093035892),
                triggerBin(70.0, 0.888372093023, 0.0214765548059),
                triggerBin(80.0, 0.918367346939, 0.0225829932723),
                triggerBin(100.0, 0.8625, 0.0385022320781),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0134474327628, 0.00284766014219),
                triggerBin(25.0, 0.0345937248592, 0.00518344097929),
                triggerBin(29.0, 0.0451306413302, 0.00584125352218),
                triggerBin(33.0, 0.493890020367, 0.0159544498051),
                triggerBin(37.0, 0.773851590106, 0.0143572665635),
                triggerBin(41.0, 0.824742268041, 0.0172634205584),
                triggerBin(45.0, 0.807073954984, 0.0223754563927),
                triggerBin(50.0, 0.84375, 0.0287049579232),
                triggerBin(55.0, 0.914634146341, 0.0308573675212),
                triggerBin(60.0, 0.74358974359, 0.0494409822762),
                triggerBin(70.0, 0.810810810811, 0.064388315182),
                triggerBin(80.0, 0.913043478261, 0.0587533847558),
                triggerBin(100.0, 0.4, 0.219089023002),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0230222322537, 0.00159321610433),
                triggerBin(25.0, 0.0288888888889, 0.00197393856807),
                triggerBin(29.0, 0.0827743902439, 0.00340199884223),
                triggerBin(33.0, 0.479384179791, 0.00664565628593),
                triggerBin(37.0, 0.796541923259, 0.00619559002844),
                triggerBin(41.0, 0.832116788321, 0.00714036635761),
                triggerBin(45.0, 0.847786537295, 0.00884625518123),
                triggerBin(50.0, 0.87170263789, 0.0115800389007),
                triggerBin(55.0, 0.827102803738, 0.0182789749367),
                triggerBin(60.0, 0.847682119205, 0.0168827369793),
                triggerBin(70.0, 0.904494382022, 0.0220296397519),
                triggerBin(80.0, 0.91935483871, 0.0244523102759),
                triggerBin(100.0, 0.893333333333, 0.0356443336102),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0197222222222, 0.00231740133272),
                triggerBin(25.0, 0.0365296803653, 0.0035159960033),
                triggerBin(29.0, 0.101577529819, 0.00592564986963),
                triggerBin(33.0, 0.489266547406, 0.0105714367116),
                triggerBin(37.0, 0.797962648557, 0.00955187961144),
                triggerBin(41.0, 0.851063829787, 0.0108285002466),
                triggerBin(45.0, 0.866108786611, 0.0127175274325),
                triggerBin(50.0, 0.81875, 0.0215347420971),
                triggerBin(55.0, 0.820987654321, 0.030119814832),
                triggerBin(60.0, 0.841530054645, 0.0269949622678),
                triggerBin(70.0, 0.909090909091, 0.0327613622798),
                triggerBin(80.0, 0.864864864865, 0.0562027291795),
                triggerBin(100.0, 0.76, 0.0854166260162),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.018850671731, 0.0011405832488),
                triggerBin(25.0, 0.0382448036952, 0.00184333613328),
                triggerBin(29.0, 0.086682427108, 0.00279254791741),
                triggerBin(33.0, 0.476364037994, 0.00524884769981),
                triggerBin(37.0, 0.789820359281, 0.00498506991503),
                triggerBin(41.0, 0.842860503411, 0.00558180908073),
                triggerBin(45.0, 0.851434798402, 0.00677846160737),
                triggerBin(50.0, 0.849348534202, 0.0102077604145),
                triggerBin(55.0, 0.866859623734, 0.0129238007516),
                triggerBin(60.0, 0.901931649331, 0.0114641990229),
                triggerBin(70.0, 0.830935251799, 0.0224795557892),
                triggerBin(80.0, 0.935643564356, 0.0172653554606),
                triggerBin(100.0, 0.876033057851, 0.0299585304844),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224014797308, 0.00106075168364),
                triggerBin(25.0, 0.0284722222222, 0.00109571361006),
                triggerBin(29.0, 0.0723280594123, 0.00155152493415),
                triggerBin(33.0, 0.536852956336, 0.00302556334621),
                triggerBin(37.0, 0.866554131119, 0.00229688920719),
                triggerBin(41.0, 0.883874718407, 0.002731075766),
                triggerBin(45.0, 0.890079460631, 0.00343208355013),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915993537964, 0.00643719403795),
                triggerBin(70.0, 0.900680272109, 0.0110321311516),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224014797308, 0.00106075168364),
                triggerBin(25.0, 0.0284722222222, 0.00109571361006),
                triggerBin(29.0, 0.0723280594123, 0.00155152493415),
                triggerBin(33.0, 0.536852956336, 0.00302556334621),
                triggerBin(37.0, 0.866554131119, 0.00229688920719),
                triggerBin(41.0, 0.883874718407, 0.002731075766),
                triggerBin(45.0, 0.890079460631, 0.00343208355013),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915993537964, 0.00643719403795),
                triggerBin(70.0, 0.900680272109, 0.0110321311516),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224014797308, 0.00106075168364),
                triggerBin(25.0, 0.0284722222222, 0.00109571361006),
                triggerBin(29.0, 0.0723280594123, 0.00155152493415),
                triggerBin(33.0, 0.536852956336, 0.00302556334621),
                triggerBin(37.0, 0.866554131119, 0.00229688920719),
                triggerBin(41.0, 0.883874718407, 0.002731075766),
                triggerBin(45.0, 0.890079460631, 0.00343208355013),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915993537964, 0.00643719403795),
                triggerBin(70.0, 0.900680272109, 0.0110321311516),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224014797308, 0.00106075168364),
                triggerBin(25.0, 0.0284722222222, 0.00109571361006),
                triggerBin(29.0, 0.0723280594123, 0.00155152493415),
                triggerBin(33.0, 0.536852956336, 0.00302556334621),
                triggerBin(37.0, 0.866554131119, 0.00229688920719),
                triggerBin(41.0, 0.883874718407, 0.002731075766),
                triggerBin(45.0, 0.890079460631, 0.00343208355013),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915993537964, 0.00643719403795),
                triggerBin(70.0, 0.900680272109, 0.0110321311516),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224014797308, 0.00106075168364),
                triggerBin(25.0, 0.0284722222222, 0.00109571361006),
                triggerBin(29.0, 0.0723280594123, 0.00155152493415),
                triggerBin(33.0, 0.536852956336, 0.00302556334621),
                triggerBin(37.0, 0.866554131119, 0.00229688920719),
                triggerBin(41.0, 0.883874718407, 0.002731075766),
                triggerBin(45.0, 0.890079460631, 0.00343208355013),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915993537964, 0.00643719403795),
                triggerBin(70.0, 0.900680272109, 0.0110321311516),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224014797308, 0.00106075168364),
                triggerBin(25.0, 0.0284722222222, 0.00109571361006),
                triggerBin(29.0, 0.0723280594123, 0.00155152493415),
                triggerBin(33.0, 0.536852956336, 0.00302556334621),
                triggerBin(37.0, 0.866554131119, 0.00229688920719),
                triggerBin(41.0, 0.883874718407, 0.002731075766),
                triggerBin(45.0, 0.890079460631, 0.00343208355013),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915993537964, 0.00643719403795),
                triggerBin(70.0, 0.900680272109, 0.0110321311516),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0224014797308, 0.00106075168364),
                triggerBin(25.0, 0.0284722222222, 0.00109571361006),
                triggerBin(29.0, 0.0723280594123, 0.00155152493415),
                triggerBin(33.0, 0.536852956336, 0.00302556334621),
                triggerBin(37.0, 0.866554131119, 0.00229688920719),
                triggerBin(41.0, 0.883874718407, 0.002731075766),
                triggerBin(45.0, 0.890079460631, 0.00343208355013),
                triggerBin(50.0, 0.903327596099, 0.00500507058512),
                triggerBin(55.0, 0.898295766905, 0.00708700667331),
                triggerBin(60.0, 0.915993537964, 0.00643719403795),
                triggerBin(70.0, 0.900680272109, 0.0110321311516),
                triggerBin(80.0, 0.888704318937, 0.0128179789923),
                triggerBin(100.0, 0.902173913043, 0.0154863319529),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byMediumCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronVTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronVTightMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0248643761302, 0.00165538394071),
                triggerBin(25.0, 0.0320360074133, 0.00202609732711),
                triggerBin(29.0, 0.0754251234229, 0.00309247166358),
                triggerBin(33.0, 0.462443859377, 0.00620477487655),
                triggerBin(37.0, 0.787349631354, 0.005699603928),
                triggerBin(41.0, 0.816012084592, 0.00673486582205),
                triggerBin(45.0, 0.841998990409, 0.00819489660817),
                triggerBin(50.0, 0.853346456693, 0.011098444664),
                triggerBin(55.0, 0.790513833992, 0.0180907742008),
                triggerBin(60.0, 0.81914893617, 0.0162069919977),
                triggerBin(70.0, 0.892376681614, 0.0207527122573),
                triggerBin(80.0, 0.823170731707, 0.0297920309945),
                triggerBin(100.0, 0.829545454545, 0.0400851073837),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0258035310095, 0.00194762060328),
                triggerBin(25.0, 0.0311669913228, 0.00231240026083),
                triggerBin(29.0, 0.0725114155251, 0.00350481756229),
                triggerBin(33.0, 0.476958049184, 0.0071801008066),
                triggerBin(37.0, 0.82858649789, 0.00612008248743),
                triggerBin(41.0, 0.866937119675, 0.00684090875083),
                triggerBin(45.0, 0.876143560873, 0.0087387616222),
                triggerBin(50.0, 0.890322580645, 0.0112248734766),
                triggerBin(55.0, 0.862694300518, 0.0175177810756),
                triggerBin(60.0, 0.852028639618, 0.0173463824878),
                triggerBin(70.0, 0.908536585366, 0.0225098702494),
                triggerBin(80.0, 0.961240310078, 0.0169946129996),
                triggerBin(100.0, 0.863636363636, 0.0422418353311),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.018147086915, 0.0041252790883),
                triggerBin(25.0, 0.0351317440402, 0.00652160819134),
                triggerBin(29.0, 0.0519337016575, 0.00737597955211),
                triggerBin(33.0, 0.500685871056, 0.0185185010956),
                triggerBin(37.0, 0.807383627608, 0.0157994709808),
                triggerBin(41.0, 0.889807162534, 0.0164350609598),
                triggerBin(45.0, 0.839826839827, 0.0241314688237),
                triggerBin(50.0, 0.872, 0.0298819008766),
                triggerBin(55.0, 0.964285714286, 0.0247987526725),
                triggerBin(60.0, 0.72972972973, 0.0516255032406),
                triggerBin(70.0, 0.785714285714, 0.109664210511),
                triggerBin(80.0, 1.0, 0.0),
                triggerBin(100.0, 0.4, 0.219089023002),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0272401433692, 0.00217916650562),
                triggerBin(25.0, 0.0305154639175, 0.00246978735173),
                triggerBin(29.0, 0.0765864332604, 0.00393383325677),
                triggerBin(33.0, 0.472749391727, 0.00778759079569),
                triggerBin(37.0, 0.832754812244, 0.00662940071999),
                triggerBin(41.0, 0.862987630828, 0.00750007865059),
                triggerBin(45.0, 0.883193277311, 0.00931082825945),
                triggerBin(50.0, 0.893846153846, 0.0120821041915),
                triggerBin(55.0, 0.845454545455, 0.0198983140008),
                triggerBin(60.0, 0.878260869565, 0.0176042414649),
                triggerBin(70.0, 0.92, 0.0221509969678),
                triggerBin(80.0, 0.953703703704, 0.0202193868385),
                triggerBin(100.0, 0.901639344262, 0.0381295972),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0234128770824, 0.00320854851172),
                triggerBin(25.0, 0.0403775563713, 0.0045075947862),
                triggerBin(29.0, 0.0990643918547, 0.0070085504081),
                triggerBin(33.0, 0.504944375773, 0.012429667477),
                triggerBin(37.0, 0.828193832599, 0.010221080698),
                triggerBin(41.0, 0.862721893491, 0.0118388003141),
                triggerBin(45.0, 0.878571428571, 0.0138024113751),
                triggerBin(50.0, 0.904564315353, 0.0189263384003),
                triggerBin(55.0, 0.841666666667, 0.0333246516472),
                triggerBin(60.0, 0.875862068966, 0.0273833205101),
                triggerBin(70.0, 0.949152542373, 0.0286006974195),
                triggerBin(80.0, 0.857142857143, 0.059148476515),
                triggerBin(100.0, 0.727272727273, 0.0949514487031),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0207080828323, 0.00150258658222),
                triggerBin(25.0, 0.0372551705246, 0.0022164487871),
                triggerBin(29.0, 0.0826128722382, 0.00322497087726),
                triggerBin(33.0, 0.473684210526, 0.00607962338413),
                triggerBin(37.0, 0.817552876062, 0.00542992831874),
                triggerBin(41.0, 0.865432098765, 0.0059953526547),
                triggerBin(45.0, 0.869911090314, 0.00727704917336),
                triggerBin(50.0, 0.869752421959, 0.0110426878161),
                triggerBin(55.0, 0.872865275142, 0.0145111019851),
                triggerBin(60.0, 0.938650306748, 0.0108518474853),
                triggerBin(70.0, 0.906735751295, 0.020932413893),
                triggerBin(80.0, 0.95625, 0.0161701765412),
                triggerBin(100.0, 0.895833333333, 0.0311775781182),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221802142407, 0.00116902504462),
                triggerBin(25.0, 0.0265463233342, 0.00117132394766),
                triggerBin(29.0, 0.0680924605746, 0.00165579792542),
                triggerBin(33.0, 0.53405206416, 0.00330233940807),
                triggerBin(37.0, 0.870610583446, 0.0024726212662),
                triggerBin(41.0, 0.897764685496, 0.00281994860186),
                triggerBin(45.0, 0.900925266904, 0.0035645332878),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.934405144695, 0.00627823117321),
                triggerBin(70.0, 0.915, 0.0113852975367),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221802142407, 0.00116902504462),
                triggerBin(25.0, 0.0265463233342, 0.00117132394766),
                triggerBin(29.0, 0.0680924605746, 0.00165579792542),
                triggerBin(33.0, 0.53405206416, 0.00330233940807),
                triggerBin(37.0, 0.870610583446, 0.0024726212662),
                triggerBin(41.0, 0.897764685496, 0.00281994860186),
                triggerBin(45.0, 0.900925266904, 0.0035645332878),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.934405144695, 0.00627823117321),
                triggerBin(70.0, 0.915, 0.0113852975367),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221802142407, 0.00116902504462),
                triggerBin(25.0, 0.0265463233342, 0.00117132394766),
                triggerBin(29.0, 0.0680924605746, 0.00165579792542),
                triggerBin(33.0, 0.53405206416, 0.00330233940807),
                triggerBin(37.0, 0.870610583446, 0.0024726212662),
                triggerBin(41.0, 0.897764685496, 0.00281994860186),
                triggerBin(45.0, 0.900925266904, 0.0035645332878),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.934405144695, 0.00627823117321),
                triggerBin(70.0, 0.915, 0.0113852975367),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221802142407, 0.00116902504462),
                triggerBin(25.0, 0.0265463233342, 0.00117132394766),
                triggerBin(29.0, 0.0680924605746, 0.00165579792542),
                triggerBin(33.0, 0.53405206416, 0.00330233940807),
                triggerBin(37.0, 0.870610583446, 0.0024726212662),
                triggerBin(41.0, 0.897764685496, 0.00281994860186),
                triggerBin(45.0, 0.900925266904, 0.0035645332878),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.934405144695, 0.00627823117321),
                triggerBin(70.0, 0.915, 0.0113852975367),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221802142407, 0.00116902504462),
                triggerBin(25.0, 0.0265463233342, 0.00117132394766),
                triggerBin(29.0, 0.0680924605746, 0.00165579792542),
                triggerBin(33.0, 0.53405206416, 0.00330233940807),
                triggerBin(37.0, 0.870610583446, 0.0024726212662),
                triggerBin(41.0, 0.897764685496, 0.00281994860186),
                triggerBin(45.0, 0.900925266904, 0.0035645332878),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.934405144695, 0.00627823117321),
                triggerBin(70.0, 0.915, 0.0113852975367),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221802142407, 0.00116902504462),
                triggerBin(25.0, 0.0265463233342, 0.00117132394766),
                triggerBin(29.0, 0.0680924605746, 0.00165579792542),
                triggerBin(33.0, 0.53405206416, 0.00330233940807),
                triggerBin(37.0, 0.870610583446, 0.0024726212662),
                triggerBin(41.0, 0.897764685496, 0.00281994860186),
                triggerBin(45.0, 0.900925266904, 0.0035645332878),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.934405144695, 0.00627823117321),
                triggerBin(70.0, 0.915, 0.0113852975367),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0221802142407, 0.00116902504462),
                triggerBin(25.0, 0.0265463233342, 0.00117132394766),
                triggerBin(29.0, 0.0680924605746, 0.00165579792542),
                triggerBin(33.0, 0.53405206416, 0.00330233940807),
                triggerBin(37.0, 0.870610583446, 0.0024726212662),
                triggerBin(41.0, 0.897764685496, 0.00281994860186),
                triggerBin(45.0, 0.900925266904, 0.0035645332878),
                triggerBin(50.0, 0.918172519605, 0.00506122568191),
                triggerBin(55.0, 0.905835543767, 0.00752086008928),
                triggerBin(60.0, 0.934405144695, 0.00627823117321),
                triggerBin(70.0, 0.915, 0.0113852975367),
                triggerBin(80.0, 0.894422310757, 0.0137153068862),
                triggerBin(100.0, 0.902280130293, 0.0169470046522),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)

tauLegEfficiency_byTightCombinedIsolationDeltaBetaCorr3Hits_againstMuonTight2_againstElectronVTightMVA3 = cms.untracked.PSet(
    # The selected triggers for the efficiency. If one trigger is
    # given, the parametrization of it is used as it is (i.e.
    # luminosity below is ignored). If multiple triggers are given,
    # their parametrizations are used weighted by the luminosities
    # given below.
    # selectTriggers = cms.VPSet(
    #     cms.PSet(
    #         trigger = cms.string("HLT_IsoPFTau35_Trk20_EPS"),
    #         luminosity = cms.double(0)
    #     ),
    # ),
    # The parameters of the trigger efficiency parametrizations,
    # looked dynamically from TriggerEfficiency_cff.py

    # Offline selection: Sum$(PFTauPt > 20 && abs(PFTauEta) < 2.1&& PFTauLeadChargedHadrCandPt > 20&& PFTauProng == 1&& PFTau_againstElectronVTightMVA3 > 0.5&& PFTau_againstMuonTight2 > 0.5&& PFTau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5) == 1 && Sum$(MuonPt > 15&& MuonIsGlobalMuon) == 1&& sqrt(2*(sqrt(MuonPt*TMath::Cos(MuonPhi)*MuonPt*TMath::Cos(MuonPhi)+MuonPt*TMath::Sin(MuonPhi)*MuonPt*TMath::Sin(MuonPhi)+MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta))))*sqrt(PFTauPt*TMath::Cos(PFTauPhi)*PFTauPt*TMath::Cos(PFTauPhi)+PFTauPt*TMath::Sin(PFTauPhi)*PFTauPt*TMath::Sin(PFTauPhi)+PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))-MuonPt*TMath::Cos(MuonPhi)*PFTauPt*TMath::Cos(PFTauPhi)-MuonPt*TMath::Sin(MuonPhi)*PFTauPt*TMath::Sin(PFTauPhi)-MuonPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-MuonEta)))*PFTauPt/TMath::Tan(2.0*TMath::ATan(TMath::Exp(-PFTauEta))))) < 80&& sqrt( 2 * MuonPt * PFMET_ET * (1-cos(MuonPhi-PFMET_phi)) ) < 40

    dataParameters = cms.PSet(
        # 2012ABC
        runs_190456_202585 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(202585),
            luminosity = cms.double(11736), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0256213169357, 0.00178834101867),
                triggerBin(25.0, 0.0313888066331, 0.00212168846819),
                triggerBin(29.0, 0.071916249431, 0.00318222910574),
                triggerBin(33.0, 0.462676529926, 0.0064650391674),
                triggerBin(37.0, 0.792965459141, 0.00588021470429),
                triggerBin(41.0, 0.813983739837, 0.00701714998125),
                triggerBin(45.0, 0.839803171132, 0.00857647566756),
                triggerBin(50.0, 0.871244635193, 0.0109709634731),
                triggerBin(55.0, 0.809210526316, 0.0184003271815),
                triggerBin(60.0, 0.829365079365, 0.0167568183525),
                triggerBin(70.0, 0.895238095238, 0.0211330082677),
                triggerBin(80.0, 0.839160839161, 0.0307220707412),
                triggerBin(100.0, 0.819277108434, 0.0422360161545),
            ),
        ),
        # 2012AB
        runs_190456_196531 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(5126), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0262165867032, 0.00209151805801),
                triggerBin(25.0, 0.0313547623743, 0.00244730064919),
                triggerBin(29.0, 0.0690842787682, 0.00360958456451),
                triggerBin(33.0, 0.477043673012, 0.00747482534226),
                triggerBin(37.0, 0.834530307383, 0.00629837152731),
                triggerBin(41.0, 0.864111498258, 0.00715138740579),
                triggerBin(45.0, 0.873379099924, 0.00918444144813),
                triggerBin(50.0, 0.908579465541, 0.0108085773837),
                triggerBin(55.0, 0.879310344828, 0.0174629050449),
                triggerBin(60.0, 0.866485013624, 0.0177546658709),
                triggerBin(70.0, 0.915584415584, 0.0224026890668),
                triggerBin(80.0, 0.958333333333, 0.0182415632452),
                triggerBin(100.0, 0.852459016393, 0.0454075608933),
            ),
        ),
        # 2012A
        runs_190456_193621 = cms.PSet(
            firstRun = cms.uint32(190456),
            lastRun = cms.uint32(193621),
            luminosity = cms.double(697.308), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0188470066519, 0.00452779014347),
                triggerBin(25.0, 0.0397163120567, 0.00735511850658),
                triggerBin(29.0, 0.0530759951749, 0.00778626841095),
                triggerBin(33.0, 0.503671071953, 0.0191595251931),
                triggerBin(37.0, 0.815008726003, 0.0162210678158),
                triggerBin(41.0, 0.889534883721, 0.0169010951864),
                triggerBin(45.0, 0.839622641509, 0.0252026186658),
                triggerBin(50.0, 0.877192982456, 0.0307402036864),
                triggerBin(55.0, 0.958333333333, 0.0288424439685),
                triggerBin(60.0, 0.761904761905, 0.0536605876018),
                triggerBin(70.0, 0.785714285714, 0.109664210511),
                triggerBin(80.0, 1.0, 0.0),
                triggerBin(100.0, 0.4, 0.219089023002),
            ),
        ),
        # 2012B
        runs_193834_196531 = cms.PSet(
            firstRun = cms.uint32(193834),
            lastRun = cms.uint32(196531),
            luminosity = cms.double(4428), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.027563842724, 0.00233077772146),
                triggerBin(25.0, 0.030004580852, 0.00258188418966),
                triggerBin(29.0, 0.072315558802, 0.00404160306489),
                triggerBin(33.0, 0.472251585624, 0.0081156744417),
                triggerBin(37.0, 0.838376891334, 0.00682612404927),
                triggerBin(41.0, 0.859631147541, 0.00786233491442),
                triggerBin(45.0, 0.879890809827, 0.00980626587532),
                triggerBin(50.0, 0.914572864322, 0.011439839008),
                triggerBin(55.0, 0.866666666667, 0.0196261352585),
                triggerBin(60.0, 0.888157894737, 0.0180763593026),
                triggerBin(70.0, 0.928571428571, 0.0217660500079),
                triggerBin(80.0, 0.950980392157, 0.021378174203),
                triggerBin(100.0, 0.892857142857, 0.0413312544541),
            ),
        ),
        # 2012C
        runs_198022_203742 = cms.PSet(
            firstRun = cms.uint32(198022),
            lastRun = cms.uint32(203742),
            luminosity = cms.double(6892), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0253807106599, 0.00354353133297),
                triggerBin(25.0, 0.038027332145, 0.0046621606814),
                triggerBin(29.0, 0.0948640483384, 0.00720292239581),
                triggerBin(33.0, 0.509103169252, 0.0129815765586),
                triggerBin(37.0, 0.834254143646, 0.0104467744615),
                triggerBin(41.0, 0.869062901155, 0.0120861570626),
                triggerBin(45.0, 0.876447876448, 0.0144585011478),
                triggerBin(50.0, 0.923076923077, 0.0179246685549),
                triggerBin(55.0, 0.87037037037, 0.0323215598198),
                triggerBin(60.0, 0.868613138686, 0.0288621634959),
                triggerBin(70.0, 0.946428571429, 0.0300896074288),
                triggerBin(80.0, 0.913043478261, 0.0587533847558),
                triggerBin(100.0, 0.727272727273, 0.0949514487031),
            ),
        ),
        # 2012D
        runs_202807_208686 = cms.PSet(
            firstRun = cms.uint32(202807),
            lastRun = cms.uint32(208686),
            luminosity = cms.double(7274), # 1/pb
            bins = cms.VPSet(
                triggerBin(20.0, 0.0223118618429, 0.0016582475028),
                triggerBin(25.0, 0.0389016018307, 0.00238825843839),
                triggerBin(29.0, 0.0803693052823, 0.00334464233772),
                triggerBin(33.0, 0.470408981556, 0.00632105951281),
                triggerBin(37.0, 0.819743422483, 0.00566829997909),
                triggerBin(41.0, 0.867627345845, 0.0062039222272),
                triggerBin(45.0, 0.873232323232, 0.0074771582437),
                triggerBin(50.0, 0.867058823529, 0.0116451363273),
                triggerBin(55.0, 0.874239350913, 0.0149335857796),
                triggerBin(60.0, 0.947136563877, 0.010501614439),
                triggerBin(70.0, 0.919075144509, 0.0207344932315),
                triggerBin(80.0, 0.950704225352, 0.0181670071736),
                triggerBin(100.0, 0.888888888889, 0.033126933),
            ),
        ),
    ),
    mcParameters = cms.PSet(
        Summer12_PU_2012ABC = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217671390791, 0.00120162777912),
                triggerBin(25.0, 0.0269204389575, 0.001223618005),
                triggerBin(29.0, 0.0683673469388, 0.00171878809199),
                triggerBin(33.0, 0.533857089413, 0.00341136018278),
                triggerBin(37.0, 0.87009167964, 0.00255292983991),
                triggerBin(41.0, 0.897147077832, 0.00291881025225),
                triggerBin(45.0, 0.902168967086, 0.00365881729775),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.930103806228, 0.00670746709179),
                triggerBin(70.0, 0.909090909091, 0.0121374061326),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012AB = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217671390791, 0.00120162777912),
                triggerBin(25.0, 0.0269204389575, 0.001223618005),
                triggerBin(29.0, 0.0683673469388, 0.00171878809199),
                triggerBin(33.0, 0.533857089413, 0.00341136018278),
                triggerBin(37.0, 0.87009167964, 0.00255292983991),
                triggerBin(41.0, 0.897147077832, 0.00291881025225),
                triggerBin(45.0, 0.902168967086, 0.00365881729775),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.930103806228, 0.00670746709179),
                triggerBin(70.0, 0.909090909091, 0.0121374061326),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012A = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217671390791, 0.00120162777912),
                triggerBin(25.0, 0.0269204389575, 0.001223618005),
                triggerBin(29.0, 0.0683673469388, 0.00171878809199),
                triggerBin(33.0, 0.533857089413, 0.00341136018278),
                triggerBin(37.0, 0.87009167964, 0.00255292983991),
                triggerBin(41.0, 0.897147077832, 0.00291881025225),
                triggerBin(45.0, 0.902168967086, 0.00365881729775),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.930103806228, 0.00670746709179),
                triggerBin(70.0, 0.909090909091, 0.0121374061326),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012B = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217671390791, 0.00120162777912),
                triggerBin(25.0, 0.0269204389575, 0.001223618005),
                triggerBin(29.0, 0.0683673469388, 0.00171878809199),
                triggerBin(33.0, 0.533857089413, 0.00341136018278),
                triggerBin(37.0, 0.87009167964, 0.00255292983991),
                triggerBin(41.0, 0.897147077832, 0.00291881025225),
                triggerBin(45.0, 0.902168967086, 0.00365881729775),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.930103806228, 0.00670746709179),
                triggerBin(70.0, 0.909090909091, 0.0121374061326),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012C = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217671390791, 0.00120162777912),
                triggerBin(25.0, 0.0269204389575, 0.001223618005),
                triggerBin(29.0, 0.0683673469388, 0.00171878809199),
                triggerBin(33.0, 0.533857089413, 0.00341136018278),
                triggerBin(37.0, 0.87009167964, 0.00255292983991),
                triggerBin(41.0, 0.897147077832, 0.00291881025225),
                triggerBin(45.0, 0.902168967086, 0.00365881729775),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.930103806228, 0.00670746709179),
                triggerBin(70.0, 0.909090909091, 0.0121374061326),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_2012D = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217671390791, 0.00120162777912),
                triggerBin(25.0, 0.0269204389575, 0.001223618005),
                triggerBin(29.0, 0.0683673469388, 0.00171878809199),
                triggerBin(33.0, 0.533857089413, 0.00341136018278),
                triggerBin(37.0, 0.87009167964, 0.00255292983991),
                triggerBin(41.0, 0.897147077832, 0.00291881025225),
                triggerBin(45.0, 0.902168967086, 0.00365881729775),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.930103806228, 0.00670746709179),
                triggerBin(70.0, 0.909090909091, 0.0121374061326),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
        Summer12_PU_Unweighted = cms.PSet(
            bins = cms.VPSet(
                triggerBin(20.0, 0.0217671390791, 0.00120162777912),
                triggerBin(25.0, 0.0269204389575, 0.001223618005),
                triggerBin(29.0, 0.0683673469388, 0.00171878809199),
                triggerBin(33.0, 0.533857089413, 0.00341136018278),
                triggerBin(37.0, 0.87009167964, 0.00255292983991),
                triggerBin(41.0, 0.897147077832, 0.00291881025225),
                triggerBin(45.0, 0.902168967086, 0.00365881729775),
                triggerBin(50.0, 0.91768511862, 0.00521083666235),
                triggerBin(55.0, 0.906628652887, 0.0077677045217),
                triggerBin(60.0, 0.930103806228, 0.00670746709179),
                triggerBin(70.0, 0.909090909091, 0.0121374061326),
                triggerBin(80.0, 0.893162393162, 0.0142792160091),
                triggerBin(100.0, 0.896551724138, 0.0178834088091),
            ),
        ),
    ),
    dataSelect = cms.vstring(),
    mcSelect = cms.string("Summer12_PU_2012ABC"),
    mode = cms.untracked.string("disabled") # dataEfficiency, scaleFactor, disabled
)
