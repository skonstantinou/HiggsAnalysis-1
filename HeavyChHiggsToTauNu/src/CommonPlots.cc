// -*- c++ -*-
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/CommonPlots.h"

#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/EventCounter.h"
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/HistoWrapper.h"
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/TransverseMass.h"
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/DeltaPhi.h"
#include "FWCore/Framework/interface/Event.h"

namespace HPlus {
  HistogramSettings::HistogramSettings(const edm::ParameterSet& iConfig)
  : fBins(iConfig.getUntrackedParameter<uint32_t>("nBins")),
    fAxisMin(iConfig.getUntrackedParameter<double>("axisMin")),
    fAxisMax(iConfig.getUntrackedParameter<double>("axisMax")) { }
  HistogramSettings::~HistogramSettings() { }

  CommonPlots::CommonPlots(const edm::ParameterSet& iConfig, EventCounter& eventCounter, HistoWrapper& histoWrapper, AnalysisType analysisType, bool isEmbeddedData) :
    // Switch off all extras for QCD normalization systematics
    bOptionEnableTauFakeRateAnalysis(iConfig.getUntrackedParameter<bool>("enableTauFakeRateAnalysis") && (analysisType != kQCDNormalizationSystematicsSignalRegion && analysisType != kQCDNormalizationSystematicsControlRegion)),
    bOptionEnableNormalisationAnalysis(iConfig.getUntrackedParameter<bool>("enableNormalisationAnalysis") && (analysisType != kQCDNormalizationSystematicsSignalRegion && analysisType != kQCDNormalizationSystematicsControlRegion)),
    bOptionEnableMETOscillationAnalysis(iConfig.getUntrackedParameter<bool>("enableMETOscillationAnalysis") && (analysisType != kQCDNormalizationSystematicsSignalRegion && analysisType != kQCDNormalizationSystematicsControlRegion)),
    bDisableCommonPlotsFilledAtEveryStep(false),
    fAnalysisType(analysisType),
    fEventCounter(eventCounter),
    fHistoWrapper(histoWrapper),
    fSplittedHistogramHandler(iConfig.getUntrackedParameter<edm::ParameterSet>("histogramSplitting"), histoWrapper, (analysisType != kQCDNormalizationSystematicsSignalRegion && analysisType != kQCDNormalizationSystematicsControlRegion)),
    fCommonBaseDirectory(histoWrapper.mkdir(HistoWrapper::kVital, *fs, "CommonPlots")),
    fEveryStepDirectory(histoWrapper.mkdir(HistoWrapper::kVital, fCommonBaseDirectory, "AtEveryStep")),
    fTauFakeRateAnalysis(0),
    fTauSelection(0),
    fFakeTauIdentifier(0),
    fMetTrgSF(0),
    fPtBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("ptBins")),
    fEtaBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("etaBins")),
    fPhiBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("phiBins")),
    fRtauBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("rtauBins")),
    fNjetsBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("njetsBins")),
    fMetBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("metBins")),
    fBJetDiscriminatorBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("bjetDiscriminatorBins")),
    fTailKiller1DSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("tailKiller1DBins")),
    fTopMassBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("topMassBins")),
    fWMassBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("WMassBins")),
    fMtBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("mtBins")),
    fInvmassBinSettings(iConfig.getUntrackedParameter<edm::ParameterSet>("invmassBins")),
    fMETPhiOscillationCorrectionAfterTaus(0),
    fMETPhiOscillationCorrectionAfterLeptonVeto(0),
    fMETPhiOscillationCorrectionAfterNjets(0),
    fMETPhiOscillationCorrectionAfterBjets(0),
    fMETPhiOscillationCorrectionAfterAllSelections(0),
    fMETPhiOscillationCorrectionEWKControlRegion(0) {
    // Update analysis type for embedding
    if (isEmbeddedData)
      fAnalysisType = kEmbedding;
    // Create histograms
    createHistograms();
    // Create tau fake rate analysis if asked
    if (bOptionEnableTauFakeRateAnalysis) {
      fTauFakeRateAnalysis = new TauFakeRateAnalysis(histoWrapper);
    }
    // Create objects for normalisation analysis if asked
    if (bOptionEnableNormalisationAnalysis) {
      fNormalisationAnalysisObjects.push_back(new NormalisationDYEnrichedWithGenuineTaus(eventCounter, histoWrapper));
      fNormalisationAnalysisObjects.push_back(new NormalisationDYEnrichedWithFakeTaus(eventCounter, histoWrapper));
      fNormalisationAnalysisObjects.push_back(new NormalisationWJetsEnrichedWithGenuineTaus(eventCounter, histoWrapper));
      fNormalisationAnalysisObjects.push_back(new NormalisationWJetsEnrichedWithFakeTaus(eventCounter, histoWrapper));
      fNormalisationAnalysisObjects.push_back(new NormalisationTTJetsEnrichedWithGenuineTaus(eventCounter, histoWrapper));
      fNormalisationAnalysisObjects.push_back(new NormalisationWJetsEnrichedBoostedWH(eventCounter, histoWrapper));
      fNormalisationAnalysisObjects.push_back(new NormalisationTTJetsEnrichedWithFakeTaus(eventCounter, histoWrapper));
      fNormalisationAnalysisObjects.push_back(new NormalisationTTJetsEnrichedBoostedWH(eventCounter, histoWrapper));
    }
    // Create objects for MET phi oscillation analysis
    if (bOptionEnableMETOscillationAnalysis) {
      fMETPhiOscillationCorrectionAfterTaus = new METPhiOscillationCorrection(eventCounter, fHistoWrapper, "AfterTaus");
      fMETPhiOscillationCorrectionAfterLeptonVeto = new METPhiOscillationCorrection(eventCounter, fHistoWrapper, "AfterLeptonVeto");
      fMETPhiOscillationCorrectionAfterNjets = new METPhiOscillationCorrection(eventCounter, fHistoWrapper, "AfterNjets");
      fMETPhiOscillationCorrectionAfterMETSF = new METPhiOscillationCorrection(eventCounter, fHistoWrapper, "AfterMETSF");
      fMETPhiOscillationCorrectionAfterCollinearCuts = new METPhiOscillationCorrection(eventCounter, fHistoWrapper, "AfterCollinearCuts");
      fMETPhiOscillationCorrectionAfterBjets = new METPhiOscillationCorrection(eventCounter, fHistoWrapper, "AfterBjets");
      fMETPhiOscillationCorrectionAfterAllSelections = new METPhiOscillationCorrection(eventCounter, fHistoWrapper, "AfterAllSelections");
      fMETPhiOscillationCorrectionEWKControlRegion = new METPhiOscillationCorrection(eventCounter, fHistoWrapper, "AfterAllSelections_EKWControlRegion");
    }
  }

  void CommonPlots::createHistograms() {
    // Create directories for data driven control plots
    std::string myLabel = "ForDataDrivenCtrlPlots";
    std::string myFakeLabel = "ForDataDrivenCtrlPlotsEWKFakeTaus";
    if (fAnalysisType == kQCDNormalizationSystematicsSignalRegion) {
      myLabel += "QCDNormalizationSignal";
      myFakeLabel = "Empty";
    }
    if (fAnalysisType == kQCDNormalizationSystematicsControlRegion) {
      myLabel += "QCDNormalizationControl";
      myFakeLabel = "Empty";
    }
    TFileDirectory myCtrlDir = fHistoWrapper.mkdir(HistoWrapper::kSystematics, *fs, myLabel);
    TFileDirectory myCtrlEWKFakeTausDir = fHistoWrapper.mkdir(HistoWrapper::kSystematics, *fs, myFakeLabel);

    // Create histograms

    // vertex

    // tau selection

    // tau trigger SF
    if (fAnalysisType != kQCDNormalizationSystematicsSignalRegion && fAnalysisType != kQCDNormalizationSystematicsControlRegion) {
      TFileDirectory myTauDir = fCommonBaseDirectory.mkdir("TausWithSF");
      hTauPhiOscillationX = fHistoWrapper.makeTH<TH2F>(HistoWrapper::kInformative, myTauDir, "TauPhiOscillationX", "TauPhiOscillationX;N_{vertices};#tau p_{x}, GeV/c", 60, 0., 60., 1200, -300, 300);
      hTauPhiOscillationY = fHistoWrapper.makeTH<TH2F>(HistoWrapper::kInformative, myTauDir, "TauPhiOscillationY", "TauPhiOscillationY;N_{vertices};#tau p_{y}, GeV/c", 60, 0., 60., 1200, -300, 300);
    }

    // veto tau selection

    // electron veto

    // muon veto

    // jet selection
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlNjets,            "Njets", "Number of selected jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
    if (fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausNjets, "Njets", "Number of selected jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());

    // MET trigger SF
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlNjetsAfterJetSelectionAndMETSF,            "NjetsAfterJetSelectionAndMETSF", "Number of selected jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
    if (fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausNjetsAfterJetSelectionAndMETSF, "NjetsAfterJetSelectionAndMETSF", "Number of selected jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());

    // improved delta phi collinear cuts (currently the point of the std. selections)
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlQCDTailKillerCollinearMinimum,         "ImprovedDeltaPhiCutsCollinearMinimum", "min(#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{1..3},MET))^{2}}), ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlQCDTailKillerCollinearJet1,            "ImprovedDeltaPhiCutsJet1Collinear", "#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{1},MET))^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlQCDTailKillerCollinearJet2,            "ImprovedDeltaPhiCutsJet2Collinear", "#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{2},MET))^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlQCDTailKillerCollinearJet3,            "ImprovedDeltaPhiCutsJet3Collinear", "#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{3},MET))^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlQCDTailKillerCollinearJet4,            "ImprovedDeltaPhiCutsJet4Collinear", "#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{4},MET))^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerCollinearMinimum, "ImprovedDeltaPhiCutsCollinearMinimum", "min(#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{1..3},MET))^{2}}), ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerCollinearJet1, "ImprovedDeltaPhiCutsJet1Collinear", "#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{1},MET))^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerCollinearJet2, "ImprovedDeltaPhiCutsJet2Collinear", "#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{2},MET))^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerCollinearJet3, "ImprovedDeltaPhiCutsJet3Collinear", "#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{3},MET))^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerCollinearJet4, "ImprovedDeltaPhiCutsJet4Collinear", "#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{4},MET))^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    }

    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauPtAfterStandardSelections, "SelectedTau_pT_AfterStandardSelections", "#tau p_{T}, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauEtaAfterStandardSelections, "SelectedTau_eta_AfterStandardSelections", "#tau #eta;N_{events} / 0.1", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauPhiAfterStandardSelections, "SelectedTau_phi_AfterStandardSelections", "#tau #phi;N_{events} / 0.087", fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
    hSelectedTauEtaVsPhiAfterStandardSelections = fHistoWrapper.makeTH<TH2F>(HistoWrapper::kInformative, myCtrlDir, "SelectedTau_etavsphi_AfterStandardSelections", "SelectedTau_etavsphi_AfterStandardSelections;#tau #eta;#tau #phi", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max(), fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauLeadingTrkPtAfterStandardSelections, "SelectedTau_LeadingTrackPt_AfterStandardSelections", "#tau ldg.ch.particle p_{T}, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauRtauAfterStandardSelections, "SelectedTau_Rtau_AfterStandardSelections", "R_{#tau};N_{events} / 0.1", fRtauBinSettings.bins(), fRtauBinSettings.min(), fRtauBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauPAfterStandardSelections, "SelectedTau_p_AfterStandardSelections", "#tau p, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauLeadingTrkPAfterStandardSelections, "SelectedTau_LeadingTrackP_AfterStandardSelections", "#tau ldg.ch.particle p, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauDecayModeAfterStandardSelections, "SelectedTau_DecayMode_AfterStandardSelections", "#tau decay mode;N_{events}", 30,0,30);
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauPtAfterStandardSelections, "SelectedTau_pT_AfterStandardSelections", "#tau p_{T}, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauEtaAfterStandardSelections, "SelectedTau_eta_AfterStandardSelections", "#tau #eta;N_{events} / 0.1", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauPhiAfterStandardSelections, "SelectedTau_phi_AfterStandardSelections", "#tau #phi;N_{events} / 0.087", fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
      hEWKFakeTausSelectedTauEtaVsPhiAfterStandardSelections = fHistoWrapper.makeTH<TH2F>(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, "SelectedTau_etavsphi_AfterStandardSelections", "#tau #eta;#tau #phi", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max(), fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauLeadingTrkPtAfterStandardSelections, "SelectedTau_LeadingTrackPt_AfterStandardSelections", "#tau ldg.ch.particle p_{T}, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauRtauAfterStandardSelections, "SelectedTau_Rtau_AfterStandardSelections", "R_{#tau};N_{events} / 0.1", fRtauBinSettings.bins(), fRtauBinSettings.min(), fRtauBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauPAfterStandardSelections, "SelectedTau_p_AfterStandardSelections", "#tau p, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauLeadingTrkPAfterStandardSelections, "SelectedTau_LeadingTrackP_AfterStandardSelections", "#tau ldg.ch.particle p, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauDecayModeAfterStandardSelections, "SelectedTau_DecayMode_AfterStandardSelections", "#tau decay mode;N_{events}", 30,0,30);
    }

    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlNjetsAfterStandardSelections, "Njets_AfterStandardSelections", "Number of selected jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlJetPtAfterStandardSelections, "JetPt_AfterStandardSelections", "Jet p_{T}, GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlJetEtaAfterStandardSelections, "JetEta_AfterStandardSelections", "Jet #eta;N_{events}", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausNjetsAfterStandardSelections, "Njets_AfterStandardSelections", "Number of selected jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausJetPtAfterStandardSelections, "JetPt_AfterStandardSelections", "Jet p_{T}, GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausJetEtaAfterStandardSelections, "JetEta_AfterStandardSelections", "Jet #eta;N_{events}", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
    }
    // MET selection
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlMET,            "MET", "MET, GeV;N_{events}", fMetBinSettings.bins(), fMetBinSettings.min(), fMetBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlMETPhi,         "METPhi", "METPhi, ^{o};N_{events}", fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlTauPlusMETPt,   "TauPlusMETPt", "p_{T}(#tau+MET), GeV;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausMET,    "MET", "MET, GeV;N_{events}", fMetBinSettings.bins(), fMetBinSettings.min(), fMetBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausMETPhi, "METPhi", "METPhi, ^{o};N_{events}", fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausTauPlusMETPt, "TauPlusMETPt", "p_{T}(#tau+MET), GeV;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    }
    // b tagging
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlNbjets,            "NBjets", "Number of identified b jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlBJetPt,            "BJetPt", "b jet p_{T}, GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlBJetEta,           "BJetEta", "b jet #eta;N_{events}", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlBDiscriminator,    "BtagDiscriminator", "Btag discriminator;b tag discriminator;N_{events}", fBJetDiscriminatorBinSettings.bins(), fBJetDiscriminatorBinSettings.min(), fBJetDiscriminatorBinSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausNbjets,         "NBjets", "Number of identified b jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausBJetPt,         "BJetPt", "b jet p_{T}, GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausBJetEta,        "BJetEta", "b jet #eta;N_{events}", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausBDiscriminator, "BtagDiscriminator", "Btag discriminator;b tag discriminator;N_{events}", fBJetDiscriminatorBinSettings.bins(), fBJetDiscriminatorBinSettings.min(), fBJetDiscriminatorBinSettings.max());
    }

    // improved delta phi back to back cuts
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlQCDTailKillerBackToBackMinimum,        "ImprovedDeltaPhiCutsBackToBackMinimum", "min(#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{1..3},MET)^{2}}), ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlQCDTailKillerBackToBackJet1,           "ImprovedDeltaPhiCutsJet1BackToBack", "#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{1},MET)^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlQCDTailKillerBackToBackJet2,           "ImprovedDeltaPhiCutsJet2BackToBack", "#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{2},MET)^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlQCDTailKillerBackToBackJet3,           "ImprovedDeltaPhiCutsJet3BackToBack", "#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{3},MET)^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlQCDTailKillerBackToBackJet4,           "ImprovedDeltaPhiCutsJet4BackToBack", "#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{4},MET)^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerBackToBackMinimum, "ImprovedDeltaPhiCutsBackToBackMinimum", "min(#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{1..3},MET)^{2}}), ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerBackToBackJet1,"ImprovedDeltaPhiCutsJet1BackToBack", "#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{1},MET)^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerBackToBackJet2,"ImprovedDeltaPhiCutsJet2BackToBack", "#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{2},MET)^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerBackToBackJet3,"ImprovedDeltaPhiCutsJet3BackToBack", "#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{3},MET)^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerBackToBackJet4,"ImprovedDeltaPhiCutsJet4BackToBack", "#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{4},MET)^{2}}, ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    }

    // top selection
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlTopMass, "TopMass", "m_{bqq'}, GeV/c^{2};N_{events}", fTopMassBinSettings.bins(), fTopMassBinSettings.min(), fTopMassBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlTopPt,   "TopPt", "p_{T}(bqq'), GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlWMass,   "WMass", "m_{qq'}, GeV/c^{2};N_{events}", fWMassBinSettings.bins(), fWMassBinSettings.min(), fWMassBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlWPt,     "WPt", "p_{T}(qq'), GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausTopMass, "TopMass", "m_{bqq'}, GeV/c^{2};N_{events}", fTopMassBinSettings.bins(), fTopMassBinSettings.min(), fTopMassBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausTopPt,   "TopPt", "p_{T}(bqq'), GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausWMass,   "WMass", "m_{qq'}, GeV/c^{2};N_{events}", fWMassBinSettings.bins(), fWMassBinSettings.min(), fWMassBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausWPt,     "WPt", "p_{T}(qq'), GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    }

    // evt topology

    // ctrl plots after all selections
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlQCDTailKillerCollinearMinimumAfterMtSelections,         "ImprovedDeltaPhiCutsCollinearMinimumAfterMtSelections", "min(#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{1..3},MET))^{2}}), ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerCollinearMinimumAfterMtSelections, "ImprovedDeltaPhiCutsCollinearMinimumAfterMtSelections", "min(#sqrt{#Delta#phi(#tau,MET)^{2}+(180^{o}-#Delta#phi(jet_{1..3},MET))^{2}}), ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    }
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauPtAfterMtSelections, "SelectedTau_pT_AfterMtSelections", "#tau p_{T}, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauEtaAfterMtSelections, "SelectedTau_eta_AfterMtSelections", "#tau #eta;N_{events} / 0.1", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauPhiAfterMtSelections, "SelectedTau_phi_AfterMtSelections", "#tau #phi;N_{events} / 0.087", fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauLeadingTrkPtAfterMtSelections, "SelectedTau_LeadingTrackPt_AfterMtSelections", "#tau ldg.ch.particle p_{T}, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauRtauAfterMtSelections, "SelectedTau_Rtau_AfterMtSelections", "R_{#tau};N_{events} / 0.1", fRtauBinSettings.bins(), fRtauBinSettings.min(), fRtauBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauPAfterMtSelections, "SelectedTau_p_AfterMtSelections", "#tau p, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauLeadingTrkPAfterMtSelections, "SelectedTau_LeadingTrackP_AfterMtSelections", "#tau ldg.ch.particle p, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlSelectedTauDecayModeAfterMtSelections, "SelectedTau_DecayMode_AfterMtSelections", "#tau decay mode;N_{events}", 30,0,30);
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauPtAfterMtSelections, "SelectedTau_pT_AfterMtSelections", "#tau p_{T}, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauEtaAfterMtSelections, "SelectedTau_eta_AfterMtSelections", "#tau #eta;N_{events} / 0.1", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauPhiAfterMtSelections, "SelectedTau_phi_AfterMtSelections", "#tau #phi;N_{events} / 0.087", fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauLeadingTrkPtAfterMtSelections, "SelectedTau_LeadingTrackPt_AfterMtSelections", "#tau ldg.ch.particle p_{T}, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauRtauAfterMtSelections, "SelectedTau_Rtau_AfterMtSelections", "R_{#tau};N_{events} / 0.1", fRtauBinSettings.bins(), fRtauBinSettings.min(), fRtauBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauPAfterMtSelections, "SelectedTau_p_AfterMtSelections", "#tau p, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauLeadingTrkPAfterMtSelections, "SelectedTau_LeadingTrackP_AfterMtSelections", "#tau ldg.ch.particle p, GeV/c;N_{events} / 5 GeV/c", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausSelectedTauDecayModeAfterMtSelections, "SelectedTau_DecayMode_AfterMtSelections", "#tau decay mode;N_{events}", 30,0,30);
    }
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlNjetsAfterMtSelections, "Njets_AfterMtSelections", "Number of selected jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlJetPtAfterMtSelections, "JetPt_AfterMtSelections", "Jet p_{T}, GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir, hCtrlJetEtaAfterMtSelections, "JetEta_AfterMtSelections", "Jet #eta;N_{events}", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausNjetsAfterMtSelections, "Njets_AfterMtSelections", "Number of selected jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausJetPtAfterMtSelections, "JetPt_AfterMtSelections", "Jet p_{T}, GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausJetEtaAfterMtSelections, "JetEta_AfterMtSelections", "Jet #eta;N_{events}", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
    }
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlMETAfterMtSelections,            "METAfterMtSelections", "MET, GeV;N_{events}", fMetBinSettings.bins(), fMetBinSettings.min(), fMetBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlMETPhiAfterMtSelections,         "METPhiAfterMtSelections", "METPhi, ^{o};N_{events}", fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlTauPlusMETPtAfterMtSelections,   "TauPlusMETPtAfterMtSelections", "p_{T}(#tau+MET), GeV;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausMETAfterMtSelections,    "METAfterMtSelections", "MET, GeV;N_{events}", fMetBinSettings.bins(), fMetBinSettings.min(), fMetBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausMETPhiAfterMtSelections, "METPhiAfterMtSelections", "METPhi, ^{o};N_{events}", fPhiBinSettings.bins(), fPhiBinSettings.min(), fPhiBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausTauPlusMETPtAfterMtSelections, "TauPlusMETPtAfterMtSelections", "p_{T}(#tau+MET), GeV;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    }
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlNbjetsAfterMtSelections,            "NBjetsAfterMtSelections", "Number of identified b jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlBJetPtAfterMtSelections,            "BJetPtAfterMtSelections", "b jet p_{T}, GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlBJetEtaAfterMtSelections,           "BJetEtaAfterMtSelections", "b jet #eta;N_{events}", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlBDiscriminatorAfterMtSelections,    "BtagDiscriminatorAfterMtSelections", "Btag discriminator;b tag discriminator;N_{events}", fBJetDiscriminatorBinSettings.bins(), fBJetDiscriminatorBinSettings.min(), fBJetDiscriminatorBinSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausNbjetsAfterMtSelections,         "NBjetsAfterMtSelections", "Number of identified b jets;N_{events}", fNjetsBinSettings.bins(), fNjetsBinSettings.min(), fNjetsBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausBJetPtAfterMtSelections,         "BJetPtAfterMtSelections", "b jet p_{T}, GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausBJetEtaAfterMtSelections,        "BJetEtaAfterMtSelections", "b jet #eta;N_{events}", fEtaBinSettings.bins(), fEtaBinSettings.min(), fEtaBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausBDiscriminatorAfterMtSelections, "BtagDiscriminatorAfterMtSelections", "Btag discriminator;b tag discriminator;N_{events}", fBJetDiscriminatorBinSettings.bins(), fBJetDiscriminatorBinSettings.min(), fBJetDiscriminatorBinSettings.max());
    }
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlQCDTailKillerBackToBackMinimumAfterMtSelections,        "ImprovedDeltaPhiCutsBackToBackMinimumAfterMtSelections", "min(#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{1..3},MET)^{2}}), ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausQCDTailKillerBackToBackMinimumAfterMtSelections, "ImprovedDeltaPhiCutsBackToBackMinimumAfterMtSelections", "min(#sqrt{(180^{o}-#Delta#phi(#tau,MET))^{2}+#Delta#phi(jet_{1..3},MET)^{2}}), ^{o};N_{events}", fTailKiller1DSettings.bins(), fTailKiller1DSettings.min(), fTailKiller1DSettings.max());
    }
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlTopMassAfterMtSelections, "TopMassAfterMtSelections", "m_{bqq'}, GeV/c^{2};N_{events}", fTopMassBinSettings.bins(), fTopMassBinSettings.min(), fTopMassBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlTopPtAfterMtSelections,   "TopPtAfterMtSelections", "p_{T}(bqq'), GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics,   myCtrlDir,            hCtrlWMassAfterMtSelections,   "WMassAfterMtSelections", "m_{qq'}, GeV/c^{2};N_{events}", fWMassBinSettings.bins(), fWMassBinSettings.min(), fWMassBinSettings.max());
    fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative,   myCtrlDir,            hCtrlWPtAfterMtSelections,     "WPtAfterMtSelections", "p_{T}(qq'), GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    if (fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausTopMassAfterMtSelections, "TopMassAfterMtSelections", "m_{bqq'}, GeV/c^{2};N_{events}", fTopMassBinSettings.bins(), fTopMassBinSettings.min(), fTopMassBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausTopPtAfterMtSelections,   "TopPtAfterMtSelections", "p_{T}(bqq'), GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausWMassAfterMtSelections,   "WMassAfterMtSelections", "m_{qq'}, GeV/c^{2};N_{events}", fWMassBinSettings.bins(), fWMassBinSettings.min(), fWMassBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kInformative, myCtrlEWKFakeTausDir, hCtrlEWKFakeTausWPtAfterMtSelections,     "WPtAfterMtSelections", "p_{T}(qq'), GeV/c;N_{events}", fPtBinSettings.bins(), fPtBinSettings.min(), fPtBinSettings.max());
    }

    // all selections
    if (fAnalysisType != kQCDNormalizationSystematicsSignalRegion && fAnalysisType != kQCDNormalizationSystematicsControlRegion) {
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeTransverseMass,            "shapeTransverseMass", "m_{T}(tau,MET), GeV/c^{2};N_{events}", fMtBinSettings.bins(), fMtBinSettings.min(), fMtBinSettings.max());
        fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeEWKFakeTausTransverseMass, "shapeEWKFakeTausTransverseMass", "m_{T}(tau,MET), GeV/c^{2};N_{events}", fMtBinSettings.bins(), fMtBinSettings.min(), fMtBinSettings.max());
        fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeEmbeddingLikeMultipleTausTransverseMass, "shapeEmbeddingLikeMultipleTausTransverseMass", "m_{T}(tau,MET), GeV/c^{2};N_{events}", fMtBinSettings.bins(), fMtBinSettings.min(), fMtBinSettings.max());
        fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeProbabilisticBtagTransverseMass, "shapeProbabilisticBtagTransverseMass", "m_{T}(tau,MET), GeV/c^{2};N_{events}", fMtBinSettings.bins(), fMtBinSettings.min(), fMtBinSettings.max());
        fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeProbabilisticBtagEWKFakeTausTransverseMass, "shapeProbabilisticBtagEWKFakeTausTransverseMass", "m_{T}(tau,MET), GeV/c^{2};N_{events}", fMtBinSettings.bins(), fMtBinSettings.min(), fMtBinSettings.max());
        fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeProbabilisticBtagEmbeddingLikeMultipleTausTransverseMass, "shapeProbabilisticBtagEmbeddingLikeMultipleTausTransverseMass", "m_{T}(tau,MET), GeV/c^{2};N_{events}", fMtBinSettings.bins(), fMtBinSettings.min(), fMtBinSettings.max());
      // all selections with full mass
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeFullMass,            "shapeInvariantMass", "m_{H+}, GeV/c^{2};N_{events}", fInvmassBinSettings.bins(), fInvmassBinSettings.min(), fInvmassBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeEWKFakeTausFullMass, "shapeEWKFakeTausInvariantMass", "m_{H+}, GeV/c^{2};N_{events}", fInvmassBinSettings.bins(), fInvmassBinSettings.min(), fInvmassBinSettings.max());
      fSplittedHistogramHandler.createShapeHistogram(HistoWrapper::kSystematics, *fs, hShapeEmbeddingLikeMultipleTausFullMass, "shapeEmbeddingLikeMultipleTausFullMass", "m_{H+}, GeV/c^{2};N_{events}", fInvmassBinSettings.bins(), fInvmassBinSettings.min(), fInvmassBinSettings.max());
    }
  }

  CommonPlots::~CommonPlots() {
    for (std::vector<CommonPlotsFilledAtEveryStep*>::iterator it = hEveryStepHistograms.begin(); it < hEveryStepHistograms.end(); ++it)
      delete (*it);
    hEveryStepHistograms.clear();
  }

  void CommonPlots::initialize(const edm::Event& iEvent,
                               const edm::EventSetup& iSetup,
                               VertexSelection::Data& vertexData,
                               TauSelection& tauSelection,
                               FakeTauIdentifier& fakeTauIdentifier,
                               ElectronSelection& eVeto,
                               MuonSelection& muonVeto,
                               JetSelection& jetSelection,
                               METTriggerEfficiencyScaleFactor& metTrgSF,
                               METSelection& metSelection,
                               BTagging& bTagging,
                               QCDTailKiller& qcdTailKiller,
                               BjetSelection& bjetSelection,
                               TopSelectionManager& topSelectionManager,
                               EvtTopology& evtTopology,
                               FullHiggsMassCalculator& fullHiggsMassCalculator) {
    if (!vertexData.passedEvent()) return; // Require valid vertex
    fTauSelection = &tauSelection;
    fTauData = tauSelection.silentAnalyze(iEvent, iSetup, vertexData.getSelectedVertex()->z());
    initialize(iEvent,iSetup,
               vertexData,
               fTauData,
               fakeTauIdentifier,
               eVeto,
               muonVeto,
               jetSelection,
               metTrgSF,
               metSelection,
               bTagging,
               qcdTailKiller,
               bjetSelection,
               topSelectionManager,
               evtTopology,
               fullHiggsMassCalculator);
  }

  void CommonPlots::initialize(const edm::Event& iEvent,
                               const edm::EventSetup& iSetup,
                               VertexSelection::Data& vertexData,
                               TauSelection::Data& tauData,
                               FakeTauIdentifier& fakeTauIdentifier,
                               ElectronSelection& eVeto,
                               MuonSelection& muonVeto,
                               JetSelection& jetSelection,
                               METTriggerEfficiencyScaleFactor& metTrgSF,
                               METSelection& metSelection,
                               BTagging& bTagging,
                               QCDTailKiller& qcdTailKiller,
                               BjetSelection& bjetSelection,
                               TopSelectionManager& topSelectionManager,
                               EvtTopology& evtTopology,
                               FullHiggsMassCalculator& fullHiggsMassCalculator) {
    fSplittedHistogramHandler.initialize();
    fFakeTauIdentifier = &fakeTauIdentifier;
    if (iEvent.isRealData())
      metTrgSF.setRun(iEvent.id().run());
    fMetTrgSF = &metTrgSF;
    // Obtain data objects
    fVertexData = vertexData;
    if (!vertexData.passedEvent()) return; // Require valid vertex
    fTauData = tauData;
    if (fTauData.passedEvent())
      fFakeTauData = fakeTauIdentifier.silentMatchTauToMC(iEvent, *(fTauData.getSelectedTau()));
    fElectronData = eVeto.silentAnalyze(iEvent, iSetup);
    fMuonData = muonVeto.silentAnalyze(iEvent, iSetup, fVertexData.getSelectedVertex());
    if (fTauData.passedEvent())
      fJetData = jetSelection.silentAnalyze(iEvent, iSetup, fTauData.getSelectedTau(), fVertexData.getNumberOfAllVertices());
    else
      fJetData = jetSelection.silentAnalyze(iEvent, iSetup, fVertexData.getNumberOfAllVertices());
    fBJetData = bTagging.silentAnalyze(iEvent, iSetup, fJetData.getSelectedJets());

    // Need to require one tau in the event
    if (fTauData.getSelectedTau().isNull()) {
      fMETData = metSelection.silentAnalyzeNoIsolatedTaus(iEvent, iSetup);
      // Plots do not make sense if no tau has been found
      edm::Ptr<pat::Tau> myZeroTauPointer;
      for (std::vector<CommonPlotsFilledAtEveryStep*>::iterator it = hEveryStepHistograms.begin(); it != hEveryStepHistograms.end(); ++it) {
        (*it)->cacheDataObjects(&fVertexData, 0, 0, &fElectronData, &fMuonData, &fJetData, &fMETData, &fBJetData, 0, 0, 0);
      }
      return;
    }
    // A tau exists beyond this point, now obtain MET with residual type I MET
    fMETData = metSelection.silentAnalyze(iEvent, iSetup, vertexData.getNumberOfAllVertices(), fTauData.getSelectedTau(), fJetData.getAllJets());
    // Obtain improved delta phi cut data object
    fQCDTailKillerData = qcdTailKiller.silentAnalyze(iEvent, iSetup, fTauData.getSelectedTau(), fJetData.getSelectedJetsIncludingTau(), fMETData.getSelectedMET());
    // Obtain top selection object
    BjetSelection::Data bjetSelectionData = bjetSelection.silentAnalyze(iEvent, iSetup, fJetData.getSelectedJets(), fBJetData.getSelectedJets(), fTauData.getSelectedTau(), fMETData.getSelectedMET());
    fTopData = topSelectionManager.silentAnalyze(iEvent, iSetup, fJetData.getSelectedJets(), fBJetData.getSelectedJets(), bjetSelectionData.getBjetTopSide(), bjetSelectionData.passedEvent());
    // Do full higgs mass only if tau and b jet was found
    if (fBJetData.passedEvent()) {
      fFullHiggsMassData = fullHiggsMassCalculator.silentAnalyze(iEvent, iSetup, fTauData.getSelectedTau(), fBJetData, fMETData);
    }
//FIXME : add met SF also to every set plots
    // Pass pointer to cached data objects to CommonPlotsFilledAtEveryStep
    if (!hEveryStepHistograms.size() && !bDisableCommonPlotsFilledAtEveryStep)
      throw cms::Exception("Assert") << "CommonPlots::initialize() was called before creating CommonPlots::createCommonPlotsFilledAtEveryStep()!" << endl<<  "  make first all CommonPlots::createCommonPlotsFilledAtEveryStep() and then call CommonPlots::initialize()";
    for (std::vector<CommonPlotsFilledAtEveryStep*>::iterator it = hEveryStepHistograms.begin(); it != hEveryStepHistograms.end(); ++it) {
      (*it)->cacheDataObjects(&fVertexData, &fTauData, &fFakeTauData, &fElectronData, &fMuonData, &fJetData, &fMETData, &fBJetData, &fQCDTailKillerData, &fTopData, &fFullHiggsMassData);
    }
  }

  CommonPlotsFilledAtEveryStep* CommonPlots::createCommonPlotsFilledAtEveryStep(std::string label, bool enterSelectionFlowPlot, std::string selectionFlowPlotLabel) {
    // Create and return object, but sneakily save the pointer for later use
    CommonPlotsFilledAtEveryStep* myObject = new CommonPlotsFilledAtEveryStep(fHistoWrapper, fEveryStepDirectory, label, enterSelectionFlowPlot, selectionFlowPlotLabel);
    hEveryStepHistograms.push_back(myObject);
    return myObject;
  }

//------ Control plot filling
  void CommonPlots::fillControlPlotsAfterVertexSelection(const edm::Event& iEvent, const VertexSelection::Data& data) {
    //----- MET phi oscillation
    //fMETData = metSelection.silentAnalyzeNoIsolatedTaus(iEvent, iSetup, fJetData.getAllJets());
    if (bOptionEnableTauFakeRateAnalysis && fTauSelection && fFakeTauIdentifier) {
      fTauFakeRateAnalysis->analyseTauFakeRate(iEvent, fVertexData, *fTauSelection, fTauData, *fFakeTauIdentifier, fJetData);
    }
  }

  void CommonPlots::fillControlPlotsAfterTauSelection(const edm::Event& iEvent, const edm::EventSetup& iSetup, const TauSelection::Data& tauData, const FakeTauIdentifier::Data& fakeTauData, JetSelection& jetSelection, METSelection& metSelection, BTagging& btagging, QCDTailKiller& qcdTailKiller) {
    fTauData = tauData;
    fFakeTauData = fakeTauData;
    // Obtain all other objects, whose selection depends on the tau
    fJetData = jetSelection.silentAnalyze(iEvent, iSetup, tauData.getSelectedTau(), fVertexData.getNumberOfAllVertices());
    fMETData = metSelection.silentAnalyze(iEvent, iSetup, fVertexData.getNumberOfAllVertices(), fTauData.getSelectedTau(), fJetData.getAllJets());
    fBJetData = btagging.silentAnalyze(iEvent, iSetup, fJetData.getSelectedJetsPt20());
    fQCDTailKillerData = qcdTailKiller.silentAnalyze(iEvent, iSetup, fTauData.getSelectedTau(), fJetData.getSelectedJetsIncludingTau(), fMETData.getSelectedMET());
    // Set splitted bin info
    setSplittingOfPhaseSpaceInfoAfterTauSelection(iEvent, iSetup, fTauData, metSelection);
    // Obtain new MET object corresponding to the selected tau
    if (bOptionEnableTauFakeRateAnalysis) {
      // e->tau normalisation
      fTauFakeRateAnalysis->analyseEToTauFakes(fVertexData, tauData, fakeTauData, fElectronData, fMuonData, fJetData, fMETData);
    }
  }

  void CommonPlots::setSplittingOfPhaseSpaceInfoAfterTauSelection(const edm::Event& iEvent, const edm::EventSetup& iSetup, const TauSelection::Data& tauData, METSelection& metSelection) {
    METSelection::Data metData = metSelection.silentAnalyze(iEvent, iSetup, fVertexData.getNumberOfAllVertices(), fTauData.getSelectedTau(), fJetData.getAllJets());
    double myDeltaPhiTauMET = DeltaPhi::reconstruct(*(tauData.getSelectedTau()), *(metData.getSelectedMET())) * 57.3; // converted to degrees    
    fSplittedHistogramHandler.setFactorisationBinForEvent(tauData.getSelectedTau()->pt(), tauData.getSelectedTau()->eta(), fVertexData.getNumberOfAllVertices(), myDeltaPhiTauMET);
  }

  void CommonPlots::fillControlPlotsAfterTauTriggerScaleFactor(const edm::Event& iEvent) {
    if (bOptionEnableMETOscillationAnalysis) fMETPhiOscillationCorrectionAfterTaus->analyze(iEvent, fVertexData.getNumberOfAllVertices(), fMETData);
    hTauPhiOscillationX->Fill(fVertexData.getNumberOfAllVertices(), fTauData.getSelectedTau()->px());
    hTauPhiOscillationY->Fill(fVertexData.getNumberOfAllVertices(), fTauData.getSelectedTau()->py());

    // Do normalisation analyses
    if (bOptionEnableNormalisationAnalysis) {
      for (std::vector<NormalisationAnalysis*>::iterator it = fNormalisationAnalysisObjects.begin(); it != fNormalisationAnalysisObjects.end(); ++it) {
        (*it)->analyse(iEvent, fTauData, fFakeTauData, fElectronData, fMuonData, fJetData, fMetTrgSF, fQCDTailKillerData, fMETData, fBJetData);
      }
    }
  }

  void CommonPlots::fillControlPlotsAtTauVetoSelection(const edm::Event& iEvent, const edm::EventSetup& iSetup, const VetoTauSelection::Data& tauVetoData) {

  }

  void CommonPlots::fillControlPlotsAtElectronSelection(const edm::Event& iEvent, const ElectronSelection::Data& data) {
    fElectronData = data;
  }

  void CommonPlots::fillControlPlotsAtMuonSelection(const edm::Event& iEvent, const MuonSelection::Data& data) {
    fMuonData = data;
    if (bOptionEnableMETOscillationAnalysis) fMETPhiOscillationCorrectionAfterLeptonVeto->analyze(iEvent, fVertexData.getNumberOfAllVertices(), fMETData);
  }

  void CommonPlots::fillControlPlotsAtJetSelection(const edm::Event& iEvent, const JetSelection::Data& data) {
    fJetData = data;
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlNjets, data.getHadronicJetCount());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausNjets, data.getHadronicJetCount());
    if (bOptionEnableMETOscillationAnalysis) fMETPhiOscillationCorrectionAfterNjets->analyze(iEvent, fVertexData.getNumberOfAllVertices(), fMETData);
  }

  void CommonPlots::fillControlPlotsAfterMETTriggerScaleFactor(const edm::Event& iEvent) {
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlNjetsAfterJetSelectionAndMETSF, fJetData.getHadronicJetCount());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausNjetsAfterJetSelectionAndMETSF, fJetData.getHadronicJetCount());
    if (bOptionEnableMETOscillationAnalysis) fMETPhiOscillationCorrectionAfterMETSF->analyze(iEvent, fVertexData.getNumberOfAllVertices(), fMETData);
  }

  void CommonPlots::fillControlPlotsAtCollinearDeltaPhiCuts(const edm::Event& iEvent, const QCDTailKiller::Data& data) {
    fQCDTailKillerData = data;
    bool myPassStatus = true;
    double myMinimumRadius = 999.;
    for (int i = 0; i < data.getNConsideredJets(); ++i) {
      double myRadius = data.getRadiusFromCollinearCorner(i);
      if (myRadius < myMinimumRadius && data.collinearCutActiveForJet(i))
        myMinimumRadius = myRadius;
      if (i == 0 && myPassStatus) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerCollinearJet1, myRadius); // Make control plot before cut
        if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
          fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerCollinearJet1, myRadius); // Make control pl
      } else if (i == 1 && myPassStatus) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerCollinearJet2, myRadius); // Make control plot before cut
        if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
          fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerCollinearJet2, myRadius); // Make control pl
      } else if (i == 2 && myPassStatus) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerCollinearJet3, myRadius); // Make control plot before cut
        if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
          fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerCollinearJet3, myRadius); // Make control pl
      } else if (i == 3 && myPassStatus) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerCollinearJet4, myRadius); // Make control plot before cut
        if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
          fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerCollinearJet4, myRadius); // Make control pl
      }
      if (!data.passCollinearCutForJet(i))
        myPassStatus = false;
    }
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerCollinearMinimum, myMinimumRadius);
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerCollinearMinimum, myMinimumRadius);

    // Fill control plots for selected taus after standard selections
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauRtauAfterStandardSelections, fTauData.getSelectedTauRtauValue());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauLeadingTrkPtAfterStandardSelections, fTauData.getSelectedTau()->leadPFChargedHadrCand()->pt());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauPtAfterStandardSelections, fTauData.getSelectedTau()->pt());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauEtaAfterStandardSelections, fTauData.getSelectedTau()->eta());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauPhiAfterStandardSelections, fTauData.getSelectedTau()->phi());
    hSelectedTauEtaVsPhiAfterStandardSelections->Fill(fTauData.getSelectedTau()->eta(), fTauData.getSelectedTau()->phi());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauPAfterStandardSelections, fTauData.getSelectedTau()->p());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauLeadingTrkPAfterStandardSelections, fTauData.getSelectedTau()->leadPFChargedHadrCand()->p());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauDecayModeAfterStandardSelections, fTauData.getSelectedTau()->decayMode());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauRtauAfterStandardSelections, fTauData.getSelectedTauRtauValue());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauLeadingTrkPtAfterStandardSelections, fTauData.getSelectedTau()->leadPFChargedHadrCand()->pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauPtAfterStandardSelections, fTauData.getSelectedTau()->pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauEtaAfterStandardSelections, fTauData.getSelectedTau()->eta());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauPhiAfterStandardSelections, fTauData.getSelectedTau()->phi());
      hEWKFakeTausSelectedTauEtaVsPhiAfterStandardSelections->Fill(fTauData.getSelectedTau()->eta(), fTauData.getSelectedTau()->phi());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauPAfterStandardSelections, fTauData.getSelectedTau()->p());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauLeadingTrkPAfterStandardSelections, fTauData.getSelectedTau()->leadPFChargedHadrCand()->p());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauDecayModeAfterStandardSelections, fTauData.getSelectedTau()->decayMode());
    }
    // Fill control plots for selected jets
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlNjetsAfterStandardSelections, fJetData.getHadronicJetCount());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausNjetsAfterStandardSelections, fJetData.getHadronicJetCount());
    for (edm::PtrVector<pat::Jet>::iterator jet = fJetData.getSelectedJets().begin(); jet != fJetData.getSelectedJets().end(); ++jet) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlJetPtAfterStandardSelections, (*jet)->pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlJetEtaAfterStandardSelections, (*jet)->eta());
      if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausJetPtAfterStandardSelections, (*jet)->pt());
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausJetEtaAfterStandardSelections, (*jet)->eta());
      }
    }
    // MET oscillation analysis
    if (bOptionEnableMETOscillationAnalysis) fMETPhiOscillationCorrectionAfterCollinearCuts->analyze(iEvent, fVertexData.getNumberOfAllVertices(), fMETData);
  }

  void CommonPlots::fillControlPlotsAtMETSelection(const edm::Event& iEvent, const METSelection::Data& data) {
    fMETData = data;
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlMET, data.getSelectedMET()->et());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlMETPhi, data.getSelectedMET()->phi());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlTauPlusMETPt, (fTauData.getSelectedTau()->p4()+data.getSelectedMET()->p4()).pt());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausMET, data.getSelectedMET()->et());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausMETPhi, data.getSelectedMET()->phi());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausTauPlusMETPt, (fTauData.getSelectedTau()->p4()+data.getSelectedMET()->p4()).pt());
    }
  }

  void CommonPlots::fillControlPlotsAtBtagging(const edm::Event& iEvent, const BTagging::Data& data) {
    fBJetData = data;
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlNbjets, data.getBJetCount());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausNbjets, data.getBJetCount());
    // Loop over selected jets
    for (edm::PtrVector<pat::Jet>::const_iterator iJet = fJetData.getSelectedJets().begin(); iJet != fJetData.getSelectedJets().end(); ++iJet) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlBDiscriminator, (*iJet)->bDiscriminator(fBJetData.getDiscriminatorName()));
      if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausBDiscriminator, (*iJet)->bDiscriminator(fBJetData.getDiscriminatorName()));
      }
    }
    // Loop over selected b jets
    for (edm::PtrVector<pat::Jet>::const_iterator iJet = data.getSelectedJets().begin(); iJet != data.getSelectedJets().end(); ++iJet) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlBJetPt, (*iJet)->pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlBJetEta, (*iJet)->eta());
      if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausBJetPt, (*iJet)->pt());
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausBJetEta, (*iJet)->eta());
      }
    }
    // MET oscillation analysis
    if (bOptionEnableMETOscillationAnalysis) fMETPhiOscillationCorrectionAfterBjets->analyze(iEvent, fVertexData.getNumberOfAllVertices(), fMETData);
  }

  void CommonPlots::fillControlPlotsAtBackToBackDeltaPhiCuts(const edm::Event& iEvent, const QCDTailKiller::Data& data) {
    fQCDTailKillerData = data;
    bool myPassStatus = true;
    double myMinimumRadius = 999.;
    for (int i = 0; i < data.getNConsideredJets(); ++i) {
      double myRadius = data.getRadiusFromBackToBackCorner(i);
      if (myRadius < myMinimumRadius && data.backToBackCutActiveForJet(i))
        myMinimumRadius = myRadius;
      if (i == 0 && myPassStatus) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerBackToBackJet1, myRadius); // Make control plot before cut
        if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
          fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerBackToBackJet1, myRadius); // Make control plot before cut
      } else if (i == 1 && myPassStatus) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerBackToBackJet2, myRadius); // Make control plot before cut
        if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
          fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerBackToBackJet2, myRadius); // Make control plot before cut
      } else if (i == 2 && myPassStatus) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerBackToBackJet3, myRadius); // Make control plot before cut
        if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
          fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerBackToBackJet3, myRadius); // Make control plot before cut
      } else if (i == 3 && myPassStatus) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerBackToBackJet4, myRadius); // Make control plot before cut
        if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
          fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerBackToBackJet4, myRadius); // Make control plot before cut
      }
      if (!data.passBackToBackCutForJet(i))
        myPassStatus = false;
    }
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerBackToBackMinimum, myMinimumRadius);
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerBackToBackMinimum, myMinimumRadius);
  }

  void CommonPlots::fillControlPlotsAtTopSelection(const edm::Event& iEvent, const TopSelectionManager::Data& data) {
    fTopData = data;
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlTopMass, data.getTopMass());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlTopPt, data.getTopP4().pt());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlWMass, data.getWMass());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlWPt, data.getWP4().pt());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausTopMass, data.getTopMass());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausTopPt, data.getTopP4().pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausWMass, data.getWMass());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausWPt, data.getWP4().pt());
    }
  }

  void CommonPlots::fillControlPlotsAtEvtTopology(const edm::Event& iEvent, const EvtTopology::Data& data) {
    
  }

  void CommonPlots::fillControlPlotsAfterAllSelections(const edm::Event& iEvent, double transverseMass) {
    // ctrl plots after all selections
    double myMinimumRadius = 999.;
    for (int i = 0; i < fQCDTailKillerData.getNConsideredJets(); ++i) {
      double myRadius = fQCDTailKillerData.getRadiusFromCollinearCorner(i);
      if (myRadius < myMinimumRadius && fQCDTailKillerData.collinearCutActiveForJet(i))
        myMinimumRadius = myRadius;
    }
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerCollinearMinimumAfterMtSelections, myMinimumRadius);
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerCollinearMinimumAfterMtSelections, myMinimumRadius);
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauRtauAfterMtSelections, fTauData.getSelectedTauRtauValue());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauLeadingTrkPtAfterMtSelections, fTauData.getSelectedTau()->leadPFChargedHadrCand()->pt());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauPtAfterMtSelections, fTauData.getSelectedTau()->pt());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauEtaAfterMtSelections, fTauData.getSelectedTau()->eta());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauPhiAfterMtSelections, fTauData.getSelectedTau()->phi());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauPAfterMtSelections, fTauData.getSelectedTau()->p());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauLeadingTrkPAfterMtSelections, fTauData.getSelectedTau()->leadPFChargedHadrCand()->p());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlSelectedTauDecayModeAfterMtSelections, fTauData.getSelectedTau()->decayMode());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauRtauAfterMtSelections, fTauData.getSelectedTauRtauValue());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauLeadingTrkPtAfterMtSelections, fTauData.getSelectedTau()->leadPFChargedHadrCand()->pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauPtAfterMtSelections, fTauData.getSelectedTau()->pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauEtaAfterMtSelections, fTauData.getSelectedTau()->eta());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauPhiAfterMtSelections, fTauData.getSelectedTau()->phi());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauPAfterMtSelections, fTauData.getSelectedTau()->p());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauLeadingTrkPAfterMtSelections, fTauData.getSelectedTau()->leadPFChargedHadrCand()->p());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausSelectedTauDecayModeAfterMtSelections, fTauData.getSelectedTau()->decayMode());
    }
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlNjetsAfterMtSelections, fJetData.getHadronicJetCount());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausNjetsAfterMtSelections, fJetData.getHadronicJetCount());
    for (edm::PtrVector<pat::Jet>::iterator jet = fJetData.getSelectedJets().begin(); jet != fJetData.getSelectedJets().end(); ++jet) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlJetPtAfterMtSelections, (*jet)->pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlJetEtaAfterMtSelections, (*jet)->eta());
      if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausJetPtAfterMtSelections, (*jet)->pt());
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausJetEtaAfterMtSelections, (*jet)->eta());
      }
    }
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlMETAfterMtSelections, fMETData.getSelectedMET()->et());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlMETPhiAfterMtSelections, fMETData.getSelectedMET()->phi());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlTauPlusMETPtAfterMtSelections, (fTauData.getSelectedTau()->p4()+fMETData.getSelectedMET()->p4()).pt());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausMETAfterMtSelections, fMETData.getSelectedMET()->et());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausMETPhiAfterMtSelections, fMETData.getSelectedMET()->phi());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausTauPlusMETPtAfterMtSelections, (fTauData.getSelectedTau()->p4()+fMETData.getSelectedMET()->p4()).pt());
    }
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlNbjetsAfterMtSelections, fBJetData.getBJetCount());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausNbjetsAfterMtSelections, fBJetData.getBJetCount());
    for (edm::PtrVector<pat::Jet>::const_iterator iJet = fJetData.getSelectedJets().begin(); iJet != fJetData.getSelectedJets().end(); ++iJet) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlBDiscriminatorAfterMtSelections, (*iJet)->bDiscriminator(fBJetData.getDiscriminatorName()));
      if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausBDiscriminatorAfterMtSelections, (*iJet)->bDiscriminator(fBJetData.getDiscriminatorName()));
      }
    }
    for (edm::PtrVector<pat::Jet>::const_iterator iJet = fBJetData.getSelectedJets().begin(); iJet != fBJetData.getSelectedJets().end(); ++iJet) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlBJetPtAfterMtSelections, (*iJet)->pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlBJetEtaAfterMtSelections, (*iJet)->eta());
      if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausBJetPtAfterMtSelections, (*iJet)->pt());
        fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausBJetEtaAfterMtSelections, (*iJet)->eta());
      }
    }
    myMinimumRadius = 999.;
    for (int i = 0; i < fQCDTailKillerData.getNConsideredJets(); ++i) {
      double myRadius = fQCDTailKillerData.getRadiusFromBackToBackCorner(i);
      if (myRadius < myMinimumRadius && fQCDTailKillerData.backToBackCutActiveForJet(i))
        myMinimumRadius = myRadius;
    }
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlQCDTailKillerBackToBackMinimumAfterMtSelections, myMinimumRadius);
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis)
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausQCDTailKillerBackToBackMinimumAfterMtSelections, myMinimumRadius);
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlTopMassAfterMtSelections, fTopData.getTopMass());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlTopPtAfterMtSelections, fTopData.getTopP4().pt());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlWMassAfterMtSelections, fTopData.getWMass());
    fSplittedHistogramHandler.fillShapeHistogram(hCtrlWPtAfterMtSelections, fTopData.getWP4().pt());
    if (fFakeTauData.isEWKFakeTauLike() && fAnalysisType == kSignalAnalysis) {
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausTopMassAfterMtSelections, fTopData.getTopMass());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausTopPtAfterMtSelections, fTopData.getTopP4().pt());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausWMassAfterMtSelections, fTopData.getWMass());
      fSplittedHistogramHandler.fillShapeHistogram(hCtrlEWKFakeTausWPtAfterMtSelections, fTopData.getWP4().pt());
    }

    // MET oscillation
    if (bOptionEnableMETOscillationAnalysis) {
      fMETPhiOscillationCorrectionAfterAllSelections->analyze(iEvent, fVertexData.getNumberOfAllVertices(), fMETData);
      if (transverseMass < 80.0) {
        fMETPhiOscillationCorrectionEWKControlRegion->analyze(iEvent, fVertexData.getNumberOfAllVertices(), fMETData);
      }
    }
    //double myDeltaPhiTauMET = DeltaPhi::reconstruct(*(fTauData.getSelectedTau()), *(fMETData.getSelectedMET())) * 57.3; // converted to degrees
    if (fAnalysisType != kQCDNormalizationSystematicsSignalRegion && fAnalysisType != kQCDNormalizationSystematicsControlRegion) {
      fSplittedHistogramHandler.fillShapeHistogram(hShapeTransverseMass, transverseMass);
        if (fFakeTauData.isEWKFakeTauLike())
          fSplittedHistogramHandler.fillShapeHistogram(hShapeEWKFakeTausTransverseMass, transverseMass);
        if (fFakeTauData.isEmbeddingGenuineTauLikeWithMultipleTausInAcceptance())
          fSplittedHistogramHandler.fillShapeHistogram(hShapeEmbeddingLikeMultipleTausTransverseMass, transverseMass);
    }
  }

  void CommonPlots::fillControlPlotsAfterAllSelectionsWithProbabilisticBtag(const edm::Event& iEvent, double transverseMass) {
    if (fAnalysisType != kQCDNormalizationSystematicsSignalRegion && fAnalysisType != kQCDNormalizationSystematicsControlRegion) {
      fSplittedHistogramHandler.fillShapeHistogram(hShapeProbabilisticBtagTransverseMass, transverseMass);
      if (fFakeTauData.isEWKFakeTauLike())
        fSplittedHistogramHandler.fillShapeHistogram(hShapeProbabilisticBtagEWKFakeTausTransverseMass, transverseMass);
      if (fFakeTauData.isEmbeddingGenuineTauLikeWithMultipleTausInAcceptance())
        fSplittedHistogramHandler.fillShapeHistogram(hShapeProbabilisticBtagEmbeddingLikeMultipleTausTransverseMass, transverseMass);
    }
  }

  void CommonPlots::fillControlPlotsAfterAllSelectionsWithFullMass(const edm::Event& iEvent, FullHiggsMassCalculator::Data& data) {
    fFullHiggsMassData = data;
    if (fAnalysisType != kQCDNormalizationSystematicsSignalRegion && fAnalysisType != kQCDNormalizationSystematicsControlRegion) {
      fSplittedHistogramHandler.fillShapeHistogram(hShapeFullMass, data.getHiggsMass());
      if (fFakeTauData.isEWKFakeTauLike())
        fSplittedHistogramHandler.fillShapeHistogram(hShapeEWKFakeTausFullMass, data.getHiggsMass());
      if (fFakeTauData.isEmbeddingGenuineTauLikeWithMultipleTausInAcceptance())
        fSplittedHistogramHandler.fillShapeHistogram(hShapeEmbeddingLikeMultipleTausFullMass, data.getHiggsMass());
    }
  }

  void CommonPlots::fillAllControlPlots(const edm::Event& iEvent, double transverseMass) {
    fillControlPlotsAtJetSelection(iEvent, fJetData);
    fillControlPlotsAtCollinearDeltaPhiCuts(iEvent, fQCDTailKillerData);
    fillControlPlotsAtMETSelection(iEvent, fMETData);
    fillControlPlotsAtBtagging(iEvent, fBJetData);
    fillControlPlotsAtBackToBackDeltaPhiCuts(iEvent, fQCDTailKillerData);
    fillControlPlotsAtTopSelection(iEvent, fTopData);
    fillControlPlotsAtEvtTopology(iEvent, fEvtTopology);
    fillControlPlotsAfterAllSelections(iEvent, transverseMass);
    fillControlPlotsAfterAllSelectionsWithFullMass(iEvent, fFullHiggsMassData);
  }

}
