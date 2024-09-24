$(document).ready(function() {
    $('#eventsTable').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: false,
        lengthChange: false,
        pageLength: 5 // Set the number of rows per page
    });
    $('#priestsTable').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: false,
        lengthChange: false,
        pageLength: 5
    });
});