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
    "embedding_dict": {},
    "text_id_to_ref_doc_id": {},
    "metadata_dict": {}
}

# Loop through each folder
for folder in folders:
    file_path = os.path.join(folder, 'image__vector_store.json')
    
    # Load the contents of the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Merge the embedding_dict
    merged_data['embedding_dict'] = {**merged_data['embedding_dict'], **data['embedding_dict']}
    
    # Merge the text_id_to_ref_doc_id
    merged_data['text_id_to_ref_doc_id'] = {**merged_data['text_id_to_ref_doc_id'], **data['text_id_to_ref_doc_id']}
    
    # Merge the metadata_dict
    merged_data['metadata_dict'] = {**merged_data['metadata_dict'], **data['metadata_dict']}

# Write the merged data to a new JSON file
with open('home_service/image_vector_store.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)
