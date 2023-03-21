from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import CardTransactions
from rest_framework.parsers import FileUploadParser


class UploadCsv(APIView):

    def post(self,request):
        if request.method == 'POST':
            # Check if a file was uploaded
            if 'file' not in request.data:
                return Response({'error': 'No file was uploaded'}, status=status.HTTP_400_BAD_REQUEST)
            
            csv_file = request.data['file']
            print(csv_file,type(csv_file))

            CardTransactions.insert_rows_from_csv(request.data['file'])

            return Response({'message': 'CSV file uploaded successfully'}, status=status.HTTP_200_OK)

class Sort(APIView):
    def get(self, request):
        column_name = request.GET.get('column_name')
        sort_order = request.GET.get('sort_order', 'asc')
        
        if sort_order not in ['asc', 'desc']:
            return JsonResponse({'error': 'Invalid sort order'})
        
        order = '-' if sort_order == 'desc' else ''

        if column_name not in [field.name for field in CardTransactions._meta.get_fields()]:
            return JsonResponse({'error': 'Invalid column name'})
        
        qs = CardTransactions.objects.values_list('data_value').order_by(f'{order}{column_name}')[:50]
        data = list(qs.values('data_value'))
        
        return JsonResponse(data, safe=False)