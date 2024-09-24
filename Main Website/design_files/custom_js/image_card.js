$(document).ready(function() {
    console.log("image_card.js loaded"); // Debugging line
    $('.image-card').click(function() {
        var imageUrl = $(this).data('image-url');
        var cardTitle = $(this).find('.card-title').text();
        
        console.log("Image URL: " + imageUrl); // Debugging line
        console.log("Card Title: " + cardTitle); // Debugging line
        
        $('#modalImage').attr('src', imageUrl);
        $('#imageModalLabel').text(cardTitle);
        $('#imageModal').modal('show');
    });
});