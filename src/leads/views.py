from django.shortcuts import redirect, render, reverse
from django.core.mail import send_mail
from .models import Lead
from .forms import LeadForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Landing Page Class.
class LandingPageView(TemplateView):

    template_name = 'landing.html'


# Lead List. Class.
class LeadListView(LoginRequiredMixin, ListView):

    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


# Lead Details Class.
class LeadDetailView(LoginRequiredMixin, DetailView):

    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


# Create Lead Class.
class CreateLeadView(LoginRequiredMixin, CreateView):

    template_name = 'leads/lead_create.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead-list')


# Update Lead Class.
class UpdateLeadView(LoginRequiredMixin, UpdateView):

    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead-list')


# Delete Lead Class.
class DeleteLeadView(LoginRequiredMixin, DeleteView):

    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):

        return reverse('leads:lead-list')


class RegisterUserView(CreateView):

    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

# ====================================================
# == FUNCTIONS ==

# Landing Page Function.


# def landing_page(request):

#     return render(request, 'landing.html', {})


# # Leads List Function.
# def lead_list(request):

#     leads = Lead.objects.all()

#     context = {
#         'leads': leads,
#     }

#     return render(request, 'leads/lead_list.html', context)


# # Lead Details Function.
# def lead_detail(request, pk):

#     lead = Lead.objects.get(pk=pk)

#     context = {
#         'lead': lead
#     }

#     return render(request, 'leads/lead_detail.html', context)


# # Create Lead Function
# def lead_create(request):

#     form = LeadForm()

#     if request.method == 'POST':

#         form = LeadForm(request.POST)

#         if form.is_valid():

#             form.save()
#             messages.success(request, ('Lead was created.'))
#             send_mail(
#                 subject='A lead has been created.',
#                 message='Go to the CRM to see new Lead.',
#                 from_email='test@test.com',
#                 recipient_list=['test@test.com']
#             )
#             return redirect('leads:lead-list')

#     context = {
#         'form': form,
#     }

#     return render(request, 'leads/lead_create.html', context)


# # Update Lead Function.
# def lead_update(request, pk):

#     lead = Lead.objects.get(pk=pk)
#     form = LeadForm(instance=lead)

#     if request.method == 'POST':
#         form = LeadForm(request.POST or None, instance=lead)

#         if form.is_valid():
#             form.save()
#             return redirect('leads:lead-list')

#     context = {
#         'form': form,
#         'lead': lead,
#     }

#     return render(request, 'leads/lead_update.html', context)


# # Delete Lead Function.
# def lead_delete(request, pk):

#     lead = Lead.objects.get(pk=pk)
#     lead.delete()
#     messages.success(
#         request, ('Lead was deleted.'))
#     return redirect('leads:lead-list')


# def login_user(request):

#     if request.method == 'POST':

#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(
#                 request, ('Logged in.'))
#             return redirect('leads:lead-list')
#         else:
#             messages.success(
#                 request, ('Sorry there was an error while loging in. Try again.'))
#             return redirect('login')

#     else:
#         return render(request, 'registration/login.html', {})


# def logout_user(request):

#     logout(request)

#     messages.success(
#         request, ('You Were Logged Out.'))
#     return redirect('login')
