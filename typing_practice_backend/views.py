from django.shortcuts import render
from essential_generators import DocumentGenerator
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import random

gen = DocumentGenerator()


file=open('para.json','r')
ParaGraphs= json.loads(file.read())

@api_view(['GET'])
def ParaGraphGeneratorEasy(request):    
    index=random.randint(0, len(ParaGraphs))
    return Response(ParaGraphs[str(index)])

@api_view(['GET'])
def ParaGraphGeneratorMedium(request):
    raw_paragraph=gen.paragraph(20,25)
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    idiol_para=''.join(filter(whitelist.__contains__, raw_paragraph))
    return Response(idiol_para)

@api_view(['GET'])
def ParaGraphGeneratorHard(request):
    raw_paragraph=gen.paragraph(20,25)
    whitelist = set('abcdefghijklmnopqrstuvwxyz 1234567890.;ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    idiol_para=''.join(filter(whitelist.__contains__, raw_paragraph))
    return Response(idiol_para)

@api_view(['GET'])
def ParaGraphGeneratorExtreme(request):
    raw_paragraph=gen.paragraph(20,25)    
    return Response(raw_paragraph)

