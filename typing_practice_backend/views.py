from django.shortcuts import render
from essential_generators import DocumentGenerator
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import random

gen = DocumentGenerator()


file=open('para.json','r')
ParaGraphs= json.loads(file.read())

mostCommon=open('most_common.json','r')
MostCommonWords=(json.loads(mostCommon.read()))


Common=open('words.json','r')
CommonWords=(json.loads(Common.read()))

@api_view(['GET'])
def ParaGraphGeneratorEasy(request):
    SendableWords=''
    for i in range(0,300):
        index=random.randint(0,len(MostCommonWords))
        SendableWords+=MostCommonWords[str(index)][0]+' '
    return Response(SendableWords)

@api_view(['GET'])
def ParaGraphGeneratorMedium(request):
    SendableWords=''
    for i in range(0,300):
        index=random.randint(0,len(CommonWords))
        SendableWords+=CommonWords[str(index)][0]+' '
    return Response(SendableWords)

@api_view(['GET'])
def ParaGraphGeneratorHard(request):
    index=random.randint(0, len(ParaGraphs))
    return Response(ParaGraphs[str(index)])

@api_view(['GET'])
def ParaGraphGeneratorExtreme(request):
    raw_paragraph=gen.paragraph(20,25)    
    return Response(raw_paragraph)

