# Example data
videos = [
    {'title': 'Video 1', 'sentiment_score': 0.8, 'comments': 20, 'views': 5000, 'likes': 100, 'upload_days_ago': 10},
    {'title': 'Video 2', 'sentiment_score': 0.6, 'comments': 30, 'views': 10000, 'likes': 200, 'upload_days_ago': 20},
]

for video in videos:
    # Weighted scores
    sentiment_score_weighted = video['sentiment_score'] * 0.5
    views_per_day_weighted = 1 / (video['views'] / video['upload_days_ago']) * 0.25
    likes_comments_weighted = (video['likes'] + video['comments']) * 0.25

    # Overall score
    overall_score = sentiment_score_weighted + views_per_day_weighted + likes_comments_weighted
    video['overall_score'] = overall_score

# Sorting videos based on overall score
videos.sort(key=lambda x: x['overall_score'], reverse=True)

# Assigning ranks to videos
for rank, video in enumerate(videos, start=1):
    video['rank'] = rank

# Printing the ranked videos
for video in videos:
    print(f"Rank: {video['rank']}, Title: {video['title']}, Overall Score: {video['overall_score']}")
