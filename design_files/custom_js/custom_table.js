$(document).ready(function() {
    $('.table').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: false,
        lengthChange: false,
        pageLength: 5 // Set the number of rows per page
    });
});