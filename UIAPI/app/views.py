from django.shortcuts import render,redirect
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .models import CustomUser, Role
from .serializers import CustomUserSerializer, RoleSerializer


def Registration(request):
    roles=Role.objects.all()
    return render(request,'registration.html',{'roles':roles})

def Registration_Data(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        email=request.POST['email']
        datejoined=request.POST['datejoined']
        age=request.POST['age']
        number=request.POST['number']
        address=request.POST['address']
        password=request.POST['password']
        roles=request.POST['roles']
        username=request.POST['username']

        if CustomUser.objects.filter(email=email).exists():
            return render(request,'registration.html',{'msg':'email already exists'})

        else:
            CustomUser.objects.create(username=username,first_name=name,last_name=lastname,email=email,date_joined=datejoined,
                                      age=age,phone_number=number,address=address,password=password,roles=roles)
            return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def login_data(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if CustomUser.objects.filter(username=username,password=password).exists():
            data=CustomUser.objects.all()
            return render(request,'table.html',{'data':data})

def table(request):
    data=CustomUser.objects.all()
    return render(request,'table.html',{'data':data})

def update(request, tid):
    tid = CustomUser.objects.get(id=tid)
    return render(request, 'update.html', {'id': tid})

def update_data(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        lastname=request.POST['lastname']
        email=request.POST['email']
        datejoined=request.POST['datejoined']
        age=request.POST['age']
        number=request.POST['number']
        address=request.POST['address']
        password=request.POST['password']
        roles=request.POST['roles']
        username=request.POST['username']

        CustomUser.objects.filter(id=id).update(username=username,first_name=name,last_name=lastname,email=email,date_joined=datejoined,
                                      age=age,phone_number=number,address=address,password=password,roles=roles)
        data=CustomUser.objects.all()
        return render(request,'table.html',{'data':data})

def delete(request, tid):
    CustomUser.objects.filter(id=tid).delete()
    data=CustomUser.objects.all()
    return render(request,'table.html',{'data':data})

def roles(request):
    return render(request,'roles.html')

def roles_data(request):
    if request.method=='POST':
        rolename=request.POST['rolename']
        description=request.POST['description']
        Role.objects.create(name=rolename,description=description)
        return render(request,'login.html')

# api view for user registration
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to register


# api view for user login
class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Get username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            return Response({'message': 'Login successful!', 'user_id': user.id}, status=200)
        else:
            return Response({'message': 'Invalid credentials'}, status=401)

# api view for user list (requires authentication)
class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

# api view for role management (list all roles and create a new role)
class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]

# api view for role detail (retrieve, update, delete role)
class RoleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]