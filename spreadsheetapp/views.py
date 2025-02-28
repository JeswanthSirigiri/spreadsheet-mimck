from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Spreadsheetapp
from .serializers import SpreadsheetappSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Spreadsheet
@api_view(['POST'])
def save_spreadsheet(request):
    serializer = SpreadsheetappSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Spreadsheet saved successfully'},status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def load_spreadsheet(request, name):
    spreadsheet = get_object_or_404(Spreadsheetapp, name=name)
    serializer = SpreadsheetappSerializer(spreadsheet)
    return Response(serializer.data)

@api_view(['POST'])
def perform_operation(request):
    """
    Perform arithmetic and data quality operations.
    Expected request format: { "operation": "sum", "data": [1, 2, 3, 4] }
    """
    operation = request.data.get('operation')
    data = request.data.get('data')

    if not isinstance(data, list):
        return Response({'error': 'Data should be a list'}, status=400)

    try:
        df = pd.Series(data)  # Using Pandas for operations

        operations = {
            "sum": df.sum(),
            "average": df.mean(),
            "count": df.count(),
            "max": df.max(),
            "min": df.min(),
            "trim": [str(item).strip() for item in data],
            "upper": [str(item).upper() for item in data],
            "lower": [str(item).lower() for item in data],
            "find_replace": data.replace(request.data.get('find', ''), request.data.get('replace', ''))
        }

        result = operations.get(operation, "Invalid operation")
        return Response({"result": result})
    except Exception as e:
        return Response({'error': str(e)}, status=400)

def index(request):
    spreadsheets = Spreadsheet.objects.all()
    return render(request, 'spreadsheet/index.html',{'spreadsheets': spreadsheets})
