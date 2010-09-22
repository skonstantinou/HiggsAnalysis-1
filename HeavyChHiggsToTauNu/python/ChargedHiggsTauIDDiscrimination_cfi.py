import FWCore.ParameterSet.Config as cms
import copy

from RecoTauTag.RecoTau.PFRecoTauQualityCuts_cfi import *
hplusTrackQualityCuts = PFTauQualityCuts.clone()
hplusTrackQualityCuts.maxTrackChi2 = cms.double(10.)
hplusTrackQualityCuts.minTrackHits = cms.uint32(8)

from RecoTauTag.RecoTau.PFRecoTauDiscriminationByLeadingTrackFinding_cfi import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByLeadingTrackPtCut_cfi import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByCharge_cfi import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByECALIsolation_cfi import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationAgainstElectron_cfi import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationAgainstMuon_cfi import *
from HiggsAnalysis.HeavyChHiggsToTauNu.PFRecoTauDiscriminationByTauPolarization_cfi import *
from HiggsAnalysis.HeavyChHiggsToTauNu.PFRecoTauDiscriminationByDeltaE_cfi import *
from HiggsAnalysis.HeavyChHiggsToTauNu.PFRecoTauDiscriminationByInvMass_cfi import *
from HiggsAnalysis.HeavyChHiggsToTauNu.PFRecoTauDiscriminationByFlightPathSignificance_cfi import *
from HiggsAnalysis.HeavyChHiggsToTauNu.PFRecoTauDiscriminationByNProngs_cfi import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByTrackIsolation_cfi import *

def addDiscriminator(process, tau, name, module):
    module.PFTauProducer = cms.InputTag(tau+"Producer")
    process.__setattr__(tau+name, module)
    return module

def addDiscriminatorSequence(process, tau):
    lst = []
#    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationByLeadingTrackFinding", 
#                                pfRecoTauDiscriminationByLeadingTrackFinding.clone()))

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationByLeadingTrackPtCut",
                                pfRecoTauDiscriminationByLeadingTrackPtCut.clone(
                                   MinPtLeadingObject = cms.double(20.0),
                                   qualityCuts = hplusTrackQualityCuts
                                   )))

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationByCharge", 
                                pfRecoTauDiscriminationByCharge.clone()))

    # index -1 points to the last element in the list
    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationByECALIsolation", 
                                pfRecoTauDiscriminationByECALIsolation.clone()))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationAgainstElectron",
                                pfRecoTauDiscriminationAgainstElectron.clone()))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationAgainstMuon",
                                pfRecoTauDiscriminationAgainstMuon.clone()))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationByTauPolarization",
                                pfRecoTauDiscriminationByTauPolarization.clone()))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationByDeltaE",
                                pfRecoTauDiscriminationByDeltaE.clone()))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')
    
    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationByInvMass",
                                pfRecoTauDiscriminationByInvMass.clone()))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationByFlightPathSignificance",
                                pfRecoTauDiscriminationByFlightPathSignificance.clone()))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationBy1Prong",
                                pfRecoTauDiscriminationByNProngs.clone(
                                  nProngs = cms.uint32(1)
                                  )))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationBy3Prongs",
                                pfRecoTauDiscriminationByNProngs.clone(
                                  nProngs = cms.uint32(3)
                                  )))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationBy3ProngCombined",
                                pfRecoTauDiscriminationByNProngs.clone(
                                  nProngs = cms.uint32(3),
                                  Prediscriminants = cms.PSet(
	                               BooleanOperator = cms.string("and"),
	                               leadTrack = cms.PSet(
	                                   Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding'),
	                                   cut = cms.double(0.5)
	                               ),
	                               deltaE = cms.PSet(
	                                   Producer = cms.InputTag(tau+'HplusTauDiscriminationByDeltaE'),
	                                   cut = cms.double(0.5)
	                               ),
	                               invMass = cms.PSet(
	                                   Producer = cms.InputTag(tau+'HplusTauDiscriminationByInvMass'),
	                                   cut = cms.double(0.5)
	                               ),
	                               flightPathSig = cms.PSet(
	                                   Producer = cms.InputTag(tau+'HplusTauDiscriminationByFlightPathSignificance'),
	                                   cut = cms.double(0.5)
	                               )
	                          )
                                )))
    lst[-1].Prediscriminants.leadTrack.Producer = cms.InputTag(tau+'DiscriminationByLeadingTrackFinding')

    lst.append(addDiscriminator(process, tau, "HplusTauDiscriminationBy1or3Prongs",
                                pfRecoTauDiscriminationByLeadingTrackFinding.clone(
	 			    Prediscriminants = cms.PSet(
	 			        BooleanOperator = cms.string("or"),
	 			        oneProng = cms.PSet(
	 			            Producer = cms.InputTag(tau+'HplusTauDiscriminationBy1Prong'),
	 			            cut = cms.double(0.5)
	 			        ),
	 			        threeProng = cms.PSet(
	 			            Producer = cms.InputTag(tau+'HplusTauDiscriminationBy3ProngCombined'),
	 			            cut = cms.double(0.5)
	 			        )
	 			    )
	 			)))
    lst.append(addDiscriminator(process, tau, "HplusTauDiscrimination",
       			        pfRecoTauDiscriminationByTrackIsolation.clone(
	                             Prediscriminants = cms.PSet(
	 			        BooleanOperator = cms.string("and"),
	 			        leadingTrack = cms.PSet(
	 			            Producer = cms.InputTag(tau+'HplusTauDiscriminationByLeadingTrackPtCut'),
	 			            cut = cms.double(0.5)
	 			        ),
	 			        charge = cms.PSet(
	 			            Producer = cms.InputTag(tau+'HplusTauDiscriminationByCharge'),
	 			            cut = cms.double(0.5)
	 			        ),
	 			        ecalIsolation = cms.PSet(
	 			            Producer = cms.InputTag(tau+'HplusTauDiscriminationByECALIsolation'),
	 			            cut = cms.double(0.5)
	 			        ),
	 			        electronVeto = cms.PSet(
	 			            Producer = cms.InputTag(tau+'HplusTauDiscriminationAgainstElectron'),
	 			            cut = cms.double(0.5)
	 			        ),
	 			        polarization = cms.PSet(
	 			            Producer = cms.InputTag(tau+'HplusTauDiscriminationByTauPolarization'),
	 			            cut = cms.double(0.5)
	 			        ),
	 			        prongs = cms.PSet(
	 			            Producer = cms.InputTag(tau+'HplusTauDiscriminationBy1or3Prongs'),
	 			            cut = cms.double(0.5)
	 			        )
	 			    )
	 			)))

    sequence = cms.Sequence()
    for m in lst:
        sequence *= m

    process.__setattr__(tau+"HplusDiscriminationSequence", sequence)
    return sequence

def addHplusTauDiscriminationSequence(process):
    process.hplusTauDiscriminationSequence = cms.Sequence(
        addDiscriminatorSequence(process, "fixedConePFTau") *
	addDiscriminatorSequence(process, "fixedConeHighEffPFTau") *
        addDiscriminatorSequence(process, "shrinkingConePFTau") 
#	addDiscriminatorSequence(process, "caloTau")
    )

    return process.hplusTauDiscriminationSequence
