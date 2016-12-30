from django.shortcuts import get_object_or_404, render
from .models import Ticket

# Create your views here.
def issue_list(request):
    latest_issue_list = Ticket.objects.order_by('-submitted_date')[:9]
    context = {'latest_issue_list': latest_issue_list}
    return render(request, 'issue\issue_list.html', context)
    
def issue_detail(request, issue_id):
    issue = get_object_or_404(Ticket, pk=issue_id)
    return render(request, 'issue\issue_detail.html', {'issue':issue})