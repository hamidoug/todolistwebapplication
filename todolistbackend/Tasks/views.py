from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


# Create your views here.

#View To Display Task feed and add items to it
class TaskFeedView(APIView):
    #Function to get whole todolist
    def get(self, request, pk=None):
        try:
            if pk:
                task = Task.objects.get(pk=pk)
                serializer = TaskSerializer(task)
            else:
                tasks = Task.objects.all()
                serializer = TaskSerializer(tasks, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #Function to add task to list 
    def post(self, request):
        try: 
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Invalid data provided', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   
    
    #Edit Individual Task
    def put(self, request, pk):
        try: 
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid data provided', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)
        
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   

    #Function to delete a task
    def delete(self, request, pk):
        try:
            Task.objects.get(pk=pk).delete()
            return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    
    

   
  
