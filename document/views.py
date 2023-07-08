from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages

from .models import Document, TypeDocument
from order.models import Cart


class TypeDocumentListView(ListView):
    model = TypeDocument
    template_name = 'document/type_documents.html'
    context_object_name = 'type_documents'


class DocumentListView(ListView):
    model = Document
    template_name = 'document/document_lawyer.html'
    context_object_name = 'documents_lawyer'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        type_document = TypeDocument.objects.get(id=self.kwargs['id'])
        qs = qs.filter(type=type_document)
        return qs


class DocumentLawyerDetailView(DetailView):
    model = Document
    template_name = 'document/document_lawyer_detail.html'
    context_object_name = 'document_lawyer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        document = context['document_lawyer']
        context['documents_lawyer'] = Document.objects.filter(lawyer=document.lawyer)
        return context


class BookDocumentiew(View):
    def post(self, request, pk):
        document = Document.objects.get(id=pk)

        try:
            # get or create cart
            print(document.lawyer.name)
            cart, created = Cart.objects.get_or_create(
                user=request.user,
                document=document
            )
            print(created)

            if created:
                cart.save()
            else:
                messages.info(request, 'Item already exists in your cart')

            return redirect('order:cart')
        except Exception as e:
            print(e)
            return redirect('document:lawyer-detail', pk=pk)

def book_document(request):
    return render(request, 'document/dokcart.html')