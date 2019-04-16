from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        if self.kwargs:
            product_id = int(self.kwargs['pk'])
            context['object'] = Product.objects.get(id=product_id)
            context['reviews'] = Review.objects.filter(product_id=product_id)
            context['form'] = ReviewForm

            if product_id in self.request.session.get('reviewed_products', []):
                context['is_review_exist'] = True

        return context

    def get_queryset(self):
        return Product.objects.all()

    def post(self, request, *args, **kwargs):
        product_id = int(self.kwargs['pk'])
        form = ReviewForm(self.request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.save()
            self.request.session['reviewed_products'] = self.request.session.get('reviewed_products', []) + [product_id]

        return redirect(reverse('product_detail', kwargs={'pk': product_id}))
