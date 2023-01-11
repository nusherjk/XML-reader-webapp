from django.shortcuts import render
import utils

import csv
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method== 'GET':
        return render(request, 'upload.html')
    if request.method == 'POST':
        f = request.FILES['xmlfile']
        data =utils.xmlsplitter(f)
        # writer = csv.writer(response)
        # writer.writerow([
        #             "Settlement Date",
        #             "Transaction Date",
        #             "BIN",
        #             "Card Number",
        #             "RRN",
        #             "ARN",
        #             "DRN",
        #             "SRN",
        #             "Auth Code",
        #             "Source Account",
        #             "Beneficiary Account",
        #             "MCC",
        #             "Request Category",
        #             "Msg Code",
        #             "Trans Type",
        #             "Trans Currency",
        #             "Trans Amount",
        #             "Merchant Name",
        #             "Merchant ID",
        #             "Original Contract Number",
        #             "Original Member Id",
        #             "Phase Date",
        #             "Reconciliation Currency",
        #             "Reconciliation Amount",])
        
        
        # for dat in data:
        #     writer.writerow([x for x in dat])

        return render(request, 'upload.html', context={'treeData': data})
    

def downloadlink(request, data):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow([
                "Settlement Date",
                "Transaction Date",
                "BIN",
                "Card Number",
                "RRN",
                "ARN",
                "DRN",
                "SRN",
                "Auth Code",
                "Source Account",
                "Beneficiary Account",
                "MCC",
                "Request Category",
                "Msg Code",
                "Trans Type",
                "Trans Currency",
                "Trans Amount",
                "Merchant Name",
                "Merchant ID",
                "Original Contract Number",
                "Original Member Id",
                "Phase Date",
                "Reconciliation Currency",
                "Reconciliation Amount",])
    
    for dat in data:
        writer.writerow([x for x in dat])

    return response