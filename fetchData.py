#Adapted from https://mushfiq.me/2014/06/02/python-script-to-download-google-spreadsheet/
#Run as python fetchData.py
import os
import sys
from getpass import getpass

import gdata.docs.service
import gdata.spreadsheet.service


'''
    get user information from the command line argument and 
    pass it to the download method
'''
def get_gdoc_information():
    #email = raw_input('Email address:')
    email = ""
    #password = getpass('Password:')
    password = ""

    #-----------------------------------------------------------
    #Google Sheet URL
    #https://docs.google.com/spreadsheets/d/1i0_UUkdoidqzm1u-tkLcUl7kKGRr9K8H6W5deAfHoa0/edit#gid=1867477683
    #From this, we can extract the google docid as:
    #1i0_UUkdoidqzm1u-tkLcUl7kKGRr9K8H6W5deAfHoa0#gid=1867477683
    #-----------------------------------------------------------

    #gdoc_id = raw_input('Google Doc Id:')
    gdoc_id = "1i0_UUkdoidqzm1u-tkLcUl7kKGRr9K8H6W5deAfHoa0#gid=1867477683"

    try:
        download(gdoc_id, email, password)
    except Exception, e:
        raise e
    
def download(gdoc_id, email, password, download_path=None, ):

    print "Downloading the CSV file with id %s" % gdoc_id

    gd_client = gdata.docs.service.DocsService()

    #auth using ClientLogin
    gs_client = gdata.spreadsheet.service.SpreadsheetsService()
    gs_client.ClientLogin(email, password)

    #getting the key(resource id and tab id from the ID)
    resource    = gdoc_id.split('#')[0]
    tab         = gdoc_id.split('#')[1].split('=')[1]
    resource_id = 'spreadsheet:'+resource

    if download_path is None:
        download_path = os.path.abspath(os.path.dirname(__file__))

    import time
    #file_name = os.path.join(download_path, '%s.csv' % (gdoc_id))
    timestamp = time.strftime("%m.%d.%Y") + "_" + time.strftime("%H_%M_%S")
    file_name = os.path.join(download_path, '%s%s.csv' % ("arrivalData_",timestamp))
    
    print 'Downloading spreadsheet to %s...' % file_name

    docs_token = gd_client.GetClientLoginToken()
    gd_client.SetClientLoginToken(gs_client.GetClientLoginToken())
    gd_client.Export(resource_id, file_name, gid=tab)
    gd_client.SetClientLoginToken(docs_token)

    print "Download Completed!"

    return file_name
    
if __name__=='__main__':
    get_gdoc_information()
