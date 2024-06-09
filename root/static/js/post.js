document.getElementById('postForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const title = document.getElementById('postTitle').value;
    const content = document.getElementById('postContent').value;
    const author = document.getElementById('postAuthor').value;

    alert('Post saved!\n\n' +
        'Title: ' + title + '\n' +
        'Content: ' + content + '\n' +
        'Author: ' + author);
});
