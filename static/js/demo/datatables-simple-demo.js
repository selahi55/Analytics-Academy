window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
    const datatablesSimpleNoPagination = document.getElementById('');
    if (datatablesSimpleNoPagination) {
        new simpleDatatables.DataTable(datatablesSimpleNoPagination, {
            paging: false,
            searchable: false
        });
}
});
