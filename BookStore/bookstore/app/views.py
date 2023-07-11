from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Count
from . models import Book

# Create your views here.
def home(request):
    featuredBooks = Book.objects.filter(featured=True)
    topSellers = Book.objects.filter(topSeller=True)
    return render(request, "app/home.html", locals())

class CategoryView(View):
    def get(self, request, val):
        book = Book.objects.filter(category=val)
        title = Book.objects.filter(category=val).values('title')
        category_name = Book.objects.filter(category=val).values('category')
        return render(request, "app/category.html", locals())

class SearchView(View):
    def get(self, request):
        return render(request, "app/search.html", locals())
    
class SignupView(View):
    def get(self, request):
        return render(request, "app/signup.html", locals())

class SignupSuccessView(View):
    def get(self, request):
        return render(request, "app/signupSuccess.html", locals())
    
class SigninView(View):
    def get(self, request):
        return render(request, "app/signin.html", locals())
    
class ProfileView(View):
    def get(self, request):
        return render(request, "app/profile.html", locals())
    
class ChangePwdView(View):
    def get(self, request):
        return render(request, "app/changePwd.html", locals())

class BookDetailsView(View):
    def get(self, request, book_isbn):
        book = get_object_or_404(Book, ISBN=book_isbn)
        return render(request, "app/bookDetails.html", locals())
    
class CartView(View):
    def get(self, request):
        return render(request, "app/cart.html", locals())

class CheckoutView(View):
    def get(self, request):
        return render(request, "app/checkout.html", locals())

class OrderSummaryView(View):
    def get(self, request):
        return render(request, "app/orderSummary.html", locals())
    
class OrderSuccessView(View):
    def get(self, request):
        return render(request, "app/orderSuccess.html", locals())
    
class OrderHistoryView(View):
    def get(self, request):
        return render(request, "app/orderHistory.html", locals())