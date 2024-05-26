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
    "index_store/data": {
        "vector_index": {
            "__type__": "vector_store",
            "__data__": "{\"index_id\": \"vector_index\", \"summary\": null, \"nodes_dict\": {}, \"doc_id_dict\": {}, \"embeddings_dict\": {}}"
        }
    }
}

# Loop through each folder
for folder in folders:
    file_path = os.path.join(folder, 'index_store.json')
    
    # Load the contents of the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Merge the vector_index data
    vector_index_data = json.loads(merged_data['index_store/data']['vector_index']['__data__'])
    vector_index_data['nodes_dict'] = {**vector_index_data['nodes_dict'], **json.loads(data['index_store/data']['vector_index']['__data__'])['nodes_dict']}
    vector_index_data['doc_id_dict'] = {**vector_index_data['doc_id_dict'], **json.loads(data['index_store/data']['vector_index']['__data__'])['doc_id_dict']}
    vector_index_data['embeddings_dict'] = {**vector_index_data['embeddings_dict'], **json.loads(data['index_store/data']['vector_index']['__data__'])['embeddings_dict']}
    merged_data['index_store/data']['vector_index']['__data__'] = json.dumps(vector_index_data)

# Write the merged data to a new JSON file
with open('combined_index/index_store.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)
