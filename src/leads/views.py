from django.shortcuts import redirect, render
from .models import Lead
from .forms import LeadModelForm


# Leads List.
def lead_list(request):

    leads = Lead.objects.all()

    context = {
        'leads': leads,
    }

    return render(request, 'leads/lead_list.html', context)


# Lead Details.
def lead_detail(request, pk):

    lead = Lead.objects.get(pk=pk)

    context = {
        'lead': lead
    }

    return render(request, 'leads/lead_detail.html', context)


# Create Lead.
def lead_create(request):

    form = LeadModelForm()

    if request.method == 'POST':

        form = LeadModelForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/leads')

    context = {
        'form': form,
    }

    return render(request, 'leads/lead_create.html', context)


# Update Lead.
def lead_update(request, pk):

    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)

    if request.method == 'POST':
        form = LeadModelForm(request.POST or None, instance=lead)

        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        'form': form,
        'lead': lead,
    }

    return render(request, 'leads/lead_update.html', context)


# Delete Lead.
def lead_delete(request, pk):

    lead = Lead.objects.get(pk=pk)
    lead.delete()

    return redirect('/leads')
