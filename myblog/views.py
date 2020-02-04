from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Question,Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .forms import PostForm
from django.urls import reverse
 


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {"posts" : posts })
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/poll/post_detail.html', {'post': post}) 

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('myblog:post_detail', pk=post.pk)
    
    else:

        form = PostForm()
    return render(request, 'myblog/post_edit.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('myblog:post_detail', pk=post.pk)
            
    else:
        form = PostForm(instance=post)
    return render(request, 'myblog/post_edit.html', {'form': form})

#poll app functions    

def poll(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:6]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myblog/poll_index.html', context)



def poll_detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'myblog/poll_detail.html', {'question': question})
    




def poll_result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myblog/poll_result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myblog/poll_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('myblog:poll_result', args=(question.id,)))
