# views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer
from rest_framework.permissions import IsAuthenticated

class MedicationSKUViewSet(viewsets.ModelViewSet):
    queryset = MedicationSKU.objects.all()
    serializer_class = MedicationSKUSerializer
    permission_classes = [IsAuthenticated]  # Optional: Only authenticated users can access this

    def perform_create(self, serializer):
        # Set the user who created the record as `created_by`
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['post'], url_path='bulk-create')
    def bulk_create(self, request):
        data = request.data

        # Ensure data is a list for bulk creation
        if not isinstance(data, list):
            return Response(
                {"error": "Data must be a list of objects."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Add `created_by` field for each entry
        for entry in data:
            entry['created_by'] = request.user.id

        serializer = MedicationSKUSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
