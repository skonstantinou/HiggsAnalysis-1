#include "HiggsAnalysis/HPlusRootFileDumper/interface/HPlusJetSelection.h"

#include <iostream>
#include <string>
#include <vector>

#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/EgammaCandidates/interface/ElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/Electron.h"

#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "DataFormats/Common/interface/Handle.h"
#include <vector>
#include <algorithm>

namespace HPlusAnalysis {
  
  HPlusJetSelection::HPlusJetSelection(const edm::ParameterSet& iConfig) : 
    HPlusAnalysis::HPlusAnalysisBase("JetSelection"),
    HPlusAnalysis::HPlusSelectionBase(iConfig) {
    // Parse the list of triggers in the config file
    if (iConfig.exists("JetCollectionName")) {
      fJetCollectionName = iConfig.getParameter<edm::InputTag>("JetCollectionName");
    } else {
      throw cms::Exception("Configuration") << "JetSelection: InputTag 'JetCollectionName' is missing in config!" << std::endl;
    }
    if (iConfig.exists("CutMinNJets")) {
      fCutMinNJets = iConfig.getParameter<double>("CutMinNJets");
    } else {
      throw cms::Exception("Configuration") << "JetSelection: int value 'CutMinNJets' is missing in config!" << std::endl;
    }
    if (iConfig.exists("CutMinJetEt")) {
      fCutMinJetEt = iConfig.getParameter<double>("CutMinJetEt");
    } else {
      throw cms::Exception("Configuration") << "JetSelection: double value 'CutMinJetEt' is missing in config!" << std::endl;
    }
    if (iConfig.exists("CutMaxAbsJetEta")) {
      fCutMaxAbsJetEta = iConfig.getParameter<double>("CutMaxAbsJetEta");
    } else {
      throw cms::Exception("Configuration") << "JetSelection: double value 'CutMaxAbsJetEta' is missing in config!" << std::endl;
    }
    if (iConfig.exists("CutMaxEMFraction")) {
      fCutMaxEMFraction = iConfig.getParameter<double>("CutMaxEMFraction");
    } else {
      throw cms::Exception("Configuration") << "JetSelection: double value 'CutMaxEMFraction' is missing in config!" << std::endl;
    }
    
    // Initialize counters
    fCounterJetsPriorSelection = fCounter->addCounter("All Jets");
    fCounterJetsPostSelection  = fCounter->addCounter("Selected Jets");
    fCounterJetCollectionHandleEmpty = fCounter->addCounter("Empty Jet Handle");
    fCounterError = fCounter->addCounter("Random Errors");

    std::string alias;
    // Declare produced items (class-specific):  Max Jet Et 
    produces<float>(alias = "JetSelectionMaxJetEt").setBranchAlias(alias);
  
  } //eof: HPlusAnalysis::HPlusSelectionBase(iConfig) {

  HPlusJetSelection::~HPlusJetSelection() {}
  

  void HPlusJetSelection::beginJob() {
    // Set histograms
    if (isHistogrammed()) {
      
      // myHisto =  fs->make<TH1D>(tName, tName, nBins, min, max ); // (const char*, const char*, Int_t, Float_t, Float_t)
      hLdgJetEt = fFileService->make<TH1F>("LdgJetEt", "LdgJet  E_{T}",  200, 0.0, 200.);// LdgJet Et 
      hSecondLdgJetEt = fFileService->make<TH1F>("SecondLdgJetEt", "2nd LdgJet  E_{T}",  100, 0., 200.);
      hThirdLdgJetEt = fFileService->make<TH1F>("ThirdLdgJetEt", "3rd LdgJet  E_{T}",  100, 0., 200.);
      hFourthLdgJetEt = fFileService->make<TH1F>("FourthLdgJetEt", "4th LdgJet  E_{T}",  100, 0., 200.);
      // hFifthLdgJetEt = fFileService->make<TH1F>("FifthLdgJetEt", "5th LdgJet  E_{T}",  100, 0., 200.);
      //
      hLdgJetEta = fFileService->make<TH1F>("LdgJetEta", "LdgJet  E_{T}",  30, -3., 3.);// LdgJet Eta
      hSecondLdgJetEta = fFileService->make<TH1F>("SecondLdgJetEta", "2nd LdgJet  E_{T}",  30, -3., 3.);
      hThirdLdgJetEta = fFileService->make<TH1F>("ThirdLdgJetEta", "3rd LdgJet  E_{T}",  30, -3., 3.);
      hFourthLdgJetEta = fFileService->make<TH1F>("FourthLdgJetEta", "4th LdgJet  E_{T}",  30, -3., 3.);
      // hFifthLdgJetEta = fFileService->make<TH1F>("FifthLdgJetEta", "5th LdgJet  E_{T}",  30, -3., 3.);
    }
  }
  
  void HPlusJetSelection::endJob() {
    
  }
  
  bool HPlusJetSelection::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {

    // std::cout << "(fJetCollectionName.label()).compare(\"ak5CaloJets\") = " << (fJetCollectionName.label()).compare("ak5CaloJets")  << std:: endl;
    // std::cout << "(fJetCollectionName.label()).compare(\"JetPlusTrackZSPCorJetAntiKt5\") = " << (fJetCollectionName.label()).compare("JetPlusTrackZSPCorJetAntiKt5")  << std:: endl;
    
    // According to the JetCollectionName decide the class of jets to be used!
    //     if( (fJetCollectionName.label()).compare("ak5CaloJets") == 0){ myJetClass = "reco::CaloJet"; }
    //     else if(fJetCollectionName.label().compare("JetPlusTrackZSPCorJetAntiKt5") == 0){ myJetClass = "reco::JPTJet";}
    //     else{std::cout << "ERROR: No such class exists!!! Please select either \"ak5CaloJets\" or \"JetPlusTrackZSPCorJetAntiKt5\""<< std::endl;}
    
    bool decision = false; // filter decision true iff at least NJets survive the selection criteria.

    // ************************************************************************************************
    // FIXME
//     std::auto_ptr<float> myLdgJetEt(new float); // highest pt of jet that has passed all criteria
//     std::auto_ptr<float> mySecondLdgJetEt(new float); // Et of ldg jet
//     std::auto_ptr<float> myThirdLdgJetEt(new float); 
//     std::auto_ptr<float> myFourthdLdgJetEt(new float); 
//     std::auto_ptr<float> myFifthdLdgJetEt(new float); 
//     std::auto_ptr<float> mySecondLdgJetEta(new float); // Eta of ldg jet
//     std::auto_ptr<float> myThirdLdgJetEta(new float); 
//     std::auto_ptr<float> myFourthdLdgJetEta(new float); 
//     std::auto_ptr<float> myFifthdLdgJetEta(new float); 
    // ************************************************************************************************
    
    // Get JetCollection handle
    edm::Handle<reco::CaloJetCollection> myCaloJets;       // create an empty handle 
    iEvent.getByLabel(fJetCollectionName, myCaloJets);     // attach handle to JetCollection
    if (!myCaloJets->size()) {
      edm::LogInfo("HPlus") << "*** WARNING: Jet handle is empty! ***" << std::endl;
      fCounter->addCount(fCounterJetCollectionHandleEmpty);
    return decision;
    }
    const size_t myJetCount = myCaloJets->size();
    
    // Initialisation of variables (move to header)
    std::vector<reco::CaloJet> myUnsortedJets;
    std::vector<reco::CaloJet> mySortedJets;
    std::vector<reco::CaloJet> myFilteredJets;

    // Step 1) Store all jets in a vector
    // **********************************
    for (size_t i = 0; i < myJetCount; ++i) {
      const reco::CaloJet & myJet = (*myCaloJets)[i];
      myUnsortedJets.push_back(myJet);
      // Reference counter. Count total number of jets prior any selection in each Event.
      fCounter->addCount(fCounterJetsPriorSelection);
    }
    
    // Step 2) Order Jets according to Jet Energy
    // ******************************************
    const size_t myUnsortedJetsSize = myUnsortedJets.size();
    // Call a function to take an unsorted caloJet vector and sort it according to caloJet-Energies
    if(myUnsortedJetsSize!=0){mySortedJets = sortCaloJets(myUnsortedJets, myUnsortedJetsSize);}
    const size_t mySortJetsSize = mySortedJets.size();
    
    // Step 3) Filter the now ordered Jets: Apply Jet Et, Eta and EMFraction Cuts
    // ************************************
    if(mySortJetsSize==myUnsortedJetsSize){ myFilteredJets = filterCaloJets(mySortedJets, mySortJetsSize); }
    else{
      edm::LogInfo("HPlus") << "Jet handle is empty!" << std::endl;
      fCounter->addCount(fCounterError);
    }

    // Step 4) Now analyze the filtered Jets
    // *************************************
    const size_t myFilteredJetsSize = myFilteredJets.size();
    if(myFilteredJetsSize!=0){
      // remember: if fCutMinNJets is NOT satisfied, then then "myFilteredJets" vector is returned empty!
      decision = true; 
      // Create a vector iterator for the filtered jets
      std::vector<reco::CaloJet>::const_iterator iFilteredJet;
      // Loop over all the filtered jets
      for(iFilteredJet =  myFilteredJets.begin(); iFilteredJet != myFilteredJets.end(); iFilteredJet++){
	// Count total number of jets prio any selection in each Event.
	fCounter->addCount(fCounterJetsPostSelection);
      }
    }
    else{ 
      //std::cout << "*** WARNING:  myFilteredJetsSize == 0 ***" << std::endl; 
    }

    // Step 5) Fill some validation histograms
    // ***************************************  
    if(myFilteredJets.size()!=0){

      hLdgJetEt->Fill(myFilteredJets.at(0).et()); // LdgJet Et
      hSecondLdgJetEt->Fill(myFilteredJets.at(1).et());
      hThirdLdgJetEt->Fill(myFilteredJets.at(2).et());
      hFourthLdgJetEt->Fill(myFilteredJets.at(3).et());
      // hFifthLdgJetEt->Fill(myFilteredJets.at(4).et());
      //
      hLdgJetEta->Fill(myFilteredJets.at(0).eta()); // LdgJet Et
      hSecondLdgJetEta->Fill(myFilteredJets.at(1).eta());
      hThirdLdgJetEta->Fill(myFilteredJets.at(2).eta());
      hFourthLdgJetEta->Fill(myFilteredJets.at(3).eta());
      // hFifthLdgJetEta->Fill(myFilteredJets.at(4).eta());
    }  else{
      hLdgJetEt->Fill(-1.0);
      hSecondLdgJetEt->Fill(-1.0);
      hThirdLdgJetEt->Fill(-1.0);
      hFourthLdgJetEt->Fill(-1.0);
      // hFifthLdgJetEt->Fill(-1.0);
      //
      hLdgJetEta->Fill(-1.0);
      hSecondLdgJetEta->Fill(-1.0);
      hThirdLdgJetEta->Fill(-1.0);
      hFourthLdgJetEta->Fill(-1.0);
      // hFifthLdgJetEta->Fill(-1.0);
    }
    
    return decision;
      
  }//eof:  HPlusJetSelection::analyze()
  
  std::vector<reco::CaloJet> HPlusJetSelection::sortCaloJets(std::vector<reco::CaloJet> caloJetsToSort, const size_t caloJetSize) {
    
    // Declare variables
    reco::CaloJet myTmpLdgJet;
    reco::CaloJet myTmpLdgJet_new;
    std::vector<reco::CaloJet> caloJetsSorted;
    std::vector<reco::CaloJet>::iterator myJet;
    
    // Store the "first" N jets [wrt energy). 
    for ( size_t i = 0; i < caloJetSize; i++) {
      for ( myJet = caloJetsToSort.begin(); myJet != caloJetsToSort.end(); ++myJet) {
	
	if( (*myJet).energy() > myTmpLdgJet.energy() ){
	  myTmpLdgJet = (*myJet);

	} else{}
      }
      // Store myJet as ith-LdgJet (descending order in Energy)
      caloJetsSorted.push_back(myTmpLdgJet);
      // Delete myJet from vector list
      caloJetsToSort = eraseVectorElement(caloJetsToSort, myTmpLdgJet);
      myTmpLdgJet = myTmpLdgJet_new;
    }//eof: for ( size_t i = 0; i < caloJetsToSort.size(); i++) {
    
    return caloJetsSorted;
    
  }//eof: HPlusJetSelection::sortCaloJets()

  std::vector<reco::CaloJet> HPlusJetSelection::filterCaloJets(std::vector<reco::CaloJet> caloJetsSorted, const size_t caloJetSize) {
    
    // Declare variables
    reco::CaloJet myJet;
    // std::vector<reco::CaloJet> caloJetsFilteredCands;
    std::vector<reco::CaloJet> caloJetsFiltered;
    std::vector<reco::CaloJet> caloJetsEmpty;
    std::vector<reco::CaloJet>::iterator it_caloJetsFilteredCands;
    std::vector<reco::CaloJet>::iterator it_caloJetsFiltered;
    bool passedNJets      = false;
    bool passedJetEt      = false;
    bool passedJetEta     = false;
    bool passedEMFraction = false;  
    bool jetSurvives = false;   
    
    if(caloJetSize >= fCutMinNJets){
      
      // Loop over sorted Jets and apply quality cuts
      for( it_caloJetsFilteredCands = caloJetsSorted.begin(); it_caloJetsFilteredCands != caloJetsSorted.end(); ++it_caloJetsFilteredCands) {
	passedJetEt      = false;
	passedJetEta     = false;
	passedEMFraction = false;
	if( (*it_caloJetsFilteredCands).energy() >= fCutMinJetEt){ passedJetEt = true;}
	if( fabs((*it_caloJetsFilteredCands).eta()) <= fCutMaxAbsJetEta){ passedJetEta = true;}
	if( (*it_caloJetsFilteredCands).emEnergyFraction() >= fCutMaxEMFraction ){ passedEMFraction = true;}
	
	// Boolean will be used to erase those jets that do not satisfy criteria
	jetSurvives = ( passedJetEt && passedJetEta && passedEMFraction) ;
	if(jetSurvives){ 
	  caloJetsFiltered.push_back(*it_caloJetsFilteredCands);
	} 
	else{ 
	  // std::cout << "Jet did not survive " << std::endl;  
	}
      }
    }
    
    // Last criterion: Is the number of jets enough? 
    double myFilteredJetsSize = caloJetsFiltered.size();
    if( myFilteredJetsSize >= fCutMinNJets  ){ passedNJets = true;}
    
    // If fCutMinNJets criterion is not satisfied, return an empty vector of caloJets!
    if(passedNJets){ 
      // do nothing 
    }
    else{
      // return an empty vector!
      caloJetsFiltered = caloJetsEmpty;      
    }
    
    return caloJetsFiltered;
    
  }//eof: HPlusJetSelection::filterCaloJets


  std::vector<reco::CaloJet> HPlusJetSelection::eraseVectorElement( std::vector<reco::CaloJet> myJetVector, reco::CaloJet test) {

    std::vector<reco::CaloJet>::iterator it;
    int counter = 0;
    //  bool success = false;

    for ( it = myJetVector.begin(); it!=myJetVector.end(); ++it) {

      if( (*it).energy() == test.energy() ){
	
	// std::cout << " Found match. Deleting vector with (*it).energy() = " << (*it).energy()  << std::endl;
	myJetVector.erase(myJetVector.begin()+counter);
	// success = true;
	break;
      } else{counter++;}
    }
    return myJetVector;
  }//eof: HPlusJetSelection::eraseVectorElement()
  
  DEFINE_FWK_MODULE(HPlusJetSelection); 
  
}//eof: namespace HPlusAnalysis {
