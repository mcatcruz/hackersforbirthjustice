import streamlit as st

# In-memory data storage
if 'posts' not in st.session_state:
    st.session_state.posts = []

if 'comments' not in st.session_state:
    st.session_state.comments = {}

# Function to add a post
def add_post(title, content):
    post_id = len(st.session_state.posts) + 1
    st.session_state.posts.append({'id': post_id, 'title': title, 'content': content, 'comments': []})

# Function to add a comment
def add_comment(post_id, comment):
    st.session_state.comments.setdefault(post_id, []).append(comment)

# Streamlit App Layout
st.title("Forum App")

# Sidebar for adding new posts
st.sidebar.header("Create a New Post")
title = st.sidebar.text_input("Title")
content = st.sidebar.text_area("Content")
if st.sidebar.button("Post"):
    add_post(title, content)
    st.sidebar.success("Post added successfully")

# Display posts
st.header("All Posts")
for post in st.session_state.posts:
    st.subheader(post['title'])
    st.write(post['content'])
    st.write(f"Post ID: {post['id']}")

    # Display comments
    st.write("Comments:")
    post_comments = st.session_state.comments.get(post['id'], [])
    for comment in post_comments:
        st.write(comment)

    # Add a comment
    comment_text = st.text_area(f"Add a comment for post {post['id']}", key=f"comment_{post['id']}")
    if st.button("Submit", key=f"submit_{post['id']}"):
        add_comment(post['id'], comment_text)
        st.success("Comment added successfully")
        st.experimental_rerun()
