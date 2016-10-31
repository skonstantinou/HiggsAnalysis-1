#!/usr/bin/env python

from HiggsAnalysis.NtupleAnalysis.main import PSet
import HiggsAnalysis.NtupleAnalysis.parameters.scaleFactors as scaleFactors

#================================================================================================
# General parameters
#================================================================================================
verbose               = False
histogramAmbientLevel = "Debug"  # Options: Systematics, Vital, Informative, Debug


#================================================================================================
# Trigger
#================================================================================================
trigger = PSet(
  # No need to specify version numbers, they are automatically scanned in range 1--100 (remove the '_v' suffix)
    triggerOR = [
        "HLT_PFHT400_SixJet30_DoubleBTagCSV_p056",
        "HLT_PFHT450_SixJet40_BTagCSV_p056",
        #"HLT_QuadJet45_DoubleBTagCSV_p087",
        #"HLT_QuadPFJetBF",
        #"HLT_PFHT300",
        #"HLT_PFHT400",
        #"HLT_PFHT475",
        #"HLT_PFHT600",
        #"HLT_PFHT650",
        #"HLT_PFHT400_SixJet30_DoubleBTagCSV_p056",
        #"HLT_PFHT450_SixJet40_BTagCSV_p056",
        #"HLT_PFHT400_SixJet30",
        #"HLT_PFHT450_SixJet40",
        #"HLT_HT200",
        #"HLT_HT275",
        #"HLT_HT325",
        #"HLT_HT425",
        #"HLT_HT575",
        #"HLT_HT650",
        #"HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200",
        #"HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460",
        #"HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240",
        #"HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500",
        #"HLT_QuadPFJet_VBF",
    ],
  triggerOR2 = [],
)

#================================================================================================
# MET filter
#================================================================================================
metFilter = PSet(
    discriminators = ["hbheNoiseTokenRun2Loose", # Loose is recommended
                      "Flag_HBHENoiseIsoFilter",
                      "Flag_EcalDeadCellTriggerPrimitiveFilter",
                      "Flag_CSCTightHaloFilter",
                      "Flag_eeBadScFilter",
                      "Flag_goodVertices"]
)

#================================================================================================
# Electron veto
#================================================================================================
eVeto = PSet(
    electronPtCut         = 15.0,
    electronEtaCut        = 2.5,
    electronNCutValue     =  1,
    electronNCutDirection = "<",    # options: ==, !=, <, <=, >, >=
    electronID            = "cutBasedElectronID_Spring15_25ns_V1_standalone_veto",
    electronIsolation     = "veto", # loosest possible for vetoing ("veto"), "tight" for selecting
)

#================================================================================================
# Muon veto
#================================================================================================
muVeto = PSet(
    muonPtCut         = 10.0,
    muonEtaCut        = 2.5,
    muonNCutValue     =  1,
    muonNCutDirection = "<",         # options: ==, !=, <, <=, >, >=
    muonID            = "muIDLoose", # loosest option for vetoing (options: muIDLoose, muIDMedium, muIDTight)
    muonIsolation     = "veto",      # loosest possible for vetoing ("veto"), "tight" for selecting
)

#================================================================================================
# Jet selection
#================================================================================================
jetSelection = PSet(
    jetType                  = "Jets",    # options: Jets (AK4PFCHS), JetsPuppi (AK4Puppi)
    jetPtCut                 = 30.0,
    jetEtaCut                =  5.0,
    numberOfJetsCutValue     =  6,
    numberOfJetsCutDirection = ">=",      # options: ==, !=, <, <=, >, >=
    jetIDDiscr               = "IDloose", # options: IDloose, IDtight, IDtightLeptonVeto
    jetPUIDDiscr             = "",        # does not work at the moment 
    tauMatchingDeltaR        = 0.4,       # todo: remove dependency
    # jetLdgPtCuts             = [70.0, 50.0, 40.0],
)

#================================================================================================
# B-jet selection
#================================================================================================
bjetSelection = PSet(
    jetPtCut                  = 30.0,
    jetEtaCut                 = 2.5,
    bjetDiscr                 = "pfCombinedInclusiveSecondaryVertexV2BJetTags",
    bjetDiscrWorkingPoint     = "Loose",
    numberOfBJetsCutValue     = 1,
    numberOfBJetsCutDirection = ">=", # options: ==, !=, <, <=, >, >=
)

scaleFactors.setupBtagSFInformation(btagPset               = bjetSelection, 
                                    btagPayloadFilename    = "CSVv2.csv",
                                    btagEfficiencyFilename = "btageff_hybrid.json",
                                    direction              = "nominal")

#================================================================================================
# MET selection
#================================================================================================
metSelection = PSet(
    METCutValue                 = 100.0,
    METCutDirection             = "<=",        # options: ==, !=, <, <=, >, >=
    METSignificanceCutValue     = -1000.0,
    METSignificanceCutDirection = ">",         # options: ==, !=, <, <=, >, >=
    METType                     = "MET_Type1", # options: MET_Type1, MET_Type1_NoHF, MET_Puppi, GenMET, L1MET, HLTMET, CaloMET
    applyPhiCorrections          = False
)


#================================================================================================
# HT selection
#================================================================================================
htSelection = PSet(
    HtCutValue                 = 300.0,
    HtCutDirection             = ">=",        # options: ==, !=, <, <=, >, >=
    HtSignificanceCutValue     = -1000.0,
    HtSignificanceCutDirection = ">=",        # options: ==, !=, <, <=, >, >=
    # HTType                     = "MET_Type1", # options: MET_Type1, MET_Type1_NoHF, MET_Puppi, GenMET, L1MET, HLTMET, CaloMET
)

#================================================================================================
# MET trigger SF
#================================================================================================
scaleFactors.assignMETTriggerSF(metSelection, bjetSelection.bjetDiscrWorkingPoint, "nominal")


#================================================================================================
# Common plots options
#================================================================================================
commonPlotsOptions = PSet(
    # Splitting of histograms as function of one or more parameters
    # Example: histogramSplitting = [PSet(label="tauPt", binLowEdges=[60, 70, 80, 100, 120], useAbsoluteValues=False)],
    histogramSplitting = [],

    # By default, inclusive (i.e. fake tau+genuine tau) and fake tau histograms are produced. Set to true to also produce genuine tau histograms
    enableGenuineTauHistograms = False, 

    # Bin settings (final bin setting done in datacardGenerator, there also variable bin width is supported)
    nVerticesBins     = PSet(nBins =  80, axisMin =  0.0, axisMax =  60.0),
    bjetDiscrBins     = PSet(nBins =  20, axisMin = -1.0, axisMax =   1.0),
    ptBins            = PSet(nBins =  50, axisMin =  0.0, axisMax = 500.0),
    etaBins           = PSet(nBins =  50, axisMin = -5.0, axisMax =   5.0),
    phiBins           = PSet(nBins =  64, axisMin = -3.2, axisMax =   3.2),  # PSet(nBins =  72, axisMin = -3.1415926, axisMax=3.1415926),
    invmassBins       = PSet(nBins =  50, axisMin =  0.0, axisMax = 500.0),
    deltaEtaBins      = PSet(nBins =  50, axisMin =  0.0, axisMax =  10.0),
    deltaPhiBins      = PSet(nBins =  32, axisMin =  0.0, axisMax =  3.2),  # Note: putting high number of bins here will cause troubles
    deltaRBins        = PSet(nBins =  50, axisMin =  0.0, axisMax =  10.0),
    njetsBins         = PSet(nBins =  20, axisMin =  0.0, axisMax = 10.0),
    metBins           = PSet(nBins =  80, axisMin =  0.0, axisMax = 800.0), # Note: use 10 GeV bin width because of QCD measurement
    enablePUDependencyPlots = True, # Enable/Disable some debug-level plots
    # Todo: Remove dependency on these unused
    rtauBins          = PSet(nBins=55, axisMin=0., axisMax=1.1),
    angularCuts1DBins = PSet(nBins=52, axisMin=0., axisMax=260.),
    topMassBins = PSet(nBins=60, axisMin=0., axisMax=600.),
    WMassBins = PSet(nBins=60, axisMin=0., axisMax=300.),
    mtBins = PSet(nBins=800, axisMin=0., axisMax=4000.), # 5 GeV bin width for tail fitter
    #invmassBins = PSet(nBins=50, axisMin=0., axisMax=500.),
)

#================================================================================================
# Build all selections group
#================================================================================================
allSelections = PSet(
    BJetSelection         = bjetSelection,
    CommonPlots           = commonPlotsOptions,
    ElectronSelection     = eVeto,
    HistogramAmbientLevel = histogramAmbientLevel,
    HtSelection           = htSelection,
    JetSelection          = jetSelection,
    METFilter             = metFilter,
    METSelection          = metSelection,
    MuonSelection         = muVeto,
    Trigger               = trigger,
    Verbose               = verbose,
)

