import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input =  
cms.untracked.int32(2000) )

process.source = cms.Source("PoolSource",
                              fileNames = cms.untracked.vstring(


#Run 68958
#           'file:/data/TriggerStudies/0012A63D-81A9-DD11-8B82-000423D99660.root'
    'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/0012A63D-81A9-DD11-8B82-000423D99660.root'
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/0012A63D-81A9-DD11-8B82-000423D99660.root',
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/0019C32E-0DA9-DD11-8B57-001617DBCF6A.root',
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/00627A66-3EA9-DD11-8B8E-000423D9970C.root',
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/00CFAFE8-0AA9-DD11-9F68-001D09F28EC1.root',
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/020D2001-6FA9-DD11-97CD-000423D98BC4.root',
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/021D2E3E-0AA9-DD11-B45B-001D09F29169.root',
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/023642A3-68A9-DD11-AB48-000423D98BE8.root',
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/024ADBC7-7DA9-DD11-8881-001617E30CE8.root',
#         'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/068/958/0299FA29-0DA9-DD11-BA37-001617C3B5E4.root'


#Run 66692
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/0205EAD9-909C-DD11-90C9-000423D985B0.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/0C71A004-8F9C-DD11-AE7C-000423D98B28.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/1A41E121-8F9C-DD11-BF76-001617C3B6CC.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/20248577-939C-DD11-9CE5-001617E30D00.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/2EA03040-909C-DD11-ABDD-000423D6AF24.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/3AD553B1-929C-DD11-B8B0-000423D98E6C.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/3C4DC76F-919C-DD11-BD12-001617DBCF6A.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/48A05B2E-949C-DD11-BBE2-000423D33970.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/7C0022DC-959C-DD11-AAD4-000423D94908.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/860EC1EF-989C-DD11-9DA1-000423D9939C.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/9283D82A-939C-DD11-B476-000423D6CA72.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/ACB4A5E5-8D9C-DD11-9A37-000423D99394.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/B2FDD097-939C-DD11-ABD0-000423D9870C.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/BAF25EA4-929C-DD11-80CE-000423D9863C.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/BE2D445F-909C-DD11-BE93-000423D99A8E.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/C06493F4-909C-DD11-A8EF-000423D6CAF2.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/C2D67ADA-909C-DD11-920F-000423DD2F34.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/CA09D1E5-949C-DD11-89D0-001617E30F56.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/DAABD9C1-8F9C-DD11-BC9E-000423D6A6F4.root',
#'rfio:/castor/cern.ch/cms/store/data/Commissioning08/Calo/RECO/v1/000/066/692/E465456D-919C-DD11-B554-000423D98844.root'




             )
                             )

#process.load("L1TriggerOffline/L1Analyzer/L1NonIsoEmRecoAnalysis_cff")
process.load("L1TriggerOffline/L1Analyzer/L1CenJetRecoAnalysis_cff")
process.load("L1TriggerOffline/L1Analyzer/L1ForJetRecoAnalysis_cff")
process.load("L1TriggerOffline/L1Analyzer/L1TauJetRecoAnalysis_cff")
process.load("L1TriggerOffline/L1Analyzer/L1MuonRecoAnalysis_cff")

#process.demo = cms.Path(process.L1NonIsoEmRecoAnalysis)
process.demo = cms.Path(process.L1CenJetRecoAnalysis+process.L1ForJetRecoAnalysis+process.L1TauJetRecoAnalysis+process.L1MuonRecoAnalysis)

