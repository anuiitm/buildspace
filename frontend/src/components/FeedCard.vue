<template>
  <div class="feed-card" :style="{ animationDelay: (index * 0.1) + 's' }">
    <div class="feed-card-header">
      <div class="avatar" :class="post.avatarColor">{{ post.avatar }}</div>
      <div class="feed-card-user-info">
        <div class="feed-card-username">
          {{ post.user }}
          <span v-if="post.verified" class="verified-badge">✓</span>
        </div>
        <div class="feed-card-meta">
          {{ post.handle }} · {{ post.time }}
          <span class="feed-card-type" :class="'type-' + post.type">{{ post.type }}</span>
        </div>
      </div>
    </div>
    <div class="feed-card-content">
      <h3 v-if="post.title">{{ post.title }}</h3>
      <p>{{ post.content }}</p>
    </div>
    <div class="feed-card-tags" v-if="post.tags && post.tags.length">
      <span class="tag" v-for="tag in post.tags" :key="tag">{{ tag }}</span>
    </div>
    <div class="feed-card-footer">
      <button class="feed-action" :class="{ liked: post.liked }" @click="$emit('like', post.id)">
        Like {{ post.likes }}
      </button>
      <button class="feed-action">
        Comments {{ post.comments }}
      </button>
      <button class="feed-action">
        Share {{ post.shares }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeedCard',
  props: {
    post: { type: Object, required: true },
    index: { type: Number, default: 0 },
  },
  emits: ['like'],
};
</script>
