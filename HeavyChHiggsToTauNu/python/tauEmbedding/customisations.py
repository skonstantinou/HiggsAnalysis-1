import FWCore.ParameterSet.Config as cms

import HiggsAnalysis.HeavyChHiggsToTauNu.HChTools as HChTools
import HiggsAnalysis.HeavyChHiggsToTauNu.HChSignalAnalysisParameters_cff as HChSignalAnalysisParameters

def customiseParamForTauEmbedding(param):
    # Change the triggers to muon
    param.trigger.triggers = ["HLT_Mu9",
                              "HLT_Mu15_v1"]
    param.trigger.hltMetCut = -1 # disable

    # Use PatJets and PFMet directly
    param.changeJetCollection(moduleLabel="selectedPatJets") # these are really AK5PF
    param.changeMetCollection(moduleLabel="pfMet") # no PAT object at the moment

    # Use the muons where the original muon is removed in global muon veto
    param.GlobalMuonVeto.MuonCollectionName.setModuleLabel("selectedPatMuonsEmbeddingMuonCleaned")

    # Use the taus matched to the original muon in tau selections
    postfix = "TauEmbeddingMuonMatched"
    param.setAllTauSelectionSrcSelectedPatTaus()
    param.forEachTauSelection(lambda x: x.src.setModuleLabel(x.src.getModuleLabel()+postfix))

    # Remove TCTau
    i = param.tauSelections.index(param.tauSelectionCaloTauCutBased)
    print "Removing %s from the list of tau selections" % param.tauSelectionNames[i]
    del param.tauSelections[i]
    del param.tauSelectionNames[i]

    # Set the analyzer
    param.TauEmbeddingAnalysis.embeddingMode = True
    param.TauEmbeddingAnalysis.originalMetSrc = cms.untracked.InputTag("pfMet", "", "RECO")
    param.TauEmbeddingAnalysis.originalMuon = cms.untracked.InputTag("tauEmbeddingMuons")
    param.TauEmbeddingAnalysis.embeddingMetSrc = param.MET.src
    

def addMuonSelection(process, postfix="", cut="(isolationR03().emEt+isolationR03().hadEt+isolationR03().sumPt)/pt() < 0.10"):
    body = "muonSelectionAnalysis"+postfix
    counters = []

    allEvents = cms.EDProducer("EventCountProducer")
    setattr(process, body+"AllEvents", allEvents)
    counters.append(body+"AllEvents")

    muons = cms.EDFilter("PATMuonSelector",
        src = cms.InputTag("tauEmbeddingMuons"),
        cut = cms.string(cut)
    )
    setattr(process, body+"Muons", muons)

    muonsFilter = cms.EDFilter("CandViewCountFilter",
        src = cms.InputTag(body+"Muons"),
        minNumber = cms.uint32(1)
    )
    setattr(process, body+"MuonsFilter", muonsFilter)

    selected = cms.EDProducer("EventCountProducer")
    setattr(process, body+"Selected", selected)
    counters.append(body+"Selected")

    seq = cms.Sequence(
        allEvents *
        muons *
        muonsFilter *
        selected
    )
    setattr(process, body+"Sequence", seq)
    
    return (seq, counters, body+"Muons")

def _signalAnalysisSetMuon(module, muons):
    module.tauEmbedding.originalMuon = cms.untracked.InputTag(muons)

def addMuonRelativeIsolation(process, sequence, cut=0.1, prefix="muonSelectionIsolation"):
    return addMuonIsolation(process, sequence, prefix, "(isolationR03().emEt+isolationR03().hadEt+isolationR03().sumPt)/pt() < %f" % cut)

def addMuonIsolation(process, sequence, prefix, isolation):
    selector = prefix+"Selected"
    filter = prefix+"Filter"
    counter = prefix

    # Create modules
    m1 = cms.EDFilter("HPlusCandViewLazyPtrSelector",
        src = cms.InputTag("tauEmbeddingMuons"),
        cut = cms.string(isolation)
    )
    m2 = cms.EDFilter("CandViewCountFilter",
        src = cms.InputTag(selector),
        minNumber = cms.uint32(1)
    )
    m3 = cms.EDProducer("EventCountProducer")

    # Add modules to process
    setattr(process, selector, m1)
    setattr(process, filter, m2)
    setattr(process, counter, m3)

    # Add modules to sequence
    sequence *= (m1 * m2 * m3)

    # Return list of counter names
    return [counter]

def addMuonIsolationAnalyses(process, prefix, prototype, commonSequence, additionalCounters, modify=_signalAnalysisSetMuon, signalAnalysisCounters=True):
    detRelIso = "(isolationR03().emEt+isolationR03().hadEt+isolationR03().sumPt)/pt()"
    #pfRelIso = 
    isolations = [
        ("RelIso05", detRelIso+" < 0.05"),
        ("RelIso10", detRelIso+" < 0.10"),
        ("RelIso15", detRelIso+" < 0.15"),
        ("RelIso20", detRelIso+" < 0.20"),
        ("RelIso25", detRelIso+" < 0.25"),
        ("RelIso50", detRelIso+" < 0.50"),
        ]

    for name, cut in isolations:
        (sequence, counters, muons) = addMuonSelection(process, name, cut)
        cseq = cms.Sequence(commonSequence*sequence)
        setattr(process, prefix+name+"CommonSequence", cseq)

        module = prototype.clone()
        modify(module, muons)

        HChTools.addAnalysis(process, prefix+name, module, cseq, additionalCounters+counters, signalAnalysisCounters)

def addTauAnalyses(process, prefix, prototype, commonSequence, additionalCounters):
    def disableRtau(module):
        return module.clone(rtauCut = -1)

    values = [
        HChSignalAnalysisParameters.tauSelectionHPSLooseTauBased,
        disableRtau(HChSignalAnalysisParameters.tauSelectionHPSLooseTauBased),
        disableRtau(HChSignalAnalysisParameters.tauSelectionHPSMediumTauBased),
        disableRtau(HChSignalAnalysisParameters.tauSelectionHPSTauBased),
        disableRtau(HChSignalAnalysisParameters.tauSelectionShrinkingConeCutBased),
        ]
    names = [
        "TauSelectionHPSLooseTauBased",
        "TauSelectionHPSLooseTauNoRtauBased",
        "TauSelectionHPSMediumTauNoRtauBased",
        "TauSelectionHPSTightTauNoRtauBased",
        "TauSelectionShrinkingConeCutNoRtauBased",
        ]

    HChTools.addAnalysisArray(process, prefix, prototype, HChSignalAnalysisParameters.setTauSelection,
                              values=values, names=names,
                              preSequence=commonSequence, additionalCounters=additionalCounters)
    


def addTauEmbeddingMuonTaus(process):
    seq = cms.Sequence()

    # Remove the embedding muon from the list of muons, use the rest
    # as an input for the global muon veto
    from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import cleanPatMuons
    process.selectedPatMuonsEmbeddingMuonCleaned = cleanPatMuons.clone(
        src = cms.InputTag("selectedPatMuons"),
        checkOverlaps = cms.PSet(
            muons = cms.PSet(
                src                 = cms.InputTag("tauEmbeddingMuons"),
                algorithm           = cms.string("byDeltaR"),
                preselection        = cms.string(""),
                deltaR              = cms.double(0.1),
                checkRecoComponents = cms.bool(False),
                pairCut             = cms.string(""),
                requireNoOverlaps   = cms.bool(True),
            ),
        )
    )
    seq *= process.selectedPatMuonsEmbeddingMuonCleaned

    # Select the taus matching to the original muon
    prototype = cms.EDProducer("HPlusPATTauCandViewDeltaRSelector",
        src = cms.InputTag("dummy"),
        refSrc = cms.InputTag("tauEmbeddingMuons"),
        deltaR = cms.double(0.1),
    )

    for tau in ["selectedPatTausShrinkingConePFTau", "selectedPatTausHpsPFTau", "selectedPatTausHpsTancPFTau"]:
        m = prototype.clone(
            src = tau
        )
        setattr(process, tau+"TauEmbeddingMuonMatched", m)
        seq *= m

    return seq

    