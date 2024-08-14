document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    let slug;
    try {
        slug = document.querySelector('meta[name="post-slug"]').getAttribute('content');
    } catch (error) {
        console.error("Error: Unable to find post slug. Make sure the meta tag is present in the HTML.");
        slug = '';
    }

    // Edit functionality
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            commentForm.setAttribute("action", `edit_comment/${commentId}`);
        });
    }

    // Delete functionality
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment-id");
            if (slug) {
                deleteConfirm.href = `/${slug}/delete_comment/${commentId}`;
            } else {
                console.error("Error: Post slug is not available. Unable to construct delete URL.");
                return;
            }
            deleteModal.show();
        });
    }
});