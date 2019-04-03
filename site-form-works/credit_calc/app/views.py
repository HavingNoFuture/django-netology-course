from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        form = CalcForm(request.GET)
        context = {
            'form': form,
        }
        print('kwargs', **kwargs)
        if self.kwargs:
            sum = int(request.GET.get('initial_fee'))
            percent = int(request.GET.get('rate')) / 100
            months = int(request.GET.get('months_count'))

            result = (sum + sum * percent) / months

            context = {
                'form': form,
                'result': result,
                'common_result': sum + sum * percent
            }

        return self.render_to_response(context)
