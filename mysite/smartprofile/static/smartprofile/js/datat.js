$(document).ready(function() {
    var dt_table = $('.datatable').dataTable({
        language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {
                name: 'SubmissionDate	',
                orderable: true,
                searchable: true,
                targets: [0]
            },
            {
                name: 'start',
                orderable: true,
                searchable: true,
                targets: [1]
            }
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        bDestroy : true,
        ajax: "{% url 'smartprofile:HouseholdListJson' %}"
    });
});
