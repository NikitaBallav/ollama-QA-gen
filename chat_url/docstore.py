import os
import json

# List of folders
folders = ['awards_index', 'centralised-aadhaar-vault_index', 'command-and-control-centre_index',
          'data-centre_index', 'directory_index', 'District_index',
          'district-website_index', 'domain-registration_index', 'eforms_index',
          'events_index', 'helpdisk_index', 'Home_index',
          'igod_index', 'infrastructure_index', 'lans_index',
          'messaging_index', 'national-cloud_index', 'news_index',
          'nicnet_index', 'nkn_index', 'organization-structure_index',
          'profile_index', 'remote-sensing_index', 'RTI_index',
          'security_index', 'Services_index', 'vedio-conferencing_index',
          'webcast_index']


# Initialize merged data
merged_data = {
    "docstore/metadata": {},
    "docstore/data": {},
    "docstore/ref_doc_info": {}
}

# Loop through each folder
for folder in folders:
    file_path = os.path.join(folder, 'docstore.json')
    
    # Load the contents of the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Merge the docstore/metadata
    merged_data['docstore/metadata'] = {**merged_data['docstore/metadata'], **data['docstore/metadata']}
    
    # Merge the docstore/data
    merged_data['docstore/data'] = {**merged_data['docstore/data'], **data['docstore/data']}
    
    # Merge the docstore/ref_doc_info
    merged_data['docstore/ref_doc_info'] = {**merged_data['docstore/ref_doc_info'], **data['docstore/ref_doc_info']}

# Create the merged JSON data
merged_data_final = {
    "docstore/metadata": merged_data['docstore/metadata'],
    "docstore/data": merged_data['docstore/data'],
    "docstore/ref_doc_info": merged_data['docstore/ref_doc_info']
}

# Write the merged data to a new JSON file
with open('home_service/docstore.json', 'w') as merged_file:
    json.dump(merged_data_final, merged_file, indent=4)
