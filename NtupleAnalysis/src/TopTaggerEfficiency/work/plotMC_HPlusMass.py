#!/usr/bin/env python
'''
Description:

Usage:
./plotMC_HPlusMass.py -m <pseudo_mcrab> [opts]

Examples:
./plotMC_HPlusMass.py -m <peudo_mcrab> -o "" --url --nomaliseToOne
./plotMC_HPlusMass.py -m <peudo_mcrab> --folder topologySelection_ --url --normaliseToOne
./plotMC_HPlusMass.py -m <peudo_mcrab> --normaliseToOne --url
./plotMC_HPlusMass.py -m <peudo_mcrab> --normaliseToOne --url --signalMass 500
./plotMC_HPlusMass.py -m <peudo_mcrab> --normaliseToOne --url --signalMass 500

Last Used:
./plotMC_HPlusMass.py -m /uscms_data/d3/skonstan/workspace/pseudo-multicrab/TopTaggerEfficiency/TopTaggerEfficiency_15June18_BDT0p40_Masscut300_NewTop_BugFix/ --folder topbdtSelection_ --url -v
'''

#================================================================================================ 
# Imports
#================================================================================================ 
import sys
import math
import copy
import os
import getpass
from optparse import OptionParser
import HiggsAnalysis.NtupleAnalysis.tools.aux as aux

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import HiggsAnalysis.NtupleAnalysis.tools.dataset as dataset
import HiggsAnalysis.NtupleAnalysis.tools.histograms as histograms
import HiggsAnalysis.NtupleAnalysis.tools.counter as counter
import HiggsAnalysis.NtupleAnalysis.tools.tdrstyle as tdrstyle
import HiggsAnalysis.NtupleAnalysis.tools.styles as styles
import HiggsAnalysis.NtupleAnalysis.tools.plots as plots
import HiggsAnalysis.NtupleAnalysis.tools.crosssection as xsect
import HiggsAnalysis.NtupleAnalysis.tools.multicrabConsistencyCheck as consistencyCheck

#================================================================================================ 
# Function Definition
#================================================================================================ 
def Print(msg, printHeader=False):
    fName = __file__.split("/")[-1]
    if printHeader==True:
        print "=== ", fName
        print "\t", msg
    else:
        print "\t", msg
    return

def Verbose(msg, printHeader=True, verbose=False):
    if not opts.verbose:
        return
    aux.Print(msg, printHeader)
    return

def GetLumi(datasetsMgr):
    Verbose("Determininig Integrated Luminosity")
    
    lumi = 0.0
    for d in datasetsMgr.getAllDatasets():
        if d.isMC():
            continue
        else:
            lumi += d.getLuminosity()
    Verbose("Luminosity = %s (pb)" % (lumi), True)
    return lumi


def GetListOfEwkDatasets():
    Verbose("Getting list of EWK datasets")
    return ["TT", "WJetsToQQ_HT_600ToInf", "DYJetsToQQHT", "SingleTop", "TTWJetsToQQ", "TTZToQQ", "Diboson", "TTTT"]


def GetDatasetsFromDir(opts):
    Verbose("Getting datasets")
    
    if (not opts.includeOnlyTasks and not opts.excludeTasks):
        datasets = dataset.getDatasetsFromMulticrabDirs([opts.mcrab],
                                                        dataEra=opts.dataEra,
                                                        searchMode=opts.searchMode, 
                                                        analysisName=opts.analysisName,
                                                        optimizationMode=opts.optMode)
    elif (opts.includeOnlyTasks):
        datasets = dataset.getDatasetsFromMulticrabDirs([opts.mcrab],
                                                        dataEra=opts.dataEra,
                                                        searchMode=opts.searchMode,
                                                        analysisName=opts.analysisName,
                                                        includeOnlyTasks=opts.includeOnlyTasks,
                                                        optimizationMode=opts.optMode)
    elif (opts.excludeTasks):
        datasets = dataset.getDatasetsFromMulticrabDirs([opts.mcrab],
                                                        dataEra=opts.dataEra,
                                                        searchMode=opts.searchMode,
                                                        analysisName=opts.analysisName,
                                                        excludeTasks=opts.excludeTasks,
                                                        optimizationMode=opts.optMode)
    else:
        raise Exception("This should never be reached")
    return datasets
    

def main(opts, signalMass):

    optModes = ["OptChiSqrCutValue100"]                                                                                                                             

    if opts.optMode != None:
        optModes = [opts.optMode]

    # For-loop: All optimisation modes
    for opt in optModes:
        opts.optMode = opt

        # Setup & configure the dataset manager 
        datasetsMgr = GetDatasetsFromDir(opts)
        datasetsMgr.updateNAllEventsToPUWeighted()
        datasetsMgr.loadLuminosities() # from lumi.json

        datasetsMgr_signal = GetDatasetsFromDir(opts)
        datasetsMgr_signal.updateNAllEventsToPUWeighted()
        datasetsMgr_signal.loadLuminosities() # from lumi.json

        if opts.verbose:
            datasetsMgr.PrintCrossSections()
            datasetsMgr.PrintLuminosities()

        # Set/Overwrite cross-sections
        for d in datasetsMgr.getAllDatasets():
            if "ChargedHiggs" in d.getName():
                datasetsMgr.getDataset(d.getName()).setCrossSection(1.0)
                datasetsMgr_signal.getDataset(d.getName()).setCrossSection(1.0)
        # Determine integrated Lumi before removing data
#        intLumi = datasetsMgr.getDataset("Data").getLuminosity()
        intLumi = 35920

        # Remove datasets
        if 1:
            datasetsMgr.remove(filter(lambda name: "Data" in name, datasetsMgr.getAllDatasetNames()))
            #datasetsMgr.remove(filter(lambda name: "QCD_b" in name, datasetsMgr.getAllDatasetNames()))
            #datasetsMgr.remove(filter(lambda name: "QCD_HT" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr.remove(filter(lambda name: "SingleTop" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr.remove(filter(lambda name: "DYJetsToQQHT" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr.remove(filter(lambda name: "TTZToQQ" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr.remove(filter(lambda name: "TTWJetsToQQ" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr.remove(filter(lambda name: "WJetsToQQ" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr.remove(filter(lambda name: "Diboson" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr.remove(filter(lambda name: "TTTT" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr.remove(filter(lambda name: "FakeBMeasurementTrijetMass" in name, datasetsMgr.getAllDatasetNames()))
            #datasetsMgr.remove(filter(lambda name: "M_" in name and "M_" + str(opts.signalMass) not in name, datasetsMgr.getAllDatasetNames()))

            datasetsMgr_signal.remove(filter(lambda name: "Data" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "QCD_b" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "QCD_HT" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "SingleTop" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "DYJetsToQQHT" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "TTZToQQ" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "TTWJetsToQQ" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "WJetsToQQ" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "Diboson" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "TTTT" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "TT" in name, datasetsMgr.getAllDatasetNames()))
            datasetsMgr_signal.remove(filter(lambda name: "FakeBMeasurementTrijetMass" in name, datasetsMgr.getAllDatasetNames()))

        
        if opts.noQCD:
            datasetsMgr.remove(filter(lambda name: "QCD_b" in name, datasetsMgr.getAllDatasetNames()))  
            datasetsMgr.remove(filter(lambda name: "QCD_HT" in name, datasetsMgr.getAllDatasetNames()))

        # Merge histograms (see NtupleAnalysis/python/tools/plots.py) 
        plots.mergeRenameReorderForDataMC(datasetsMgr) 

        # Merge EWK samples
        if opts.mergeEWK:
            datasetsMgr.merge("EWK", GetListOfEwkDatasets())
            plots._plotStyles["EWK"] = styles.getAltEWKStyle()

        # Re-order datasets
        datasetOrder = []
        for d in datasetsMgr.getAllDatasets():
            if "M_" in d.getName():
                if d not in signalMass:
                    continue
            datasetOrder.append(d.getName())
            #newOrder = ["TT", "QCD"]
            #newOrder = ["TT", "QCD"]
        for m in signalMass:
            #newOrder.insert(0, m)
            datasetOrder.insert(0, m)
            #datasetsMgr.selectAndReorder(newOrder)
        datasetsMgr.selectAndReorder(datasetOrder)
        datasetsMgr_signal.selectAndReorder(datasetOrder)
        # Print dataset information
        datasetsMgr.PrintInfo()

        # Apply TDR style
        style = tdrstyle.TDRStyle()
        style.setOptStat(True)
        style.setGridX(False)
        style.setGridY(False)

        # Do the topSelection histos
        folder      = opts.folder 
        histoPaths1 = ["H2"]
        if folder != "":
            histoList  = datasetsMgr.getDataset(datasetOrder[0]).getDirectoryContent(folder)
            # hList0     = [x for x in histoList if "TrijetMass" in x]
            # hList1     = [x for x in histoList if "TetrajetMass" in x]
            # hList2     = [x for x in histoList if "TetrajetBJetPt" in x]
            # histoPaths1 = [os.path.join(folder, h) for h in hList0+hList1+hList2]
            histoPaths1 = [os.path.join(folder, h) for h in histoList]
        
        folder     = ""
        histoList  = datasetsMgr.getDataset(datasetOrder[0]).getDirectoryContent(folder)
        hList0     = [x for x in histoList if "TrijetMass" in x]
        hList1     = [x for x in histoList if "TetrajetMass" in x]
        hList2     = [x for x in histoList if "TetrajetBjetPt" in x]
        histoPaths2 = [os.path.join(folder, h) for h in hList0+hList1+hList2]

        histoPaths = histoPaths1 + histoPaths2
        for h in histoPaths:
            if "vs" in h.lower(): # Skip TH2D
                continue
            '''
            if "true" in h.lower():
                PlotMC(datasetsMgr_signal, h, intLumi)
            elif "match" in h.lower():
                PlotMC(datasetsMgr_signal, h, intLumi)
            '''
                
            #if "phi" not in h.lower():
            #    continue
            '''
            if "order" in h.lower():
                PlotMC(datasetsMgr, h, intLumi)

            if "BQuarkFromH" in h:
                PlotMC(datasetsMgr, h, intLumi)

            if "within" in h:
                PlotMC(datasetsMgr, h, intLumi)
            '''
            #PlotMC(datasetsMgr, h, intLumi)
            if "ldginptb" in h.lower():
                PlotMC(datasetsMgr, h, intLumi)

    return

def getHistos(datasetsMgr, histoName):

    h1 = datasetsMgr.getDataset("Data").getDatasetRootHisto(histoName)
    h1.setName("Data")

    h2 = datasetsMgr.getDataset("EWK").getDatasetRootHisto(histoName)
    h2.setName("EWK")
    return [h1, h2]


def SavePlot(plot, plotName, saveDir, saveFormats = [".C", ".png", ".pdf"]):
    Verbose("Saving the plot in %s formats: %s" % (len(saveFormats), ", ".join(saveFormats) ) )

     # Check that path exists
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    # Create the name under which plot will be saved
    saveName = os.path.join(saveDir, plotName.replace("/", "_"))
    saveName = saveName.replace("(", "_")
    saveName = saveName.replace(")", "")
    saveName = saveName.replace(" ", "")

    # For-loop: All save formats
    for i, ext in enumerate(saveFormats):
        saveNameURL = saveName + ext
        saveNameURL = aux.convertToURL(saveNameURL, opts.url)
        Verbose(saveNameURL, i==0)
        plot.saveAs(saveName, formats=saveFormats)
    return





#PlotMC(datasetsMgr, h, intLumi)
def PlotMC(datasetsMgr, histo, intLumi):

    kwargs = {}
    if opts.normaliseToOne:
        p = plots.MCPlot(datasetsMgr, histo, normalizeToOne=True, saveFormats=[], **kwargs)
    else:
        p = plots.MCPlot(datasetsMgr, histo, normalizeToLumi=intLumi, saveFormats=[], **kwargs)

    # Draw the histograms
    _cutBox = None
    _rebinX = 1
    _format = "%0.0f"
    _xlabel = None

    _opts   = {"ymin": 1e-3, "ymaxfactor": 1.0}
    #_opts   = {"ymin": 1e-3, "ymax": 60}


    if "pt" in histo.lower():
        _rebinX = 2
        _units  = "GeV/c"
        _format = "%0.0f " + _units
        _xlabel = "p_{T} (%s)" % _units
        _cutBox = {"cutValue": 173.21, "fillColor": 16, "box": False, "line": False, "greaterThan": True}
        #_opts["xmax"] = 505 #1005

    if "ht" in histo.lower():
        _rebinX = 2
        _units  = "GeV/c"
        _format = "%0.0f " + _units
        _xlabel = "H_{T} (%s)" % _units
        _opts["xmax"] = 2000
        #_cutBox = {"cutValue": 173.21, "fillColor": 16, "box": False, "line": False, "greaterThan": True}
        #_opts["xmax"] = 505 #1005
        
    if "eta" in histo.lower():
        _units  = ""
        _format = "%0.1f " + _units
        _xlabel = "#eta %s" % _units
        _cutBox = {"cutValue": 173.21, "fillColor": 16, "box": False, "line": False, "greaterThan": True}
        _opts["xmax"] = 2.5
        _opts["xmin"] = -2.5

    if "trijetmass" in histo.lower():
        _rebinX = 2
        _units  = "GeV/c^{2}"
        _format = "%0.0f " + _units
        _xlabel = "m_{jjb} (%s)" % _units
        _cutBox = {"cutValue": 173.21, "fillColor": 16, "box": False, "line": True, "greaterThan": True}
        _opts["xmax"] = 505 #1005
        if "ldg" in histo.lower():
            _xlabel = "m_{jjb}^{ldg} (%s)" % _units
    elif "tetrajetmass" in histo.lower():
        _rebinX = 10 #5 #10 #4
        _units  = "GeV/c^{2}"
        _format = "%0.0f " + _units
        _xlabel = "m_{jjbb} (%s)" % (_units)
        _format = "%0.0f " + _units
        _opts["xmax"] = 2500 #3500.0

    elif "tetrajetpt" in histo.lower():
        _rebinX = 2 #5 #10 #4
        _units  = "GeV/c"
        _format = "%0.0f " + _units
        _xlabel = "p_{T,jjbb} (%s)" % (_units)
        _format = "%0.0f " + _units
        _opts["xmax"] = 1000 #3500.0

    elif "dijetmass" in histo.lower():
        _rebinX = 2 #5 #10 #4
        _units  = "GeV/c^{2}"
        _format = "%0.0f " + _units
        _xlabel = "m_{jj} (%s)" % (_units)
        _format = "%0.0f " + _units
        _opts["xmax"] = 800 #3500.0
        _cutBox = {"cutValue": 80.4, "fillColor": 16, "box": False, "line": True, "greaterThan": True}
        _opts["xmax"] = 300
        if "ldg" in histo.lower():
            _xlabel = "m_{jj}^{ldg} (%s)" % (_units)
    elif "tetrajetbjetpt" in histo.lower():
        _rebinX = 2
        _units  = "GeV/c"
        _format = "%0.0f " + _units
        _xlabel = "p_{T,bjet}  (%s)" % (_units)
        _format = "%0.0f " + _units
        _opts["xmax"] = 800

    elif "ldgtrijetpt" in histo.lower():
        _rebinX = 2
#        logY    = False
        _units  = "GeV/c"
        _format = "%0.0f " + _units
        _xlabel = "p_{T,jjb}^{ldg}  (%s)" % (_units)
        _format = "%0.0f " + _units
        _opts["xmax"] = 800

    elif "ldgtrijetdijetpt" in histo.lower():
        _rebinX = 2
#        logY    = False
        _units  = "GeV/c"
        _format = "%0.0f " + _units
        _xlabel = "p_{T,jj}^{ldg}  (%s)" % (_units)
        _format = "%0.0f " + _units
        _opts["xmax"] = 800


    elif "topbdt_" in histo.lower():
        _format = "%0.1f"
        _cutBox = {"cutValue": +0.40, "fillColor": 16, "box": False, "line": False, "greaterThan": True}
        _xlabel = "BDTG discriminant"
            
    if "gentop_pt" in histo.lower():
        _rebinX = 1
    if "genquark_pt" in histo.lower():
        _rebinX = 1
        _opts["xmax"] = 500
    else:
        pass

    if "delta" in histo.lower():
        _format = "%0.1f "
        if "phi" in histo.lower():
            _xlabel = "#Delta #phi"
        if "deltar" in histo.lower():
            _rebinX = 2

    if "DiBjetMaxMass_Mass" in histo:
        _units = "GeV"
        _rebinX = 4
        _xlabel = "m_{max}(bb) (%s)" % (_units)
        _format = "%0.0f " + _units
        
    if "DiJetDeltaRmin_Mass" in histo:
        _units = "GeV"
        _format = "%0.0f " + _units
        _xlabel = "m_{#DeltaR_{min}(jj)}(jj) (%s)" % (_units)
        _opts["xmax"] = 200

    if "DiBjetDeltaRmin_Mass" in histo:
        _units = "GeV"
        _format = "%0.0f " + _units
        _rebinX= 2
        _xlabel = "m_{#DeltaR_{min}(bb)}(bb) (%s)" % (_units)
        _opts["xmax"] = 600

    if "LdgBjet_SubldgBjet_Mass" in histo:
        _units = "GeV"
        _format = "%0.0f " + _units
        _rebinX= 4
        _xlabel = "m(b_{ldg}b_{sldg}) (%s)" % (_units)
        
    if "DeltaR_LdgTop_DiBjetDeltaRmin" in histo:
        _rebinX= 2        
        _format = "%0.1f "
        _xlabel = "#DeltaR (top_{ldg}, bb_{#Delta Rmin})"

    if "DeltaR_SubldgTop_DiBjetDeltaRmin" in histo:
        _rebinX= 2        
        _format = "%0.1f "
        _xlabel = "#DeltaR (top_{sldg}, bb_{#Delta Rmin})"

    if "over" in histo.lower():        
        _opts["xmax"] = 15
        _opts["xmax"] = +0.8
        _opts["xmin"] = -0.8
        _xlabel = "#Delta p_{T}(j-q)/p_{T,q}"
        _cutBox = {"cutValue": +0.32, "fillColor": 16, "box": False, "line": True, "greaterThan": True}

    if "within" in histo.lower():
        _opts["xmax"] = +0.8
        _opts["xmin"] = -0.8
        _xlabel = "#Delta p_{T}(j-q)/p_{T,q}"
        _cutBox = {"cutValue": +0.32, "fillColor": 16, "box": False, "line": True, "greaterThan": True}

    if "axis2" in histo.lower():
        _opts["xmax"] = +0.2
        _opts["xmin"] = 0.0
        _xlabel = "axis2"
        _units = ""
        _format = "%0.1f "+_units

    if "axis2" in histo.lower():
        _opts["xmax"] = +0.2
        _opts["xmin"] = 0.0
        _xlabel = "axis2"
        _units  = ""
        _format = "%0.2f "+_units

    if "mass" in histo.lower():
        _xlabel = "M (GeV/c^{2})"
        _units  = "GeV/c^{2}"
        _format = "%0.0f "+_units

    if "mult" in histo.lower():
        _xlabel = "mult"
        _units  = ""
        _format = "%0.0f "+_units

    if "BQuarkFromH_Pt" in histo:
        _opts["xmax"] = 200
        _rebinX= 1

    if "order" in histo.lower():
        _opts["xmax"] = 15
        _rebinX= 1
        if "pt" in histo.lower():
            _xlabel = "indx_{p_{T}}"
        if "csv" in histo.lower():
            _xlabel = "indx_{csv}"

    if "phi_alpha" in histo.lower() or "phi_beta" in histo.lower() or "r_alpha" in histo.lower() or "r_beta" in histo.lower():
        _format = "%0.1f "
        _opts["xmin"] = 0.0
        if "phi" in histo.lower():
            _xlabel = "#phi"
            _opts["xmax"] = 5.5
        else:
            _xlabel = "r"
            _opts["xmax"] = 6.5
        if "alpha" in histo.lower():
            _xlabel = _xlabel+"_{#alpha}"
        else:
            _xlabel = _xlabel+"_{#beta}"
    if opts.normaliseToOne:
        logY    = False
        Ylabel  = "Arbitrary Units / %s" % (_format)
    else:
        logY    = True
        Ylabel  = "Events / %s" % (_format)

    if logY:
        yMaxFactor = 2.0
    else:
        yMaxFactor = 1.2

    _opts["ymaxfactor"] = yMaxFactor
    if opts.normaliseToOne:
        _opts["ymin"] = 1e-3
        #_opts   = {"ymin": 1e-3, "ymaxfactor": yMaxFactor, "xmax": None}
    else:
        _opts["ymin"] = 1e0
        if "order" in histo.lower():
            _opts["ymin"] = 1e-3
        #_opts["ymaxfactor"] = yMaxFactor
        #_opts   = {"ymin": 1e0, "ymaxfactor": yMaxFactor, "xmax": None}

    # Customise styling
    p.histoMgr.forEachHisto(lambda h: h.getRootHisto().SetLineStyle(ROOT.kSolid))

    if "QCD" in datasetsMgr.getAllDatasetNames():
        p.histoMgr.forHisto("QCD", styles.getQCDLineStyle()) #getQCDFillStyle() )
        p.histoMgr.setHistoDrawStyle("QCD", "HIST")
        p.histoMgr.setHistoLegendStyle("QCD", "F")

    if "TT" in datasetsMgr.getAllDatasetNames():
        TTStyle           = styles.StyleCompound([styles.StyleFill(fillColor=ROOT.kMagenta-2), styles.StyleLine(lineColor=ROOT.kMagenta-2, lineStyle=ROOT.kSolid, lineWidth=3),
                                                  styles.StyleMarker(markerSize=1.2, markerColor=ROOT.kMagenta-2, markerSizes=None, markerStyle=ROOT.kFullTriangleUp)])
        p.histoMgr.forHisto("TT", TTStyle)
        p.histoMgr.setHistoDrawStyle("TT", "HIST") #AP
        p.histoMgr.setHistoLegendStyle("TT", "F")  #LP
        
        
    # Customise style
    signalM = []
    for m in signalMass:
        signalM.append(m.rsplit("M_")[-1])
    for m in signalM:
        p.histoMgr.forHisto("ChargedHiggs_HplusTB_HplusToTB_M_%s" %m, styles.getSignalStyleHToTB_M(m))
        

    plots.drawPlot(p, 
                   histo,  
                   xlabel       = _xlabel,
                   ylabel       = Ylabel,
                   log          = logY,
                   rebinX       = _rebinX, cmsExtraText = "Preliminary", 
                   #createLegend = {"x1": 0.59, "y1": 0.65, "x2": 0.92, "y2": 0.92},
                   createLegend = {"x1": 0.59, "y1": 0.70, "x2": 0.92, "y2": 0.92},
                   #createLegend = {"x1": 0.73, "y1": 0.85, "x2": 0.97, "y2": 0.77},
                   opts         = _opts,
                   opts2        = {"ymin": 0.6, "ymax": 1.4},
                   cutBox       = _cutBox,
                   )

    # Save plot in all formats    
    saveName = histo.split("/")[-1]
    savePath = os.path.join(opts.saveDir, histo.split("/")[0], opts.optMode)

    '''
    if opts.normaliseToOne:
        save_path = savePath + opts.MVAcut
        if opts.noQCD:
            save_path = savePath + opts.MVAcut + "/noQCD/"
    else:
        save_path = savePath + opts.MVAcut + "/normToLumi/"
        if opts.noQCD:
            save_path = savePath + opts.MVAcut + "/noQCD/"
     '''
    
    SavePlot(p, saveName, savePath) 

    return


#================================================================================================ 
# Main
#================================================================================================ 
if __name__ == "__main__":
    '''
    https://docs.python.org/3/library/argparse.html
 
    name or flags...: Either a name or a list of option strings, e.g. foo or -f, --foo.
    action..........: The basic type of action to be taken when this argument is encountered at the command line.
    nargs...........: The number of command-line arguments that should be consumed.
    const...........: A constant value required by some action and nargs selections.
    default.........: The value produced if the argument is absent from the command line.
    type............: The type to which the command-line argument should be converted.
    choices.........: A container of the allowable values for the argument.
    required........: Whether or not the command-line option may be omitted (optionals only).
    help............: A brief description of what the argument does.
    metavar.........: A name for the argument in usage messages.
    dest............: The name of the attribute to be added to the object returned by parse_args().
    '''
    
    # Default Settings
    ANALYSISNAME = "TopTaggerEfficiency"
    MVACUT       = "MVA"
    SEARCHMODE   = "80to1000"
    DATAERA      = "Run2016"
    OPTMODE      = ""
    BATCHMODE    = True
    PRECISION    = 3
    #SIGNALMASS   = [200, 300, 400, 500, 650, 800, 1000]
    SIGNALMASS   = [200, 300, 500, 1000]
    #SIGNALMASS   = [180, 200]
    INTLUMI      = -1.0
    SUBCOUNTERS  = False
    LATEX        = False
    MERGEEWK     = False
    URL          = False
    NOERROR      = True
    NOQCD        = False
    SAVEDIR      = None #"/publicweb/%s/%s/%s" % (getpass.getuser()[0], getpass.getuser(), ANALYSISNAME)
    VERBOSE      = False
    HISTOLEVEL   = "Vital" # 'Vital' , 'Informative' , 'Debug'
    NORMALISE    = False
    FOLDER       = "" #"topSelection_" #"ForDataDrivenCtrlPlots" #"topologySelection_"

    # Define the available script options
    parser = OptionParser(usage="Usage: %prog [options]")

    parser.add_option("-m", "--mcrab", dest="mcrab", action="store", 
                      help="Path to the multicrab directory for input")

    parser.add_option("-o", "--optMode", dest="optMode", type="string", default=OPTMODE, 
                      help="The optimization mode when analysis variation is enabled  [default: %s]" % OPTMODE)

    parser.add_option("-b", "--batchMode", dest="batchMode", action="store_false", default=BATCHMODE, 
                      help="Enables batch mode (canvas creation does NOT generate a window) [default: %s]" % BATCHMODE)

    parser.add_option("--analysisName", dest="analysisName", type="string", default=ANALYSISNAME,
                      help="Override default analysisName [default: %s]" % ANALYSISNAME)

    parser.add_option("--intLumi", dest="intLumi", type=float, default=INTLUMI,
                      help="Override the integrated lumi [default: %s]" % INTLUMI)

    parser.add_option("--searchMode", dest="searchMode", type="string", default=SEARCHMODE,
                      help="Override default searchMode [default: %s]" % SEARCHMODE)

    parser.add_option("--dataEra", dest="dataEra", type="string", default=DATAERA, 
                      help="Override default dataEra [default: %s]" % DATAERA)

    parser.add_option("--mergeEWK", dest="mergeEWK", action="store_true", default=MERGEEWK, 
                      help="Merge all EWK samples into a single sample called \"EWK\" [default: %s]" % MERGEEWK)

    #parser.add_option("--signalMass", dest="signalMass", type=float, default=SIGNALMASS, 
                      #help="Mass value of signal to use [default: %s]" % SIGNALMASS)

    parser.add_option("--saveDir", dest="saveDir", type="string", default=SAVEDIR, 
                      help="Directory where all pltos will be saved [default: %s]" % SAVEDIR)

    parser.add_option("--url", dest="url", action="store_true", default=URL, 
                      help="Don't print the actual save path the histogram is saved, but print the URL instead [default: %s]" % URL)
    
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=VERBOSE, 
                      help="Enables verbose mode (for debugging purposes) [default: %s]" % VERBOSE)

    parser.add_option("--histoLevel", dest="histoLevel", action="store", default = HISTOLEVEL,
                      help="Histogram ambient level (default: %s)" % (HISTOLEVEL))

    parser.add_option("-i", "--includeOnlyTasks", dest="includeOnlyTasks", action="store", 
                      help="List of datasets in mcrab to include")

    parser.add_option("-e", "--excludeTasks", dest="excludeTasks", action="store", 
                      help="List of datasets in mcrab to exclude")

    parser.add_option("-n", "--normaliseToOne", dest="normaliseToOne", action="store_true", 
                      help="Normalise the histograms to one? [default: %s]" % (NORMALISE) )

    parser.add_option("--folder", dest="folder", type="string", default = FOLDER,
                      help="ROOT file folder under which all histograms to be plotted are located [default: %s]" % (FOLDER) )

    parser.add_option("--MVAcut", dest="MVAcut", type="string", default = MVACUT,
                      help="Save plots to directory in respect of the MVA cut value [default: %s]" % (MVACUT) )

    parser.add_option("--noQCD", dest="noQCD", action="store_true", default = NOQCD,
                      help="Exclude QCD samples [default: %s]" % (NOQCD) )


    (opts, parseArgs) = parser.parse_args()

    # Require at least two arguments (script-name, path to multicrab)
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    if opts.mcrab == None:
        Print("Not enough arguments passed to script execution. Printing docstring & EXIT.")
        parser.print_help()
        #print __doc__
        sys.exit(1)

    # Sanity check
    if opts.mergeEWK:
        Print("Merging EWK samples into a single Datasets \"EWK\"", True)

    if opts.saveDir == None:
        opts.saveDir = aux.getSaveDirPath(opts.mcrab, prefix="", postfix="")

    # Sanity check
    allowedMass = [180, 200, 220, 250, 300, 350, 400, 500, 800, 1000, 2000, 3000]
    signalMass = []
    for m in sorted(SIGNALMASS, reverse=True):
        signalMass.append("ChargedHiggs_HplusTB_HplusToTB_M_%.f" % m)

    # Call the main function
    main(opts, signalMass)

    if not opts.batchMode:
        raw_input("=== plotMC_HPlusMass.py: Press any key to quit ROOT ...")
