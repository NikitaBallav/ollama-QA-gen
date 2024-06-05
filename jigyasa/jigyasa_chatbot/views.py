from django.shortcuts import render
from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from rest_framework import status 
from jigyasa_chatbot.models import *
from django.http import JsonResponse
#from django.conf.settings import index


class defaultJigyasa(APIView):
    def post(self, request):
        #write code to accept input from user in post request
        input_val = request.data.get("input")

        
        # query_engine = settings.INDEX_INSTANCE.as_query_engine()

        query = input_val[:4000]
        val_query_response = settings.CHAT_ENGINE.chat(query)
        print(val_query_response)

        node = val_query_response.source_nodes[0]
        response_json = {}
        response_json['response'] = val_query_response.response
        response_json['search_Score'] = node.score

        try:
            response_json['url'] = str(node.metadata['URL'])
        except  KeyError as e:
            response_json['url'] =  str(settings.FILE_TO_URL_MAPPING[node.metadata['file_name']])


        #input_val = request.data.get("input")
        return Response({"status": "success", "data": response_json}, status=status.HTTP_200_OK)



# Create your views here.
