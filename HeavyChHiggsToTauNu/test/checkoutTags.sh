#!/bin/sh

set -e

# Tag list modification history
# 7.7.2010/S.Lehti CMSSW_3_6_3
# 9.8.2010/M.Kortelainen CMSSW_3_7_0_patch_3
# 21.9.2010/S.Lehti CMSSW_3_8_4
# 27.9.2010/M.Kortelainen CMSSW_3_8_4_patch2
# 29.9.2010/S.Lehti CMSSW_3_8_4_patch2 (discriminators moved under RecoTau)
# 15.10.2010/S.Lehti CMSSW_3_8_5 (discriminators moved under RecoTau)
# 19.10.2010/M.Kortelainen CMSSW_3_8_5 (lumi tag update)
# 21.10.2010/M.Kortelainen CMSSW_3_8_5_patch2 (Updated PatAlgos tag, added revision numbers for files)
# 28.10.2010/M.Kortelainen CMSSW_3_8_5_patch3 (Electron ID and additional PAT tags from the release notes)
# 2.11.2010/M.Kortelainen CMSSW_3_8_5_patch3 (tag for filterJSON.py etc. scripts) 
# 11.11.2010/M.Kortelainen CMSSW_3_8_6 Moved the tau embedding tag here since it is needed for compilation
# 12.11.2010/M.Kortelainen CMSSW_3_8_6 Removed the tau embedding tag (added workaround)
# 9.12.2010/M.Kortelainen CMSSW_3_8_7 Updated PAT tags to latest recipe, updated lumi tag
# 27.12.2010/M.Kortelainen CMSSW_3_9_7 Updated tags to latest recipes
# 12.1.2011/M.Kortelainen CMSSW_3_9_7 Added HPS+TaNC tags
# 18.1.2011/M.Kortelainen CMSSW_3_9_7 Update PFRecoTauDiscriminationByInvMass.cc
# 19.1.2011/M.Kortelainen CMSSW_3_9_7 Updated the tau tags
# 16.2.2011/M.Kortelainen CMSSW_3_9_7 Mechanism to not to take HPS+TaNC tags
# 17.2.2011/M.Kortelainen CMSSW_3_9_7 Updated lumi tag 
# 17.3.2011/M.Kortelainen CMSSW_3_9_7 Suffering from HiggsAnalysis/Skimming being checked out without a tag...
# 18.3.2011/M.Kortelainen CMSSW_3_9_9_patch1 Updated PAT tags for trigger
# 21.3.2011/M.Kortelainen CMSSW_4_1_3 Still suffering from HiggsAnalysis/Skimming...

# addpkg requires cmsenv
eval $(scram runtime -sh)


HPSTANC="true"
if [ "x$#" = "x1" -a "x$1" = "xnoHpsTanc" ]; then
    HPSTANC="false"
fi

# HPS+TaNC
if [ "x$HPSTANC" = "xtrue" ]; then
    cvs co -r1.28 RecoTauTag/tau_tags.txt
    # This checkouts
    # RecoTauTag/RecoTau
    # RecoTauTag/TauTagTools
    # RecoTauTag/Configuration
    # DataFormats/TauReco
    addpkg -f RecoTauTag/tau_tags.txt
    cvs up -r 1.2 RecoTauTag/RecoTau/python/PFRecoTauDiscriminationByInvMass_cfi.py
    cvs up -r 1.3 RecoTauTag/RecoTau/python/PFRecoTauDiscriminationForChargedHiggs_cfi.py

    cvs co -r 1.2 RecoTauTag/tau_tags_dependencies.txt
    # This checkouts
    # DataFormats/PatCandidates 
    # JetMETCorrections/Type1MET 
    # PhysicsTools/IsolationAlgos 
    # PhysicsTools/PFCandProducer 
    # PhysicsTools/PatAlgos 
    # PhysicsTools/PatUtils
    addpkg -f RecoTauTag/tau_tags_dependencies.txt
    cvs up -r1.36 PhysicsTools/PatAlgos/python/tools/tauTools.py
fi

# PAT
addpkg CommonTools/CandUtils     V00-00-05
addpkg DataFormats/CaloTowers    V02-05-11
addpkg DataFormats/PatCandidates V06-02-21
addpkg PhysicsTools/PatAlgos     V08-03-11

if [ "x$HPSTANC" = "xtrue" ]; then
    cvs up -r1.36 PhysicsTools/PatAlgos/python/tools/tauTools.py
fi

# Luminosity
cvs co -r V02-01-03 RecoLuminosity/LumiDB

# Electron ID
cvs co -r V00-03-19 RecoEgamma/ElectronIdentification
cvs co -r V00-03-00 ElectroWeakAnalysis/WENu

# Higgs skimms
cvs co HiggsAnalysis/Skimming
rm HiggsAnalysis/Skimming/python/earlyDataInterestingEvents_cff.py
