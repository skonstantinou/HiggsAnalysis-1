## \package AnalysisModuleSelector
# Class for obtaining lists of available eras, search modes, and variations

import sys
from HiggsAnalysis.HeavyChHiggsToTauNu.tools.ShellStyles import *

## Container class for dataset manager creator and its label
class AnalysisModuleSelectorSource:
    def __init__(self, dsetMgrCreator, label):
        self._dsetMgrCreator = dsetMgrCreator
        self._label = label

    def getDsetMgrCreator(self):
        return self._dsetMgrCreator

    def getDataEras(self):
        if self._dsetMgrCreator == None:
            return None
        return self._dsetMgrCreator.getDataEras()

    def getSearchModes(self):
        if self._dsetMgrCreator == None:
            return None
        return self._dsetMgrCreator.getSearchModes()

    def getOptimizationModes(self):
        if self._dsetMgrCreator == None:
            return None
        # Add reference mode
        myList = [""]
        myList.extend(self._dsetMgrCreator.getOptimizationModes())
        return myList

    def getLabel(self):
        return self._label

## Class for handling the book keeping of available modules common to all multicrab directories and selecting of the desired modules
class AnalysisModuleSelector:
    def __init__(self):
        self._primarySource = None   # AnalysisModuleSelectorSource object that always exists
        self._otherSources = []      # AnalysisModuleSelectorSource object
        self._availableEras = []
        self._availableSearchModes = []
        self._availableOptimizationModes = []
        self._selectedEras = []
        self._selectedSearchModes = []
        self._selectedOptimizationModes = []

    def getAvailableEras(self):
        return self._availableEras

    def getAvailableSearchModes(self):
        return self._availableSearchModes

    def getAvailableOptimizationModes(self):
        return self._availableOptimizationModes

    def getSelectedEras(self):
        return self._selectedEras

    def getSelectedSearchModes(self):
        return self._selectedSearchModes

    def getSelectedOptimizationModes(self):
        return self._selectedOptimizationModes

    def addParserOptions(self, parser):
        parser.add_option("-e", "--dataEra", dest="era", type="string", action="append", help="Evaluate specified data eras")
        parser.add_option("-m", "--searchMode", dest="searchMode", type="string", action="append", help="name of search mode")
        parser.add_option("-o", "--optimizationMode", dest="optimizationMode", type="string", action="append", help="Evaluate specified optimization mode")
        parser.add_option("-l", "--list", dest="listVariations", action="store_true", default=False, help="Print a list of available variations")

    def setPrimarySource(self, label, dsetMgrCreator):
        self._primarySource = AnalysisModuleSelectorSource(dsetMgrCreator, label)

    def addOtherSource(self, label, dsetMgrCreator):
        self._otherSources.append(AnalysisModuleSelectorSource(dsetMgrCreator, label))

    def doSelect(self, opts):
        # Find available modules
        self._findCommonAvailableEras()
        self._findCommonAvailableSearchModes()
        self._findCommonAvailableOptimizationModes()
        # Check if listing was invoked
        if opts.listVariations:
            self._printAvailableModules()
            sys.exit()
        # Make sure that format of options for eras, search modes, and optimization modes is fine
        self._correctOptionsFormat(opts)
        # Check that selected options are fine for eras, search modes, and optimization modes
        self._selectedEras = self._applySelectionOnModules("Era", opts.era, self._availableEras)
        self._selectedSearchModes = self._applySelectionOnModules("SearchMode", opts.searchMode, self._availableSearchModes)
        self._selectedOptimizationModes = self._applySelectionOnModules("OptimizationMode", opts.optimizationMode, self._availableOptimizationModes)
        # Print as information a breakdown of selected eras, search modes, and optimization modes
        self._printSelection()
        # Now, the selected eras, search modes, and optimization modes are available with the getters

    def _findCommonAvailableEras(self):
        myList = self._primarySource.getDataEras()
        # Loop over other dataset creators
        for i in range(0, len(self._otherSources)):
            if self._otherSources[i] != None:
                myList = self._findCommonAvailableModules("Era",self._primarySource.getLabel(),myList,self._otherSources[i].getLabel(),self._otherSources[i].getDataEras())
        self._availableEras = myList

    def _findCommonAvailableSearchModes(self):
        myList = self._primarySource.getSearchModes()
        # Loop over other dataset creators
        for i in range(0, len(self._otherSources)):
            if self._otherSources[i] != None:
                myList = self._findCommonAvailableModules("SearchMode",self._primarySource.getLabel(),myList,self._otherSources[i].getLabel(),self._otherSources[i].getSearchModes())
        self._availableSearchModes = myList

    def _findCommonAvailableOptimizationModes(self):
        myList = self._primarySource.getOptimizationModes()
        # Loop over other dataset creators
        for i in range(0, len(self._otherSources)):
            if self._otherSources[i] != None:
                myList = self._findCommonAvailableModules("OptimizationMode",self._primarySource.getLabel(),myList,self._otherSources[i].getLabel(),self._otherSources[i].getOptimizationModes())
        if len(myList) > 1:
            self._availableOptimizationModes = myList[1:]
        else:
            self._availableOptimizationModes = myList


    # Returns list of available modules that are common between the two lists
    def _findCommonAvailableModules(self, itemLabel, primaryLabel, primaryList, otherLabel, otherList):
        availableList = []
        # Loop over first list to find common items
        for item in primaryList:
            if item in otherList:
                availableList.append(item)
            else:
                if not item in otherList:
                    print WarningStyle()+"Warning:"+NormalStyle()+" %s selection: item '%s' is available in '%s', but missing from '%s'!"%(itemLabel, item, primaryLabel, otherLabel)
        # Return list of items available in both multicrab directories
        return availableList

    # Returns list of selected modules
    def _applySelectionOnModules(self, itemLabel, optionsList, availableList):
        if optionsList == None:
            # No specific items selected in options, use all possibilities
            return availableList
        # Loop over desired modules (either digit or string)
        selectList = []
        for item in optionsList:
            if item.isdigit():
                if int(item) >= len(availableList) or int(item) < 0:
                    raise Exception(ErrorStyle()+"Error:"+NormalStyle()+" %s selection: requested for index %s, but only options 0-%d are available!"%(itemLabel, item, len(availableList)-1))
                selectList.append(availableList[int(item)])
            else:
                if not item in availableList:
                    raise Exception(ErrorStyle()+"Error:"+NormalStyle()+" %s selection: requested for %s, but only options (%s) are available!"%(itemLabel, item, (', '.join(map(str, availableList)))))
                else:
                    selectList.append(item)
        return selectList

    def _printAvailableModules(self):
        print "\nAvailable data era options common for all multicrab directories:"
        print "(you may choose any with command line options, either with the digit shown below or the full name, example: -e Run2011A -e Run2011B)"
        for i in range (0,len(self._availableEras)):
            print "  %2d: %s"%(i, self._availableEras[i].replace("Run",""))
        print "\nAvailable search mode options common for all multicrab directories:"
        print "(you may choose any with command line options, either with the digit shown below or the full name, example: -m Light)"
        for i in range (0,len(self._availableSearchModes)):
            print "  %2d: %s"%(i, self._availableSearchModes[i])
        print "\nAvailable search mode options common for all multicrab directories:"
        print "(you may choose any with command line options, either with the digit shown below or the full name, example: -o 1-3,5)"
        for i in range (0,len(self._availableOptimizationModes)):
            if self._availableOptimizationModes[i] == "":
                print "  %2d: (nominal analysis)"%(i)
            else:
                print "  %2d: %s"%(i, self._availableOptimizationModes[i].replace("Opt",""))

    def _correctOptionsFormat(self, opts):
        # Make sure that format of options for eras, search modes, and optimization modes is fine
        if opts.era != None:
            opts.era = self._disentangleDigitsInOptionString(opts.era)
            for i in range(0, len(opts.era)):
                if not opts.era[i].isdigit():
                    if not "Run" in opts.era[i]:
                        opts.era[i] = "Run%s"%opts.era[i]
                    if "run" in opts.era[i]:
                        opts.era[i].replace("run","Run")
        if opts.searchMode != None:
            opts.searchMode = self._disentangleDigitsInOptionString(opts.searchMode)
            for i in range(0, len(opts.searchMode)):
                if not opts.searchMode[i].isdigit():
                    if "light" in opts.searchMode[i]:
                        opts.searchMode[i].replace("light","Light")
                    if "heavy" in opts.searchMode[i]:
                        opts.searchMode[i].replace("heavy","Heavy")
        if opts.optimizationMode != None:
            opts.optimizationMode = self._disentangleDigitsInOptionString(opts.optimizationMode)
            for i in range(0, len(opts.optimizationMode)):
                if not opts.optimizationMode[i].isdigit():
                    if not "Opt" in opts.optimizationMode[i]:
                        opts.optimizationMode[i] = "Opt%s"%opts.optimizationMode[i]

    def _disentangleDigitsInOptionString(self, inputList):
        myDigits = []
        for item in inputList:
            myList = item.replace(" ","").split(",")
            for n in myList:
                if "-" in n:
                    # Range
                    myRangeList = n.split("-")
                    if len(myRangeList) == 2:
                        if myRangeList[0].isdigit() and myRangeList[1].isdigit():
                            for i in range(int(myRangeList[0]), int(myRangeList[1])+1):
                                myDigits.append(i)
                else:
                    if n.isdigit():
                        myDigits.append(int(n))
        # Sort and convert output to strings again
        myDigits.sort()
        myOutList = []
        for d in myDigits:
            myOutList.append(str(d))
        if len(myDigits) > 0:
            return myOutList
        return inputList

    def _printSelection(self):
        # Define style here
        myNotSelectedStr = "      "
        mySelectedStr = "  %s--> "%(HighlightStyle())
        mySelectedSuffix = " <--%s"%(NormalStyle())

        print "\nSelected data eras:"
        for i in range (0,len(self._availableEras)):
            myStr = myNotSelectedStr
            mySuffix = ""
            if self._availableEras[i] in self._selectedEras:
                myStr = mySelectedStr
                mySuffix = mySelectedSuffix
            print "%s%2d: %s%s"%(myStr, i, self._availableEras[i].replace("Run",""),mySuffix)
        print "\nSelected search modes:"
        for i in range (0,len(self._availableSearchModes)):
            myStr = myNotSelectedStr
            mySuffix = ""
            if self._availableSearchModes[i] in self._selectedSearchModes:
                myStr = mySelectedStr
                mySuffix = mySelectedSuffix
            print "%s%2d: %s%s"%(myStr, i, self._availableSearchModes[i],mySuffix)
        print "\nSelected optimization modes:"
        for i in range (0,len(self._availableOptimizationModes)):
            myStr = myNotSelectedStr
            mySuffix = ""
            if self._availableOptimizationModes[i] in self._selectedOptimizationModes:
                myStr = mySelectedStr
                mySuffix = mySelectedSuffix
            if self._availableOptimizationModes[i] == "":
                print "%s%2d: (nominal)%s"%(myStr, i, mySuffix)
            else:
                print "%s%2d: %s%s"%(myStr, i, self._availableOptimizationModes[i].replace("Opt",""),mySuffix)
        print ""
