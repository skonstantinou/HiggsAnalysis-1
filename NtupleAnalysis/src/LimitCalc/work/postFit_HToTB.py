#!/usr/bin/env python
'''
DESCRIPTION:
Script for plotting post-fit invariant mass shapes
In a nutshell, We use combine command to produce post-fit plots.

First we create a workspace with:
text2workspace.py combine_datacard_hplushadronic_m500.txt -o ws.root

This creates an output ROOT file called "ws.root" which we will use as
input to combine to produced fitDiagnonstics.root file as follows:
combine -M FitDiagnostics --robustFit=1 --X-rtd MINIMIZER_analytic ws.root --saveShapes --saveWithUncertainties --saveOverallShapes --saveNormalizations --saveWorkspace --plots --expectSignal=0 --rMin=-10

The fitDiagnostics.root is created, this contains the post-fit histos and is the input for this plotting script.


USAGE:
0) Go to the datacards directory you want to investigate
cd <datacards_dir>

1) Run the recommended closure checks commands and save all relevant plots:
../../doClosureChecks.csh 180
WARNING! the output file is not suited for post-fit plots

2) Execute this script from inside the <datacards_dir>
../.././postFit_HToTB.py --mass 180 --url


NOTE:
Results should be irrelevant of the mass point chosen since we are using the Bkg-only fit-result
as input.


EXAMPLES:
../.././postFit_HToTB.py --mass 500 --prefit && ../.././postFit_HToTB.py --mass 500 && ../.././postFit_HToTB.py --mass 180 --prefit && ../.././postFit_HToTB.py --mass 180 --url
../.././postFit_HToTB.py --mass 500 --prefit --fitUncert


LAST USED:
../.././postFit_HToTB.py --mergeRares --url --mass 250,500,1000 --fitUncert --prefit && ../.././postFit_HToTB.py --mergeRares --url --mass 250,500,1000 --fitUncert

'''

#================================================================================================  
# Imports
#================================================================================================  
import os
import sys
import re
import array 
import getpass
from optparse import OptionParser

import ROOT

import HiggsAnalysis.NtupleAnalysis.tools.dataset as dataset
import HiggsAnalysis.NtupleAnalysis.tools.tdrstyle as tdrstyle
import HiggsAnalysis.NtupleAnalysis.tools.styles as styles
import HiggsAnalysis.NtupleAnalysis.tools.plots as plots
import HiggsAnalysis.NtupleAnalysis.tools.histograms as histograms
import HiggsAnalysis.NtupleAnalysis.tools.aux as aux
import HiggsAnalysis.NtupleAnalysis.tools.ShellStyles as ShellStyles

import ROOT
ROOT.gROOT.SetBatch(True)

#================================================================================================  
# Class definition
#================================================================================================  
def Verbose(msg, printHeader=False):
    '''
    Calls Print() only if verbose options is set to true.
    '''
    if not opts.verbose:
        return
    Print(msg, printHeader)
    return


def Print(msg, printHeader=True):
    '''
    Simple print function. If verbose option is enabled prints, otherwise does nothing.
    '''
    fName = __file__.split("/")[-1]
    if printHeader:
        print "=== ", fName
    print "\t", msg
    return


class Category:
    def __init__(self, name, opts):
        xMin = 0
        if opts.logX:
            xMin = 1
        if opts.logY:
            yMin = 0.5e-2 #1e-2
            yMaxFactor = 10.0
        else:
            yMin = 0.0
            yMaxFactor = 1.2

        self.name       = name
        self.gOpts      = opts
        self.histonames = []
        self.labels     = {}
        self.colors     = {}
        self.h_data     = None
        self.h_signal   = None
        self.histograms = {}
        self.opts       = {"xmin": xMin, "xmax" : self.gOpts.xMax, "ymin" : yMin, "ymaxfactor": yMaxFactor}
        self.optsLogx   = {"xmin": xMin, "xmax": opts.xMax}
        self.opts2      = {"ymin": 0.3, "ymax": 1.7}
        self.moveLegend = {}
        return

    def addData(self,datarootfile):
        self.datafile = datarootfile
        return

    def addHisto(self, histo, legendlabel, color=0):
        self.histonames.append(histo)
        self.labels[histo] = legendlabel
        self.colors[histo] = color
        return

    def setXmax(self,xmax):
        self.opts["xmax"] = xmax
        self.optsLogx["xmax"] = xmax
        return

    def setXmin(self,xmin):
        self.opts["xmin"] = xmin
        self.optsLogx["xmin"] = xmin
        return

    def setMoveLegend(self,move):
        self.moveLegend = move
        return

    def clone(self,name):
        returnCat = Category(name, self.gOpts)
        returnCat.histonames = self.histonames
        returnCat.labels     = self.labels
        returnCat.colors     = self.colors
        returnCat.opts       = self.opts
        returnCat.opts2      = self.opts2
        returnCat.moveLegend = self.moveLegend
        return returnCat

    def __add__(self, cat):
        returnCat = Category("sum")
        returnCat.colors = self.colors
        returnCat.histonames = self.histonames

        if self.h_data == None:
            returnCat.h_data = self.h_data
        else:
            returnCat.h_data = self.h_data.Add(cat.h_data)
        if len(self.histograms) == 0:
            returnCat.histograms = cat.histograms
        else:
            returnCat.histograms = []
            for hname in self.histonames:
                h_sum = self.histograms[hname].Add(cat.histograms[hname])
                returnCat.histograms.append(h_sum)
        return returnCat

    def fetchHistograms(self, fINdata, fINpost, fINsignal):
        
        histoName  = "data_obs"
        histoData   = fINdata.Get(histoName)
        Verbose("Getting data histogram \"%s\" from ROOT file \"%s\" (Integral = %.1f)" % (histoName, fINdata.GetName(), histoData.Integral()), True)
        self.h_data = histoData.Clone("Data")

        # Inspect histogram contents?
        if opts.verbose:
            aux.PrintTH1Info(self.h_data)

        nbins = 0
        binning = []
        # For-loop: All bins
        for iBin in range(self.h_data.GetNbinsX()+1):
            binLowEdge = self.h_data.GetBinLowEdge(iBin)
            if binLowEdge >= opts.xMinRebin and binLowEdge < opts.xMaxRebin:
                nbins += 1
                binning.append(binLowEdge)

        binning.append(min(self.optsLogx["xmax"], opts.xMaxRebin))
        n = len(binning)-1
        self.h_data.SetBins(nbins, array.array("d", binning) )
        
        # Define signal histogram styles
        # if len(opts.masses) > 3:
        #     raise Exception("Cannot plot more than 3 signal mass points (got %s)." % (opts.masses) )
        # lineStyles  = [ROOT.kSolid, ROOT.kDashed, ROOT.kDotted]
        # lineColours = [ROOT.kRed, ROOT.kAzure+6, ROOT.kGreen]

        # Add signal
        self.h_signal = []
        for i, m in enumerate(opts.masses, 0):
            hName = "Hp%s" % m
            histo = fINsignal[m].Get(hName)
            Verbose("Getting signal histogram \"%s\" from ROOT file \"%s\" (Integral = %.1f)" % (hName, fINsignal[m].GetName(), histo.Integral()), False)
            if 0:
                histo.SetLineColor(lineColours[i])
                histo.SetLineStyle(lineStyles[i])
                histo.SetLineWidth(3)
            histo.SetTitle("H^{#pm} (%s GeV)" % m)
            histo.SetBins(nbins, array.array("d", binning) )
            self.h_signal.append(histo.Clone(hName))
                                   
        # Inspect histogram contents?
        if opts.verbose:
            aux.PrintTH1Info(self.h_signal)

        # For-loop: All histos
        for i, hname in enumerate(self.histonames, 1):
            Verbose("Getting histogram \"%s\" from ROOT file \"%s\"" % (histoName, fINpost.GetName()), i==1)

            template = self.h_data.Clone(hname)
            template.Reset()
            
            n = len(binning)-1
            template.SetBins(n, array.array("d",binning) )
            
            if opts.prefit:
                histoName = os.path.join("shapes_prefit", self.name, hname)
            else:
                histoName = os.path.join("shapes_fit_b", self.name, hname)

            # Get the histograms
            histo = fINpost.Get(histoName)

            # Safety net for empty histos (if datasset integral is zero corresponding histo will not exist)
            if "TH1" in str(type(histo)):
                # print "type(histo) = ", type(histo)
                pass
            else: 
                # Histograms to ignore because dataset yield is zero (hack)
                msg = "Skipping %s. Not a histogram!" % (histoName)
                Print(ShellStyles.ErrorStyle() + msg + ShellStyles.NormalStyle(), True)
                opts.empty.append(histoName.split("/")[-1])
                continue

            Verbose("Getting bkg histogram \"%s\" from ROOT file \"%s\" (Integral = %.1f)" % (histoName, fINpost.GetName(), histo.Integral()), i==1)

            # For-loop: All bins
            for iBin in range(0, histo.GetNbinsX()+1):
                template.SetBinContent(iBin, histo.GetBinContent(iBin) )
                template.SetBinError(iBin, histo.GetBinError(iBin) )

            # Customise histogram
            template.SetFillColor(self.colors[hname])
            template.SetLineWidth(0)
            self.histograms[hname] = template
        return


    def plot(self):
        style = tdrstyle.TDRStyle()
        ROOT.gStyle.SetErrorX(0.5) #required for x-axis error bars! (must be called AFTER tdrstyle.TDRStyle())

        histolist = []
        #styles.dataStyle.apply(self.h_data)
        hhd = histograms.Histo(self.h_data,"Data", legendStyle="PL", drawStyle="E1P")
        hhd.setIsDataMC(isData=True, isMC=False)
        histolist.append(hhd)

        # For-loop: All signal histo
        for i, hsignal in enumerate(self.h_signal, 1):
            mass = hsignal.GetName().replace("Hp", "")
            Verbose( "Customing signal histogram for Mass = \"%s\"" % (mass), i==1)
            hhs = histograms.Histo(hsignal,hsignal.GetTitle(), legendStyle="L", drawStyle="HIST")
            hhs.setIsDataMC(isData=False, isMC=True)
            signalStyle = styles.getSignalStyleHToTB_M(mass)
            signalStyle.apply(hhs.getRootHisto())
            histolist.append(hhs)
            
        # For-loop: All bkg histos
        for i, hname in enumerate(self.histonames, 1):
            # Safety net for empty histos
            if hname in opts.empty:
                msg = "Skipping %s. Not a histogram!" % (hname) 
                Print(ShellStyles.ErrorStyle() + msg + ShellStyles.NormalStyle(), True)
                continue
            else:
                #print hname
                pass                
            
            myLabel = self.labels[hname]
            myHisto = self.histograms[hname]
            Verbose("Creating histogram \"%s\" from ROOT file \"%s\" (Integral = %.1f)" % (hname, myHisto.GetName(), myHisto.Integral()), i==1)
            hhp = histograms.Histo(myHisto, hname, legendStyle="F", drawStyle="HIST", legendLabel=myLabel)
            hhp.setIsDataMC(isData=False,isMC=True)
            histolist.append(hhp)

        # Sanity check
        for i, h in enumerate(histolist, 1):
            hName = h.getRootHisto().GetName()
            Verbose(hName, i==1)

        # Do the plot
        p = plots.DataMCPlot2(histolist)
        p.setDefaultStyles()
        p.stackMCHistograms()
        p.setLuminosity(opts.lumi)
        
        if opts.fitUncert:
            p.addMCUncertainty(postfit=not opts.prefit) # boolean changes only the legend

        if opts.prefit:
            p.setLegendHeader("Pre-Fit")
        else:
            p.setLegendHeader("Post-Fit")

        # Customise histogram 
        units = "GeV" #(GeV/c^{2})
        myParams = {}
        myParams["xlabel"]            = "m_{jjbb} (%s)" % (units)
        myParams["ylabel"]            = "< Events / " + units + " >"
        myParams["ratio"]             = True
        myParams["ratioYlabel"]       = "Data/Bkg. "
        myParams["logx"]              = self.gOpts.logX
        myParams["log"]               = self.gOpts.logY
        myParams["ratioType"]         = "errorScale"
        myParams["ratioErrorOptions"] = {"numeratorStatSyst": False, "denominatorStatSyst": True}
        myParams["opts"]              = self.opts
        myParams["optsLogx"]          = self.optsLogx
        myParams["opts2"]             = self.opts2
        myParams["divideByBinWidth"]  = True #not opts.fitUncert # Error when used for "TGraphAsymmErrors" (uncert.)
        myParams["errorBarsX"]        = True
        myParams["xlabelsize"]        = 25
        myParams["ylabelsize"]        = 25
        myParams["addMCUncertainty"]  = True
        myParams["addLuminosityText"] = True
        myParams["moveLegend"]        = self.moveLegend
        #myParams["saveFormats"]       = []
        
        # Draw the plot
        if not os.path.exists(opts.saveDir):
            os.makedirs(opts.saveDir)
        plots.drawPlot(p, os.path.join(opts.saveDir, self.gOpts.saveName), **myParams)

        # Save the plot (not needed - drawPlot saves the canvas already)
        SavePlot(p, self.gOpts.saveName, opts.saveDir, saveFormats = [".png", ".pdf", ".C"])

        return


def SavePlot(plot, plotName, saveDir, saveFormats = [".C", ".png", ".pdf"]):
    Verbose("Saving the plot in %s formats: %s" % (len(saveFormats), ", ".join(saveFormats) ) )

     # Check that path exists
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    # Create the name under which plot will be saved
    saveName = os.path.join(saveDir, plotName.replace("/", "_"))

    # For-loop: All save formats
    for i, ext in enumerate(saveFormats):
        saveNameURL = saveName + ext
        saveNameURL = aux.convertToURL(saveNameURL, opts.url)
        Print(saveNameURL, i==0)
        plot.saveAs(saveName, formats=saveFormats)

    # Something buggy introduced with "except" added in plots.py to fix the error when
    # using "divideByBinWidth" option with "addMCUncertainty" option. Must call exit otherwise hangs
    if opts.fitUncert:
        Print("EXIT!", True)
        os._exit(0) #sys.exit()
    return


def usage():
    print
    print "### Usage: " + sys.argv[0]+" <combine fitDiagnostics rootfile>"
    print
    sys.exit()

        
def main(opts):

    # List categories and add the histogram names
    h2tb_1 = Category("tbhadr", opts)
    
    # Customise legend position and size
    hadrMoveLegend = {"dx": -0.08, "dy": -0.02, "dh": 0.14}
    h2tb_1.setMoveLegend(hadrMoveLegend)

    # Add all histograms
    h2tb_1.addHisto("FakeB"             , "Fake b (data)", color=ROOT.kBlue-1) #ROOT.kOrange-3)
    h2tb_1.addHisto("TT_GenuineB"       , "t#bar{t}"     , color=ROOT.kMagenta-2)
    h2tb_1.addHisto("SingleTop_GenuineB", "Single t"     , color=ROOT.kSpring+4)
    if opts.mergeRares:
        h2tb_1.addHisto("Rares_GenuineB", "Rares"        , color=ROOT.kViolet+10)
    else:
        h2tb_1.addHisto("TTZToQQ_GenuineB"              , "t#bar{t}+Z"       , color=ROOT.kAzure-4)
        h2tb_1.addHisto("TTTT_GenuineB"                 , "t#bar{t}t#bar{t}" , color=ROOT.kYellow-9)
        h2tb_1.addHisto("DYJetsToQQ_GenuineB"           , "Z/#gamma^{*}+jets", color=ROOT.kTeal-9)
        h2tb_1.addHisto("TTWJetsToQQ_GenuineB"          , "t#bar{t}+W"       , color=ROOT.kSpring+9)
        h2tb_1.addHisto("WJetsToQQ_HT_600ToInf_GenuineB", "W+jets"           , color=ROOT.kOrange+9)
        h2tb_1.addHisto("Diboson_GenuineB"              , "Diboson"          , color=ROOT.kBlue-4)
    categories = [h2tb_1]

    # For-loop: All files
    for i, f in enumerate(opts.dataFiles, 1):
        if os.path.isfile(f):
            Print("Opening file \"%s\"" % (f), i==1)
        else:
            raise Exception("File \"%s\" not found." % (f) )

    if os.path.isfile(opts.postfitFile):
        Print("Opening file \"%s\"" % (opts.postfitFile), False)
    else:
        raise Exception("File \"%s\" not found." % (opts.postfitFile) )
    
    # Open ROOT files
    fIN_signal = {}
    for f in opts.dataFiles:
        Verbose("Opening ROOT file \"%s\" (data)" % (f), True)
        mass = f.split("_")[-1].replace(".root", "").replace("m", "")
        fIN_signal[mass] = ROOT.TFile.Open(f, "R")

    # Sanity checks
    if 0:
        for k in fIN_signal:
            print "key = %s , value = %s" % (k, fIN_signal[k])
        
    Verbose("Opening ROOT file \"%s\" (post-fit)" % (opts.postfitFile), True)
    fIN_post = ROOT.TFile.Open(opts.postfitFile, "R")

    categorySum = categories[0].clone("sum")
    for c in categories:
        c.fetchHistograms(fIN_signal.values()[0], fIN_post, fIN_signal) 

    # For-loop: All categories (Only HToTB currently)
    for c in categories:
        c.plot() 
    
    # Close ROOT files
    for k in fIN_signal:
        fIN_signal[k].Close()
    fIN_post.Close()
    return


if __name__=="__main__":

    # Default options
    VERBOSE         = False
    SAVEDIR         = "/afs/cern.ch/user/%s/%s/public/html/FitDiagnostics" % (getpass.getuser()[0], getpass.getuser())
    SAVENAME        = None
    LUMI            = "35.9"
    URL             = False
    LOGX            = False
    LOGY            = True
    GRIDX           = False
    GRIDY           = False
    XMINREBIN       = 0.0
    XMAXREBIN       = 10000
    XMIN            = 0.0
    XMAX            = 2500 #3000
    MASS            = "300,500,800"
    POSTFITROOTFILE = None
    DATAROOTFILE    = None
    PREFIT          = False
    FITUNCERT       = False
    MERGERARES      = False

    parser = OptionParser(usage="Usage: %prog [options]", add_help_option=True, conflict_handler="resolve")

    parser.add_option("-v", "--verbose", dest="verbose", default=VERBOSE, action="store_true",
                      help="Verbose mode for debugging purposes [default: %s]" % (VERBOSE) )
    
    parser.add_option("--url", dest="url", action="store_true", default=URL,
                      help="Don't print the actual save path the plots are saved, but print the URL instead [default: %s]" % URL)

    parser.add_option("--xMinRebin", dest="xMinRebin", default=XMINREBIN, type="float",
                      help="Left edge of the last bin in re-binned input data-histogram  [default: %s]" % (XMINREBIN) )

    parser.add_option("--xMaxRebin", dest="xMaxRebin", default=XMAXREBIN, type="float",
                      help="Right edge of the last bin in re-binned input data-histogram [default: %s]" % (XMAXREBIN) )

    parser.add_option("--xMin", dest="xMin", default=XMIN, type="float",
                      help="Overwrite minimum value of x-axis [default: %s]" % (XMIN) )

    parser.add_option("--xMax", dest="xMax", default=XMAX, type="float",
                      help="Overwrite maximum value of x-axis [default: %s]" % (XMAX) )

    parser.add_option("--saveDir", dest="saveDir", type="string", default=SAVEDIR,
                      help="Directory where all plots will be saved [default: %s]" % SAVEDIR)

    parser.add_option("--mass", dest="mass", type="string", default=MASS,
                      help="Mass point to be used. Use comma-separated values (no space) [default: %s]" % MASS)

    parser.add_option("--saveName", dest="saveName", type="string", default=SAVENAME,
                      help="Name for the invariant massplot to be saved as [default: %s]" % SAVENAME)

    parser.add_option("--lumi", dest="lumi", type="string", default=LUMI,
                      help="Integrated luminosity to be printed on the canvas [default: %s]" % LUMI)

    parser.add_option("--postfitFile", dest="postfitFile", type="string", default=POSTFITROOTFILE,
                      help="The post-fit input ROOT file [default: %s]" % POSTFITROOTFILE)

    parser.add_option("--dataFile", dest="dataFile", type="string", default=DATAROOTFILE,
                      help="The data input ROOT file [default: %s]" % DATAROOTFILE)

    parser.add_option("--logX", dest="logX", action="store_true", default=LOGX,
                      help="Plot x-axis (mass) as logarithmic [default: %s]" % (LOGX) )
    
    parser.add_option("--logY", dest="logY", action="store_true", default=LOGY,
                      help="Plot y-axis (exlusion limit) as logarithmic [default: %s]" % (LOGY) )
    
    parser.add_option("--gridX", dest="gridX", default=GRIDX, action="store_true",
                      help="Enable the grid for the x-axis [default: %s]" % (GRIDX) )

    parser.add_option("--gridY", dest="gridY", default=GRIDY, action="store_true",
                      help="Enable the grid for the y-axis [default: %s]" % (GRIDY) )

    parser.add_option("--prefit", dest="prefit", default=PREFIT, action="store_true",
                      help="Draw the pre-fit histogams (not the post-fit ones) [default: %s]" % (PREFIT) )

    parser.add_option("--fitUncert", dest="fitUncert", default=FITUNCERT, action="store_true",
                      help="Include fit-uncertainty (and disable \"divideByBinWidth\" option) [default: %s]" % (FITUNCERT) )

    parser.add_option("--mergeRares", dest="mergeRares", default=MERGERARES, action="store_true",
                      help="Merge rare datasets into a single dataset? (v. small contribution to final count) [default: %s]" % (MERGERARES) )

    (opts, args) = parser.parse_args()

    if opts.postfitFile == None:
        opts.postfitFile = "fitDiagnostics_ws.root"

    opts.dataFiles = []
    opts.masses = opts.mass.split(",")
    for m in opts.masses:
        fName = "combine_histograms_hplushadronic_m%s.root" % (m)
        opts.dataFiles.append(fName)

    if opts.saveName == None:
        postfix = "postFit"
        if opts.prefit:
            postfix = "preFit"
        opts.saveName = "LdgTetrajetMass_%s" % (postfix) #results should be the same for bkg-only fit (expectedSignal=0)

    if opts.saveDir == None:
        opts.saveDir = aux.getSaveDirPath(opts.mcrab, prefix="", postfix="Closure")

    # Histograms to ignore because dataset yield is zero (hack)
    opts.empty = []

    # Main code
    main(opts)
