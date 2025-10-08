// Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
// Implement the Twitter class:
// Twitter() Initializes your twitter object.
// void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
// List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
// void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
// void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

// Example 1:
// Input
// ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
// [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
// Output
// [null, null, [5], null, null, [6, 5], null, [5]]
// Explanation
// Twitter twitter = new Twitter();
// twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
// twitter.follow(1, 2);    // User 1 follows user 2.
// twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
// twitter.unfollow(1, 2);  // User 1 unfollows user 2.
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

import java.util.*; 
class Twitter {
    private int time ; 
    private Map<Integer,List<int[]>> tweets ; 
    private Map<Integer,Set<Integer>> follows ; 

    public Twitter() {
        time = 0 ; 
        tweets = new HashMap<>(); 
        follows = new HashMap<>(); 
    }
    
    public void postTweet(int userId, int tweetId) {
        tweets.putIfAbsent(userId, new ArrayList<>()); 
        tweets.get(userId).add(new int[]{tweetId , time++}); 
    }
    
    public List<Integer> getNewsFeed(int userId) {
        List<int[]> allTweets = new ArrayList<>(); 

        if (tweets.containsKey(userId)){
            allTweets.addAll(tweets.get(userId)); 
        }

        if (follows.containsKey(userId)){
            for(int followee : follows.get(userId) ){
                if (tweets.containsKey(followee)){
                    allTweets.addAll(tweets.get(followee)); 
                }
            }
        }

        allTweets.sort((a,b)->b[1]-a[1]); 

        List<Integer> feed = new ArrayList<>(); 
        for(int i = 0 ; i < Math.min(10,allTweets.size()) ; i++){
            feed.add(allTweets.get(i)[0]);
        }

        return feed ; 
    }
    
    public void follow(int followerId, int followeeId) {
        follows.putIfAbsent(followerId , new HashSet<>()); 
        follows.get(followerId).add(followeeId); 
    }
    
    public void unfollow(int followerId, int followeeId) {
        if (follows.containsKey(followerId)){
            follows.get(followerId).remove(followeeId); 
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */