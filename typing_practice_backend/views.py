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
    index=random.randint(0,len(MostCommonWords)-302)
    print(index)
    print(len(MostCommonWords)-300)
    for i in range(0,300):
        SendableWords+=MostCommonWords[str(index+i)][0]+' '
    return Response(SendableWords)

@api_view(['GET'])
def ParaGraphGeneratorMedium(request):
    SendableWords=''
    index=random.randint(0,len(CommonWords)-400)
    print(index)
    print(len(CommonWords)-400)    
    for i in range(0,300):
        SendableWords+=CommonWords[str(index + i)][0]+' '
    return Response(SendableWords)

@api_view(['GET'])
def ParaGraphGeneratorHard(request):
    index=random.randint(0, len(ParaGraphs))
    return Response(ParaGraphs[str(index)])

@api_view(['GET'])
def ParaGraphGeneratorExtreme(request):
    raw_paragraph=gen.paragraph(20,25)    
    return Response(raw_paragraph)

