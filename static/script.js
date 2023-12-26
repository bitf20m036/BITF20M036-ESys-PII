function changePageSize() {
    var selectedPageSize = document.getElementById("page_size").value;

    //console.log("Before Assignment - Selected Page Size:", selectedPageSize);

    // Get the current URL
    var currentUrl = window.location.href;

    // Use URLSearchParams to handle the query string parameters
    var urlSearchParams = new URLSearchParams(window.location.search);

    // Set or update the 'page_size' parameter in the query string
    urlSearchParams.set('page_size', selectedPageSize);

    // Get the updated query string
    var updatedQueryString = urlSearchParams.toString();

    // Update the URL with the new query string
    var newUrl = currentUrl.split('?')[0] + '?' + updatedQueryString;

    // Redirect to the new URL
    window.location.href = newUrl;
}
