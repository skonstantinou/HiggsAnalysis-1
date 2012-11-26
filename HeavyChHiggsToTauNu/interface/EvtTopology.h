//#######################################################################
// -*- C++ -*-
//       File Name:  EvtTopology.h
// Original Author:  Alexandros Attikis
//         Created:  Mon 4 Oct 2010
//     Description:  Designed to calculate Evt Topology related variables                   
//       Institute:  UCY
//         e-mail :  attikis@cern.ch
//        Comments:  
//#######################################################################
#ifndef HiggsAnalysis_HeavyChHiggsToTauNu_EvtTopology_h
#define HiggsAnalysis_HeavyChHiggsToTauNu_EvtTopology_h
// ROOT libraries
#include <Math/Vector3D.h>
#include <Math/Point3D.h>
#include <TVector3.h>
#include <TLorentzVector.h>
// C++ libraries
#include <functional>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <iostream>
#include <vector>
// CMSSW libraries
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/BaseSelection.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Ptr.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/EventCounter.h"
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/JetSelection.h"
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/MathFunctions.h"

namespace reco {
  class Candidate;
}

namespace edm {
  class ParameterSet;
}

namespace HPlus {
  class HistoWrapper;
  class WrappedTH1;

  class EvtTopology: public BaseSelection {
  public:
    typedef struct {
      float fAlphaT;
      float fJt; // Jt = Ht - TauJetEt - LdgJetEt
      float fHt;
      float fDeltaHt;
      float fMHt;
      vector<float> vDiJetMassesNoTau;
    } AlphaStruc;

    /**
     * Class to encapsulate the access to the data members of
     * TauSelection. If you want to add a new accessor, add it here
     * and keep all the data of TauSelection private.
     */
    class Data {
    public:
      // The reason for pointer instead of reference is that const
      // reference allows temporaries, while const pointer does not.
      // Here the object pointed-to must live longer than this object.
      Data(const EvtTopology *evtTopology, bool passedEvent);
      ~Data();

      bool passedEvent() const { return fPassedEvent; }
      const EvtTopology::AlphaStruc alphaT() const { return fEvtTopology->sAlpha; }
    
    private:
      const EvtTopology *fEvtTopology;
      const bool fPassedEvent;
    };

    EvtTopology(const edm::ParameterSet& iConfig, EventCounter& eventCounter, HistoWrapper& histoWrapper);
    ~EvtTopology();

    // Use silentAnalyze if you do not want to fill histograms or increment counters
    Data silentAnalyze(const edm::Event& iEvent, const edm::EventSetup& iSetup, const reco::Candidate& tau, const edm::PtrVector<pat::Jet>& jets);
    Data analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup, const reco::Candidate& tau, const edm::PtrVector<pat::Jet>& jets);
    // Data InvMassVetoOnJets( const edm::PtrVector<pat::Jet>& jets); obsolete

  private:
    Data privateAnalyze(const edm::Event& iEvent, const edm::EventSetup& iSetup, const reco::Candidate& tau, const edm::PtrVector<pat::Jet>& jets);
    // Input parameters
    // std::string fDiscriminator;
    // double fDiscrCut;
    const double fAlphaTCut;

    // Counters
    Count fEvtTopologyCount;
    Count fAlphaTCutCount;

    // Histograms
    WrappedTH1 *hAlphaT;
    /*
      WrappedTH1 *hDiJetInvMass;
      WrappedTH1 *hDiJetInvMassCutFail;
      WrappedTH1 *hDiJetInvMassCutPass;
      WrappedTH1 *hDiJetInvMassWCutFail;
    */
    
    // Other variables
    AlphaStruc sAlpha;
    MathFunctions oMath;
  };
}

#endif
