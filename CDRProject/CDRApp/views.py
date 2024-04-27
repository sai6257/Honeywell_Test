from django.shortcuts import render
from .forms import CDRFileUploadForm
from .models import CallDetailRecord
import csv
from datetime import datetime

def upload_cdr_file(request):
    if request.method == 'POST':
        form = CDRFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cdr_file = request.FILES['cdr_file']
            if cdr_file.name.endswith('.csv'):
                decoded_file = cdr_file.read().decode('utf-8').splitlines()
                reader = csv.reader(decoded_file)
                for row in reader:
                    call_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                    caller_number = row[1]
                    callee_number = row[2]
                    duration_seconds = int(row[3])
                    call_cost = float(row[4])
                    cdr_record = CallDetailRecord.objects.create(
                        call_date=call_date,
                        caller_number=caller_number,
                        callee_number=callee_number,
                        duration_seconds=duration_seconds,
                        call_cost=call_cost
                    )
                    cdr_record.save()
                return render(request, 'upload_success.html')
            else:
                return render(request, 'upload_error.html', {'error': 'Invalid file format. Please upload a CSV file.'})
    else:
        form = CDRFileUploadForm()
    return render(request, 'upload_form.html', {'form': form})
