from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from .process import process
from .search import SearchName
# from .search_process import search
# from .process import GenerateRekonstruksi
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import redirect
from urllib.parse import urlencode
from urllib.request import urlretrieve
from django.urls import reverse_lazy


def detail(request, id):
    post = Post.objects.get(id=id)
    return HttpResponse(post.html)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PageDetailView(DetailView):
    model = Post
    template_name = 'details.html'

class SearchView(CreateView):
    model = Post
    form_class = SearchName
    template_name= 'search.html'

    def post(self, request, *args, **kwargs):
        long = float(request.POST['lon'])
        lati = float(request.POST['lat'])

        tampil1 = 'https://tangrams.github.io/heightmapper/#14.02083/{lati}/{long}'.format(
            long=long, lati=lati)

        tampil2 = 'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{long},{lati},12,0.00,0.00/960x540@2x?access_token=pk.eyJ1IjoibWFybG82NjYiLCJhIjoiY2trdmR0dDliMXY4eTJ4bnluM2JocXMwYSJ9.cxd7dZ7AyqIT2i8DNAyMJg'.format(
            long=long, lati=lati)

        params = urlencode(dict(access_key="59a30d0256ce48adb2c13172a20cb676",
                                url=tampil1,
                                height=1080,
                                width=1920
                                ))
        urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "../../../Downloads/heightmap.png")

        params2 = urlencode(dict(access_key="59a30d0256ce48adb2c13172a20cb676",
                                url=tampil2
                                ))
        urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params2, "../../../Downloads/texture.png")

        # print(is_heightMap, "Bebas")
        # if is_heightMap == "true":
        #     return redirect(tampil1)
        # else:
        #     return self.render_to_response({'params': params, 'tampil2': tampil2})

        return self.render_to_response({'params': params, 'tampil2': params2})
        # return HttpResponse(tampil1)


class PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'


    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        save_file = fs.save(uploaded_file.name, uploaded_file)

        uploaded_file2 = request.FILES['texture_map']
        # fs2 = FileSystemStorage()
        save_file2 = fs.save(uploaded_file2.name, uploaded_file2)

        html = process(fs.location+'/'+save_file, fs.location+'/'+save_file2)
        # data = Post(title=request.POST.get('title'), html=html, image=uploaded_file)
        data = Post(title=request.POST.get('title'), html=html)
        data.save()
        # request.POST
        # form = PostForm(request.POST, request.FILES)
        # if form.is_valid(): form.save()
        return HttpResponse(html)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

