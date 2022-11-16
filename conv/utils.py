import xml.etree.ElementTree as ET
class TreeData:
    def __init__(self):
        self.sttlementDate = ""
        self.transactionDate = ""
        self.bin_ = ""
        self.cardNumber= ""
        self.RRN= ""
        self.ARN= ""
        self.DRN= ""
        self.SRN= ""
        self.AuthCode= ""
        self.SourceAccount= ""
        self.BeneficiaryAccount= ""
        self.MCC= ""
        self.RequestCategory= ""
        self.MsgCode= ""
        self.TransType= ""
        self.TransCurrency= ""
        self.TransAmount= ""
        self.MerchantName= ""
        self.MerchantID= ""
        self.OrigContractNumber= ""
        self.OrigMemberId= ""
        self.PhaseDate= ""
        self.ReconCurrency= ""
        self.ReconAmount= ""


def xmlsplitter(file):
    tree =ET.parse(file)
    root = tree.getroot()
    ssttlementDate = root.find('./FileHeader/CreationDate').text
    sbin_ =  root.find('./FileHeader/Receiver').text
    doclist =root.findall('./DocList/Doc')
    
    outList =[]

    for doc in doclist:
        singleinfo = TreeData()
        singleinfo.sttlementDate =ssttlementDate
        singleinfo.bin_ =sbin_
        singleinfo.transactionDate = doc.find('./LocalDt').text
        singleinfo.cardNumber =doc.find('./Destination/ContractNumber').text
        singleinfo.OrigContractNumber = doc.find('./Originator/ContractNumber').text
        singleinfo.OrigMemberId = doc.find('./Originator/MemberId').text
        
        singleinfo.ReconCurrency = doc.find('./Reconciliation/Currency').text
        singleinfo.ReconAmount = doc.find('./Reconciliation/Amount').text

        
        
        singleinfo.TransCurrency = doc.find('./Transaction/Currency').text
        singleinfo.TransAmount = doc.find('./Transaction/Amount').text
        trxn = doc.findall('./Transaction/Extra/AddData/Parm')
        
        for ref in trxn:
            
            if(ref.find('./ParmCode').text=='CPID'):
                singleinfo.SourceAccount= ref.find('./Value').text


            if(ref.find('./ParmCode').text=='SRVC'):
                singleinfo.BeneficiaryAccount=ref.find('./Value').text
        # OrigMemberId = doc.find('./Transaction/...').text
        
        
        
        # OrigMemberId = doc.find('./SourceDtls/...').text
        singleinfo.MCC  = doc.find('./SourceDtls/SIC').text
        singleinfo.MerchantName = doc.find('./SourceDtls/MerchantName').text
        singleinfo.MerchantID = doc.find('./SourceDtls/MerchantID').text
        
        PhaseDateFILE = doc.find('./Billing/PhaseDate')

        if(PhaseDateFILE):
            singleinfo.PhaseDate =PhaseDateFILE.text
        singleinfo.PhaseDate=""

        # print(PhaseDate)

        singleinfo.RequestCategory=doc.find('./TransType/TransCode/RequestCategory').text

        MsgCodeFILE=doc.find('./TransType/TransCode/MsgCode')
        
        # singleinfo.MsgCode =""
        if(MsgCodeFILE!=None):
            print(MsgCodeFILE.text)
            singleinfo.MsgCode = MsgCodeFILE.text



        singleinfo.TransType=doc.find('./TransType/TransCode/TransTypeCode').text
        '''
        doc/DocRefSet/parm

        '''
        singleinfo.RRN =""
        singleinfo.ARN =""
        singleinfo.DRN =""
        singleinfo.SRN =""
        singleinfo.AuthCode=""
        # singleinfo.SourceAccount=""
        # singleinfo.BeneficiaryAccount=""

        docrefset = doc.findall('./DocRefSet/Parm')
        for docref in docrefset:

            if(docref.find('./ParmCode').text=='RRN'):
                singleinfo.RRN=docref.find('./Value').text
                
            if(docref.find('./ParmCode').text=='ARN'):
                singleinfo.ARN=docref.find('./Value').text

            if(docref.find('./ParmCode').text=='DRN'):
                singleinfo.DRN= docref.find('./Value').text

            if(docref.find('./ParmCode').text=='SRN'):
                singleinfo.SRN= docref.find('./Value').text


            if(docref.find('./ParmCode').text=='AuthCode'):
                singleinfo.AuthCode =docref.find('./Value').text


            # if(docref.find('./ParmCode').text=='CPID'):
            #     singleinfo.SourceAccount= docref.find('./Value').text

            # if(docref.find('./ParmCode').text=='SRVC'):
            #     singleinfo.BeneficiaryAccount=docref.find('./Value').text
        outList.append(singleinfo)
    return outList

        
