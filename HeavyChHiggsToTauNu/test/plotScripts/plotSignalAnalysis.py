#!/usr/bin/env python

######################################################################
#
# This plot script is for comparing the embedded data to embedding MC
# within the signal analysis. The corresponding python job
# configuration is signalAnalysis_cfg.py with "doPat=1
# tauEmbeddingInput=1" command line arguments.
#
# Authors: Ritva Kinnunen, Matti Kortelainen
#
######################################################################

import ROOT
ROOT.gROOT.SetBatch(True)

import HiggsAnalysis.HeavyChHiggsToTauNu.tools.dataset as dataset
import HiggsAnalysis.HeavyChHiggsToTauNu.tools.histograms as histograms
import HiggsAnalysis.HeavyChHiggsToTauNu.tools.plots as plots
import HiggsAnalysis.HeavyChHiggsToTauNu.tools.counter as counter
import HiggsAnalysis.HeavyChHiggsToTauNu.tools.tdrstyle as tdrstyle
import HiggsAnalysis.HeavyChHiggsToTauNu.tools.styles as styles

# Configuration
#analysis = "signalAnalysis"
analysis = "signalAnalysisTauSelectionHPSTightTauBased"
#analysis = "signalAnalysisTauSelectionHPSMediumTauBased"
#analysis = "signalAnalysisTauSelectionShrinkingConeTaNCBased"
counters = analysis+"Counters/weighted"

# main function
def main():
    # Read the datasets
    datasets = dataset.getDatasetsFromMulticrabCfg(counters=counters)
    datasets.remove(["WJets_TuneD6T_Winter10", "TTJets_TuneD6T_Winter10",
                     "TTToHplusBWB_M90_Winter10",
                     "TTToHplusBWB_M100_Winter10",
#                     "TTToHplusBWB_M120_Winter10",
                     "TTToHplusBWB_M140_Winter10",
                     "TTToHplusBWB_M160_Winter10",
                     ])
    datasets.loadLuminosities()
    plots.mergeRenameReorderForDataMC(datasets)

    #datasets.remove(["Data"])

    # Apply TDR style
    style = tdrstyle.TDRStyle()


    # Wrapper to decrease typing and have the common options
    def createPlot(*args):
        kwargs = {}
#        kwargs["saveFormats"] = [".png"]
        return plots.DataMCPlot(datasets, *args, **kwargs)
        #return plots.MCPlot(datasets, *args, normalizeToLumi=36, **kwargs)

    # Create the plot objects and pass them to the formatting
    # functions to be formatted, drawn and saved to files
    tauPt(createPlot(analysis+"/TauEmbeddingAnalysis_afterTauId_selectedTauPt"), ratio=True)
    tauEta(createPlot(analysis+"/TauEmbeddingAnalysis_afterTauId_selectedTauEta"), ratio=True)
    tauPhi(createPlot(analysis+"/TauEmbeddingAnalysis_afterTauId_selectedTauPhi"), ratio=True)
    leadingTrack(createPlot(analysis+"/TauEmbeddingAnalysis_afterTauId_leadPFChargedHadrPt"), ratio=True)
    rtau(createPlot(analysis+"/TauID_RtauCut"), "TauIdRtau_afterTauId")

    rtau(createPlot(analysis+"/genRtau1ProngHp"), "genRtau1ProngHp")
    rtau(createPlot(analysis+"/genRtau1ProngW"), "genRtau1ProngW")
   
    tauCandPt(createPlot(analysis+"/TauSelection_all_tau_candidates_pt"), step="begin")
    tauCandEta(createPlot(analysis+"/TauSelection_all_tau_candidates_eta"), step="begin" )
    tauCandPhi(createPlot(analysis+"/TauSelection_all_tau_candidates_phi"), step="begin" )
    
   
    met(createPlot(analysis+"/TauEmbeddingAnalysis_afterTauId_embeddingMet"), ratio=True)
    met(createPlot(analysis+"/TauEmbeddingAnalysis_begin_embeddingMet"), ratio=True)
    met2(plots.DataMCPlot(datasets, analysis+"/met"), "met", rebin=5)

    deltaPhi(createPlot(analysis+"/TauEmbeddingAnalysis_afterTauId_DeltaPhi"))
    deltaPhi2(createPlot(analysis+"/deltaPhiJetMet"), "DeltaPhiJetMet")
    deltaPhi2(plots.DataMCPlot(datasets, analysis+"/deltaPhi"), "DeltaPhiTauMet")

    transverseMass(createPlot(analysis+"/TauEmbeddingAnalysis_afterTauId_TransverseMass"))
    transverseMass2(createPlot(analysis+"/transverseMassBeforeVeto"), "transverseMassBeforeVeto")
    transverseMass2(createPlot(analysis+"/transverseMassAfterVeto"), "transverseMassAfterVeto")

    topMass(plots.DataMCPlot(datasets, analysis+"/topMass"), "topMass")    

    jetPt(createPlot(analysis+"/jet_pt"), "jetPt")
    jetEta(createPlot(analysis+"/jet_eta"), "jetEta")
    jetPhi(createPlot(analysis+"/jet_phi"), "jetPhi")
    numberOfJets(createPlot(analysis+"/NumberOfSelectedJets"), "NumberOfJets")

    jetPt(createPlot(analysis+"/bjet_pt"), "bjetPt", rebin=10)
    jetEta(createPlot(analysis+"/bjet_eta"), "bjetEta", rebin=10)
    numberOfJets(createPlot(analysis+"/NumberOfBtaggedJets"), "NumberOfBJets")
    
    jetPt(createPlot(analysis+"/GlobalElectronPt"), "electronPt", ratio=False)
    jetEta(createPlot(analysis+"/GlobalElectronEta"), "electronEta", ratio=False)
    
    jetPt(createPlot(analysis+"/GlobalMuonPt"), "muonPt", ratio=False)
    jetEta(createPlot(analysis+"/GlobalMuonEta"), "muonEta", ratio=False)
    
    jetPt(createPlot(analysis+"/MaxForwJetEt"), "maxForwJetPt")

    etSumRatio(createPlot(analysis+"/EtSumRatio"), "etSumRatio")
    
    genComparison(datasets)

    eventCounter = counter.EventCounter(datasets)
    #eventCounter.normalizeMCByLuminosity()
    eventCounter.normalizeMCToLuminosity(36)
    print "============================================================"
    print "Main counter (MC normalized by collision data luminosity)"
    print eventCounter.getMainCounterTable().format()

    
def genComparison(datasets):
    signal = "TTToHplusBWB_M120"
    background = "TTJets"

    rtauGen(plots.ComparisonPlot(datasets.getDataset(signal).getDatasetRootHisto(analysis+"/genRtau1ProngHp"),
                                 datasets.getDataset(background).getDatasetRootHisto(analysis+"/genRtau1ProngW")),
            "genRtau1Prong_Hp_vs_TT")

def scaleMC(histo, scale):
    if histo.isMC():
        th1 = histo.getRootHisto()
        th1.Scale(scale)

def scaleMCHistos(h, scale):
    h.histoMgr.forEachHisto(lambda histo: scaleMC(histo, scale))

def scaleMCfromWmunu(h):
    # Data/MC scale factor from AN 2011/053
    scaleMCHistos(h, 0.9509)


# Helper function to flip the last two parts of the histogram name
# e.g. ..._afterTauId_DeltaPhi -> DeltaPhi_afterTauId
def flipName(name):
    tmp = name.split("_")
    return tmp[-1] + "_" + tmp[-2]

# Common formatting
def common(h, xlabel, ylabel):
    h.frame.GetXaxis().SetTitle(xlabel)
    h.frame.GetYaxis().SetTitle(ylabel)
    h.draw()
    histograms.addCmsPreliminaryText()
    histograms.addEnergyText()
    h.addLuminosityText()
    h.save()

# Functions below are for plot-specific formattings. They all take the
# plot object as an argument, then apply some formatting to it, draw
# it and finally save it to files.


def tauCandPt(h, step="", rebin=1):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    ylabel = "Events /%.0f GeV/c" % h.binWidth()   
    xlabel = "p_{T}^{#tau candidate} (GeV/c)"
    opts = {"ymaxfactor": 2}
    
    h.stackMCHistograms()
    h.addMCUncertainty()

    if h.normalizeToOne:
        ylabel = "A.u."
        opts["yminfactor"] = 1e-5
    else:
        opts["ymin"] = 0.001
           

    name = "tauCandidatePt_%s_log" % step
    h.createFrameFraction(name, opts=opts)
    #h.createFrame(name, opts=opts)
    h.frame.GetXaxis().SetTitle(xlabel)
    h.frame.GetYaxis().SetTitle(ylabel)
    h.setLegend(histograms.createLegend())
    ROOT.gPad.SetLogy(True)
    h.draw()
    histograms.addCmsPreliminaryText()
    histograms.addEnergyText()
    #h.addLuminosityText()
    h.save()
    
def tauCandEta(h, step="", rebin=1):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "#eta^{#tau candidate}"
    ylabel = "Events / %.1f" % h.binWidth()
    opts = {"ymaxfactor": 2}
    
    h.stackMCHistograms()
    h.addMCUncertainty()

    if h.normalizeToOne:
        ylabel = "A.u."
        opts["yminfactor"] = 1e-5
    else:
        opts["ymin"] = 0.001
           

    name = "tauCandidateEta_%s_log" % step
    h.createFrameFraction(name, opts=opts)
    #h.createFrame(name, opts=opts)
    h.frame.GetXaxis().SetTitle(xlabel)
    h.frame.GetYaxis().SetTitle(ylabel)
    h.setLegend(histograms.createLegend(0.5, 0.1, 0.7, 0.4))
    ROOT.gPad.SetLogy(True)
    h.draw()
    histograms.addCmsPreliminaryText()
    histograms.addEnergyText()
    #h.addLuminosityText()
    h.save()

def tauCandPhi(h, step="", rebin=1):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "#phi^{#tau candidate}"
    ylabel = "Events / %.1f" % h.binWidth()
    opts = {"ymaxfactor": 2}
    
    h.stackMCHistograms()
    h.addMCUncertainty()

    if h.normalizeToOne:
        ylabel = "A.u."
        opts["yminfactor"] = 1e-5
    else:
        opts["ymin"] = 0.1
           

    name = "tauCandidatePhi_%s_log" % step
    h.createFrameFraction(name, opts=opts)
    #h.createFrame(name, opts=opts)
    h.frame.GetXaxis().SetTitle(xlabel)
    h.frame.GetYaxis().SetTitle(ylabel)
    h.setLegend(histograms.createLegend(0.5, 0.1, 0.7, 0.4))
    ROOT.gPad.SetLogy(True)
    h.draw()
    histograms.addCmsPreliminaryText()
    histograms.addEnergyText()
    #h.addLuminosityText()
    h.save()
    


def tauPt(h, rebin=5, ratio=True):
#    name = flipName(h.getRootHistoPath())

    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "p_{T}^{#tau jet} (GeV/c)"
    ylabel = "Events / %.0f GeV/c" % h.binWidth()

    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.001, "xmin": 20, "ymaxfactor": 2}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
    name = "selectedTauPt"
#    name = name+"_log"
    #h.createFrameFraction(name, opts=opts)
#    h.createFrame(name, opts=opts)
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend())
    common(h, xlabel, ylabel)
    
def tauEta(h, rebin=5, ratio=True):
#    name = flipName(h.getRootHistoPath())

    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "#eta^{#tau jet}"
    ylabel = "Events"

    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.001, "ymaxfactor": 2}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
    name = "selectedTauEta"
#    name = name+"_log"
    #h.createFrameFraction(name, opts=opts)
#    h.createFrame(name, opts=opts)
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend(0.7, 0.3, 0.9, 0.6))
    common(h, xlabel, ylabel)
    
def tauPhi(h, rebin=5, ratio=True):
    name = flipName(h.getRootHistoPath())

    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "#phi^{#tau jet}"
    ylabel = "Events"

    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.001, "ymaxfactor": 2}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
    name = "selectedTauPhi"
#    name = name+"_log"
    #h.createFrameFraction(name, opts=opts)
#    h.createFrame(name, opts=opts)
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend(0.2, 0.2, 0.4, 0.5))
    common(h, xlabel, ylabel)
    
def leadingTrack(h, rebin=5, ratio=True):
    name = flipName(h.getRootHistoPath())

    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "p_{T}^{leading track} (GeV/c)"
    ylabel = "Events / %.0f GeV/c" % h.binWidth()

    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.01, "xmin": 20, "ymaxfactor": 2}
    name = "leadingTrackPt"
#    name = name+"_log"
    #h.createFrameFraction(name, opts=opts)
    h.createFrame(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend())
    common(h, xlabel, ylabel)

def rtau(h, name, rebin=1, ratio=True):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "R_{#tau}"
    ylabel = "Events / %.2f" % h.binWidth()

    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.001, "xmax": 1.1, "ymaxfactor": 10}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
    name = name+"_log"
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
#    h.createFrame(name, opts=opts)
    #h.createFrameFraction(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend(0.2, 0.6, 0.4, 0.9))
    common(h, xlabel, ylabel)

def rtauGen(h, name, rebin=2, ratio=False):
    h.setDefaultStyles()
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "R_{#tau}"
    ylabel = "Events / %.2f" % h.binWidth()

    kwargs = {"opts": {"ymin": 10, "xmax": 1.1, "ymaxfactor": 1.1}}
    if ratio:
        kwargs["opts2"] = {"ymin": 0.5, "ymax": 1.5}
    name = name+"_log"

    h.createFrame(name, createRatio=ratio, **kwargs)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend(0.2, 0.75, 0.4, 0.9))
    common(h, xlabel, ylabel)

def met(h, rebin=5, ratio=True):
    name = flipName(h.getRootHistoPath())

    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "MET (GeV)"
    if "embedding" in name:
        xlabel = "Embedded "+xlabel
    elif "original" in name:
        xlabel = "Original "+xlabel
    ylabel = "Events / %.0f GeV" % h.binWidth()

    scaleMCfromWmunu(h)
    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.001, "ymaxfactor": 2}
    opts2 = {"ymin": 0.5, "ymax": 1.5}

    name = name+"_log"
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend())
    common(h, xlabel, ylabel)
    
def met2(h, name, rebin=10, ratio=True):
#    name = h.getRootHistoPath()
    name = "met"

    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
#    xlabel = "MET (GeV)"
#    if "embedding" in name:
#        xlabel = "Embedded "+xlabel
#    elif "original" in name:
#        xlabel = "Original "+xlabel
    ylabel = "Events / %.0f GeV" % h.binWidth()
    xlabel = "MET (GeV)"
    
#    scaleMCfromWmunu(h)
    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.001, "ymaxfactor": 2}
    opts2 = {"ymin": 0.5, "ymax": 1.5}

    name = name+"_log"
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend())
    common(h, xlabel, ylabel)

    
def deltaPhi(h, rebin=2, ratio=False):
    name = flipName(h.getRootHistoPath())

    particle = "#tau jet"
    if "Original" in name:
        particle = "#mu"

    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "#Delta#phi(%s, MET) (rad)" % particle
    ylabel = "Events / %.2f rad" % h.binWidth()
    
    scaleMCfromWmunu(h)    
    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.0, "ymaxfactor": 1.3}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
    
#    if ratio:
#        h.createFrameFraction(name, opts=opts, opts2=opts2)
#    else:
#        h.createFrame(name, opts=opts)
    #h.createFrameFraction(name)
    h.createFrame(name)
    h.setLegend(histograms.createLegend(0.2, 0.6, 0.4, 0.9))
    common(h, xlabel, ylabel)
    
def deltaPhi2(h, name, rebin=1):
#    name = flipName(h.getRootHistoPath())
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))

    particle = "#tau"
    if "Jet" in name:
        particle = "jet"
    xlabel = "#Delta#phi(%s, MET) (deg)" % particle
    ylabel = "Events / %.2f deg" % h.binWidth()
    
    scaleMCfromWmunu(h)      
    h.stackMCHistograms()
    h.addMCUncertainty()
#    name = "deltaPhiMetJet"
    #h.createFrameFraction(name)
    opts = {"ymin": 0.005, "ymaxfactor": 1.3}
    h.createFrame(name, opts=opts) 
    h.setLegend(histograms.createLegend(0.3, 0.6, 0.5, 0.9))
    h.getPad().SetLogy(True)
    common(h, xlabel, ylabel)
    
def transverseMass(h, rebin=1):
    name = flipName(h.getRootHistoPath())

    particle = ""
    if "Original" in name:
        particle = "#mu"
        name = name.replace("TransverseMass", "MtMuon")
    else:
        particle = "#tau jet"
        name = name.replace("TransverseMass", "MtTau")

    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    xlabel = "m_{T}(%s, MET) (GeV/c^{2})" % particle
    ylabel = "Events / %.2f GeV/c^{2}" % h.binWidth()
    
    scaleMCfromWmunu(h)     
    h.stackMCHistograms()
    h.addMCUncertainty()
    opts = {"ymin": 0.01, "xmax": 200, "ymaxfactor": 1.3}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
#    opts = {"xmax": 200}
    #h.createFrameFraction(name, opts=opts)
    h.createFrame(name, opts=opts)
    h.setLegend(histograms.createLegend())
    h.getPad().SetLogy(True)
    common(h, xlabel, ylabel)
    
def transverseMass2(h, name="transverseMass", rebin=2, log=True):
#    name = h.getRootHistoPath()
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    particle = "allCuts"
    if "Before" in name:
        particle = "beforeVeto"
        name = name.replace("TransverseMass", "TransverseMassBeforeVeto")
    if "After" in name:
        particle = "afterVeto"
        name = name.replace("TransverseMass", "TransverseMassAfterVeto")

    if log:
        name += "_log"

    xlabel = "m_{T}(#tau jet, MET) (GeV/c^{2})" 
    ylabel = "Events / %.2f GeV/c^{2}" % h.binWidth()
    

    scaleMCfromWmunu(h)    
    h.stackMCHistograms()
    h.addMCUncertainty()
    opts = {"xmax": 200}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
    if log:
        opts["ymin"] = 0.0001
        opts["ymaxfacror"] = 1.3

#    opts = {"xmax": 200}
    #h.createFrameFraction(name, opts=opts)
    h.createFrame(name, opts=opts)
    if log:
        h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend())
    common(h, xlabel, ylabel)

    
def topMass(h, name, rebin=5):
#    name = flipName(h.getRootHistoPath())
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    
    xlabel = "m(jjb) (GeV/c^{2})" 
    ylabel = "Events / %.2f GeV/c^{2}" % h.binWidth()
    
    scaleMCfromWmunu(h)      
    h.stackMCHistograms()
    h.addMCUncertainty()
#    name = "deltaPhiMetJet"
    #h.createFrameFraction(name)    
    opts = {"ymin": 0.0, "ymaxfactor": 1.1}
    h.createFrame(name, opts=opts) 
    h.setLegend(histograms.createLegend(0.3, 0.6, 0.5, 0.9))
#    h.getPad().SetLogy(True)
    common(h, xlabel, ylabel)

    
def jetPt(h, name, rebin=5, ratio=True):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    particle = "jet"
    if "bjet" in name:
        particle = "bjet"
    if "electron" in name:
        particle = "electron"
    if "muon" in name:
        particle = "muon"
#        name = name.replace("jetPt", "bjetPt")

    xlabel = "p_{T}^{%s} (GeV/c)" % particle
    ylabel = "Events /%.0f GeV/c" % h.binWidth()
    
    scaleMCfromWmunu(h)  
    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.001, "ymaxfactor": 5}
    opts2 = {"ymin": 0.05, "ymax": 1.5}
    name = name+"_log"
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
#    h.createFrame(name, opts=opts)
    #h.createFrameFraction(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend())
    common(h, xlabel, ylabel)

    
def jetEta(h, name, rebin=5, ratio=True):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    particle = "jet"
    if "bjet" in name:
        particle = "bjet"
    if "electron" in name:
        particle = "electron"
    if "muon" in name:
        particle = "muon"
    xlabel = "#eta^{%s}" % particle
    ylabel = "Events / %.2f" % h.binWidth()
    
    scaleMCfromWmunu(h)  
    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.001, "ymaxfactor": 5}
    opts2 = {"ymin": 0.05, "ymax": 1.5}
    name = name+"_log"
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend(0.3, 0.2, 0.5, 0.5))
    common(h, xlabel, ylabel)

def jetPhi(h, name, rebin=5, ratio=True):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    particle = "jet"
    if "bjet" in name:
        particle = "bjet"
    xlabel = "#phi^{%s}" % particle
    ylabel = "Events / %.2f" % h.binWidth()
    
    scaleMCfromWmunu(h)  
    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.01, "ymaxfactor": 1.2}
    opts2 = {"ymin": 0.01, "ymax": 2.5}
    name = name+"_log"
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend(0.2, 0.1, 0.4, 0.4))
    common(h, xlabel, ylabel)

def numberOfJets(h, name, rebin=1, ratio=False):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
    particle = "jet"
    if "Btagged" in name:
        particle = "bjet"
    xlabel = "Number of %ss" % particle
    ylabel = "Events / %.2f" % h.binWidth()

    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.0, "xmax": 10, "ymaxfactor": 1.2}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
#    name = name+"_log"
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
#    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend())
    common(h, xlabel, ylabel)

def etSumRatio(h, name, rebin=1, ratio=False):
    h.histoMgr.forEachHisto(lambda h: h.getRootHisto().Rebin(rebin))
#    particle = "jet"
#    if "bjet" in name:
#        particle = "bjet"
#        name = name.replace("jetPt", "bjetPt")

    xlabel = "#Sigma E_{T}^{Forward} / #Sigma E_{T}^{Central}"
    ylabel = "Events /%.0f GeV/c" % h.binWidth()
    
    scaleMCfromWmunu(h)  
    h.stackMCHistograms()
    h.addMCUncertainty()

    opts = {"ymin": 0.0001, "xmax":1.2, "ymaxfactor": 5}
    opts2 = {"ymin": 0.5, "ymax": 1.5}
    name = name+"_log"
    if ratio:
        h.createFrameFraction(name, opts=opts, opts2=opts2)
    else:
        h.createFrame(name, opts=opts)
#    h.createFrame(name, opts=opts)
    #h.createFrameFraction(name, opts=opts)
    h.getPad().SetLogy(True)
    h.setLegend(histograms.createLegend())
    common(h, xlabel, ylabel)


    
# Call the main function if the script is executed (i.e. not imported)
if __name__ == "__main__":
    main()