---
layout: default
title: Projects and Blog
nav_order: 3
---

# Projects and Blog

<div class="filter-controls mb-4">
  <div class="mb-2">
    <strong class="mr-2">Type:</strong>
    <button class="btn btn-primary filter-type" data-filter="all">All</button>
    <button class="btn filter-type" data-filter="project">Projects</button>
    <button class="btn filter-type" data-filter="blog">Blogs</button>
  </div>

  <div>
    <strong class="mr-2">Topic:</strong>
    <select id="topic-select" class="form-select" style="display:inline-block; width:auto; padding: 5px;">
      <option value="all">All Topics</option>
      {% assign all_topics = "" | split: "" %}
      {% for item in site.data.portfolio %}
        {% assign all_topics = all_topics | concat: item.topics %}
      {% endfor %}
      {% assign unique_topics = all_topics | uniq | sort %}
      {% for topic in unique_topics %}
      <option value="{{ topic }}">{{ topic }}</option>
      {% endfor %}
    </select>
  </div>
</div>

<div id="portfolio-container">
  {% for item in site.data.portfolio %}
  <div class="portfolio-item mb-4 p-4 border rounded" data-type="{{ item.type }}" data-topics="{{ item.topics | join: ',' }}">
    <h2 class="fs-5">
      {% if item.url != "#" %}
      <a href="{{ item.url }}">{{ item.title }}</a>
      {% else %}
      {{ item.title }}
      {% endif %}
    </h2>
    <div class="mb-2">
      <span class="btn btn-purple btn-sm" style="padding: 2px 6px; font-size: 0.8em; pointer-events: none;">{{ item.type | capitalize }}</span>
      {% for topic in item.topics %}
      <span class="btn btn-green btn-sm" style="padding: 2px 6px; font-size: 0.8em; pointer-events: none;">{{ topic }}</span>
      {% endfor %}
    </div>
    <p>{{ item.description }}</p>
    <hr>
  </div>
  {% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
const typeButtons = document.querySelectorAll('.filter-type');
const topicSelect = document.getElementById('topic-select');
const items = document.querySelectorAll('.portfolio-item');
let currentType = 'all';
let currentTopic = 'all';
function filterItems() {
items.forEach(item => {
const itemType = item.getAttribute('data-type');
const itemTopics = item.getAttribute('data-topics').split(',');
const typeMatch = (currentType === 'all') || (itemType === currentType);
const topicMatch = (currentTopic === 'all') || itemTopics.includes(currentTopic);
if (typeMatch && topicMatch) {
item.style.display = 'block';
} else {
item.style.display = 'none';
}
});
}
typeButtons.forEach(btn => {
btn.addEventListener('click', (e) => {
typeButtons.forEach(b => {
b.classList.remove('btn-primary');
});
e.target.classList.add('btn-primary');
currentType = e.target.getAttribute('data-filter');
filterItems();
});
});
if (topicSelect) {
topicSelect.addEventListener('change', (e) => {
currentTopic = e.target.value;
filterItems();
});
}
});
</script>
