from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Coach, Route, BusCompany
from .serializers import CoachSerializer, RouteSerializer, BusCompanySerializer
from rest_framework .decorators import api_view


class RouteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAdminUser]


class RouteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAdminUser]

class RouteSearchView(generics.ListAPIView):
    serializer_class = RouteSerializer

    def get_queryset(self):
        source = self.request.query_params.get('source', None)
        destination = self.request.query_params.get('destination', None)
        if source is not None and destination is not None:
            return Route.objects.filter(source=source, destination=destination)
        elif source is not None:
            return Route.objects.filter(source=source)
        elif destination is not None:
            return Route.objects.filter(destination=destination)
        else:
            return Route.objects.all()


class RecommendedRoutesView(generics.ListAPIView):
     serializer_class = RouteSerializer

     def get_queryset(self):
          source = self.request.query_params.get('source', None)
          destination = self.request.query_params.get('destination', None)
          routes = Route.objects.all()

          if source is not None and destination is not None:
               routes = routes.filter(source=source, destination=destination)
          elif source is not None:
               routes = routes.filter(source=source)
          elif destination is not None:
               routes = routes.filter(destination=destination)

          recommended_routes = []
          for route in routes:
               # Perform recommendation logic here
               recommended_routes.append(route)

          # Sort recommended routes by price
          recommended_routes.sort(key=lambda r: r.price)
          return recommended_routes
class RegisterBusCompanyView(generics.CreateAPIView):
    serializer_class = BusCompanySerializer

class BusCompanyUpdateView(generics.UpdateAPIView):
    queryset = BusCompany.objects.all()
    serializer_class = BusCompanySerializer

class BusCompanyDetailView(generics.RetrieveAPIView):
    queryset = BusCompany.objects.all()
    serializer_class = BusCompanySerializer

class BusCompanyRoutesView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_queryset(self):
        return Route.objects.filter(transport_company=self.kwargs['pk'])

class BusCompanyCoachView(generics.ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

    def get_queryset(self):
        return Trip.objects.filter(transport_company=self.kwargs['pk'])

class BusCompanyCreateRouteView(generics.CreateAPIView):
    serializer_class = RouteSerializer

    def perform_create(self, serializer):
        serializer.save(transport_company=TransportCompany.objects.get(pk=self.kwargs['pk']))


class BusCompanyUpdateRouteView(generics.UpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

