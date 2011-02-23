import FWCore.ParameterSet.Config as cms
from HiggsAnalysis.HeavyChHiggsToTauNu.HChOptions import getOptionsDataVersion

################################################################################
# Configuration

# Select the version of the data
#dataVersion = "39Xredigi"
dataVersion = "39Xdata"

##########
# Flags for additional signal analysis modules

# Perform the signal analysis with all tau ID algorithms in addition
# to the "golden" analysis
doAllTauIds = True

# Perform the signal analysis with the JES variations in addition to
# the "golden" analysis
doJESVariation = False
JESVariation = 0.03
JESEtaVariation = 0.02
JESUnclusteredMETVariation = 0.10

################################################################################

# Command line arguments (options) and DataVersion object
options, dataVersion = getOptionsDataVersion(dataVersion)

################################################################################
# Define the process
process = cms.Process("HChQCDMeasurementMethod2Part1")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source('PoolSource',
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring(
    #"file:/media/disk/attikis/PATTuples/v9_1/test_pattuple_v9_qcd120170.root"
    #"file:/media/disk/attikis/PATTuples/v9_1/test_pattuple_v9_JetMet2010A_86.root"
    #"rfio:/castor/cern.ch/user/w/wendland/test_pattuplev9_signalM120.root"
    #"rfio:/castor/cern.ch/user/w/wendland/test_pattuple_v9_qcd120170.root"
    "file:/media/disk/attikis/tmp/pattuple_19_1_3id.root"
    #"rfio:/castor/cern.ch/user/w/wendland/test_pattuplev9_signalM120.root"
    #"rfio:/castor/cern.ch/user/w/wendland/test_pattuple_v9_qcd120170.root"
    #"rfio:/castor/cern.ch/user/w/wendland/test_pattuple_v9_JetMet2010A_86.root"
    # For testing in lxplus
    #dataVersion.getAnalysisDefaultFileCastor()
    # For testing in jade
    #dataVersion.getAnalysisDefaultFileMadhatter()
    #dataVersion.getAnalysisDefaultFileMadhatterDcap()
    )
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string(dataVersion.getGlobalTag())
print "GlobalTag="+dataVersion.getGlobalTag()

process.load("HiggsAnalysis.HeavyChHiggsToTauNu.HChCommon_cfi")

# Uncomment the following in order to print the counters at the end of
# the job (note that if many other modules are being run in the same
# job, their INFO messages are printed too)
#process.MessageLogger.cerr.threshold = cms.untracked.string("INFO")
#process.MessageLogger.cerr.FwkReport.reportEvery = 5

# Fragment to run PAT on the fly if requested from command line
from HiggsAnalysis.HeavyChHiggsToTauNu.HChPatTuple import addPatOnTheFly
process.commonSequence, additionalCounters = addPatOnTheFly(process, options, dataVersion)

# Add configuration information to histograms.root
from HiggsAnalysis.HeavyChHiggsToTauNu.HChTools import addConfigInfo
process.infoPath = addConfigInfo(process, options)

################################################################################
# qcdMeasurementControlRegionSelection module

# Primary vertex selection
from HiggsAnalysis.HeavyChHiggsToTauNu.HChPrimaryVertex import addPrimaryVertexSelection
addPrimaryVertexSelection(process, process.commonSequence)

# Import default parameter set and make necessary tweaks
import HiggsAnalysis.HeavyChHiggsToTauNu.HChSignalAnalysisParameters_cff as param
# Set tau selection mode (options: 'antitautag', 'antiisolatedtau', 'standard')
#param.setAllTauSelectionOperatingMode('standard')
#param.setAllTauSelectionOperatingMode('factorized')
param.setAllTauSelectionOperatingMode('antitautag')
#param.setAllTauSelectionOperatingMode('antiisolatedtau')

param.setTauIDFactorizationMap(options) # Set Tau ID factorization map

# Set tau sources to non-trigger matched tau collections
param.setAllTauSelectionSrcSelectedPatTaus()
# Set other cuts
param.trigger.triggers = [
    "HLT_Jet30U_v3"
]

# Overwrite necessary values here
param.trigger.hltMetCut = 45.0 # note: 45 is the minimum possible value for which HLT_MET is saved (see histogram hlt_met)
#param.InvMassVetoOnJets.setTrueToUseModule = True
param.InvMassVetoOnJets.setTrueToUseModule = False
param.overrideTriggerFromOptions(options)

##############################################################################
process.qcdMeasurementMethod2Part1 = cms.EDProducer("HPlusQCDMeasurementFromAntiTauControlRegionProducer",
    trigger = param.trigger,
    primaryVertexSelection = param.primaryVertexSelection,
    # Set here the tau algorithm
    GlobalElectronVeto = param.GlobalElectronVeto,
    GlobalMuonVeto = param.GlobalMuonVeto,
    tauSelection = param.tauSelectionHPSTauBased,
    jetSelection = param.jetSelection,
    EvtTopology = param.EvtTopology, ### only for histogramming reasons - does not affect analysis
    InvMassVetoOnJets = param.InvMassVetoOnJets,
    MET = param.MET,
    bTagging = param.bTagging,                                                    
    fakeMETVeto = param.fakeMETVeto,
    TriggerEmulationEfficiency = param.TriggerEmulationEfficiency
)

# Prescale fetching done automatically for data
if dataVersion.isData():
    process.load("HiggsAnalysis.HeavyChHiggsToTauNu.HPlusPrescaleWeightProducer_cfi")
    process.hplusPrescaleWeightProducer.prescaleWeightTriggerResults.setProcessName(dataVersion.getTriggerProcess())
    process.hplusPrescaleWeightProducer.prescaleWeightHltPaths = param.trigger.triggers.value()
    process.commonSequence *= process.hplusPrescaleWeightProducer
    process.qcdMeasurementMethod2Part1.prescaleSource = cms.untracked.InputTag("hplusPrescaleWeightProducer")

# Print output
print "Trigger:", process.qcdMeasurementMethod2Part1.trigger
print "Cut on HLT MET (check histogram Trigger_HLT_MET for minimum value):", process.qcdMeasurementMethod2Part1.trigger.hltMetCut
print "TauSelection algorithm:", process.qcdMeasurementMethod2Part1.tauSelection.selection
print "TauSelection src:", process.qcdMeasurementMethod2Part1.tauSelection.src
print "TauSelection operating mode:", process.qcdMeasurementMethod2Part1.tauSelection.operatingMode
print "TauSelection selection:", process.qcdMeasurementMethod2Part1.tauSelection.selection
print "TauSelection invMassCut:", process.qcdMeasurementMethod2Part1.tauSelection.invMassCut
print "TauSelection rtauCut:", process.qcdMeasurementMethod2Part1.tauSelection.rtauCut
print "TauSelection antiRtauCut:", process.qcdMeasurementMethod2Part1.tauSelection.antiRtauCut
print "\nGlobalElectronVeto: ", process.qcdMeasurementMethod2Part1.GlobalElectronVeto
print "\nGlobalMuonVeto: ", process.qcdMeasurementMethod2Part1.GlobalMuonVeto
print "\nMET: ", process.qcdMeasurementMethod2Part1.MET
print "\nbTagging: ", process.qcdMeasurementMethod2Part1.bTagging
print "\nInvMassVetoOnJets:", process.qcdMeasurementMethod2Part1.InvMassVetoOnJets
print "\nFakeMETVeto:", process.qcdMeasurementMethod2Part1.fakeMETVeto
print "\nTriggerEmulationEfficiency:", process.qcdMeasurementMethod2Part1.TriggerEmulationEfficiency
print "\nEvtTopology:", process.qcdMeasurementMethod2Part1.EvtTopology

# Counter analyzer (in order to produce compatible root file with the
# python approach)
process.qcdMeasurementMethod2Part1Counters = cms.EDAnalyzer("HPlusEventCountAnalyzer",
    counterNames = cms.untracked.InputTag("qcdMeasurementMethod2Part1", "counterNames"),
    counterInstances = cms.untracked.InputTag("qcdMeasurementMethod2Part1", "counterInstances"),
    printMainCounter = cms.untracked.bool(True),
    printSubCounters = cms.untracked.bool(False),
    printAvailableCounters = cms.untracked.bool(True),
)
if len(additionalCounters) > 0:
    process.qcdMeasurementMethod2Part1Counters.counters = cms.untracked.VInputTag([cms.InputTag(c) for c in additionalCounters])

# PickEvent module and the main Path. The picked events are only the
# ones selected by the golden analysis defined above.
process.load("HiggsAnalysis.HeavyChHiggsToTauNu.PickEventsDumper_cfi")
process.qcdMeasurementMethod2Part1Path = cms.Path(
    process.commonSequence * # supposed to be empty, unless "doPat=1" command line argument is given
    process.qcdMeasurementMethod2Part1 *
    process.qcdMeasurementMethod2Part1Counters
    #* process.PickEvents
)

################################################################################
# The signal analysis with different tau ID algorithms
#
# Run the analysis for the different tau ID algorithms at the same job
# as the golden analysis. It is significantly more efficiency to run
# many analyses in a single job compared to many jobs (this avoids
# some of the I/O and grid overhead). The fragment below creates the
# following histogram directories
# qcdMeasurementMethod2Part1TauSelectionShrinkingConeCutBased
# qcdMeasurementMethod2Part1TauSelectionShrinkingConeTaNCBased
# qcdMeasurementMethod2Part1TauSelectionCaloTauCutBased
# qcdMeasurementMethod2Part1TauSelectionHPSTauBased
# qcdMeasurementMethod2Part1TauSelectionCombinedHPSTaNCBased
#
# The corresponding Counter directories have "Counters" postfix, and
# cms.Paths "Path" postfix. The paths are run independently of each
# other. It is important to give the process.commonSequence for the
# function, so that it will be run before the analysis module in the
# Path. Then, in case PAT is run on the fly, the framework runs the
# analysis module after PAT (and runs PAT only once).
if doAllTauIds:
    param.addTauIdAnalyses(process, "qcdMeasurementMethod2Part1", process.qcdMeasurementMethod2Part1, process.commonSequence, additionalCounters)


################################################################################
# The signal analysis with jet energy scale variation
#
# If the flag is true, create two paths for the variation in plus and
# minus, and clone the signal analysis and counter modules to the
# paths. The tau, jet and MET collections to adjust are taken from the
# configuration of the golden analysis. The fragment below creates the
# following histogram directories
# qcdMeasurementMethod2Part1CountersJESPlus05
# qcdMeasurementMethod2Part1CountersJESMinus05
from HiggsAnalysis.HeavyChHiggsToTauNu.JetEnergyScaleVariation import addJESVariationAnalysis
if doJESVariation:
    # In principle here could be more than two JES variation analyses
    JESs = "%02d" % int(JESVariation*100)
    JESe = "%02d" % int(JESEtaVariation*100)
    JESm = "%02d" % int(JESUnclusteredMETVariation*100)
    addJESVariationAnalysis(process, "signalAnalysis", "JESPlus"+JESs+"eta"+JESe+"METPlus"+JESm, process.signalAnalysis, additionalCounters, JESVariation, JESEtaVariation, JESUnclusteredMETVariation)
    addJESVariationAnalysis(process, "signalAnalysis", "JESMinus"+JESs+"eta"+JESe+"METPlus"+JESm, process.signalAnalysis, additionalCounters, -JESVariation, JESEtaVariation, JESUnclusteredMETVariation)
    addJESVariationAnalysis(process, "signalAnalysis", "JESPlus"+JESs+"eta"+JESe+"METMinus"+JESm, process.signalAnalysis, additionalCounters, JESVariation, JESEtaVariation, -JESUnclusteredMETVariation)
    addJESVariationAnalysis(process, "signalAnalysis", "JESMinus"+JESs+"eta"+JESe+"METMinus"+JESm, process.signalAnalysis, additionalCounters, -JESVariation, JESEtaVariation, -JESUnclusteredMETVariation)

# Print tau discriminators from one tau from one event. Note that if
# the path below is commented, the discriminators are not printed.
process.tauDiscriminatorPrint = cms.EDAnalyzer("HPlusTauDiscriminatorPrintAnalyzer",
    src = process.qcdMeasurementMethod2Part1.tauSelection.src
)
#process.tauDiscriminatorPrintPath = cms.Path(
#    process.patSequence *
#    process.tauDiscriminatorPrint
#)


################################################################################

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('output.root'),
    outputCommands = cms.untracked.vstring(
        "keep *_*_*_HChqcdMeasurementMethod2Part1",
        "drop *_*_counterNames_*",
        "drop *_*_counterInstances_*"
#	"drop *",
#	"keep *",
#        "keep edmMergeableCounter_*_*_*"
    )
)

# Uncomment the following line to get also the event output (can be
# useful for debugging purposes)
#process.outpath = cms.EndPath(process.out)

