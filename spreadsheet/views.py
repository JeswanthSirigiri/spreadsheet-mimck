from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Spreadsheet, Cell

def index(request):
    spreadsheets = Spreadsheet.objects.all()
    return render(request, 'spreadsheet/index.html',{'spreadsheets': spreadsheets})

def save_spreadsheet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        data = request.POST.get('data')  # Data will be sent as a stringified 2D array
        spreadsheet = Spreadsheet.objects.create(name=name)

        # Parse the data and save cells
        rows = eval(data)  # Convert stringified 2D array to Python list
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                Cell.objects.create(
                    spreadsheet=spreadsheet,
                    row=i,
                    col=j,
                    value=value
                )

        return HttpResponse(f"Spreadsheet saved with ID: {spreadsheet.id}")
    return HttpResponse("Invalid request", status=400)

def load_spreadsheet(request, id):
    spreadsheet = get_object_or_404(Spreadsheet, id=id)
    cells = spreadsheet.cells.all()

    # Reconstruct the grid
    grid = []
    max_row = max(cells.values_list('row', flat=True)) if cells else 0
    max_col = max(cells.values_list('col', flat=True)) if cells else 0

    for i in range(max_row + 1):
        row = []
        for j in range(max_col + 1):
            cell = cells.filter(row=i, col=j).first()
            row.append(cell.value if cell else '')
        grid.append(row)

    # Render the grid in a simple HTML table
    html = "<table border='1'>"
    for row in grid:
        html += "<tr>"
        for cell in row:
            html += f"<td>{cell}</td>"
        html += "</tr>"
    html += "</table>"

    return HttpResponse(html)
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Spreadsheet, Cell

def calculate_sum(request, id):
    spreadsheet = get_object_or_404(Spreadsheet, id=id)
    cells = spreadsheet.cells.all()
    total = sum(float(cell.value) for cell in cells if cell.value and cell.value.replace('.', '', 1).isdigit())
    return HttpResponse(f"Sum: {total}")

def calculate_average(request, id):
    spreadsheet = get_object_or_404(Spreadsheet, id=id)
    cells = spreadsheet.cells.all()
    values = [float(cell.value) for cell in cells if cell.value and cell.value.replace('.', '', 1).isdigit()]
    average = sum(values) / len(values) if values else 0
    return HttpResponse(f"Average: {average}")

def calculate_max(request, id):
    spreadsheet = get_object_or_404(Spreadsheet, id=id)
    cells = spreadsheet.cells.all()
    values = [float(cell.value) for cell in cells if cell.value and cell.value.replace('.', '', 1).isdigit()]
    max_value = max(values) if values else 0
    return HttpResponse(f"Max: {max_value}")

def calculate_min(request, id):
    spreadsheet = get_object_or_404(Spreadsheet, id=id)
    cells = spreadsheet.cells.all()
    values = [float(cell.value) for cell in cells if cell.value and cell.value.replace('.', '', 1).isdigit()]
    min_value = min(values) if values else 0
    return HttpResponse(f"Min: {min_value}")

def calculate_count(request, id):
    spreadsheet = get_object_or_404(Spreadsheet, id=id)
    cells = spreadsheet.cells.all()
    count = sum(1 for cell in cells if cell.value and cell.value.replace('.', '', 1).isdigit())
    return HttpResponse(f"Count: {count}")