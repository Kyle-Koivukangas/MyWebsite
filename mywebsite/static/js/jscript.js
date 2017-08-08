
$(function() { 
    $('nav-item').on('click','nav-item', function ( e ) {
        e.preventDefault();
        $(this).parents('nav-item').find('active').removeClass('active').end().end().addClass('active');
        $(activeTab).show();
    });
});