from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Sum, Count

@staff_member_required
def index(request):
    template_data = {'title': 'Admin Dashboard'}
    return render(
        request,
        'dashboard/index.html',
        {
            'template_data': template_data,
        },
    )

@staff_member_required
def top_purchaser(request):
    template_data = {'title': 'Top Purchaser'}
    # top user filtered below.
    template_data['top'] = (User.objects
        .annotate(total=Sum('order__item__quantity'))
        .order_by('-total', 'username')
        .first()
    ) 
    
    return render(
            request,
            "dashboard/top_purchaser.html",
            {
                "template_data": template_data,
            },
        )



@staff_member_required
def top_commenter(request):
    template_data = {'title': 'Top Commenter'}
    # top user filtered below.
    template_data['top'] = (User.objects
        .annotate(total=Count('review'))
        .filter(total__gt=0)
        .order_by('-total', 'username')
        .first()
    ) 
        
    return render(
            request,
            "dashboard/top_commenter.html",
            {
                "template_data": template_data,
            },
        )