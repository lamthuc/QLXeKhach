from rest_framework import generics, permissions, status, viewsets, parsers
from rest_framework.response import Response
from .models import Coach, Route, BusCompany, Delivery, User
from .serializers import CoachSerializer, RouteSerializer, BusCompanySerializer, DeliverySerializer, ReviewSerializer, UserSerializer
from rest_framework .decorators import api_view, action
from rest_framework.permissions import IsAuthenticated

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

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        bus_company_id = self.kwargs['transport_company_id']
        return Review.objects.filter(bus_company_id=bus_company_id)

class DeliveryListCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['current_user']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get', 'put'], detail=False, url_path='current-user')
    def current_user(self, request):
        u = request.user
        if request.method.__eq__('PUT'):
            for k, v in request.data.items():
                setattr(u, k, v)
            u.save()

        return Response(UserSerializer(u, context={'request': request}).data)