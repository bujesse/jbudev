var $form = $('form.series-code-form');

$form.submit((e) => {
    e.preventDefault();
    var series_code_qs = $(e.currentTarget).serialize();

    var $spinner = $('.dv-loading-spinner');
    $spinner.show();
    $.get('/bokeh_graph/get_graph?' + series_code_qs, (data) => {
        $spinner.hide();
        $('.dv-graph-container').html(data);
    });
});