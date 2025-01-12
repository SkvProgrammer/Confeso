document.getElementById('postConfessionBtn').onclick = function() {
    var modal = new bootstrap.Modal(document.getElementById('confessionModal'));
    modal.show();
};

document.getElementById('submitConfession').onclick = function() {
    const confessionContent = document.getElementById('confessionContent').value;
    if (confessionContent) {
        fetch('/post_confession', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `content=${encodeURIComponent(confessionContent)}`
        }).then(response => {
            if (response.ok) {
                location.reload();
            }
        });
    }
};

document.getElementById('cancelConfession').onclick = function() {
    document.getElementById('confessionModal').style.display = 'none';
};
