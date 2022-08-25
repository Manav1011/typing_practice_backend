from django.shortcuts import render
from essential_generators import DocumentGenerator
from rest_framework.decorators import api_view
from rest_framework.response import Response

gen = DocumentGenerator()
@api_view(['GET'])
def ParaGraphGenerator(request):
    raw_paragraph=gen.paragraph(10,15)
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    idiol_para=''.join(filter(whitelist.__contains__, raw_paragraph))
    return Response(idiol_para)    
