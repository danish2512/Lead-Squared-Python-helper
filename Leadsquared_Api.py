import logging
import json
import requests


class Leadsquared_Api:
    name = None
    accessKey = None
    secretKey = None

    def __init__(self, **data):
        if 'LSQ_NAME' in data:
            self.name = data['LSQ_NAME']

        if 'LSQ_ACCESSKEY' in data:
            self.accessKey = data['LSQ_ACCESSKEY']

        if 'LSQ_SECRETKEY' in data:
            self.secretKey = data['LSQ_SECRETKEY']

    def lsqcurl(self, url, data, name):
        result = requests.post(url, data=json.dumps(data))
        logging.info(result.request)
        response = json.loads(result.text)
        logging.info(response)
        return response

    def lsqcurlget(self, url, name):
        result = requests.get(url)
        logging.info(result.request)
        response = json.loads(result.text)
        logging.info(response)
        return response

    def create_lead(self, **data):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Lead.Create?accessKey=' + self.accessKey + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url, data = json.dumps(lead_details), name=name)

    def get_lead_by_email(self, email):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Leads.GetByEmailaddress?accessKey=' + self.accessKey + '&secretKey=' + self.secretKey + '&emailaddress=' + email
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def update_lead(self, leadId, **data):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Lead.Update?accessKey='+ self.accessKey + '&secretKey='+ self.secretKey + '&leadId='+ leadId
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def create_update_lead(self, **data):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Lead.CreateOrUpdate?postUpdatedLead=false&accessKey=' +  self.accessKey + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def convert_visitor(self, leadId, **data):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Lead.Convert?accessKey=' + self.accessKey + '&secretKey=' + self.secretKey + '&leadId=' + leadId + '&postUpdatedLead=true'
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def get_meta_data(self):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/LeadsMetaData.Get?accessKey=' + self.accessKey + '&secretKey=' + self.secretKey
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def get_lead_by_id(self, id):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Leads.GetById?accessKey='+ self.accessKey +\
              '&secretKey='+ self.secretKey + '&id=' + id
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def send_schedule_email(self, **data):
        url_base = 'https://api.leadsquared.com/v2/EmailMarketing.svc'
        url = url_base + '/ScheduleEmailToLead?accessKey=' + self.accessKey\
              + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def send_email(self, **data):
        url_base = 'https://api.leadsquared.com/v2/EmailMarketing.svc'
        url = url_base + '/SendMail?accessKey=' + self.accessKey \
              + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def quick_search(self, key):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Leads.GetByQuickSearch?accessKey=' + self.accessKey \
              + '&secretKey=' + self.secretKey + '&key=' + key
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def search_by_criteria(self, **data):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Leads.Get?accessKey=' + self.accessKey \
              + '&secretKey='+ self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def get_activity_types(self):
        url_base = 'https://api.leadsquared.com/v2/ProspectActivity.svc'
        url = url_base + '/ActivityTypes.Get?accessKey=' \
              + self.accessKey + '&secretKey=' + self.secretKey
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def post_activity(self, **data):
        url_base = 'https://api.leadsquared.com/v2/ProspectActivity.svc'
        url = url_base + '/Create?accessKey=' + self.accessKey \
              + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def create_activity_type(self, **data):
        url_base = 'https://api.leadsquared.com/v2/ProspectActivity.svc'
        url = url_base + '/CreateType?accessKey=' + \
              self.accessKey + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def get_activities_of_lead(self, leadId, **data):
        url_base = 'https://api.leadsquared.com/v2/ProspectActivity.svc'
        url = url_base + '/Retrieve?accessKey=' + self.accessKey + \
              '&secretKey=' + self.secretKey + '&leadId=' + self.leadId
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def create_product(self, **data):
        url_base = 'https://api.leadsquared.com/v2/SalesActivity.svc'
        url = url_base + '/CreateProduct?accessKey=' +\
              self.accessKey + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def update_product(self, **data):
        url_base = 'https://api.leadsquared.com/v2/SalesActivity.svc'
        url = url_base + '/UpdateProduct?accessKey='+ self.accessKey\
              + '&secretKey='+ self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def retrieve_products(self, **data):
        url_base = 'https://api.leadsquared.com/v2/SalesActivity.svc'
        url = url_base + '/RetrieveProducts?accessKey=' + \
              self.accessKey + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def add_sales_activity(self, **data):
        url_base = 'https://api.leadsquared.com/v2/SalesActivity.svc'
        url = url_base + '/Create?accessKey=' + self.accessKey \
              + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def update_sales_activity(self, **data):
        url_base = 'https://api.leadsquared.com/v2/SalesActivity.svc'
        url = url_base + '/Update?accessKey=' + self.accessKey + '&secretKey=' + self.secretKey
        lead_details = []
        for key, value in data.items():
            lead_details.append({
                'Attribute': key,
                'Value': value
            })
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def delete_product(self, product_id):
        url_base = 'https://api.leadsquared.com/v2/SalesActivity.svc'
        url = url_base + '/DeleteProduct?accessKey=' + self.accessKey \
              + '&secretKey=' + self.secretKey + '&id=' + product_id
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def retrieve_sales_activity(self, activity_id):
        url_base = 'https://api.leadsquared.com/v2/SalesActivity.svc'
        url = url_base + '/RetrieveActivity?accessKey=' +\
              self.accessKey + '&secretKey=' + self.secretKey + '&activityId=' + activity_id
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def sales_activity_settings(self):
        url_base = 'https://api.leadsquared.com/v2/SalesActivity.svc'
        url = url_base + '/RetrieveSetting?accessKey=' + \
              self.accessKey + '&secretKey=' + self.secretKey
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def get_lists(self):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Lists.Get?accessKey=' + self.accessKey +\
              '&secretKey=' + self.secretKey
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def leads_in_lists(self, listId):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/Lists.Get?accessKey=' + self.accessKey +\
              '&secretKey='+ self.secretKey + '&listId=' + listId
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def count_in_lists(self, listId):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/List/Retrieve/MemberCount?accessKey=' + \
              self.accessKey + '&secretKey=' + self.secretKey + '&listId=' + listId
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def check_lead_in_lists(self, listId, leadId):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/List.CheckLead?accessKey=' + self.accessKey + \
              '&secretKey=' + self.secretKey + '&listId=' + listId + '&leadId=' + leadId
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def add_lead_to_static_list(self, listId, leadId):
        url_base = 'https://api.leadsquared.com/v2/LeadManagement.svc'
        url = url_base + '/AddLeadToStaticList?accessKey=' + self.accessKey + \
              '&secretKey=' + self.secretKey + '&listId=' + listId + '&leadId=' + leadId
        lead_details = []
        name = self.name
        return self.lsqcurl(url=url,data = json.dumps(lead_details), name=name)

    def get_users(self):
        url_base = 'https://api.leadsquared.com/v2/UserManagement.svc'
        url = url_base + '/Users.Get?accessKey=' + self.accessKey +\
              '&secretKey=' + self.secretKey
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def get_user_by_id(self, UserId):
        url_base = 'https://api.leadsquared.com/v2/UserManagement.svc'
        url = url_base + '/User/Retrieve/ByUserId?accessKey=' + \
              self.accessKey + '&secretKey=' + self.secretKey + '&UserId=' + UserId
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def get_user_by_email(self, email):
        url_base = 'https://api.leadsquared.com/v2/UserManagement.svc'
        url = url_base + '/User/Retrieve/ByEmailAddress?accessKey=' + \
              self.accessKey + '&secretKey=' + self.secretKey + '&emailAddress=' + email
        name = self.name
        return self.lsqcurlget(url=url, name=name)

    def user_authentication(self, akey, skey):
        url_base = 'https://api.leadsquared.com/v2/UserManagement.svc'
        url = url_base + '/User/Retrieve/ByEmailAddress?accessKey=' +\
              akey + '&secretKey=' + skey
        name = self.name
        return self.lsqcurlget(url=url, name=name)

