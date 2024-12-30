from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def indexPage(request): # home page
    return render(request, 'index.html')

def tweetList(request): # list all tweets
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweetList.html', {'tweets': tweets})

def tweetCreate(request): # create new tweet
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetList')
    else:
        form = TweetForm()
    return render(request, 'tweetForm.html', {'form': form})

def tweetEdit(request, tweet_id): # edit tweet by tweet_id
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetList')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweetForm.html', {'form': form})

def tweetDelete(request, tweet_id): # delete tweet by tweet_id
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweetList')
    return render(request, 'tweetConfirmDelete.html', {'tweet': tweet})