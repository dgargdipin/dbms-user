$(document).on("click", ".assignmentLink", function () {
    var myBookId = $(this).data('id');
    $(".assignment .assignmentInput").val(myBookId);
    // As pointed out in comments, 
    // it is unnecessary to have to manually call the modal.
    // $('#addBookDialog').modal('show');
});
